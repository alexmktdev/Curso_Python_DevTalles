# set1.union(set2)
# Creamos dos conjuntos (sets) con números
set1 = {1, 2, 3}
set2 = {4, 5, 6}

# union() une ambos sets y devuelve un nuevo set con todos los elementos,
# sin repetir elementos.
union_set = set1.union(set2)
# print(union_set)  # Resultado: {1, 2, 3, 4, 5, 6}


# set1.intersection(set2)
# Nuevos conjuntos con algunos elementos en común
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# intersection() devuelve solo los elementos que están en ambos sets.
intersection = set1.intersection(set2)
# print(intersection)  # Resultado: {3, 4}


# set1.difference(set2)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# difference() devuelve los elementos de set2 que NO están en set1.
difference = set2.difference(set1)

# En este caso:
# set2 = {3, 4, 5, 6}
# set1 = {1, 2, 3, 4}
# Los que están en set2 pero no en set1 son 5 y 6.
print(difference)  # Resultado: {5, 6}
