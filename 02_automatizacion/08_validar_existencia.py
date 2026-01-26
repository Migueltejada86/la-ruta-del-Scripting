"""
08_validar_existencia.py
Valida la existencia de archivos y carpetas antes de operar.
"""

import os

ruta_archivo = "archivo_prueba.txt"
ruta_carpeta = "carpeta_prueba"

# Validar archivo
if os.path.exists(ruta_archivo):
    if os.path.isfile(ruta_archivo):
        print(f"El archivo '{ruta_archivo}' existe.")
else:
    print(f"El archivo '{ruta_archivo}' NO existe.")

# Validar carpeta
if os.path.exists(ruta_carpeta):
    if os.path.isdir(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' existe.")
else:
    print(f"La carpeta '{ruta_carpeta}' NO existe.")
