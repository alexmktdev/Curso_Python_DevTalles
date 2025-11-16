# ==============================
# TEORÍA DE *args Y **kwargs
# ==============================

# *args:
# ------
# *args permite recibir un número variable de ARGUMENTOS POSICIONALES.
# Ejemplo de llamada: funcion(1, 2, 3, 4)
# Internamente *args se convierte en una TUPLA: (1, 2, 3, 4)
#
# Se usa cuando:
# - No sabes cuántos argumentos enviará el usuario.
# - Quieres aceptar valores opcionales sin un límite.
#
# **kwargs:
# ---------
# **kwargs permite recibir un número variable de ARGUMENTOS CON NOMBRE.
# Ejemplo de llamada: funcion(a=10, b=20)
# Internamente **kwargs se convierte en un DICCIONARIO: {'a': 10, 'b': 20}
#
# Se usa cuando:
# - Quieres permitir parámetros opcionales con nombre.
# - Necesitas valores clave-valor que puedan variar.
#
# Ambos pueden combinarse en una sola función para máxima flexibilidad.


# ===================================
# EJEMPLO COMPLETO DE USO Y TEORÍA
# ===================================

def big_function(*args, **kwargs):
    # args contiene todos los argumentos posicionales como una tupla
    print("Valores posicionales (args):", args)

    # kwargs contiene los argumentos nombrados como un diccionario
    print("Valores nombrados (kwargs):", kwargs)

    # Sumamos todos los valores dentro de kwargs (los valores del diccionario)
    total_kwargs = 0
    for valor in kwargs.values():
        total_kwargs += valor

    # sum(args) suma todos los valores posicionales
    total_args = sum(args)

    # Devolvemos la suma total
    return total_args + total_kwargs


# ===================================
# LLAMADA A LA FUNCIÓN
# ===================================

# Enviamos:
# - argumentos posicionales: 1,2,3,4,5,6,7,8,9
# - argumentos nombrados: num1=77, num2=120
#
# Esto demuestra el uso real y práctico de *args y **kwargs
resultado = big_function(1, 2, 3, 4, 5, 6, 7, 8, 9, num1=77, num2=120)

print("Resultado final:", resultado)
