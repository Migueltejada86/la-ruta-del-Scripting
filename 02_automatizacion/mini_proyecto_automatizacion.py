"""
Mini Proyecto - Automatización General

✔ Crea archivos
✔ Genera backups con fecha y hora
✔ Registra acciones en logs
"""

import os
import shutil
import logging
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

BASE_DIR = "proyecto_automatizacion"
BACKUP_DIR = os.path.join(BASE_DIR, "backups")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

fecha = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(LOG_DIR, f"automatizacion_{fecha}.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# FUNCIONES
# -----------------------------

def crear_archivo(nombre, contenido):
    with open(nombre, "w") as f:
        f.write(contenido)
    logging.info(f"Archivo creado: {nombre}")


def backup_archivo(ruta):
    if not os.path.exists(ruta):
        logging.warning(f"No existe el archivo: {ruta}")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_backup = f"{os.path.basename(ruta)}_{timestamp}.bak"
    destino = os.path.join(BACKUP_DIR, nombre_backup)

    shutil.copy(ruta, destino)
    logging.info(f"Backup creado: {destino}")


# -----------------------------
# EJECUCIÓN
# -----------------------------

if __name__ == "__main__":
    archivo = os.path.join(BASE_DIR, "archivo_principal.txt")

    os.makedirs(BASE_DIR, exist_ok=True)

    crear_archivo(archivo, "Archivo principal del proyecto")
    backup_archivo(archivo)

    print("✅ Automatización completada")
