"""
Caviaroli — Generador de CSV para actualización masiva Tiendanube
Task 03: Precio (EUR→ARS) + SEO generado por IA por producto

USO:
    python caviaroli_tiendanube_update.py \
        --tc 1100 \
        --descuento 20 \
        --tiendanube tiendanube.csv \
        --vencimientos Caviaroli_Vencimientos.xlsx \
        --output caviaroli_actualizado.csv

PARÁMETROS:
    --tc           Tipo de cambio EUR → ARS (requerido, confirmar con owner)
    --descuento    % de descuento para lote urgente (default: 20)
    --tiendanube   CSV exportado de Tiendanube (default: tiendanube.csv)
    --vencimientos Excel de vencimientos (default: Caviaroli_Vencimientos.xlsx)
    --output       Nombre del CSV de salida (default: caviaroli_actualizado.csv)
    --dias-urgente Días para considerar urgente (default: 120)
    --dry-run      Muestra preview sin generar archivo

REQUIERE:
    pip install pandas openpyxl anthropic

ANTHROPIC_API_KEY debe estar en el entorno:
    export ANTHROPIC_API_KEY=sk-ant-...
"""

import argparse
import os
import sys
import json
import time
from datetime import datetime, date

import pandas as pd
import openpyxl


# ─── ARGUMENTOS ──────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="Caviaroli — CSV actualización masiva Tiendanube")
    p.add_argument("--tc",           type=float, required=True, help="Tipo de cambio EUR→ARS")
    p.add_argument("--descuento",    type=float, default=20,    help="% descuento lote urgente (default 20)")
    p.add_argument("--tiendanube",   default="tiendanube.csv",  help="CSV de Tiendanube")
    p.add_argument("--vencimientos", default="Caviaroli_Vencimientos.xlsx", help="Excel de vencimientos")
    p.add_argument("--output",       default="caviaroli_actualizado.csv",   help="CSV de salida")
    p.add_argument("--dias-urgente", type=int, default=120, help="Días umbral para urgente (default 120)")
    p.add_argument("--dry-run",      action="store_true", help="Preview sin generar archivo")
    return p.parse_args()


# ─── LECTURA DE DATOS ─────────────────────────────────────────────────────────

def leer_tiendanube(path):
    df = pd.read_csv(path, encoding="latin1", sep=";")
    print(f"  Tiendanube: {len(df)} productos cargados")
    return df


def leer_vencimientos(path, dias_urgente, today=None):
    if today is None:
        today = date.today()
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))

    vencs = {}
    for row in rows[2:]:
        if not (row[0] and row[1] and row[3]):
            continue
        nombre = str(row[1]).strip().lower()
        precio_eur = float(row[3])
        fecha_venc = row[2]
        if isinstance(fecha_venc, datetime):
            fecha_venc = fecha_venc.date()
        dias = (fecha_venc - today).days if fecha_venc else 999
        # Si hay duplicado, guardar el de vencimiento más próximo (más urgente)
        if nombre not in vencs or dias < vencs[nombre]["dias"]:
            vencs[nombre] = {
                "precio_eur": precio_eur,
                "fecha_venc": str(fecha_venc) if fecha_venc else "",
                "dias": dias,
                "urgente": dias < dias_urgente,
            }

    print(f"  Vencimientos: {len(vencs)} SKUs únicos")
    print(f"  Urgentes (<{dias_urgente} días): {sum(1 for v in vencs.values() if v['urgente'])}")
    return vencs


# ─── MATCHING NOMBRE → PRECIO ─────────────────────────────────────────────────

def normalizar(texto):
    """Normaliza nombre para matching flexible."""
    import unicodedata
    texto = str(texto).lower()
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii")
    for char in [".", ",", "-", "_", "(", ")", "/"]:
        texto = texto.replace(char, " ")
    return " ".join(texto.split())


def _palabras_clave(texto):
    import re
    texto = normalizar(texto)
    gramaje = set(re.findall(r'\d+\s*(?:g|ml|mm|u)', texto.replace(" ", "")))
    stopwords = {
        "caviaroli","aceite","oliva","virgen","extra","perlas","de","con","y",
        "e","salsa","verde","liquida","drops","by","albert","adria","pintura",
        "vino","nectar","fino","tio","pepe","pack","starter","kit","libro",
        "recetas","cook","book","vol","food","serv","tres","variedades","art",
        "muria","la","los","las","el","un","una","10mm","4mm","8mm","c","u"
    }
    palabras = {w for w in texto.split() if w not in stopwords and len(w) > 2}
    return palabras, gramaje


