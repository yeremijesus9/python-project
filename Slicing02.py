import random

def mutar_palabra(palabra):
    if len(palabra) < 4:
        return palabra
    
    # Elegimos un punto de corte al azar
    punto = random.randint(1, len(palabra) - 1)
    
    # Usamos slicing para separar y reordenar
    # parte_1: desde el inicio hasta el punto
    # parte_2: desde el punto hasta el final
    parte_1 = palabra[:punto]
    parte_2 = palabra[punto:]
    
    # ¡Las mezclamos al revés!
    return (parte_2 + parte_1).capitalize()

# Ejemplo divertido
nombres = ["Python", "Programador", "Divertido", "Unicornio"]
for n in nombres:
    print(f"{n} se transforma en... {mutar_palabra(n)}")