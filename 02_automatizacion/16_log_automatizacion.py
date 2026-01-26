"""
16_log_automatizacion.py

Sistema básico de logging para scripts de automatización.
"""

import logging
import os
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN DEL LOG
# -----------------------------

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

fecha = datetime.now().strftime("%Y-%m-%d")

log_path = os.path.join(LOG_DIR, f"automatizacion_{fecha}.log")

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# -----------------------------
# FUNCIONES CON LOG
# -----------------------------

def crear_archivo_log(nombre):
    try:
        with open(nombre, "w") as f:
            f.write("Archivo creado correctamente")

        logging.info(f"Archivo creado: {nombre}")

    except Exception as e:
        logging.error(f"Error al crear archivo {nombre}: {e}")


def borrar_archivo_log(nombre):
    try:
        os.remove(nombre)
        logging.info(f"Archivo borrado: {nombre}")

    except FileNotFoundError:
        logging.warning(f"Archivo no encontrado: {nombre}")

    except Exception as e:
        logging.error(f"Error al borrar archivo {nombre}: {e}")


# -----------------------------
# EJECUCIÓN DE PRUEBA
# -----------------------------
if __name__ == "__main__":
    crear_archivo_log("archivo_log_test.txt")
    borrar_archivo_log("archivo_log_test.txt")

    print("📄 Operaciones registradas en el log")
