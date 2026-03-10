# Animación de Texto en la Consola
# Este script muestra cómo crear una animación simple de texto en la consola.
# La palabra "German" se moverá de izquierda a derecha.

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

# --- 2. Configuración de la animación ---
palabra = "German"
ancho_terminal = 120  # Define el ancho del área de animación
velocidad = 0.075    # Tiempo en segundos entre cada "frame" de la animación

# --- 3. Bucle de animación ---
# El bucle se ejecutará para mover la palabra a través de la pantalla.
try:
    print("Iniciando animación... Presiona Ctrl+C para salir.")
    time.sleep(2) # Una pequeña pausa antes de empezar

    # El rango va desde 0 hasta el borde derecho del terminal.
    # Restamos la longitud de la palabra para que no se salga de la pantalla.
    for posicion in range(ancho_terminal - len(palabra)):
        limpiar_pantalla()

        # Creamos el "frame" de la animación:
        # ' ' * posicion -> Añade espacios en blanco a la izquierda para mover la palabra.
        frame = (' ' * posicion) + palabra

        # Imprimimos el frame en la consola.
        print(frame)

        # Esperamos un momento antes de dibujar el siguiente frame.
        time.sleep(velocidad)

except KeyboardInterrupt:
    # Permite al usuario detener la animación limpiamente con Ctrl+C.
    print("\nAnimación detenida por el usuario.")

finally:
    limpiar_pantalla()
    print("Animación finalizada.")