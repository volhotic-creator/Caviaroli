"""
Caviaroli — Pipeline de Rebrand Visual con IA
==============================================
Procesa todas las fotos scrapeadas aplicando estilo catálogo premium.
Referencia estética: tienda.havanna.com.ar

USO:
    python rebrand_imagenes.py

REQUIERE:
    pip install openai pillow

ESTRUCTURA ESPERADA:
    D:\\Volhotic\\Imagenes\\Caviaroli\\
        Caviaroli Aceite de Oliva Virgen - 50g\\
            foto1.jpg
            foto2.jpg
        Caviaroli Perlas de Mango\\
            foto1.jpg
        ...

RESULTADO:
    D:\\Volhotic\\Imagenes\\Caviaroli\\outputs\\
        Caviaroli Aceite de Oliva Virgen - 50g\\
            foto1_rebrand.png
            foto2_rebrand.png
        ...
"""

import os
import base64
import time
from pathlib import Path
from openai import OpenAI

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────

API_KEY    = os.environ.get("OPENAI_API_KEY", "")
INPUT_DIR  = Path(r"D:\Volhotic\Imagenes\Caviaroli")
OUTPUT_DIR = INPUT_DIR / "outputs"

# Extensiones de imagen válidas
IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

# Carpetas a ignorar
SKIP_DIRS = {"outputs", "blog", "inputs"}

# ─── PROMPT DE REBRAND ────────────────────────────────────────────────────────
# Estilo objetivo: tienda.havanna.com.ar
# Fondo blanco limpio, producto centrado, sombra suave, look catálogo DTC

PROMPT = """Fotografía de producto para catálogo de tienda online premium.
Tomá el producto de esta imagen y presentalo sobre fondo blanco puro.
Sombra difusa muy suave debajo del producto.
Iluminación de estudio pareja y suave, sin sombras duras.
Mantené el producto exactamente igual: mismo envase, misma etiqueta, mismos colores, misma forma.
Resultado limpio, profesional, estilo catálogo gourmet premium.
Sin personas, sin elementos extra, sin texto adicional generado."""

# ─── CLIENTE OPENAI ───────────────────────────────────────────────────────────

client = OpenAI(api_key=API_KEY)

# ─── FUNCIONES ────────────────────────────────────────────────────────────────

def procesar_imagen(input_path: Path, output_path: Path) -> bool:
    """Procesa una imagen con la API de OpenAI y guarda el resultado."""
    try:
        print(f"  → Procesando: {input_path.name}")

        with open(input_path, "rb") as img_file:
            response = client.images.edit(
                model="gpt-image-1",
                image=img_file,
                prompt=PROMPT,
                size="1024x1024",
                quality="high",
            )

        # Decodificar y guardar
        imagen_bytes = base64.b64decode(response.data[0].b64_json)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as out_file:
            out_file.write(imagen_bytes)

        print(f"  ✓ Guardado: {output_path.name}")
        return True

    except Exception as e:
        print(f"  ✗ Error en {input_path.name}: {e}")
        return False


def main():
    print("=" * 60)
    print("  CAVIAROLI — PIPELINE DE REBRAND VISUAL")
    print("=" * 60)
    print(f"  Input:  {INPUT_DIR}")
    print(f"  Output: {OUTPUT_DIR}")
    print()

    # Recolectar todas las imágenes
    tareas = []
    for carpeta in sorted(INPUT_DIR.iterdir()):
        if not carpeta.is_dir():
            continue
        if carpeta.name in SKIP_DIRS:
            continue

        for img in sorted(carpeta.iterdir()):
            if img.suffix.lower() not in IMG_EXTS:
                continue

            output_path = OUTPUT_DIR / carpeta.name / (img.stem + "_rebrand.png")

            # Saltar si ya fue procesada
            if output_path.exists():
                print(f"  ↷ Ya procesada: {carpeta.name}/{img.name}")
                continue

            tareas.append((img, output_path))

    total = len(tareas)
    print(f"  Total de imágenes a procesar: {total}")
    print()

    if total == 0:
        print("  No hay imágenes nuevas para procesar.")
        return

    # Procesar
    ok = 0
    errores = 0
    for i, (input_path, output_path) in enumerate(tareas, 1):
        print(f"[{i}/{total}] {input_path.parent.name}")
        exito = procesar_imagen(input_path, output_path)
        if exito:
            ok += 1
        else:
            errores += 1

        # Pausa entre requests para no saturar la API
        if i < total:
            time.sleep(2)

    # Resumen
    print()
    print("=" * 60)
    print(f"  COMPLETADO")
    print(f"  Procesadas: {ok}")
    print(f"  Errores:    {errores}")
    print(f"  Resultados en: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
