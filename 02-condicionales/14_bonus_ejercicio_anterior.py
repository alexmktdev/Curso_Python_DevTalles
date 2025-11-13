
# buscar en la listad de hablidades si hay python y django

# Lista de habilidades requeridas
habilidades = ["html", "css", "python", "django"]

# Variables para marcar si las tiene
tiene_python = False
tiene_django = False

# Recorremos la lista y verificamos
for h in habilidades:
    if h == "python":
        tiene_python = True
    if h == "django":
        tiene_django = True

# Resultado final
if tiene_python and tiene_django:
    print("El candidato sabe Python y Django.")
else:
    print("El candidato no cumple con las habilidades requeridas.")
