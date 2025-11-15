# metodos de busqueda en diccionarios 

usuario = {
    'Nombre': 'Alexander',
    'Edad': 31,
    'email': 'alexander@gmail.com'
}

# metodo get
print(usuario.get('Nombre')) # me trae el valor de clave que le paso al get()


# metodo in en diccionarios

print('Nombre' in usuario.keys()) # con in , sirve solo para verificar si las claves estan en los diccionarios

# me trae todas las llaves del diccionario
print(usuario.keys()) 

# me trae todos los valores del diccionario
print(usuario.values())

# si quiero verificar si un "valor" esta en un diccinario : 
print('Alexander' in usuario.values()) # debe dar True
 

# ahora si quiero las claves y valores (todo)
print(usuario.items())

