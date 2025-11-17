# calcular el promedio de los precios de una lista de diccionarios 

productos = [
    {"nombre": "Pan", "precio": 1200},
    {"nombre": "Leche", "precio": 900},
    {"nombre": "Queso", "precio": 2500},
    {"nombre": "Yogurt", "precio": 2000}
]

promedio = 0
suma_precios = 0
cantidad = 0
for producto in productos:
    if producto["precio"]:
        suma_precios+= producto["precio"]
        cantidad+=1

promedio = suma_precios/cantidad
print(f"el promedio total es {promedio}")




