def aplicar_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    return precio_final

# ejemplo
print(aplicar_descuento(10000, 20))  # debería entregar 8000
