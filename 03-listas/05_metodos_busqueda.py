# metodos de busqueda en listas 

numeros = [1,2,3,4,5,2]

# 1. index - devuelve el indice del valor que se ingresa en el metodo
print(numeros.index(2, 0, 4)) # deve devolver el indice [1] - busca el 2 desde la posicion 0 al 4 

# in - nos dice si un valor está en la lista 
print(2 in numeros) # debe devolver un True

# count 
print(numeros.count(2)) # si le pasamos el 2, devuelve cuantas veces está presente el 2 en la lista


