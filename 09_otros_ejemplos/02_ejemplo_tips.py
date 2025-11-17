
# lista de diccionarios 

ventas = [
    {"Producto": "Papas",    "Cantidad": 5,  "Precio": 9000},
    {"Producto": "Manzanas","Cantidad": 12, "Precio": 12000},
    {"Producto": "Leche",   "Cantidad": 3,  "Precio": 2500}
]

'''
 supongamos que cada diccionario en esta lista es una boleta 
 con datos como:
   - producto
   - cantidad
   - precio 
'''

# 1. si quiero acceder a una boleta (a la primera) completa 
print(ventas[0])

# 2. si quiero recorrer todas las boletas (recorremos la lista de boletas)
for venta in ventas:
    print(venta)

# 3. si quiero un dato especifico de una boleta por ejemplo el precio de la tercera boleta
print()
print(ventas[2]["Precio"])

# recorramos y sumemos los precios de todas las boletas
total_ventas = 0
for venta in ventas:
    total_ventas += venta["Precio"] * venta["Cantidad"]
print()
print(f"El total de ventas es: {total_ventas}")

# ahora el valor del producto mas vendido (el que tiene mayor cantidad)
producto_mas_vendido = ""
cantidad_mas_vendida = 0    

for venta in ventas: # recorre la lista 
    if venta["Cantidad"] > cantidad_mas_vendida: # verifica el mayor: 
        cantidad_mas_vendida = venta["Cantidad"]
        producto_mas_vendido = venta["Producto"]

print()
print(f"El producto más vendido es: {producto_mas_vendido} con una cantidad de: {cantidad_mas_vendida}")


# el producto menos vendido (el que tiene menor cantidad)
producto_menos_vendido = ""
cantidad_menos_vendida = None

for venta in ventas: # recorre la lista
    if cantidad_menos_vendida is None or venta["Cantidad"] < cantidad_menos_vendida: # verifica el menor: 
        cantidad_menos_vendida = venta["Cantidad"]
        producto_menos_vendido = venta["Producto"]
print()
print(f"El producto menos vendido es: {producto_menos_vendido} con una cantidad de: {cantidad_menos_vendida}")







