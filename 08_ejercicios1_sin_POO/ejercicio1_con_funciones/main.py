from mostrar_menu import mostrar_menu
from ingresar_ventas import ingresar_ventas
from calcular_total_vendido import calcular_total_vendido
from mostrar_producto_mas_vendido import mostrar_producto_mas_vendido
from mostrar_cantidad_total_productos import mostrar_cantidad_total_productos
from mostrar_lista_productos import mostrar_lista_productos


'''
1. Registro de ventas con acumuladores

Crea un sistema que permita ingresar ventas del día: producto, 
cantidad y precio.
Guárdalas como una lista de diccionarios. Calcula total vendido, 
producto más vendido, y cantidad total de productos. Usa contadores
y funciones.

'''

# programa principal
while True:
    mostrar_menu() # llamamos a la funcion para mostrar el menu

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        print("Ha seleccionado la opcion 1: ")
        print("Ingresar Productos: ")
        ingresar_ventas() # llamamos a la funcion para ingresar las ventas
    
    elif opcion == 2:
        print("Ha seleccionado la opción 2: ")
        print("Calcular Total Vendido del Día:  ")

        calcular_total_vendido() # llamamos a la funcion para calcular el total vendido
                
    elif opcion == 3:
        print("Ha seleccionado la opción 3: ")
        print("Mostrar Producto Más Vendido: ")
        mostrar_producto_mas_vendido() # llamamos a la funcion para mostrar el producto mas vendido
    
    elif opcion == 4:
        print("Ha seleccionado la opción 4: ")
        print("Cantidad Total de Productos: ")

        mostrar_cantidad_total_productos() # llamamos a la funcion para mostrar la cantidad total de productos vendidos
    
    elif opcion == 5:
        print("Ha seleccionado la opción 5: ")
        print("Mostrar lista de todos los productos: ")

        mostrar_lista_productos() # llamamos a la funcion para mostrar la lista de productos

    elif opcion == 6:
        print("Ha seleccionado la opción 6: ")
        print("Salir !")
        break
    else :
        print("La opcion seleccionada no es válida, intente nuevamente !")
        

