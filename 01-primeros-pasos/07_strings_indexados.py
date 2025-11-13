# strings indexados 

nombre = "Alexander" # posicion 0 : A ,  posicion 1: l y asi ...

print(nombre)

# acceder a la primera posicion (0)
print(nombre[0])

# acceder a la segunda posicion (1)
print(nombre[1])

# acceder a la ultima posicion 
print(nombre[-1])


# manejar strings con start:end 

print(nombre[0:8]) # imprime hasta "alexande" - el "end", no lo toma, toma hasta el ultimo antes de el "end"

# manejar string con start:end:pasos

print(nombre[0:8:2]) # de dos en 2 

# como escribo mi nombre al reves ?

nombre2 = "Nicolas"

print(nombre2[::-1]) # nombre al reves 