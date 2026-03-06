import json

datos = {"producto": "laptop", "precio": 1200}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo)