import os

# Listas en Python: Gestionando tu Lista de la Compra

# --- 1. Creando nuestra lista de la compra inicial ---
# Una lista es una colección ordenada y MODIFICABLE de elementos.
# Se definen con corchetes [].
lista_compra = ["Leche", "Huevos", "Pan", "Manzanas"]

os.system('clear' if os.name != 'nt' else 'cls')

print("🛒 Mi lista de la compra inicial:")
print(lista_compra)
print("-" * 30)

# --- 2. Añadiendo elementos a la lista ---
# Podemos añadir un elemento al final con .append()
print("Voy a añadir 'Pollo' al final de la lista...")
lista_compra.append("Pollo")
print(lista_compra)
print("-" * 30)

# O podemos insertar un elemento en una posición específica con .insert()
print("¡Oh! Se me olvidó el 'Queso' después de la 'Leche'. Lo inserto en la posición 1.")
lista_compra.insert(1, "Queso")
print(lista_compra)
print("-" * 30)

# --- 3. Eliminando elementos de la lista ---
# Si sabemos qué elemento queremos quitar, usamos .remove()
print("Ya he cogido el 'Pan', así que lo quito de la lista.")
lista_compra.remove("Pan")
print(lista_compra)
print("-" * 30)

# Si queremos quitar el último elemento (o uno por su posición), usamos .pop()
print("El último producto añadido, 'Pollo', lo quito con .pop().")
ultimo_elemento = lista_compra.pop()
print(f"He quitado '{ultimo_elemento}'. La lista ahora es: {lista_compra}")
print("-" * 30)

# --- 4. Accediendo y modificando elementos ---
# Accedemos a un elemento por su índice (empezando en 0)
print(f"El primer producto de mi lista es: {lista_compra[0]}")

# Las listas son mutables, así que podemos cambiar un elemento
print("Voy a cambiar 'Manzanas' por 'Naranjas'.")
lista_compra[3] = "Naranjas" # Manzanas estaba en la posición 3
print("Lista actualizada:")
print(lista_compra)
print("-" * 30)

# --- 5. Comprobando si un artículo está en la lista ---
articulo_a_buscar = "Leche"
if articulo_a_buscar in lista_compra:
    print(f"✅ Sí, '{articulo_a_buscar}' está en la lista.")
else:
    print(f"❌ No, '{articulo_a_buscar}' no está en la lista.")
print("-" * 30)

# --- 6. Ordenando la lista ---
print("Ahora voy a ordenar la lista alfabéticamente.")
lista_compra.sort()
print(lista_compra)
print("-" * 30)

# --- 7. Recorriendo la lista para mostrarla ---
print("🛒 Resumen final de la compra:")
for i, producto in enumerate(lista_compra):
    print(f"  {i+1}. {producto}")
print("-" * 30)

# --- 8. Vaciando la lista ---
print("¡Compra terminada! Vaciando la lista...")
lista_compra.clear()
print(f"La lista ahora contiene {len(lista_compra)} productos.")
print(lista_compra)