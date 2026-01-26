"""
11_rutas_absolutas_relativas.py
Diferencia entre rutas absolutas y relativas.
"""

import os

# Ruta relativa
ruta_relativa = "archivo.txt"
print("Ruta relativa:", ruta_relativa)

# Convertir a absoluta
ruta_absoluta = os.path.abspath(ruta_relativa)
print("Ruta absoluta:", ruta_absoluta)

# Ruta del script actual
ruta_script = os.path.dirname(__file__)
print("Carpeta del script:", ruta_script)

# Ruta absoluta segura desde el script
ruta_segura = os.path.join(ruta_script, "archivo.txt")
print("Ruta segura:", ruta_segura)

