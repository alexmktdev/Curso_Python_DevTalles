# tipos de datos en python 

# String - cadenas de texto 
nombre = "nicolas"
saludo = "hola a todos"
numero_string = "20"

# int - integer - enteros
edad = 20
numero_de_personas = 12

# float - decimales 
temperatura = 20.5
dinero = 9.99

# booleanos - estados (true o false)
esta_prendido = True
esta_apagado = False


# Datos especiales 

# listas
lista = [1,2,3,4,5] # coleccion de numeros 
lista_nombres = ['nicolas', 'fabian', 'fernanda'] # coleccion de strings

# tuplas 
tupla = (1,2,3) # datos en grupos, agrupados

# sets
mi_set = {1,2,3} # coleccion qe no se repiten datos

# diccionarios
mi_diccionario = {
    'nombre': 'ricardo',
    'apellido': 'Ruiz',
    'rut': 18679045-6,
}

# como saber el tipo de dato de un objeto
print(type(tupla))

# las ventajas de que las cosas sean objetos, es que tienen metodos, y con esos metodos se pueden aplicar 
# muchas funcionalidades 

# todo en python es un OBJETO !