'''
1. Registro de ventas con acumuladores

Crea un sistema que permita ingresar ventas del día: producto, 
cantidad y precio.
Guárdalas como una lista de diccionarios. Calcula total vendido, 
producto más vendido, y cantidad total de productos. Usa contadores
y funciones.

'''

# creamos una lista para guardar las ventas del dia 
ventas_del_dia = []


while True:
    # después lo pasamos a una funcion 
    print()
    print()
    print(" ***** Sistema de Registro de Ventas Diarias *****")

    print("*** Menú de Opciones ***")
    print(" 1. Ingresar Productos Véndidos ")
    print(" 2. Calcular Total Vendido del Día ")
    print(" 3. Mostrar Producto Más Vendido ")
    print(" 4. Cantidad Total de Productos ")
    print(" 5. Mostrar lista de todos los productos ")
    print(" 6. Salir")
    print()
    print()

    opcion = int(input("Ingrese la opcion: "))

    if opcion == 1:
        print("Ha seleccionado la opcion 1: ")
        print("Ingresar Productos: ")


        numero_de_productos = int(input("Cuantos productos quiere agregar: "))
        for i in range(1, numero_de_productos + 1):
            print()
            print(f" Datos del Producto {i}")
            producto = str(input("Ingresa el Nombre del Producto: "))
            cantidad = int(input("Ingresa la Cantidad del Producto:  "))
            precio = int(input("Ingrese el Precio del Producto: "))
            print()

            # creamos el diccionario que se guardará en la lista
            diccionario_venta = {
                'Producto': producto,
                'Cantidad': cantidad,
                'Precio': precio
            }
            ventas_del_dia.append(diccionario_venta)
        print()
        print("Si desea agregar más productos al registro de ventas")
        print("Vuelva a seleccionar la opción 1 ")
        print()
    
    elif opcion == 2:
        print("Ha seleccionado la opción 2: ")
        print("Calcular Total Vendido del Día:  ")
        total_ventas = 0
        # verificamos si el diccionario de ventas está vacio o no 
        if len(ventas_del_dia) == 0:
            print("No hay ventas registradas")
        else:
            for venta in ventas_del_dia: # recorre la lista (que tiene un diccionario por posicion)
                total_ventas += venta["Precio"] * venta["Cantidad"] #
            print()
            print(f"El total de ventas es: {total_ventas}")
                
    elif opcion == 3:
        print("Ha seleccionado la opción 3: ")
        print("Mostrar Producto Más Vendido: ")
        producto_mas_vendido = ""
        cantidad_mas_vendida = 0
        for venta in ventas_del_dia: # recorre la lista 
            if venta["Cantidad"] > cantidad_mas_vendida: # verifica el mayor: 
                cantidad_mas_vendida = venta["Cantidad"]
                producto_mas_vendido = venta["Producto"]
        print()
        print(f"El producto más vendido es: {producto_mas_vendido} con una cantidad de: {cantidad_mas_vendida}")
    
    elif opcion == 4:
        print("Ha seleccionado la opción 4: ")
        print("Cantidad Total de Productos: ")
        cantidad_total_productos = 0
        for venta in ventas_del_dia:
            cantidad_total_productos += venta["Cantidad"]
        print()
        print(f"La cantidad total de productos vendidos es: {cantidad_total_productos}")
    
    elif opcion == 5:
        print("Ha seleccionado la opción 5: ")
        print("Mostrar lista de todos los productos: ")
        if len(ventas_del_dia) == 0:
            print("No hay ventas registradas")
        else:
            for venta in ventas_del_dia:
                print(f"""
                        Producto: {venta['Producto']} - Cantidad: {venta['Cantidad']} - Precio: ${venta['Precio']}
                       """)
    elif opcion == 6:
        print("Ha seleccionado la opción 6: ")
        print("Salir !")
        break
    else :
        print("La opcion seleccionada no es válida, intente nuevamente !")
        







