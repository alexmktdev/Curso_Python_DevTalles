# metodos de eliminacion de elementos en listas 

numeros = [1,2,3,4,5,6]

# 1. metodo pop - elimina un elemento al final de la lista

numeros.pop() # elimina el 6 de la lista numeros
print(numeros)

# 2. metodo pop - elimina un elemento con un indice
numeros.pop(0) # elimina el elemento del indice 0
print(numeros)

# 3. metodo remove - se le pasa el valor que queremos eliminar
numeros.remove(5) # elimina el 5
print(numeros)

# 4. metodo clear() - limpia o elimina toda la lista completa
numeros.clear()
print(numeros)