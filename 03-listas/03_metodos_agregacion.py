
# metodos de agregacion en listas

numeros = [1,2,3,4,5,6]

# 1. append 
# agregamos un elemento al final de la lista
numeros.append(7)
print(numeros)


# 2. insert
# agregarun elemento en la lista pero con el indice
numeros.insert(1, 200) # se agrega un 200 en el indice [1]
print(numeros)

# 3. extends
numeros.extend([300,400,500]) # se agrega una lista al final de la lista original
print(numeros)