# Lista con números
numbers = [1, 2, 3, 4, 5]

# Un iterable es un objeto del que se pueden obtener elementos uno por uno.
# La lista "numbers" es un iterable.

# Creamos un iterador a partir de la lista
iterator = iter(numbers)   # El iterador recuerda su posición interna

# Mostramos cada elemento usando next()
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
print(next(iterator))  # 5
# Si intentas: print(next(iterator)) --> dará StopIteration porque ya no quedan elementos


# Diccionario con datos
user = {
    'name': 'Ricardo',
    'age': 22,
    'can_swim': False
}

# user.items() devuelve pares clave-valor como tuplas
# Ejemplo: ('name', 'Ricardo')

# Recorremos el diccionario obteniendo key y value
for key, value in user.items():
    print(key, value)
