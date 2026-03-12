import json

datos = {"producto": "televisor", "precio": 1000}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo)