import json

my_person = {
    "name": "Carlo",
    "age": 30,
    "city": "Madrid"
}

json_data = json.dumps(my_person, indent=4)

print("\n")
print("\n")
print("### dictionary to JSON ###")
print(json_data)
print("__________________________")
print("\n")