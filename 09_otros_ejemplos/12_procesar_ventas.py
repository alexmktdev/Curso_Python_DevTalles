def procesar_ventas(lista_productos):
    total_vendido = 0
    total_cantidad = 0
    producto_mayor = ""
    mayor_subtotal = 0

    for producto in lista_productos:
        subtotal = producto["cantidad"] * producto["precio"]
        total_vendido += subtotal
        total_cantidad += producto["cantidad"]

        if subtotal > mayor_subtotal:
            mayor_subtotal = subtotal
            producto_mayor = producto["nombre"]

    return total_vendido, total_cantidad, producto_mayor, mayor_subtotal

# Programa principal 
ventas = [
    {"nombre": "Pan", "cantidad": 3, "precio": 1200},
    {"nombre": "Leche", "cantidad": 2, "precio": 900},
    {"nombre": "Queso", "cantidad": 1, "precio": 2500}
]

print(procesar_ventas(ventas))
