# =============================================================================
#  CAVIAROLI — PROYECTO DIGITAL COMPLETO
#  Documentación + Ejecución de las 4 Tasks
#  Asignado a: Nahuel
#  Fecha: Jun 2026
# =============================================================================
#
#  CONTEXTO
#  --------
#  La estrategia cambia: ya no es comunicación de marca genérica.
#  Es producto directo al consumidor final. Dos frentes simultáneos:
#    1. Urgencia comercial — lote a vencer
#    2. Construcción de audiencia orgánica con contenido de producto
#
#  SITIOS
#  ------
#  Web global:        https://www.caviaroli.com
#  Web Argentina:     https://www.caviaroli.com.ar
#  IG global:         https://www.instagram.com/caviaroli
#  IG Argentina:      https://www.instagram.com/caviaroli.argentina/
#
# =============================================================================
#
#  T-01 · IMAGEN DE PERFIL INSTAGRAM — ESFERA DE OLIVA
#  ────────────────────────────────────────────────────
#  Estado:    Abierta (requiere diseño)
#  Asignado:  Nahuel
#
#  Objetivo:
#    Rediseñar el perfil de @caviaroli y @caviaroli.argentina con una imagen
#    de una esfera de oliva perfecta — glossy, tridimensional, con tallo —
#    sobre fondo negro profundo. Sin texto ni logotipo.
#
#  Fundamento estratégico:
#    En la búsqueda de Instagram, Caviaroli compite hoy contra su propio frasco
#    y su logotipo tipográfico. La esfera es el elemento faltante: es producto
#    puro, destaca sobre fondo oscuro y genera reconocimiento inmediato.
#
#  Entregables:
#    - 2 versiones: Global (@caviaroli) + Argentina (@caviaroli.argentina)
#    - Diferenciación sutil entre versiones (ej: variación de fondo o tallo)
#    - Formato: PNG circular 1:1, mínimo 320x320px
#    - Testear a 46px (tamaño búsqueda) y 150px (perfil)
#
#  Checklist:
#    [ ] Definir fondo final: negro profundo (#0a0a0a) vs verde bosque (#0a1a05)
#    [ ] Render / ilustración esfera con brillo realista
#    [ ] Versión Global
#    [ ] Versión Argentina con diferenciador sutil
#    [ ] Test de legibilidad a 46px y 150px
#    [ ] Exportar PNG circular listo para subir
#
#  Herramientas sugeridas:
#    - Midjourney / Firefly / Ideogram para render fotorrealista
#    - Canva o Photoshop para recorte circular
#    - Prompt sugerido: "a perfect olive sphere, glossy, photorealistic,
#      3D render, with a small stem, on deep black background, studio lighting,
#      macro photography, ultra high detail"
#
# =============================================================================
#
#  T-02 · REDISEÑO DE FEED + ESTRATEGIA DE CONTENIDO ORGÁNICO
#  ────────────────────────────────────────────────────────────
#  Estado:    Abierta
#  Asignado:  Nahuel
#  Urgencia:  Alta — hay lote a vencer
#
#  Objetivos simultáneos:
#    1. [URGENTE] Generar tráfico orgánico → ventas del lote a vencer
#    2. Encuadrar al consumidor final: qué es Caviaroli, cómo se usa, por qué vale
#
#  Cambio estratégico clave:
#    Dejamos de comunicar MARCA y empezamos a comunicar PRODUCTO DIRECTO.
#    Cada post debe tener un propósito claro: educar, desear o convertir.
#
#  Motor de producción:
#    IA generativa — Higgsfield AI como opción principal para video de producto
#    con movimiento y estética premium, sin necesidad de producción física.
#    URL: https://higgsfield.ai
#
#  Estructura de contenido:
#    A. GRILLA VISUAL UNIFICADA
#       - Definir paleta de colores del feed (negro + verde oliva + blanco)
#       - Tipografía para copy en posts
#       - Estilo de encuadre: macro de producto, fondo neutro, textura
#
#    B. SERIE URGENCIA (lote a vencer)
#       - 3-5 posts: precio + disponibilidad limitada + CTA directo
#       - Copy ejemplo: "Stock limitado. Caviaroli Albahaca 200g a precio especial."
#       - CTA: "Link en bio → comprar ahora"
#
#    C. EDUCACIÓN DE PRODUCTO
#       - Qué es el caviar de aceite (explicación simple)
#       - Cómo se usa: sobre huevo, en sushi, en cocktails
#       - Maridajes: con qué va cada sabor
#       - Recetas simples (1 ingrediente + Caviaroli)
#
#    D. VIDEO IA CON HIGGSFIELD
#       - Shot de esfera cayendo en slow motion
#       - Aceite fluyendo / perlas estallando
#       - Plato final con Caviaroli como toque final
#
#    E. REELS DE CONVERSIÓN
#       - Duración: 7-15 segundos
#       - Gancho en los primeros 2 segundos
#       - CTA: swipe up / link en bio / "disponible en caviaroli.com.ar"
#
#  Checklist:
#    [ ] Definir paleta y estética visual del feed
#    [ ] Producir 3-5 posts de urgencia para lote a vencer
#    [ ] Producir 5-8 posts de educación de producto
#    [ ] Generar 2-3 videos con Higgsfield AI
#    [ ] Editar 2-3 reels de conversión
#    [ ] Actualizar bio, highlights y link con nueva estrategia
#    [ ] Programar publicaciones (sugerido: 1 post/día durante 2 semanas)
#
# =============================================================================
#
#  T-03 · CSV ACTUALIZACIÓN MASIVA TIENDANUBE — PRECIO + SEO IA
#  ─────────────────────────────────────────────────────────────
#  Estado:    Script listo — PENDIENTE tipo de cambio EUR→ARS (confirmar owner)
#  Asignado:  Nahuel
#  Prerequisito de: T-04
#
#  Situación actual:
#    - 66 productos en Tiendanube con precio = 0 y sin SEO
#    - 74 registros en Excel de vencimientos con precio en EUR
#    - 60/66 productos con match automático de precio
#    - 6 productos a cargar manualmente: Libro, Pasta Pura, Drops by Albert Adrià
#    - 52 productos urgentes (vencen en <120 días) → precio promocional -20%
#
#  Qué hace este script:
#    1. Lee el CSV de Tiendanube y el Excel de vencimientos
#    2. Cruza productos por nombre (matching flexible por palabras clave + gramaje)
#    3. Convierte precios EUR→ARS usando el tipo de cambio indicado
#    4. Asigna precio promocional (-20%) a productos con vencimiento <120 días
#    5. Genera Título SEO y Descripción SEO por producto con Claude Sonnet (IA)
#    6. Exporta CSV listo para importar en Tiendanube
#
#  Archivos necesarios (en la misma carpeta que este script):
#    - tiendanube[...].csv       (exportar desde Tiendanube → Productos → Exportar)
#    - Caviaroli_Vencimientos.xlsx
#
#  Instalación:
#    pip install pandas openpyxl anthropic
#    export ANTHROPIC_API_KEY=sk-ant-...     # solo para SEO con IA
#
#  Uso:
#    python caviaroli_proyecto_completo.py task3 \
#        --tc 1100 \
#        --tiendanube tiendanube.csv \
#        --vencimientos Caviaroli_Vencimientos.xlsx
#
#  Parámetros:
#    --tc            Tipo de cambio EUR→ARS (REQUERIDO — confirmar con owner)
#    --descuento     % descuento lote urgente (default: 20)
#    --tiendanube    CSV de Tiendanube (default: tiendanube.csv)
#    --vencimientos  Excel de vencimientos (default: Caviaroli_Vencimientos.xlsx)
#    --output        CSV de salida (default: caviaroli_actualizado.csv)
#    --dias-urgente  Días umbral para urgente (default: 120)
#    --dry-run       Preview sin generar archivo
#
#  Checklist de ejecución:
#    [ ] Confirmar tipo de cambio EUR→ARS con owner
#    [ ] Instalar dependencias: pip install pandas openpyxl anthropic
#    [ ] Configurar ANTHROPIC_API_KEY en el entorno (para SEO con IA)
#    [ ] Ejecutar con --dry-run primero para validar
#    [ ] Revisar 6 productos sin match e ingresar precio manualmente
#    [ ] Ejecutar definitivo y obtener CSV
#    [ ] Importar CSV en Tiendanube → Productos → Importar
#    [ ] Validar precios y SEO en la tienda antes de confirmar
#
# =============================================================================
#
#  T-04 · GOOGLE SHOPPING — START PACK ORGÁNICO SIN INVERSIÓN PUBLICITARIA
#  ────────────────────────────────────────────────────────────────────────
#  Estado:    Depende de T-03 (ejecutar después de importar CSV con precios)
#  Asignado:  Nahuel
#  Costo:     $0 — integración nativa Tiendanube → Google Merchant Center
#
#  Por qué Google Shopping orgánico funciona para Caviaroli:
#    - Producto de nicho con poca competencia paga en Argentina
#    - Quien busca "caviar de aceite Argentina" ya tiene intención de compra
#    - Las fichas gratuitas aparecen en la pestaña Shopping y en búsqueda directa
#    - Los precios promocionales (lote a vencer) aparecen con tachado de precio
#      anterior → efecto visual de oferta sin costo adicional
#    - El SEO generado en T-03 alimenta directamente el feed de Google
#    - Activación: 48 hs desde configuración
#
#  IMPORTANTE: Sin precios cargados (T-03), Google rechaza todos los productos.
#  Ejecutar T-03 PRIMERO.
#
#  Pasos de configuración:
#
#    PASO 1 — Crear cuenta Google Merchant Center
#      URL: https://merchants.google.com
#      - Usar el email Google del negocio
#      - Completar: nombre empresa, país (Argentina), URL caviaroli.com.ar
#      - Verificar y reclamar el dominio (opciones: Google Analytics o tag manual)
#
#    PASO 2 — Vincular Tiendanube con Merchant Center
#      - En Tiendanube: Canales de venta → Google Shopping → Conectar
#      - Elegir la cuenta de Merchant Center creada
#      - Tiendanube genera el feed XML automáticamente (se sincroniza cada 24 hs)
#      - Guía oficial: https://ayuda.tiendanube.com/es_ES/123352-google-shopping/
#                      como-vincular-tu-tiendanube-con-google-shopping
#
#    PASO 3 — Activar fichas gratuitas de producto
#      - En Merchant Center: Crecimiento → Gestionar programas
#      - Activar "Fichas de producto gratuitas"
#      - Esto habilita el listado orgánico sin costo en Shopping y búsqueda
#
#    PASO 4 — Configurar categorías Google Shopping en Tiendanube
#      - En Tiendanube, cada categoría tiene campo "Categoría de Google Shopping"
#      - Mapeo sugerido:
#          Perlas de aceite    → "Alimentos > Condimentos y salsas"
#          Aceites Caviaroli   → "Alimentos > Aceites comestibles"
#          Perlas de vinagre   → "Alimentos > Vinagres"
#          Perlas de vino      → "Alimentos > Condimentos y salsas"
#          Salsas Oliquida     → "Alimentos > Salsas"
#          Pinturas de aceite  → "Alimentos > Condimentos y salsas"
#          Packs / Starter Kit → "Alimentos > Canastas y sets de alimentos"
#
#    PASO 5 — Importar CSV T-03 y esperar sincronización
#      - Importar el CSV generado en T-03 en Tiendanube
#      - El feed se sincroniza a Merchant Center en 24-48 hs
#
#    PASO 6 — Verificar estado del feed
#      - En Merchant Center: Productos → Diagnóstico
#      - Errores comunes: precio en 0 (solucionado con T-03), imagen sin fondo
#        blanco, título muy corto
#      - Corregir y confirmar productos activos
#
#  Checklist:
#    [ ] T-03 ejecutada e importada en Tiendanube (prerequisito)
#    [ ] Crear cuenta Google Merchant Center
#    [ ] Verificar y reclamar dominio caviaroli.com.ar
#    [ ] Vincular Tiendanube → Merchant Center
#    [ ] Activar fichas gratuitas de producto
#    [ ] Mapear categorías Google Shopping en Tiendanube
#    [ ] Esperar 48 hs y revisar diagnóstico
#    [ ] Confirmar productos activos en Google Shopping
#
# =============================================================================
#
#  ORDEN DE EJECUCIÓN RECOMENDADO
#  ───────────────────────────────
#  T-01 y T-02 pueden ejecutarse en paralelo (no tienen dependencias entre sí)
#  T-03 requiere confirmación del tipo de cambio EUR→ARS con el owner
#  T-04 requiere que T-03 esté ejecutada e importada en Tiendanube
#
#  PENDING BLOQUEANTE: tipo de cambio EUR→ARS (confirmar con owner)
#
# =============================================================================


