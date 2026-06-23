# /data

Carpeta para archivos de trabajo locales. No se commitean al repo.

## Archivos esperados

| Archivo | Origen | Descripción |
|---|---|---|
| `tiendanube.csv` | TiendaNube → Productos → Exportar | Catálogo actual de la tienda |
| `Caviaroli_Vencimientos.xlsx` | Inventario propio | Fechas de vencimiento por producto |
| `caviaroli_actualizado.csv` | Output del script | CSV listo para importar en TiendaNube |
| `productos_scrapeados.json` | Output del scraper | Data cruda de caviaroli.com |

## .gitignore

Los archivos `.csv`, `.xlsx` y `.json` de esta carpeta están ignorados por git
para no commitear datos sensibles de inventario o precios.
