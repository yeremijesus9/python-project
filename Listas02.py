# Loteria Primitiva: Generador de Números Aleatorios
# Este script simula un sorteo de la Lotería Primitiva, generando los números necesarios.

import random

# --- 1. Definir los parámetros del sorteo ---
# La Lotería Primitiva en España consiste en elegir 6 números de un bombo de 49.
CANTIDAD_NUMEROS_PRINCIPALES = 6
NUMERO_MINIMO = 1
NUMERO_MAXIMO = 49

print("🍀 ¡Mucha suerte en el sorteo de la Lotería Primitiva! 🍀")
print("-" * 50)

# --- 2. Generar los 6 números principales ---
# Usamos `random.sample` para obtener 6 números únicos del rango 1-49.
# `range(NUMERO_MINIMO, NUMERO_MAXIMO + 1)` crea una secuencia de 1 a 49.
bombo_principal = range(NUMERO_MINIMO, NUMERO_MAXIMO + 1)
numeros_principales = random.sample(bombo_principal, CANTIDAD_NUMEROS_PRINCIPALES)

# Ordenamos los números para que sea más fácil leerlos.
numeros_principales.sort()

print("Los 6 números de la combinación ganadora son:")
print(numeros_principales)
print("-" * 50)

# --- 3. Generar el número Complementario (C) ---
# El complementario es un número adicional del mismo bombo (1-49),
# que no puede ser uno de los 6 números principales.
while True:
    complementario = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)
    if complementario not in numeros_principales:
        break

print("El número Complementario (C) es:")
print(complementario)
print("-" * 50)

# --- 4. Generar el número del Reintegro (R) ---
# El reintegro es un número del 0 al 9, elegido de un bombo diferente.
reintegro = random.randint(0, 9)

print("El número del Reintegro (R) es:")
print(reintegro)
print("-" * 50)

print("\n¡A comprobar tus boletos!")