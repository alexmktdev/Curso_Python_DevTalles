# Ejemplo: Sistema simple de recomendación de transporte

edad = int(input("Ingresa tu edad: "))
distancia = float(input("Ingresa la distancia a tu destino (en km): "))

if edad < 18:
    if distancia < 3:
        print("Te conviene ir caminando 🚶‍♂️")
    else:
        print("Podrías usar transporte público 🚌")
else:
    if distancia < 2:
        print("Podés ir caminando o en bici 🚴‍♀️")
    elif 2 <= distancia <= 10:
        print("El auto o la moto son buenas opciones 🚗🏍️")
    else:
        print("Mejor tomar un tren o un colectivo 🚆🚌")

'''
El primer if clasifica según la edad (menor o mayor de 18).
Dentro de cada bloque, hay otro if que evalúa la distancia.
Así se combinan condiciones jerárquicas (primero edad → luego distancia).

'''