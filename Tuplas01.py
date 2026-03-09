# ¡Bienvenido al mundo de las Tuplas en Python!
# Una tupla es una colección de elementos ordenados que NO se pueden modificar.
# Piensa en ellas como una lista de solo lectura. Se definen con paréntesis ().

# --- 1. Creando nuestra primera tupla ---
# Vamos a crear una tupla con los días de la semana.
import os

dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

os.system('clear' if os.name != 'nt' else 'cls')

print("Esta es nuestra tupla de días de la semana:")
print(dias_semana)
print("-" * 30)

# --- 2. Accediendo a los elementos de la tupla ---
# Podemos acceder a un día específico usando su posición (índice), que empieza en 0.
primer_dia = dias_semana[0]
tercer_dia = dias_semana[2]

print(f"El primer día de la semana es: {primer_dia}")
print(f"El tercer día de la semana es: {tercer_dia}")
print("-" * 30)

# --- 3. La principal característica: ¡Son inmutables! ---
# Si intentamos cambiar un valor, Python nos dará un error.
# Descomenta la siguiente línea para ver lo que sucede:
# dias_semana[0] = "Lunes Festivo"  # Esto generará un TypeError

print("¿Podemos cambiar la tupla? No, es inmutable.")
print("Esto es útil para datos que no deben cambiar nunca.")
print("-" * 30)

# --- 4. Desempaquetado de tuplas ---
# Podemos asignar los valores de la tupla a variables individuales.
dia1, dia2, dia3, _, _, _, _ = dias_semana
print(f"Los tres primeros días son: {dia1}, {dia2}, y {dia3}.")
