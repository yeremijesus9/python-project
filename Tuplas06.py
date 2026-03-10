# Animación de Texto en la Consola
# Este script muestra cómo crear una animación simple de texto en la consola.
# La palabra "German" se moverá de izquierda a derecha, ahora con letras grandes.

import os
import time

# --- 1. Función para limpiar la pantalla de la consola ---
# Esto nos permite "refrescar" la animación en cada paso.
def limpiar_pantalla():
    """Limpia la pantalla de la consola, compatible con Windows, Mac y Linux."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Mac y Linux (os.name es 'posix')
        os.system('clear')

# --- 2. Definición de letras grandes (ASCII Art) ---
LETRAS_GRANDES = {
    'G': [" GGG ", "G   G", "G GGG", "G   G", " GGG "],
    'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
    'R': ["RRRR ", "R   R", "RRRR ", "R  R ", "R   R"],
    'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    'A': [" AAA ", "A   A", "AAAAA", "A   A", "A   A"],
    'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"]
}
ALTO_LETRA = 5
ANCHO_LETRA = 5 # Cada letra tiene 5 caracteres de ancho

# --- 3. Configuración de la animación ---
palabra = "GERMAN" # Usamos mayúsculas para que coincida con el diccionario
ancho_terminal = 80  # Aumentamos el ancho para la palabra más grande
velocidad = 0.075    # Tiempo en segundos entre cada "frame" de la animación

# --- 4. Bucle de animación ---
# El bucle se ejecutará para mover la palabra a través de la pantalla.
try:
    print("Iniciando animación... Presiona Ctrl+C para salir.")
    time.sleep(2) # Una pequeña pausa antes de empezar

    # Calculamos el ancho total de la palabra en formato ASCII grande
    ancho_palabra_grande = len(palabra) * ANCHO_LETRA

    # El rango va desde 0 hasta el borde derecho, sin que la palabra se salga.
    for posicion in range(ancho_terminal - ancho_palabra_grande + 1):
        limpiar_pantalla()

        # Creamos los espacios en blanco para el desplazamiento
        espacios = ' ' * posicion

        # Dibujamos la palabra grande, construyendo cada una de sus 5 líneas
        for i in range(ALTO_LETRA):
            linea_para_imprimir = espacios
            for letra in palabra:
                # Concatenamos la fila 'i' de cada letra en la palabra
                linea_para_imprimir += LETRAS_GRANDES[letra][i]
            print(linea_para_imprimir)

        # Esperamos un momento antes de dibujar el siguiente frame.
        time.sleep(velocidad)

except KeyboardInterrupt:
    # Permite al usuario detener la animación limpiamente con Ctrl+C.
    print("\nAnimación detenida por el usuario.")

finally:
    limpiar_pantalla()
    print("Animación finalizada.")