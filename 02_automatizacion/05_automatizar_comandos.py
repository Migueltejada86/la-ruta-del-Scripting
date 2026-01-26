"""
05_automatizar_comandos.py
Ejecuta comandos del sistema operativo desde Python.
"""

import os

print("Listando archivos del directorio actual:\n")

# Comando para Windows
os.system("dir")

# Si estuvieras en Linux/Mac usarías:
# os.system("ls")
