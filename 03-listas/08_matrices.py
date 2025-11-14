# matrices en python (lista de listas)

# hagamos una matriz de 3 filas y 3 columnas 

matriz = [[1,2,3], # indice 0 de la lista de afuera
          [4,5,6], # indice 1 de la lista de afuera
          [7,8,9] #  indice 2 de la lista de afuera 
                 ]

# y de cada lista chica por ejemplo [1,2,3] que es la primera fila cada una tiene su indice interno [0,1,2] -> indices

# imprime la primera fila de la matriz
print("fila 1 de la matriz") 
print(f"{matriz[0][0]}, {matriz[0][1]}, {matriz[0][2]}") # fila 1

# imprime la segunda fila de la matriz
print("fila 2 de la matriz")
print(f"{matriz[1][0]}, {matriz[1][1]}, {matriz[1][2]}") # fila 2

# imprime la primera columna
print(" Columna 1 de la matriz")
print(f" {matriz[0][0]}")
print(f" {matriz[1][0]}")
print(f" {matriz[2][0]}")

# imprime la columna 3 de la matriz
print(" Columna 1 de la matriz")
print(f" {matriz[0][2]}")
print(f" {matriz[1][2]}")
print(f" {matriz[2][2]}")

# imprime la columna 2 de la matriz 
print(" Columna 2 de la matriz")
print(f" {matriz[0][1]}")
print(f" {matriz[1][1]}")
print(f" {matriz[2][1]}")

# imprime la diagonal de la matriz 
print(" Diagonal de la matriz")
print(f" {matriz[0][0]}")
print(f" {matriz[1][1]}")
print(f" {matriz[2][2]}")

# imprime la diagonal invertida de la matriz 
print(" Diagonal de la matriz")
print(f" {matriz[0][2]}")
print(f" {matriz[1][1]}")
print(f" {matriz[2][0]}")