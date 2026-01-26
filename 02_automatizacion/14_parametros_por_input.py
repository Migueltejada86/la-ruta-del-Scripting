"""
14_parametros_por_input.py

Script interactivo.
El usuario decide:
- nombre base
- carpeta destino
- cantidad de archivos
- contenido

Ideal para automatización real y uso general.
"""

from datetime import datetime
import os

# -----------------------------
# INPUT DEL USUARIO
# -----------------------------

nombre_base = input("📄 Nombre base del archivo: ").strip()
carpeta_destino = input("📂 Carpeta destino: ").strip()
extension = input("🧩 Extensión (ej: .txt): ").strip()

cantidad = int(input("🔢 Cantidad de archivos a crear: "))
contenido = input("✏️ Contenido del archivo: ")

# -----------------------------
# VALIDACIONES BÁSICAS
# -----------------------------

if not extension.startswith("."):
    extension = "." + extension

if cantidad <= 0:
    print("❌ La cantidad debe ser mayor a 0")
    exit()

# -----------------------------
# CREAR CARPETA SI NO EXISTE
# -----------------------------

if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
    print(f"📁 Carpeta creada: {carpeta_destino}")

# -----------------------------
# CREAR ARCHIVOS
# -----------------------------

for i in range(1, cantidad + 1):

    fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    nombre_archivo = f"{nombre_base}_{fecha_hora}_{i}{extension}"
    ruta = os.path.join(carpeta_destino, nombre_archivo)

    with open(ruta, "w") as archivo:
        archivo.write(contenido + "\n")

    print(f"✅ Archivo creado: {ruta}")

print("\n🚀 Proceso finalizado correctamente")
