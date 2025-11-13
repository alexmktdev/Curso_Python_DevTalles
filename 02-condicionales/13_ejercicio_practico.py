# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.

nombre = input("Ingrese su nombre por favor: ")
experiencia = int(input("Ingrese sus años de experiencia: "))

# Se obtiene la entrada, se pasa todo a minúsculas y se eliminan espacios globalmente
entrada_habilidades = input("Ingrese sus habilidades (separadas por coma): ")
entrada_limpia = entrada_habilidades.lower().replace(" ", "")  # elimina espacios y pone todo en minúsculas
habilidades = entrada_limpia.split(",")  # genera la lista

# Verificaciones
verificar_python = 'python' in habilidades
verificar_django = 'django' in habilidades
verificar_habilidades = verificar_python and verificar_django

# pero ahora me gustaria comparar esto con una lista donde están las habilidades que requiere el cargo
habilidades_requeridas = ['python','django']


# Condiciones del problema
if verificar_habilidades and experiencia > 3:
    print(f"{nombre} es un Candidato óptimo.")
elif verificar_habilidades and experiencia > 1:
    print(f"{nombre} es un Buen Candidato.")
elif verificar_habilidades:
    print(f"{nombre} es un Posible Candidato.")
elif not verificar_python:
    print(f"{nombre} no es óptimo, se guardará el CV.")