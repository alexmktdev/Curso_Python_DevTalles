# keys en diccionarios 


# creamos uno 
usuario = {
    'Nombre': 'Alexander',
    'Edad': 31,
    'email': 'alexanderzananiri@gmail.com'
}

# accedamos a un valor del diccionario 
print(usuario['Nombre']) 

# modifiquemos un valor de un diccionario (ya que son mutables)
usuario['Nombre'] = 'Alexander Patricio'
usuario['Edad'] = 30

# mostramos el diccionario modificado 
print(usuario)

# agregar un valor nuevo a un diccionario
usuario['Direccion'] = "Avenida Oriente 2135, Molina"

# mostramos el diccionario modificado
print(usuario)

# las tuplas no son mutables, por lo que pueden ser keys 
usuario[(2.5, 3.2)] = '(Coordenada X, Coordenada Y)' 

# mostramos nuevamente el diccionario modificado
print(usuario)

# agregamos otra tupla 
usuario[("Coord X", "Coord. Y")] = (1.5 , 2.5)

print(usuario)