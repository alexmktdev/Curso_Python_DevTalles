'''
Recibir como entrada del teclado 
nombre, apellido, año de nacimiento, correo y contraseña 

y imprima algo como :

Nombre: Alexander
email: alexanderruiz@gmail.com
tendras tal edad en 2050
Tu contraseña es: *** (si es de 4 digitos)

'''


nombre = str(input("ingrese el nombre: "))
apellido = str(input("ingrese el apellido: "))
anio_nacimiento = int(input("ingrese su año de nacimiento: "))
contrasenia = str(input("ingrese su contraseña:  "))
contrasenia_final = len(contrasenia) * ("*") # se obtiene el total de caracteres y se multiplica por un asterisco
edad_2050 = 2050 - anio_nacimiento

print(f"""
      - Nombre: {nombre} {apellido}
      - email : {nombre}{apellido}@gmail.com
      - tendras {edad_2050} en el 2050
      - Tu contraseña es: {contrasenia_final}
           
      """)