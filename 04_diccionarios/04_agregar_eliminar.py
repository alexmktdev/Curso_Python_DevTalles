# metodos de agregar o eliminar diccionarios 

usuario = {
    'Nombre': 'Alexander',
    'Edad': 31,
    'email': 'alexander@gmail.com'
}

# metodo copy()  - sacamos una copia del diccionario 
usuario2 = usuario.copy()
print(usuario2) 


# ahora modificamos la copia sin afectar al original
usuario2['Edad'] = 40

print(usuario2)

# metodo .pop() - elimina a un elemento

usuario2.pop('Edad') # se le pasa una llave del diccionario y la elimina, en este caso Edad
print(usuario2)


# eliminar el ultimo elemento de un diccionario
usuario2.popitem()
print(usuario2)

# metodo - update()
usuario2.update({'Nombre': ' Juanito'})
print(usuario2)

# metodo append() - antes de agregar, se le agrega una lista a la clave 'lenguajes' para ir guardando en esa lista con append
usuario2['lenguajes'] = usuario2.get('lenguajes', [])
usuario2['lenguajes'].append('Python')
usuario2['lenguajes'].append('FASTAPI')

print(usuario2)