# El Quijote con Letras de Colores
# Este script imprime las primeras frases de "El Quijote" en la consola,
# coloreando cada letra de forma aleatoria y con un efecto de escritura.

import time
import random
import os

# --- 1. Definición de colores usando códigos de escape ANSI ---
# Estos códigos le dicen a la terminal que cambie el color del texto.
class Colores:
    RESET = '\033[0m'       # Vuelve al color por defecto
    ROJO = '\033[91m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIAN = '\033[96m'

# Creamos una lista con los colores para poder elegir uno al azar fácilmente.
LISTA_COLORES = [Colores.ROJO, Colores.VERDE, Colores.AMARILLO, Colores.AZUL, Colores.MAGENTA, Colores.CIAN]

# --- 2. El texto a mostrar ---
texto_quijote = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."

# --- 3. Función para imprimir con efecto ---
def imprimir_con_colores(texto, velocidad=0.05):
    """Imprime el texto letra por letra, asignando un color aleatorio a cada una."""
    for caracter in texto:
        color_aleatorio = random.choice(LISTA_COLORES)
        print(color_aleatorio + caracter, end='', flush=True)
        time.sleep(velocidad)
    print(Colores.RESET) # Importante resetear el color al final.

os.system('clear' if os.name != 'nt' else 'cls')
print("Mostrando las primeras frases del Quijote...\n")
imprimir_con_colores(texto_quijote)
print("\n\n¡Fin!")