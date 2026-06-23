# Caviaroli Argentina — Pipeline DTC

**Objetivo:** Activar `caviaroli.com.ar` como canal directo al consumidor (DTC) ingiriendo datos de `caviaroli.com`, aplicando rebrand visual con IA y priorizando el lote a vencer con descuento promocional.

Referencia estética y de plataforma: [tienda.havanna.com.ar](https://tienda.havanna.com.ar) (mismo stack TiendaNube).

---

## Estructura del proyecto

```
Caviaroli/
├── scripts/                        # Pipeline Python
│   ├── caviaroli_proyecto_completo.py   # Scraper completo caviaroli.com
│   ├── caviaroli_tiendanube_update.py   # Generador CSV para TiendaNube
│   ├── rebrand_imagenes.py              # Rebrand batch de fotos (gpt-image-1)
│   └── rebrand_test.py                  # Test editorial con 4 imágenes
│
├── presentaciones/                 # Decks HTML
│   ├── curso-imagenes-ia-nahuel.html    # Curso de fotografía con IA (10 módulos)
│   ├── presentacion-proyecto.html       # Deck técnico del proyecto
│   └── presentacion.html                # Versión anterior
│
├── img/                            # Imágenes editoriales AI
│   └── [imágenes generadas con ChatGPT/gpt-image-1]
│
├── data/                           # Archivos de trabajo local (no se commitean)
│   └── README.md
│
├── presentacion-final.html         # ← Deck ejecutivo principal (abrir este)
├── requirements.txt                # Dependencias Python
├── .env.example                    # Variables de entorno requeridas
└── .gitignore
```

---

## Setup local

```bash
# 1. Clonar
git clone https://github.com/volhotic-creator/Caviaroli.git
cd Caviaroli
git checkout claude/wonderful-edison-xuqgyi

# 2. Entorno virtual
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Dependencias
pip install -r requirements.txt

# 4. Variables de entorno
cp .env.example .env
# Editar .env con tus API keys reales
```

---

## Pipeline — 5 fases

### Fase 1 · Scraping de caviaroli.com
```bash
python scripts/caviaroli_proyecto_completo.py
# Output: data/productos_scrapeados.json
```
Extrae nombre, descripción, precio EUR, imágenes y variantes de los ~63 productos del sitio global.

### Fase 2 · Rebrand visual con IA
```bash
# Test con 4 imágenes editoriales
python scripts/rebrand_test.py

# Batch completo del catálogo
python scripts/rebrand_imagenes.py
```
Requiere `OPENAI_API_KEY`. Usa `gpt-image-1` para reencuadrar cada foto al estilo catálogo premium (fondo blanco, sombra suave, iluminación de estudio).

### Fase 3 · Generación CSV para TiendaNube
```bash
python scripts/caviaroli_tiendanube_update.py \
  --tc 1200 \
  --tiendanube data/tiendanube.csv \
  --vencimientos data/Caviaroli_Vencimientos.xlsx
# Output: data/caviaroli_actualizado.csv
```
Convierte precios EUR → ARS, aplica -20% al lote urgente (≤120 días), genera títulos y descripciones SEO con Claude.

### Fase 4 · Importación en TiendaNube
1. Panel TiendaNube → **Productos → Importar productos**
2. Subir `data/caviaroli_actualizado.csv`
3. Subir imágenes rebranded a cada producto

### Fase 5 · Google Shopping (orgánico)
- Verificar dominio en Google Search Console
- Conectar feed en Google Merchant Center
- 48 hs para que los productos aparezcan en Shopping

---

## Parámetros del script de actualización

| Parámetro | Descripción | Default |
|---|---|---|
| `--tc` | Tipo de cambio EUR → ARS **(requerido)** | — |
| `--descuento` | % descuento lote urgente | `20` |
| `--tiendanube` | CSV exportado de TiendaNube | `tiendanube.csv` |
| `--vencimientos` | Excel de vencimientos | `Caviaroli_Vencimientos.xlsx` |
| `--output` | Nombre del CSV de salida | `caviaroli_actualizado.csv` |
| `--dias-urgente` | Días para marcar urgente | `120` |
| `--dry-run` | Preview sin generar archivo | — |

---

## API Keys necesarias

| Key | Uso | Dónde obtener |
|---|---|---|
| `OPENAI_API_KEY` | Rebrand de imágenes (gpt-image-1) | platform.openai.com/api-keys |
| `ANTHROPIC_API_KEY` | SEO con IA (Claude) | console.anthropic.com |

Copiar `.env.example` → `.env` y completar. **Nunca commitear el `.env`.**

---

## Presentación ejecutiva

Abrir `presentacion-final.html` en el navegador para ver el deck completo de 10 slides que cubre contexto, urgencia comercial, pipeline técnico y roadmap de 7 días.

---

## Urgencia comercial

Hay un **lote a vencer en ≤120 días**. Estrategia:
- Precio con **-20% automático** vía precio promocional en TiendaNube
- Canal DTC directo (sin intermediarios)
- Activación inmediata sin depender de distribución tradicional
