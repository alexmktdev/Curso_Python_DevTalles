# conversion de esctructuras en python 

# Lista con números repetidos
list1 = [1, 2, 3, 4, 2, 3, 4, 5, 1, 2, 5, 6, 2, 4, 9, 10]

# Convertimos la lista en una tupla
# Las tuplas son iguales a las listas pero NO se pueden modificar (son inmutables)
tuple1 = tuple(list1)
# print(list1)   # Muestra la lista
# print(tuple1)  # Muestra la tupla generada a partir de la lista

# Convertimos la tupla en un set (conjunto)
# Un set elimina automáticamente los elementos duplicados
set1 = set(tuple1)
# print(set1)    # Muestra los números sin repetir

# Lista de tuplas donde cada tupla es: (clave, valor)
list_tuple = [('a', 1), ('b', 2), ('c', 3)]

# Convertimos la lista de tuplas en un diccionario
# dict() toma cada tupla como clave y valor respectivamente
dictionary = dict(list_tuple)

# Mostramos el diccionario final
print(dictionary)
# Resultado: {'a': 1, 'b': 2, 'c': 3}
