'''
El objetivo es revisar un diccionario con un inventario de dulces
e ir agregando al carrito lo que me interesa, finalmente se debe
calcular el total del carrito y mostrarlo en pantalla
'''

inventario = {
    # nombre de dulce - precio 
    "chocolate": 10,
    "gomitas": 5,
    "paleta": 8,
    "chicle": 2,
    "mexicano": 8,
    "galletas": 12
}

# creamos una lista vacia para el carrito 
carrito_de_compras = []

print("Bienvenido a la Tienda de Dulces: ")
print(" ***** Disponibilidad ******")

for dulce, precio in inventario.items():
    print(f" Dulce: {dulce} - Precio : ${precio}")


opcion = "" # mi opcion de entrada (inicial string vacio para que no de error)

while True: # esto se ejecuta siempre..
    opcion = str(input("Que quiere agregar al carrito: "))

    # con este bloque de codigo, finaliza de inmediato el ciclo y no evalua nada más
    if opcion == "salir":
        print("gracias por comprar con nosotros")
        print("Vuelve Pronto !")
        break

    # verificamos que la entrada (opcion que puede ser un chocolate)
    # esté dentro del inventario
    if opcion in inventario:
        carrito_de_compras.append(opcion)
        print(f" Se agregó {opcion} al carrito!")
    else:
        print("El producto no existe en el inventario ")
        print("Intente de Nuevo por favor !")


# ahra calculamos el total de la compra 
total = 0

for item in carrito_de_compras:
    print(f" {item} - precio: ${inventario[item]}")
    total = total + inventario[item]

'''
como sabe el precio en el ciclo que se calcula el total ?
- a inventario[] le pasa de argumento el item que corresponde
  a cada uno de los elementos del carrito, y ese item es la clave
  del diccionario inventario, entonces:

  - si se agrego chocolate , el diccionario queda inventario['chocolate] 
    va al inventario y se encuentra con que inventario['chocolate'] = 10 y
    lo suma a total, si agrego otro item, repite el proceso y lo agrega a total
    y asi va sumando el total de la compra.

'''

print(f"El total fue de ${total} ")