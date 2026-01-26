"""
06_bucle_tareas.py
Ejecuta una tarea repetida varias veces automáticamente.
"""

for i in range(1, 6):
    nombre_archivo = f"archivo_{i}.txt"
    
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"Este es el archivo número {i}\n")
    
    print(f"{nombre_archivo} creado")
