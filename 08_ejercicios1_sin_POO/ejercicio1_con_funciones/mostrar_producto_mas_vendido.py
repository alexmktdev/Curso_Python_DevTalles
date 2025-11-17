from datos import ventas_del_dia

# creamos una funcion para mostrar el producto mas vendido
def mostrar_producto_mas_vendido():
    producto_mas_vendido = ""
    cantidad_mas_vendida = 0
    for venta in ventas_del_dia: # recorre la lista 
        if venta["Cantidad"] > cantidad_mas_vendida: # verifica el mayor: 
            cantidad_mas_vendida = venta["Cantidad"]
            producto_mas_vendido = venta["Producto"]
    print()
    print(f"El producto más vendido es: {producto_mas_vendido} con una cantidad de: {cantidad_mas_vendida}")