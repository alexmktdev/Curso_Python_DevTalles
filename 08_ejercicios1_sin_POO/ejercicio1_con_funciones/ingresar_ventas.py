from datos import ventas_del_dia

# creamos una funcion para ingresar las ventas

def ingresar_ventas():
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