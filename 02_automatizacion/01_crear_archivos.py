"""
Docstring for 02_automatizacion.01_crear_archivos
Crea un archivo automaticamente y escribe contenido dentro 
"""

# Nombre del archivo a crear
nombre_archivo = "archivo_creado.txt"

# Contenido que se va a escribir

contenido = "Este archivo fue creado automaticamente con Python"

# Abrimos (o creamos) el archivo en modo escritura
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print(f"Archivo ´{nombre_archivo} creado correcatamente.")