# Ejemplo: Clasificar el clima según la temperatura y el estado del cielo

temperatura = float(input("Ingresa la temperatura en °C: "))
cielo = input("¿Está soleado, nublado o lluvioso? ").lower()

if temperatura > 30 and cielo == "soleado":
    print("Hace mucho calor, mejor busca sombra 😎☀️")
elif 20 <= temperatura <= 30 and (cielo == "soleado" or cielo == "nublado"):
    print("Clima agradable, ideal para salir 😊")
elif 10 <= temperatura < 20 and cielo == "nublado":
    print("Está fresco, lleva una chaqueta 🧥")
elif temperatura < 10 or cielo == "lluvioso":
    print("Hace frío o está lloviendo, mejor quedarse en casa ☔")
else:
    print("Clima desconocido, mejor revisa el pronóstico 🌦️")
