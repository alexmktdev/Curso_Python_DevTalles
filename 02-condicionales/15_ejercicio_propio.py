 
'''
La idea es ingresar mis habilidades de programación.
Existe una lista fija con habilidades que requiere un cargo de programación.

Objetivo:
Verificar si todas mis habilidades están dentro de las requeridas.
Si lo están → mostrar mensaje de éxito.
Si falta al menos una → mostrar mensaje de error.
'''

# 1. Ingreso de habilidades
mis_habilidades = input("Ingrese sus habilidades separadas por coma: ")
mis_habilidades_limpias = mis_habilidades.lower().replace(" ", "").split(",")
print("Tus habilidades:", mis_habilidades_limpias)

# 2. Lista de habilidades requeridas
habilidades_requeridas = ['python', 'django', 'fastapi', 'java']

# 3. Asumimos al inicio que todas están
habilidades_presentes = True

# 4. Verificamos si todas las habilidades del candidato están en las requeridas
for habilidad in mis_habilidades_limpias: # iteramos cada una, para tener acceso a comparar cada una
    if habilidad not in habilidades_requeridas: # si "python" por ej no está en habilidades requeridas !
        habilidades_presentes = False # se cambia esta bandera a falso altiro
        break  # ya sabemos que falta al menos una, no seguimos revisando, rompemos el bucle 

# 5. Resultado final
if habilidades_presentes: # si es verderadero 
    print("Todas las habilidades del candidato están dentro de las requeridas.")
else:  # si no es verdadero, es decir, es falso 
    print("El candidato no cumple con las habilidades requeridas.")

