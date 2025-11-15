# diccionarios anidados 

# Creamos un diccionario anidado.
# Cada clave (Persona1, Persona2, Persona3) tiene como valor otro diccionario.
nested_dict = {
    "Persona1": {"Nombre": "Ricardo", "edad": 29, "ciudad": "Ciudad de México"},
    "Persona2": {"Nombre": "Brenda", "edad": 26, "ciudad": "Huejutla de Reyes"},
    "Persona3": {"Nombre": "Estela", "edad": 50, "ciudad": "Cancún"}
}

# Primer ciclo for:
# .items() devuelve pares (clave, valor)
# key será "Persona1", "Persona2", etc.
# value será el diccionario interno de cada persona.
for key, value in nested_dict.items():
    print(f"{key}:")  # Imprime el nombre de la persona (clave principal)

    # Segundo ciclo for:
    # Recorre el diccionario interno de cada persona.
    # sub_key será "Nombre", "edad", "ciudad"
    # sub_value será el valor asociado.
    for sub_key, sub_value in value.items():
        # Imprime los datos internos con sangría para verse más ordenado.
        print(f"  {sub_key}: {sub_value}")
