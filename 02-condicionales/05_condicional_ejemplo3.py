# Ejemplo: Sistema de recomendación de transporte (sin if anidados)

edad = int(input("Ingresa tu edad: "))
distancia = float(input("Ingresa la distancia a tu destino (en km): "))

if edad < 18 and distancia < 3:
    print("Te conviene ir caminando 🚶‍♂️")
elif edad < 18 and distancia >= 3:
    print("Podrías usar transporte público 🚌")
elif edad >= 18 and distancia < 2:
    print("Podés ir caminando o en bici 🚴‍♀️")
elif edad >= 18 and 2 <= distancia <= 10:
    print("El auto o la moto son buenas opciones 🚗🏍️")
else:
    print("Mejor tomar un tren o un colectivo 🚆🚌")
