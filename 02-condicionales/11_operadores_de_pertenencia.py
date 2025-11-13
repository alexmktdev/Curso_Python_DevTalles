# Operadores de pertenencia en python 


# Operadores de pertenencia en Python:
# 'in'     → Devuelve True si un valor se encuentra dentro de una secuencia (lista, cadena, tupla, etc.)
# 'not in' → Devuelve True si un valor NO se encuentra dentro de una secuencia

# Ejemplo 1: uso con listas
frutas = ["manzana", "pera", "banana"]

# Verificar si "pera" está en la lista
resultado1 = "pera" in frutas
print("¿'pera' está en la lista de frutas?:", resultado1)

# Verificar si "naranja" está en la lista
resultado2 = "naranja" in frutas
print("¿'naranja' está en la lista de frutas?:", resultado2)

# Verificar si "uva" no está en la lista
resultado3 = "uva" not in frutas
print("¿'uva' no está en la lista de frutas?:", resultado3)


# Ejemplo 2: uso con cadenas de texto
texto = "Python es un lenguaje poderoso"

# Verificar si la palabra "Python" está en el texto
resultado4 = "Python" in texto
print("¿La palabra 'Python' está en el texto?:", resultado4)

# Verificar si la palabra "java" está en el texto
resultado5 = "java" in texto
print("¿La palabra 'java' está en el texto?:", resultado5)

# Verificar si la palabra "fácil" no está en el texto
resultado6 = "fácil" not in texto
print("¿La palabra 'fácil' no está en el texto?:", resultado6)
