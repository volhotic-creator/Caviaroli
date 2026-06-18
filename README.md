# Caviaroli — Script de actualización masiva Tiendanube

## Qué hace

Toma el CSV exportado de Tiendanube y el Excel de vencimientos, y genera un CSV listo para importar con:

- **Precios en ARS** convertidos desde EUR con el tipo de cambio que confirmes
- **Precio promocional** automático para productos con vencimiento próximo (descuento configurable)
- **Título SEO y Descripción SEO** generados por IA (Claude) para cada producto, orientados a búsqueda argentina

---

## Instalación

```bash
pip install pandas openpyxl anthropic
```

Configurar la API key de Anthropic:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

---

## Uso básico

```bash
python caviaroli_tiendanube_update.py \
  --tc 1100 \
  --tiendanube tiendanube646256...csv \
  --vencimientos Caviaroli_Vencimientos.xlsx
```

Esto genera `caviaroli_actualizado.csv` listo para importar.

---

## Parámetros

| Parámetro | Descripción | Default |
|---|---|---|
| `--tc` | Tipo de cambio EUR → ARS **(requerido)** | — |
| `--descuento` | % descuento para lote urgente | `20` |
| `--tiendanube` | CSV exportado de Tiendanube | `tiendanube.csv` |
| `--vencimientos` | Excel de vencimientos | `Caviaroli_Vencimientos.xlsx` |
| `--output` | Nombre del CSV de salida | `caviaroli_actualizado.csv` |
| `--dias-urgente` | Días para marcar como urgente | `120` |
| `--dry-run` | Preview sin generar archivo | — |

---

## Ejemplo con todos los parámetros

```bash
python caviaroli_tiendanube_update.py \
  --tc 1200 \
  --descuento 25 \
  --tiendanube tiendanube646256...csv \
  --vencimientos Caviaroli_Vencimientos.xlsx \
  --output caviaroli_julio2026.csv \
  --dias-urgente 90
```

---

## Dry run (preview sin generar archivo)

```bash
python caviaroli_tiendanube_update.py --tc 1100 --dry-run \
  --tiendanube tiendanube646256...csv \
  --vencimientos Caviaroli_Vencimientos.xlsx
```

---

## Sin API key (modo placeholder)

Si no tenés la API key de Anthropic configurada, el script igual genera el CSV con precios correctos pero con títulos y descripciones SEO de placeholder. Podés completar el SEO después.

---

## Importar en Tiendanube

1. Ir a **Productos → Importar productos**
2. Subir el CSV generado
3. Confirmar la importación
4. Esperar 48 hs a que Google Merchant Center sincronice el feed

---

## Dependencias entre tasks

```
Task 03 (este script) → importar CSV en Tiendanube → Task 04 (Google Shopping)
```

Sin precios cargados, Google rechaza los productos del feed de Shopping.

---

## Archivos necesarios

- `tiendanube646256...csv` — exportar desde Tiendanube → Productos → Exportar
- `Caviaroli_Vencimientos.xlsx` — el Excel de inventario/vencimientos
- `ANTHROPIC_API_KEY` — en variable de entorno (para SEO con IA)
