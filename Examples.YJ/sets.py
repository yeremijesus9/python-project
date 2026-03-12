# ==========================================
# DEMOSTRACIÓN DE SETS (CONJUNTOS) EN PYTHON
# ==========================================

# 1. ¿QUÉ ES UN SET?
# un set es una colección desordenada de elementos únicos 
# no permite duplicados y no mantiene un orden específico

# ------------------------------------------
# PUNTO 1: creación de un Set
# ------------------------------------------
# se pueden crear usando llaves {} o la función set()
frutas = {"manzana", "pera", "plátano"}
print("1. conjunto original:", frutas)

# crear un conjunto vacío (debe usar set(), ya que {} crea un diccionario)
vacio = set()
print("   conjunto vacío:", vacio)


# ------------------------------------------
# PUNTO 2: eliminación automática de duplicados
# ------------------------------------------
# si intentamos añadir elementos repetidos, el set los ignora
numeros_lista = [1, 2, 2, 3, 4, 4, 4, 5]
numeros_set = set(numeros_lista)
print("\n2. lista con duplicados:", numeros_lista)
print("   set resultante (sin duplicados):", numeros_set)


# ------------------------------------------
# PUNTO 3: añadir y eliminar elementos
# ------------------------------------------
# .add() para un solo elemento
frutas.add("naranja")

# .update() para múltiples elementos
frutas.update(["mango", "uva"])

# .remove() elimina un elemento (lanza error si no existe)
# .discard() elimina un elemento (NO lanza error si no existe)
frutas.discard("pera")

print("\n3. frutas después de modificaciones:", frutas)


# ------------------------------------------
# PUNTO 4: operaciones matemáticas de conjuntos
# ------------------------------------------
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("\n4. operaciones entre conjunto a", a, "y conjunto b", b)

# unión: elementos en A o en B
print("   unión (a | b):", a | b)

# intersección: elementos en ambos (repetidos)
print("   intersección (a & b):", a & b)

# diferencia: elementos en A pero no en B (saca los elementos de un lado que no estan en el otro)
print("   diferencia (a - b):", a - b)

# diferencia simétrica: elementos en A o en B, pero no en ambos (los elementos que estan en ambos)
print("   diferencia simétrica (a ^ b):", a ^ b)


# ------------------------------------------
# PUNTO 5: pertenencia (super rápido)
# ------------------------------------------
# los sets son mucho más rápidos que las listas para comprobar si algo existe
print("\n5. ¿Está 'manzana' en el set de frutas?", "manzana" in frutas)
print("   ¿Está 'pera' en el set de frutas?", "pera" in frutas)


# ------------------------------------------
# PUNTO 6: recorrer un set
# ------------------------------------------
print("\n6. Recorriendo el set (el orden puede variar):")
for fruta in frutas:
    print(f"   - {fruta}")
