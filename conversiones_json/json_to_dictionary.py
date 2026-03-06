import json

json_data = '[{"nombre": "Laura", "edad": 28, "ciudad": "Barcelona"}, {"nombre": "Isa", "edad": 30, "ciudad": "Bilbao"}]'

persons = json.loads(json_data)

print("\n")
print("\n")
print("### JSON to Dictionary ###")
print(persons)
print(type(persons))
print("__________________________")
print("\n")