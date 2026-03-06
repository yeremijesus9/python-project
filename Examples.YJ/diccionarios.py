persona = {
    "nombre": "Yeremi",
    "edad": 29,
    "ciudad": "Bilbao"
}

# acceder
print(persona["nombre"])

# añadir
persona["profesion"] = "Programador"

# modificar
persona["edad"] = 30

# recorrer
for clave, valor in persona.items():
    print(clave, ":", valor)

# eliminar
persona.pop("ciudad")

print(persona)
