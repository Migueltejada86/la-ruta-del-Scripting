"""
Mini Proyecto - Mantenimiento Básico de PC

✔ Limpieza de temporales
✔ Eliminación de archivos viejos
✔ Backup automático
✔ Log completo
"""

import os
import shutil
import logging
import time
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN
# -----------------------------

TEMP_DIR = "temp"
BACKUP_DIR = "backup_mantenimiento"
LOG_DIR = "logs"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

log_file = os.path.join(
    LOG_DIR,
    f"mantenimiento_{datetime.now().strftime('%Y-%m-%d')}.log"
)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# FUNCIONES
# -----------------------------

def limpiar_temporales(dias=1):
    ahora = time.time()
    limite = dias * 86400

    for archivo in os.listdir(TEMP_DIR):
        ruta = os.path.join(TEMP_DIR, archivo)

        if os.path.isfile(ruta):
            if ahora - os.path.getmtime(ruta) > limite:
                os.remove(ruta)
                logging.info(f"Archivo temporal eliminado: {ruta}")


def backup_logs():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destino = os.path.join(BACKUP_DIR, f"logs_backup_{timestamp}")

    shutil.copytree(LOG_DIR, destino)
    logging.info("Backup de logs realizado")


# -----------------------------
# EJECUCIÓN
# -----------------------------

if __name__ == "__main__":
    limpiar_temporales(dias=1)
    backup_logs()

    print("🧹 Mantenimiento del sistema completado")
