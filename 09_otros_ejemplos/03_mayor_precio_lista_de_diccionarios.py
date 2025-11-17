# sacar el maor precio de una lista de diccionarios

ventas = [
    {"Producto": "Papas", "Precio": 1000},
    {"Producto": "Papas", "Precio": 1500},
    {"Producto": "Papas", "Precio": 1200},
]

mayor_precio = 0 # inicializamos el mayor precio en 0, porque? porque los precios son positivos 

for venta in ventas: # 1ro - recorrer la lista de diccionarios
    if venta["Precio"] > mayor_precio: # 2do - comparar el precio de cada diccionario con el mayor precio
        mayor_precio = venta["Precio"] # 3ro - actualizar el mayor precio si es necesario

print("Mayor precio:", mayor_precio) # 4to - mostrar el mayor precio