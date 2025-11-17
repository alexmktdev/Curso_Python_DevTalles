
"""
- Cuenta cuantas veces fue ingresado cierto producto
- Emite un aviso si es que "tal producto" fue ingresado antes

"""

# 1. Pedimos el ingreso de los productos por teclado 

# modulo 1 - ingreso de productos 
print("*** modulo 1 - Ingreso de Productos")
ventas = [] # para guardar los productos 
contador_papas = 0
vistos = set() # se ocupa un set, ya que no guarda duplicados 
opcion = ""
while opcion != "no":
    
    opcion = input("desea agregar productos al sistema (si/no): ")

    if opcion == "si":
        n_articulos = int(input("Cuantos productos quiere ingresar al sistema: "))

        for art in range(1, n_articulos + 1):
            nombre_producto = input(f"Ingrese el nombre del producto N°{art} ")
            cantidad = int(input(f"Ingrese la cantidad del producto N°{art} "))
            precio = int(input(f"Ingrese el precio del producto N°{art} "))

            # contar cuantas veces se ingreso un cierto articulo
            if nombre_producto == "papas":
                contador_papas+=1

            # aviso que tal producto ya fue ingresado antes
            if nombre_producto in vistos:
                print(f"Atención: el producto '{nombre_producto}' ya fue ingresado antes.")
            else:
                vistos.add(nombre_producto)


            # creamos el diccionario con los ingresos de datos
            diccionario_ventas = {
                    "Producto": nombre_producto,
                    "Cantidad": cantidad,
                    "Precio": precio
            }
            # ahora agregamos cada diccionario creado a la lista de de ventas final
            ventas.append(diccionario_ventas)

            
if len(ventas) == 0: # verificamos si la lista ventas tiene elementos
    print("No ha agregado productos al sistema !")
else: 
    print("Lista de productos agregados: ")
    print(ventas)

    print(f"se ingreso {contador_papas} veces el producto 'papas' al sistema")

