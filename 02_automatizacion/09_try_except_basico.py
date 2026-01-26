"""
09_try_except_basico.py
Maneja errores comunes sin que el script se rompa.
"""

archivo = "archivo_inexistente.txt"

try:
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe.")

except Exception as error:
    print(f"Ocurrió un error inesperado: {error}")
