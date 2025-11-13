# Diferencia entre 'is' y '=='
# ----------------------------------------
# '==' compara SI DOS VALORES SON IGUALES en contenido.
# 'is' compara SI DOS VARIABLES APUNTAN AL MISMO OBJETO en memoria.

# Ejemplo 1: comparación de números
a = 10
b = 10

# Compara si los valores son iguales
resultado_igualdad = (a == b)
print("¿a == b?:", resultado_igualdad)

# Compara si apuntan al mismo objeto en memoria
resultado_identidad = (a is b)
print("¿a is b?:", resultado_identidad)

# En este caso, ambos dan True porque Python reutiliza algunos enteros pequeños (optimizaciones internas)


# Ejemplo 2: comparación de listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1  # lista3 apunta al mismo objeto que lista1

# Compara si los contenidos son iguales
resultado1 = (lista1 == lista2)
print("¿lista1 == lista2?:", resultado1)

# Compara si apuntan al mismo objeto
resultado2 = (lista1 is lista2)
print("¿lista1 is lista2?:", resultado2)

# Ahora comparamos lista1 con lista3 (que es la misma en memoria)
resultado3 = (lista1 is lista3)
print("¿lista1 is lista3?:", resultado3)


# Ejemplo 3: comparación de cadenas
texto1 = "hola"
texto2 = "hola"
texto3 = str("hola")

# Compara si los textos son iguales
resultado4 = (texto1 == texto3)
print("¿texto1 == texto3?:", resultado4)

# Compara si son el mismo objeto
resultado5 = (texto1 is texto3)
print("¿texto1 is texto3?:", resultado5)

# A veces las cadenas iguales pueden compartir la misma referencia (por optimización interna),
# pero no siempre. Por eso 'is' no se debe usar para comparar contenido, sino identidad.
