"""
03_mover_archivos.py
Mueve un archivo a otra carpeta.
"""

import shutil
import os

archivo = "archivo_renombrado.txt"
carpeta_destino = "archivos_movidos"

# Crear carpeta si no existe
os.makedirs(carpeta_destino, exist_ok=True)

if os.path.exists(archivo):
    shutil.move(archivo, carpeta_destino)
    print("Archivo movido correctamente.")
else:
    print("El archivo no existe.")
