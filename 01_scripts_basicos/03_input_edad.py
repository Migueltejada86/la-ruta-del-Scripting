"""
Script: Ingreso de edad
Objetivo:
- Convertir texto a número
- Entender tipos de datos (str, int)
"""
edad = int(input("¿Qué edad tenés? "))
# input siempre devuelve texto (str)
# Convertimos a entero para poder usarlo como número

if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")



