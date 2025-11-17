"""
Encontrar el mayor precio en una lista de diccionarios
"""

# Crear una funcion que se le pasa la lista de productos y devuelve el nombre y precio del producto más caro
def encontrar_producto_mas_caro(lista_productos):
    mayor_precio = 0
    nombre_producto_mas_caro = ""
    for producto in lista_productos:
        if producto['precio'] > mayor_precio:
            mayor_precio = producto['precio']
            nombre_producto_mas_caro = producto['nombre']
    return nombre_producto_mas_caro, mayor_precio


# Programa principal 
# Lista de diccionarios con productos y sus precios
productos = [
        {'nombre': 'Producto A', 'precio': 150},
        {'nombre': 'Producto B', 'precio': 250},
        {'nombre': 'Producto C', 'precio': 100},
        {'nombre': 'Producto D', 'precio': 300},
    ]

    # llamamos a la funcion para encontrar el producto más caro
producto_mas_caro, precio_mas_caro = encontrar_producto_mas_caro(productos)
print(f"El producto más caro es: {producto_mas_caro} con un precio de ${precio_mas_caro}")