def match_precio(nombre_tienda, vencs):
    norm = normalizar(nombre_tienda)
    # 1) Exacto
    for clave, datos in vencs.items():
        if normalizar(clave) == norm:
            return datos
    # 2) Palabras clave + gramaje
    palabras_t, gramaje_t = _palabras_clave(nombre_tienda)
    if not gramaje_t:
        return None
    mejores = []
    for clave, datos in vencs.items():
        palabras_c, gramaje_c = _palabras_clave(clave)
        if not gramaje_c & gramaje_t:
            continue
        comun = palabras_t & palabras_c
        if len(comun) >= 1:
            mejores.append((len(comun), datos))
    if mejores:
        mejores.sort(key=lambda x: -x[0])
        return mejores[0][1]
    return None


# ─── SEO CON IA (ANTHROPIC) ──────────────────────────────────────────────────

def generar_seo_lote(productos_sin_seo, batch_size=10):
    """
    Genera Título SEO + Descripción SEO para una lista de productos
    usando la API de Anthropic. Procesa en batches para eficiencia.
    
    productos_sin_seo: lista de dicts con keys 'nombre', 'categoria', 'tags'
    Retorna: dict {nombre: {'titulo_seo': str, 'desc_seo': str}}
    """
    try:
        import anthropic
    except ImportError:
        print("  AVISO: 'anthropic' no instalado. Ejecutar: pip install anthropic")
        print("  Usando títulos y descripciones de placeholder.")
        return _seo_placeholder(productos_sin_seo)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("  AVISO: ANTHROPIC_API_KEY no encontrada en el entorno.")
        print("  Usando títulos y descripciones de placeholder.")
        return _seo_placeholder(productos_sin_seo)

    client = anthropic.Anthropic(api_key=api_key)
    resultados = {}

    for i in range(0, len(productos_sin_seo), batch_size):
        lote = productos_sin_seo[i:i + batch_size]
        lista_txt = "\n".join(
            f'- Nombre: "{p["nombre"]}" | Categoría: {p["categoria"]} | Tags: {p["tags"]}'
            for p in lote
        )

        prompt = f"""Sos un experto en SEO para e-commerce de alimentos gourmet en Argentina.
Para cada producto de la lista generá:
1. Título SEO (máx 60 caracteres): descriptivo, con keyword principal, orientado a búsqueda argentina
2. Descripción SEO (máx 160 caracteres): beneficio principal + uso sugerido + marca Caviaroli

Productos:
{lista_txt}

Respondé ÚNICAMENTE con un JSON válido con este formato exacto, sin texto adicional:
{{
  "productos": [
    {{
      "nombre": "nombre exacto del producto",
      "titulo_seo": "...",
      "desc_seo": "..."
    }}
  ]
}}"""

        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            raw = response.content[0].text.strip()
            # Limpiar posibles backticks
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            data = json.loads(raw)
            for item in data["productos"]:
                resultados[item["nombre"]] = {
                    "titulo_seo": item["titulo_seo"][:60],
                    "desc_seo":   item["desc_seo"][:160],
                }
            print(f"  SEO generado: lote {i//batch_size + 1} ({len(lote)} productos)")
            time.sleep(0.5)  # rate limit gentil
        except Exception as e:
            print(f"  Error en lote SEO {i//batch_size + 1}: {e}")
            for p in lote:
                resultados[p["nombre"]] = _seo_placeholder_uno(p["nombre"])

    return resultados


def _seo_placeholder(productos):
    return {p["nombre"]: _seo_placeholder_uno(p["nombre"]) for p in productos}


def _seo_placeholder_uno(nombre):
    titulo = f"Comprar {nombre} | Caviaroli Argentina"[:60]
    desc   = f"Caviaroli {nombre} — caviar de aceite gourmet. Ideal para cocina de vanguardia. Envío a todo el país."[:160]
    return {"titulo_seo": titulo, "desc_seo": desc}


