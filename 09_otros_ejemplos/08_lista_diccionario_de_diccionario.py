personas = [
    {
        "nombre": "Ana",
        "edad": 25,
        "mascota": {
            "tipo": "Perro",
            "nombre": "Firulais",
            "edad": 4
        }
    },
    {
        "nombre": "Luis",
        "edad": 30,
        "mascota": {
            "tipo": "Gato",
            "nombre": "Michi",
            "edad": 2
        }
    },
    {
        "nombre": "Carla",
        "edad": 28,
        "mascota": {
            "tipo": "Hámster",
            "nombre": "Pelusa",
            "edad": 1
        }
    }
]

# accedamos al nombre de la mascota de luis 
print(personas[1]["mascota"]["nombre"])

# accedamos a todos los datos de carla 
print(personas[2])

# accedamos a todos los datos de la mascota de ana
print(personas[0]["mascota"])

# quedaria el desafio de recorrer y calcular cosas de lo que hay dentro de los diccionarios 
# o dentro de los diccionarios que hay dentro de otros diccionarios 