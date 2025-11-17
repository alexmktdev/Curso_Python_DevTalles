# creamos una funcion para calcular el total vendido del dia    
from datos import ventas_del_dia

def calcular_total_vendido():
    total_ventas = 0
    # verificamos si el diccionario de ventas está vacio o no 
    if len(ventas_del_dia) == 0:
        print("No hay ventas registradas")
    else:
        for venta in ventas_del_dia: # recorre la lista (que tiene un diccionario por posicion)
            total_ventas += venta["Precio"] * venta["Cantidad"] #
        print()
        print(f"El total de ventas es: {total_ventas}")