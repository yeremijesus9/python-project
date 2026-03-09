import random

# Definimos los datos en una tupla (inmutable)
# Cada elemento es otra tupla: (País, Capital)
DATOS = (
    ("España", "Madrid"),
    ("México", "Ciudad de México"),
    ("Argentina", "Buenos Aires"),
    ("Francia", "París"),
    ("Japón", "Tokio")
)

def jugar():
    # Convertimos a lista solo para desordenar, pero los datos siguen siendo tuplas
    preguntas = list(DATOS)
    random.shuffle(preguntas)
    
    puntos = 0
    print("--- 🌍 RETO DE CAPITALES 🌍 ---")
    
    for pais, capital in preguntas:
        respuesta = input(f"¿Cuál es la capital de {pais}?: ").strip()
        
        if respuesta.lower() == capital.lower():
            print("✅ ¡Correcto!")
            puntos += 1
        else:
            print(f"❌ Error. La respuesta correcta era {capital}.")
            
    print(f"\nJuego terminado. Tu puntuación: {puntos}/{len(DATOS)}")

jugar()