# ─── GENERACIÓN DEL CSV ───────────────────────────────────────────────────────

def generar_csv(df_store, vencs, tc, descuento_pct, dias_urgente, output, dry_run):
    df_out = df_store.copy()
    today  = date.today()

    # Asegurar columnas de precio como float y SEO como string
    df_out["Precio"]               = pd.to_numeric(df_out["Precio"], errors="coerce").fillna(0.0)
    df_out["Precio promocional"]   = pd.to_numeric(df_out["Precio promocional"], errors="coerce")
    df_out["Título para SEO"]      = df_out["Título para SEO"].astype(object)
    df_out["Descripción para SEO"] = df_out["Descripción para SEO"].astype(object)

    sin_precio  = []
    sin_seo     = []
    con_promo   = []
    sin_match   = []

    for idx, row in df_out.iterrows():
        nombre = row["Nombre"]
        match  = match_precio(nombre, vencs)

        if match:
            precio_ars = round(match["precio_eur"] * tc, 2)
            df_out.at[idx, "Precio"] = precio_ars

            if match["urgente"]:
                precio_promo = round(precio_ars * (1 - descuento_pct / 100), 2)
                df_out.at[idx, "Precio promocional"] = precio_promo
                con_promo.append(nombre)
            else:
                df_out.at[idx, "Precio promocional"] = float("nan")
        else:
            sin_match.append(nombre)

        # Preparar lista para generar SEO
        sin_seo.append({
            "nombre":    nombre,
            "categoria": str(row.get("Categorías", "")),
            "tags":      str(row.get("Tags", "")),
        })

    # Generar SEO con IA
    print(f"\n→ Generando SEO para {len(sin_seo)} productos...")
    seo_data = generar_seo_lote(sin_seo)

    for idx, row in df_out.iterrows():
        nombre = row["Nombre"]
        if nombre in seo_data:
            df_out.at[idx, "Título para SEO"]      = seo_data[nombre]["titulo_seo"]
            df_out.at[idx, "Descripción para SEO"] = seo_data[nombre]["desc_seo"]

    # Reporte
    con_precio = len(df_out[df_out["Precio"] > 0])
    print(f"\n─── RESUMEN ──────────────────────────────────")
    print(f"  Total productos:        {len(df_out)}")
    print(f"  Con precio asignado:    {con_precio}")
    print(f"  Con precio promocional: {len(con_promo)}")
    print(f"  Sin match en Excel:     {len(sin_match)}")
    print(f"  Con SEO generado:       {len(seo_data)}")
    if sin_match:
        print(f"\n  Productos sin match (revisar manualmente):")
        for n in sin_match:
            print(f"    · {n}")

    if dry_run:
        print(f"\n  DRY RUN — no se generó archivo.")
        print(f"\n  Preview primeras 3 filas:")
        cols_preview = ["Nombre", "Precio", "Precio promocional", "Título para SEO", "Descripción para SEO"]
        print(df_out[cols_preview].head(3).to_string(index=False))
        return

    # Exportar — mismo encoding que el original
    df_out.to_csv(output, index=False, encoding="latin1", sep=";")
    print(f"\n  CSV generado: {output}")
    print(f"  Listo para importar en Tiendanube → Productos → Importar")


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()

    print("\n=== Caviaroli — Actualización masiva Tiendanube ===")
    print(f"  Tipo de cambio:  EUR 1 = ARS {args.tc:,.0f}")
    print(f"  Descuento promo: {args.descuento}%")
    print(f"  Días urgente:    <{args.dias_urgente} días")
    print(f"  Dry run:         {args.dry_run}")
    print()

    print("→ Leyendo archivos...")
    df_store = leer_tiendanube(args.tiendanube)
    vencs    = leer_vencimientos(args.vencimientos, args.dias_urgente)

    print("\n→ Cruzando precios y generando CSV...")
    generar_csv(
        df_store    = df_store,
        vencs       = vencs,
        tc          = args.tc,
        descuento_pct = args.descuento,
        dias_urgente  = args.dias_urgente,
        output      = args.output,
        dry_run     = args.dry_run,
    )
    print("\n=== Listo ===\n")


if __name__ == "__main__":
    main()
