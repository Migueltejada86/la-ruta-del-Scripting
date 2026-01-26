"""
04_listar_archivos.py
Lista archivos de una carpeta y los filtra por extensión.
"""

import os

ruta = "archivos_movidos"
extension = ".txt"

if os.path.exists(ruta):
    archivos = os.listdir(ruta)
    
    print("Archivos encontrados:")
    for archivo in archivos:
        if archivo.endswith(extension):
            print(f"- {archivo}")
else:
    print("La carpeta no existe.")
