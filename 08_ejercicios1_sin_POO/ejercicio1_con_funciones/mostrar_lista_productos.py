from datos import ventas_del_dia


# creamos una funcion para mostrar la lista de todos los productos
def mostrar_lista_productos():
    if len(ventas_del_dia) == 0:
        print("No hay ventas registradas")
    else:
        for venta in ventas_del_dia:
            print(f"""
                    Producto: {venta['Producto']} - Cantidad: {venta['Cantidad']} - Precio: ${venta['Precio']}
                   """)
    