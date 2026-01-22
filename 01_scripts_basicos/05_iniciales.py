"""
Script: Iniciales del usuario
Objetivo:
- Manipulación básica de strings
- Acceso a caracteres por índice
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Accedemos al primer carácter de cada string
iniciales = nombre[0] + apellido[0]

print(f"Sus iniciales son: {iniciales.upper()}")
