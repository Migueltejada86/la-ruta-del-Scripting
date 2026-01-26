"""
10_trabajar_con_rutas.py
Uso correcto de rutas en Python.
"""

import os

# Ruta actual
ruta_actual = os.getcwd()
print("Ruta actual:", ruta_actual)

# Crear ruta segura
ruta_archivo = os.path.join(ruta_actual, "archivo.txt")
print("Ruta completa:", ruta_archivo)

# Separar nombre y carpeta
print("Nombre del archivo:", os.path.basename(ruta_archivo))
print("Carpeta contenedora:", os.path.dirname(ruta_archivo))
