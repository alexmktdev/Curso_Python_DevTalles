# Creamos una lista "anidada", es decir, una lista que contiene otras listas dentro.
nested_list = [
    [1, 2, 3],  # Primera sublista
    [4, 5, 6],  # Segunda sublista
    [7, 8, 9]   # Tercera sublista
]

# Primer ciclo for:
# "sublist" va tomando cada lista interna una por una.
for sublist in nested_list:

    # Segundo ciclo for:
    # "item" recorre los elementos dentro de cada sublista.
    for item in sublist:
        # Imprime cada número de la sublista en la misma línea.
        # end=" " evita el salto de línea y pone un espacio al final.
        print(item, end=" ")

    # Este print vacío se ejecuta después de terminar cada sublista.
    # Genera un salto de línea para separar visualmente las filas.
    print()
