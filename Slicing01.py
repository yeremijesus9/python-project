import random

# Nuestra despensa de comida
comida = ["🍕", "🍔", "🌮", "🍣", "🍦", "🍩", "🍪", "🍓", "🍍", "🥑"]

# 1. Mezclamos todo (Shuffle) para que el orden sea sorpresa
random.shuffle(comida) 

# 2. Elegimos índices aleatorios para el corte
inicio = random.randint(0, 5)
fin = random.randint(inicio + 1, len(comida))
salto = random.choice([1, 2]) # A veces normal, a veces saltando uno

# 3. Aplicamos el Slicing aleatorio
plato_sorpresa = comida[inicio:fin:salto]

print(f"Buffet completo hoy: {comida}")
print(f"Corte aplicado: [{inicio}:{fin}:{salto}]")
print(f"Tu plato es: {plato_sorpresa}")