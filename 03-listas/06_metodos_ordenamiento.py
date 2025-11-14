# metodos de ordenamiento en listas 

letras = ['a', 'b', 'm', 'o', 'c','z','g','d','e']

# metodo sort
letras.sort() # ordena las listas en alfabetico

print(letras)

# metodo sorted - hace lo mismo que sort() pero crea una nueva lista
nueva_lista = sorted(letras)
print(nueva_lista)

# metodo copy() - crea una copia de una lista 
otra_lista = nueva_lista.copy()
print(otra_lista)

# invertir una lista
otra_lista.reverse()
print(otra_lista)