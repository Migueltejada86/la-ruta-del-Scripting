"""
15_parametros_por_funcion.py

Funciones reutilizables para crear archivos automáticamente.
Pensado para ser importado desde otros scripts.
"""

import os
from datetime import datetime


def crear_archivo(
    nombre_base,
    carpeta,
    contenido,
    extension=".txt",
    agregar_fecha=True
):
    """
    Crea un archivo con nombre dinámico.

    :param nombre_base: nombre base del archivo
    :param carpeta: carpeta destino
    :param contenido: texto a escribir
    :param extension: extensión del archivo
    :param agregar_fecha: si agrega fecha y hora al nombre
    """

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    if agregar_fecha:
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"{nombre_base}_{fecha}{extension}"
    else:
        nombre_archivo = f"{nombre_base}{extension}"

    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, "w") as f:
        f.write(contenido)

    return ruta


# -----------------------------
# PRUEBA DIRECTA (opcional)
# -----------------------------
if __name__ == "__main__":
    ruta_creada = crear_archivo(
        nombre_base="reporte",
        carpeta="salida_funcion",
        contenido="Archivo creado desde una función"
    )

    print(f"✅ Archivo creado en: {ruta_creada}")
