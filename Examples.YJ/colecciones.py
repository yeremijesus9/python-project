# EJEMPLOS DE MÉTODOS DE COLECCIONES

# 1. como crear una lista
print("--- 1. Cómo crear ---")
mi_lista = [10, 20, 30, 40]
print("Lista inicial:", mi_lista)

# 2. como acceder a los elementos
print("\n--- 2. Cómo acceder ---")
# accediendo al primer elemento (índice 0)
primer_elemento = mi_lista[0]
print("Primer elemento:", primer_elemento)
# accediendo al último elemento (índice -1)
ultimo_elemento = mi_lista[-3]
print("Último elemento:", ultimo_elemento)

# 3. como modificar (añadir elementos)
print("\n--- 3. Cómo modificar (añadir) ---")
# usando append(): Añade UN SOLO elemento al final de la lista
mi_lista.append(50)
print("Lista después de append(50):", mi_lista)

# usando extend(): Añade MÚLTIPLES elementos (otra colección) al final
otra_lista = [60, 70]
mi_lista.extend(otra_lista)
print("Lista después de extend([60, 70]):", mi_lista)

# 4. como borrar elementos
print("\n--- 4. Cómo borrar ---")
# usando remove(): Elimina la primera aparición de un valor específico
mi_lista.remove(30)
print("Lista después de remove(30):", mi_lista)

# extra: Usando pop() para eliminar por índice (por defecto el último)
elemento_borrado = mi_lista.pop(2)
print("Lista después de pop() (elimina el último):", mi_lista)
print("Elemento que fue borrado con pop:", elemento_borrado)
