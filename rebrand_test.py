"""
Caviaroli Argentina — Generador de Imágenes Editoriales con IA
===============================================================
Toma 4 imágenes de referencia de Caviaroli (estilo editorial con texto)
y genera versiones NUEVAS adaptadas para Caviaroli Argentina.

Estilo objetivo: mismo lenguaje visual — acción de producto, fondo oscuro/claro,
fotografía editorial gastronómica — pero imágenes 100% nuevas.

USO:
    1. Copiá tus 4 imágenes de referencia en la carpeta inputs\editorial\
       - 01_aceite_negro.jpg     (aceite cayendo, fondo negro)
       - 02_esparrago_blanco.jpg (esparrago con aceite, fondo blanco)
       - 03_tomate_gris.jpg      (salsa tomate cayendo, fondo gris)
       - 04_pasta_aceite.jpg     (pasta con aceite, fondo gris)

    2. Ejecutar:
       set OPENAI_API_KEY=sk-...
       python rebrand_test.py

RESULTADO:
    D:\\Volhotic\\Imagenes\\Caviaroli\\outputs\\editorial\\
        01_caviaroli_aceite_negro.png
        02_caviaroli_esparrago.png
        03_caviaroli_tomate.png
        04_caviaroli_pasta.png
"""

import os
import base64
import time
from pathlib import Path
from openai import OpenAI

# ─── CONFIGURACIÓN ────────────────────────────────────────────────────────────

API_KEY    = os.environ.get("OPENAI_API_KEY", "")
BASE_DIR   = Path(r"D:\Volhotic\Imagenes\Caviaroli")
INPUT_DIR  = BASE_DIR / "inputs" / "editorial"
OUTPUT_DIR = BASE_DIR / "outputs" / "editorial"

client = OpenAI(api_key=API_KEY)

# ─── LAS 4 IMÁGENES Y SUS PROMPTS ────────────────────────────────────────────
# Cada imagen de referencia tiene un prompt específico que captura
# su esencia y la adapta para Caviaroli Argentina.

IMAGENES = [
    {
        "input":  "01_aceite_negro.jpg",
        "output": "01_caviaroli_aceite_negro.png",
        "nombre": "Aceite cayendo — fondo negro",
        "prompt": (
            "Editorial food photography. A small glass jar of premium olive oil pearls "
            "tipped sideways, golden olive oil pearls slowly falling out, dark dramatic "
            "background (#0a0a0a). Low-key studio lighting with a single point light "
            "highlighting the pearls. Cinematic, luxury food brand aesthetic. "
            "Photorealistic, ultra high detail, no text, no logo."
        ),
    },
    {
        "input":  "02_esparrago_blanco.jpg",
        "output": "02_caviaroli_esparrago.png",
        "nombre": "Espárrago con aceite — fondo blanco",
        "prompt": (
            "Editorial food photography. A single white asparagus on a pure white surface, "
            "golden olive oil drizzling over it in a thin elegant stream. Soft natural studio "
            "lighting, high-key white background. Minimalist gourmet aesthetic, macro detail "
            "of oil texture. Clean, premium, Spanish gastronomy style. "
            "Photorealistic, ultra high detail, no text, no logo."
        ),
    },
    {
        "input":  "03_tomate_gris.jpg",
        "output": "03_caviaroli_tomate.png",
        "nombre": "Tomate con aceite — fondo gris claro",
        "prompt": (
            "Editorial food photography. A ripe halved tomato on a light gray surface (#e8e6e1), "
            "a thin stream of golden extra virgin olive oil falling from above onto it, "
            "creating a vivid red and gold composition. Soft studio lighting, slight shadow. "
            "High-end Spanish gastronomy magazine style. "
            "Photorealistic, ultra high detail, no text, no logo."
        ),
    },
    {
        "input":  "04_pasta_aceite.jpg",
        "output": "04_caviaroli_pasta.png",
        "nombre": "Pasta con aceite — fondo gris",
        "prompt": (
            "Editorial food photography. A nest of fresh tagliolini pasta on a light gray "
            "surface, a dark glass olive oil bottle pouring a thin stream of golden oil over it "
            "from above. Soft natural light, minimal shadow. Premium Italian-Spanish gastronomy "
            "aesthetic, clean composition. "
            "Photorealistic, ultra high detail, no text, no logo."
        ),
    },
]

# ─── MAIN ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  CAVIAROLI ARGENTINA — IMÁGENES EDITORIALES IA")
    print("=" * 60)

    if not API_KEY:
        print("\n  ERROR: Falta OPENAI_API_KEY")
        print("  Ejecutá: set OPENAI_API_KEY=sk-...")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\n  Input:  {INPUT_DIR}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"\n  Imágenes a generar: {len(IMAGENES)}\n")

    for i, img in enumerate(IMAGENES, 1):
        print(f"  {i}. {img['nombre']}")

    print()
    confirmar = input("  ¿Generamos las 4 imágenes? (s/n): ").strip().lower()
    if confirmar != "s":
        print("  Cancelado.")
        return

    print()
    ok = 0
    for i, img in enumerate(IMAGENES, 1):
        output_path = OUTPUT_DIR / img["output"]
        input_path  = INPUT_DIR / img["input"]

        print(f"[{i}/4] {img['nombre']}")

        if output_path.exists():
            print(f"       ↷ Ya existe — {output_path.name}\n")
            ok += 1
            continue

        try:
            # Si existe la imagen de referencia, usamos edición (más fiel al estilo)
            # Si no, usamos generación pura con el prompt
            if input_path.exists():
                print(f"       → Modo: edición con referencia")
                with open(input_path, "rb") as f:
                    response = client.images.edit(
                        model="gpt-image-1",
                        image=f,
                        prompt=img["prompt"],
                        size="1024x1536",   # vertical 2:3 — formato Stories/vertical
                        quality="high",
                    )
            else:
                print(f"       → Modo: generación pura (no se encontró referencia)")
                response = client.images.generate(
                    model="gpt-image-1",
                    prompt=img["prompt"],
                    size="1024x1536",
                    quality="high",
                    n=1,
                )

            img_bytes = base64.b64decode(response.data[0].b64_json)
            with open(output_path, "wb") as out:
                out.write(img_bytes)
            print(f"       ✓ Guardado: {output_path.name}\n")
            ok += 1

        except Exception as e:
            print(f"       ✗ Error: {e}\n")

        if i < len(IMAGENES):
            time.sleep(3)

    print("=" * 60)
    print(f"  LISTO — {ok}/4 imágenes generadas")
    print(f"  Carpeta: {OUTPUT_DIR}")
    print("=" * 60)
    print()
    print("  Próximo paso: copiar las imágenes generadas a la")
    print("  carpeta img\\ de la presentación HTML.")

if __name__ == "__main__":
    main()
