import os

# Nuestra despensa de comida
comida = ["🍕", "🍔", "🌮", "🍣", "🍦", "🍩", "🍪", "🍓", "🍍", "🥑"]

# 3. Aplicamos el Slicing basico
SubListaBase = comida[2:5]
#Desde el inicio
DesdeInicio = comida[:4]
#HastaElFinal
HastaElFinal = comida[6:]
#Con Paso
ConPaso = comida[::3]
#InvertirLista
ListaInvertida=comida[::-1]
#Indices negativos 
ListaNegativo = comida[-3:]

os.system('clear' if os.name != 'nt' else 'cls')

print("\n"*2)
print(f"Buffet completo hoy: {comida}")
print("\n")
print(f"slicing Sub Lista Basica: {SubListaBase}")
print("\n")
print(f"slicing desde el inicio: {DesdeInicio}")
print("\n")
print(f"slicing Hasta El Final: {HastaElFinal}")
print("\n")
print(f"slicing con paso o salto: {ConPaso}")
print("\n")
print(f"slicing ListaInvertida: {ListaInvertida}")
print("\n")
print(f"slicing Negativo: {ListaNegativo}")
print("\n")
