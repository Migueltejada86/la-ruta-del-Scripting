"""
07_funciones_utiles.py
Define funciones reutilizables para automatización.
"""

def crear_archivo(nombre, contenido):
    """
    Crea un archivo con el contenido indicado.
    """
    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print(f"Archivo '{nombre}' creado.")


def saludar(nombre):
    print(f"Hola {nombre}")


# Uso de las funciones
crear_archivo("funcion.txt", "Archivo creado usando una función\n")
saludar("Miguel")
