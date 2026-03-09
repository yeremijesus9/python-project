import os

# Tuplas: Coordenadas Inmutables

# --- 1. Definiendo coordenadas con tuplas ---
# Una tupla es ideal para representar datos que forman un conjunto fijo,
# como las coordenadas (x, y) o (x, y, z).
punto_2d = (10, 20)
punto_3d = (5, -3, 12)

os.system('clear' if os.name != 'nt' else 'cls')

print("Ejemplos de coordenadas como tuplas:")
print(f"Coordenada en 2D: {punto_2d}")
print(f"Coordenada en 3D: {punto_3d}")
print("-" * 30)

# --- 2. Accediendo y desempaquetando coordenadas ---
# Podemos acceder a cada eje por su índice.
eje_x = punto_2d[0]
eje_y = punto_2d[1]

print(f"El valor del eje X en 2D es: {eje_x}")
print(f"El valor del eje Y en 2D es: {eje_y}")
print("-" * 30)

# El desempaquetado es aún más intuitivo para las coordenadas.
x, y, z = punto_3d
print("Desempaquetando la tupla 3D:")
print(f"Valor de x: {x}")
print(f"Valor de y: {y}")
print(f"Valor de z: {z}")
print("-" * 30)

# --- 3. Inmutabilidad en acción ---
# Si intentamos reasignar una coordenada, obtendremos un error.
# Esto garantiza que un "punto" no pueda ser alterado accidentalmente.
# punto_2d[0] = 15  # Esto generaría un TypeError

print("Las coordenadas son fijas y no se pueden cambiar.")
print("Si necesitas un nuevo punto, creas una nueva tupla.")
nuevo_punto_2d = (15, 25)
print(f"Punto original: {punto_2d}, Nuevo punto: {nuevo_punto_2d}")
print("-" * 30)

# --- 4. Tuplas en listas: Un conjunto de puntos ---
# Podemos tener una lista de tuplas para representar una ruta o una figura.
ruta = [(0, 0), (1, 2), (3, 3), (5, 1)]

print("Ruta definida por una lista de tuplas (puntos):")
for i, punto in enumerate(ruta):
    print(f"  Punto {i+1}: {punto}")

print("\nAccediendo al segundo punto de la ruta:")
segundo_punto = ruta[1]
print(f"El segundo punto es {segundo_punto} y su coordenada Y es {segundo_punto[1]}.")