"""
Script: Escritura y lectura de archivos
Objetivo:
- Crear archivos
- Escribir texto
- Leer contenido
- Usar with (buena práctica)
"""

# Guardar texto en un archivo
with open("archivo.txt", "w") as f:
    f.write("Esto es un script que guarda texto.")

# Leer el archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)

"""
Notas:
- "w" = write (crea o sobrescribe)
- "r" = read
- with cierra el archivo automáticamente
"""
