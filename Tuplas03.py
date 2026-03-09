# Tuplas: Dibujando con Coordenadas ASCII

# --- 1. Definiendo la forma con tuplas ---
# Usaremos un conjunto de tuplas para representar los píxeles de nuestro dibujo.
# Cada tupla es un punto (x, y) inmutable en un lienzo imaginario.
# Usar un conjunto ({}) es eficiente para comprobar si un punto existe.

puntos_casa = {
    # Techo (triángulo)
    (4, 0), (3, 1), (5, 1),
    (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),

    # Paredes
    (2, 3), (6, 3),
    (2, 4), (6, 4),

    # Base
    (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)
}

print("Dibujando una figura usando un conjunto de tuplas como coordenadas.")
print("-" * 40)

# --- 2. Calculando el tamaño del lienzo ---
# Para saber qué tan grande debe ser nuestro dibujo, encontramos las coordenadas
# máximas 'x' e 'y' de nuestra figura.
ancho_lienzo = max(p[0] for p in puntos_casa) + 2
alto_lienzo = max(p[1] for p in puntos_casa) + 2

# --- 3. Renderizando el dibujo ASCII ---
# Recorremos cada "píxel" de nuestro lienzo, fila por fila.
print("Resultado del dibujo ASCII:")

for y in range(alto_lienzo):
    linea_para_imprimir = ""
    for x in range(ancho_lienzo):
        punto_actual = (x, y)
        if punto_actual in puntos_casa:
            linea_para_imprimir += "* "
        else:
            linea_para_imprimir += "  "
    print(linea_para_imprimir)

print("\n" + "-" * 40)
print("Cada '*' representa una tupla de coordenadas (x, y) en el lienzo.")