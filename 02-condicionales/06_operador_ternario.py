# operador ternario en python 

# es basicamente un ejemplo condicional con maximo 2 opciones pero en una sola linea 

'''
valor_si_verdadero if condicion else valor_si_falso
'''

edad = int(input("Ingresa tu edad: "))

mensaje = "Mayor de edad " if edad >= 18 else "Menor de edad"

print(f"la persona es {mensaje}")

