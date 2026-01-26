"""
13_nombres_dinamicos.py

Este script genera archivos con nombres dinámicos usando:
- nombre base
- fecha
- hora
- contador automático

Ideal para logs, backups, reportes y automatización.
"""

from datetime import datetime
import os

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

CARPETA_SALIDA = "archivos_generados"
NOMBRE_BASE = "reporte"
EXTENSION = ".txt"

# Cantidad de archivos a crear
CANTIDAD = 3

# -----------------------------
# CREAR CARPETA SI NO EXISTE
# -----------------------------

if not os.path.exists(CARPETA_SALIDA):
    os.makedirs(CARPETA_SALIDA)

# -----------------------------
# GENERAR ARCHIVOS
# -----------------------------

for i in range(1, CANTIDAD + 1):

    fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    nombre_archivo = f"{NOMBRE_BASE}_{fecha_hora}_{i}{EXTENSION}"
    ruta_completa = os.path.join(CARPETA_SALIDA, nombre_archivo)

    with open(ruta_completa, "w") as archivo:
        archivo.write(f"Archivo generado automáticamente\n")
        archivo.write(f"Nombre: {nombre_archivo}\n")
        archivo.write(f"Iteración: {i}\n")

    print(f"✅ Archivo creado: {ruta_completa}")