import argparse
import os
import json
import time
from datetime import datetime, date

import pandas as pd
import openpyxl


# ─── ARGUMENTOS ──────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(
        description="Caviaroli — Proyecto digital completo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Tareas disponibles:
  task3    Generar CSV de actualización masiva Tiendanube con precios y SEO

Ejemplos:
  python caviaroli_proyecto_completo.py task3 --tc 1100 --dry-run
  python caviaroli_proyecto_completo.py task3 --tc 1100 --tiendanube tiendanube.csv --vencimientos Caviaroli_Vencimientos.xlsx
        """
    )
    p.add_argument("task", choices=["task3"], help="Task a ejecutar")
    p.add_argument("--tc",           type=float, help="Tipo de cambio EUR→ARS (requerido para task3)")
    p.add_argument("--descuento",    type=float, default=20,    help="Descuento %% lote urgente (default: 20)")
    p.add_argument("--tiendanube",   default="tiendanube.csv",  help="CSV de Tiendanube")
    p.add_argument("--vencimientos", default="Caviaroli_Vencimientos.xlsx", help="Excel de vencimientos")
    p.add_argument("--output",       default="caviaroli_actualizado.csv",   help="CSV de salida")
    p.add_argument("--dias-urgente", type=int, default=120, help="Días umbral urgente (default: 120)")
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
    for clave, datos in vencs.items():
        if normalizar(clave) == norm:
            return datos
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


# ─── SEO CON IA ──────────────────────────────────────────────────────────────

def generar_seo_lote(productos, batch_size=10):
    try:
        import anthropic
    except ImportError:
        print("  AVISO: 'anthropic' no instalado → pip install anthropic")
        print("  Usando SEO placeholder. Configurar ANTHROPIC_API_KEY para SEO real.")
        return _seo_placeholder(productos)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("  AVISO: ANTHROPIC_API_KEY no encontrada en el entorno.")
        print("  Usando SEO placeholder. Exportar ANTHROPIC_API_KEY=sk-ant-... para SEO real.")
        return _seo_placeholder(productos)

    client = anthropic.Anthropic(api_key=api_key)
    resultados = {}

    for i in range(0, len(productos), batch_size):
        lote = productos[i:i + batch_size]
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
            time.sleep(0.5)
        except Exception as e:
            print(f"  Error lote SEO {i//batch_size + 1}: {e}")
            for p in lote:
                resultados[p["nombre"]] = _seo_placeholder_uno(p["nombre"])
    return resultados


def _seo_placeholder(productos):
    return {p["nombre"]: _seo_placeholder_uno(p["nombre"]) for p in productos}


def _seo_placeholder_uno(nombre):
    return {
        "titulo_seo": f"Comprar {nombre} | Caviaroli Argentina"[:60],
        "desc_seo":   f"Caviaroli {nombre} — caviar de aceite gourmet. Ideal para cocina de vanguardia. Envío a todo el país."[:160],
    }


# ─── TASK 3: GENERAR CSV ─────────────────────────────────────────────────────

def task3(args):
    if not args.tc:
        print("\n  ERROR: --tc es requerido para task3.")
        print("  Ejemplo: python caviaroli_proyecto_completo.py task3 --tc 1100")
        print("  Confirmar tipo de cambio EUR→ARS con el owner antes de ejecutar.\n")
        return

    print(f"\n=== T-03 · CSV actualización masiva Tiendanube ===")
    print(f"  Tipo de cambio:  EUR 1 = ARS {args.tc:,.0f}")
    print(f"  Descuento promo: {args.descuento}%  (productos urgentes <{args.dias_urgente} días)")
    print(f"  Dry run:         {args.dry_run}\n")

    print("→ Leyendo archivos...")
    df_store = leer_tiendanube(args.tiendanube)
    vencs    = leer_vencimientos(args.vencimientos, args.dias_urgente)

    df_out = df_store.copy()
    df_out["Precio"]               = pd.to_numeric(df_out["Precio"], errors="coerce").fillna(0.0)
    df_out["Precio promocional"]   = pd.to_numeric(df_out["Precio promocional"], errors="coerce")
    df_out["Título para SEO"]      = df_out["Título para SEO"].astype(object)
    df_out["Descripción para SEO"] = df_out["Descripción para SEO"].astype(object)

    con_promo, sin_match, lista_seo = [], [], []

    print("\n→ Cruzando precios...")
    for idx, row in df_out.iterrows():
        nombre = row["Nombre"]
        match  = match_precio(nombre, vencs)
        if match:
            precio_ars = round(match["precio_eur"] * args.tc, 2)
            df_out.at[idx, "Precio"] = precio_ars
            if match["urgente"]:
                df_out.at[idx, "Precio promocional"] = round(precio_ars * (1 - args.descuento / 100), 2)
                con_promo.append(nombre)
            else:
                df_out.at[idx, "Precio promocional"] = float("nan")
        else:
            sin_match.append(nombre)
        lista_seo.append({
            "nombre":    nombre,
            "categoria": str(row.get("Categorías", "")),
            "tags":      str(row.get("Tags", "")),
        })

    print(f"\n→ Generando SEO para {len(lista_seo)} productos...")
    seo_data = generar_seo_lote(lista_seo)

    for idx, row in df_out.iterrows():
        nombre = row["Nombre"]
        if nombre in seo_data:
            df_out.at[idx, "Título para SEO"]      = seo_data[nombre]["titulo_seo"]
            df_out.at[idx, "Descripción para SEO"] = seo_data[nombre]["desc_seo"]

    con_precio = len(df_out[df_out["Precio"] > 0])
    print(f"\n─── RESUMEN T-03 ─────────────────────────────────")
    print(f"  Total productos:        {len(df_out)}")
    print(f"  Con precio asignado:    {con_precio}")
    print(f"  Con precio promocional: {len(con_promo)}")
    print(f"  Sin match (manual):     {len(sin_match)}")
    print(f"  Con SEO generado:       {len(seo_data)}")
    if sin_match:
        print(f"\n  Productos sin match — cargar precio manualmente en Tiendanube:")
        for n in sin_match:
            print(f"    · {n}")

    if args.dry_run:
        print(f"\n  DRY RUN — no se generó archivo.")
        cols = ["Nombre", "Precio", "Precio promocional", "Título para SEO", "Descripción para SEO"]
        print("\n  Preview primeras 5 filas:")
        print(df_out[cols].head(5).to_string(index=False))
        print(f"\n  Próximo paso: ejecutar sin --dry-run para generar el CSV.")
        return

    df_out.to_csv(args.output, index=False, encoding="latin1", sep=";")
    print(f"\n  CSV generado: {args.output}")
    print(f"  Importar en Tiendanube → Productos → Importar productos")
    print(f"\n  Próximo paso: T-04 — vincular Tiendanube con Google Merchant Center")
    print(f"  Guía: https://ayuda.tiendanube.com/es_ES/123352-google-shopping/")
    print(f"        como-vincular-tu-tiendanube-con-google-shopping")


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    args = parse_args()
    if args.task == "task3":
        task3(args)
    print("\n=== Listo ===\n")


if __name__ == "__main__":
    main()
