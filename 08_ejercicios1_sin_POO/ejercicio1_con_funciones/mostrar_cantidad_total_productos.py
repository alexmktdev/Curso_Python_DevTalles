from datos import ventas_del_dia

# creamos una funcion para mostrar la cantidad total de productos vendidos
def mostrar_cantidad_total_productos():
    cantidad_total_productos = 0
    for venta in ventas_del_dia:
        cantidad_total_productos += venta["Cantidad"]
    print()
    print(f"La cantidad total de productos vendidos es: {cantidad_total_productos}")