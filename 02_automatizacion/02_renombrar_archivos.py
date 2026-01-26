"""
02_renombrar_archivos.py
Renombra un archivo existente automáticamente.
"""

import os

nombre_actual = "archivo_creado.txt"
nuevo_nombre = "archivo_renombrado.txt"

if os.path.exists(nombre_actual):
    os.rename(nombre_actual, nuevo_nombre)
    print(f"Archivo renombrado a ´{nuevo_nombre}")
else:
    print("El archivo no existe, no se puede renombrar.")