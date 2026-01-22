"""
Mini Proyecto FASE 1
Script: Backup automático de archivos
Autor: Miguel Tejada
Objetivo:
- Leer un archivo existente
- Crear una copia con fecha
- Usar funciones, if y librerías estándar
"""

import shutil
from datetime import datetime
import os


def crear_backup(archivo_origen):
    # Verificamos si el archivo existe
    if not os.path.exists(archivo_origen):
        print("❌ El archivo no existe")
        return

    # Obtenemos fecha actual
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Nombre del backup
    backup = f"backup_{fecha}_{archivo_origen}"

    # Copiamos el archivo
    shutil.copy(archivo_origen, backup)

    print(f"✅ Backup creado: {backup}")


# Programa principal
archivo = input("Ingrese el nombre del archivo a respaldar: ")
crear_backup(archivo)
