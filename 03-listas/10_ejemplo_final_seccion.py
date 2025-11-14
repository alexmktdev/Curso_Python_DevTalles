# Crearás un carrito de compras que haga las siguientes funciones:
# Agregar producto
# Eliminar producto
# Mostrar la lista ordenada
# Buscar producto
# Contar productos del carrito
# Vaciar el carrito

print("Carrito de compras")
print("Opciones: ")
print("1. Agregar producto")
print("2. Eliminar producto")
print("3. Mostrar la lista ordenada")
print("4. Buscar producto")
print("5. Contar productos del carrito")
print("6. Vaciar el carrito")

carrito_de_compras = ['TV LG','Mouse logitech','Iphone 15 pro'] # carrito inicialmente vacio 

# hacemos el menu de opciones 
opcion = str(input("ingrese una opcion : "))

if opcion == '1':
    producto = str(input("ingrese el producto que quiere agregar: "))
    carrito_de_compras.append(producto)
    print(f"El producto {producto} fue agregado con exito al carrito !")
    print("carrito: ")
    print(carrito_de_compras)
elif opcion == '2':
    # 1. pedir el nombre 
    producto = str(input("ingrese el producto que quiere eliminar: "))
    # 2. verificar si esta en lista , si esta, eliminar
    if producto in carrito_de_compras:
        carrito_de_compras.remove(producto)
        print(f"El producto {producto} fué eliminado con exito!")
        print("carrito: ")
        print(carrito_de_compras)
    else:
        print(f"El producto {producto} no se puede eliminar, ya que no existe!")
elif opcion == '3':
    print("carrito de compras ordenado: ")
    carrito_de_compras.sort()
    print(carrito_de_compras)

elif opcion == '4':
    # 1. pedir el nombre 
    producto = str(input("ingrese el producto que quiere buscar: "))
    # 2. verificar si esta en lista 
    if producto in carrito_de_compras:
        print(f"El producto {producto} fue encontrado con exito!")
    else:
        print(f"El producto {producto} no existe!")
elif opcion == '5':
    print(f"el total de productos del carrito es {len(carrito_de_compras)}")
elif opcion == '6':
    carrito_de_compras.clear()
    print("el carrito ha sido vaciado con exito !")
    print(carrito_de_compras)
else: 
    print("opcion ingresada no es valida, reinicie el programa !")
