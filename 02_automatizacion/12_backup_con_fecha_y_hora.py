"""
12_backup_con_fecha_y_hora.py

Este script crea un backup automático de un archivo o carpeta,
agregando la fecha y hora al nombre para evitar sobreescrituras.

"""

import shutil
import os
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

# Archivo o carpeta a respaldar
ORIGEN = "datos_importantes.txt"   # puede ser archivo o carpeta

# Carpeta donde se guardan los backups
CARPETA_BACKUP = "backup"

# -----------------------------
# CREAR CARPETA BACKUP SI NO EXISTE
# -----------------------------

if not os.path.exists(CARPETA_BACKUP):
    os.makedirs(CARPETA_BACKUP)

# -----------------------------
# OBTENER FECHA Y HORA ACTUAL
# -----------------------------

fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# -----------------------------
# CREAR NOMBRE DEL BACKUP
# -----------------------------

nombre_original = os.path.basename(ORIGEN)
nombre_backup = f"{nombre_original}_backup_{fecha_hora}"

ruta_backup = os.path.join(CARPETA_BACKUP, nombre_backup)

# -----------------------------
# REALIZAR BACKUP
# -----------------------------

try:
    if os.path.isfile(ORIGEN):
        shutil.copy2(ORIGEN, ruta_backup)
        print(f"✅ Backup de archivo creado: {ruta_backup}")

    elif os.path.isdir(ORIGEN):
        shutil.copytree(ORIGEN, ruta_backup)
        print(f"✅ Backup de carpeta creado: {ruta_backup}")

    else:
        print("❌ El archivo o carpeta de origen no existe.")

except Exception as error:
    print("⚠️ Error al crear el backup:", error)
