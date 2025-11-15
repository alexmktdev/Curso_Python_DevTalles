  # --------------------------
# Ejemplo de la instrucción pass
# --------------------------

# El ciclo for recorre la lista [1, 2, 3, 4, 5]
# Pero como adentro solo tiene "pass", NO hace nada.
# "pass" se usa como marcador de posición cuando
# quieres dejar el bloque vacío sin generar error.
for item in [1, 2, 3, 4, 5]:
    pass  # No hace nada, solo evita errores por bloque vacío


# --------------------------
# Ejemplo de break (Detener ciclo)
# --------------------------

# Este bloque está comentado, pero te explico:
# for item in [1, 2, 3, 4, 5]:
#     if item == 4:   # Cuando llega al número 4...
#         break       # ...se detiene COMPLETAMENTE el ciclo
#     print(item)     # Solo imprime 1, 2, 3


# --------------------------
# Ejemplo de continue (Saltar a la siguiente iteración)
# --------------------------

number = 0  # Inicializamos number en 0

# El ciclo se ejecutará mientras "number" sea menor que 5
while number < len([1, 2, 3, 4, 5]):

    number += 1  # Primero sumamos 1 a "number"

    continue     # continue saltará TODO lo que viene debajo
                 # y volverá al inicio del ciclo

    # Esta línea NUNCA se ejecuta
    # porque "continue" la salta SIEMPRE
    print(number)

    number += 1  # Esta línea tampoco se ejecuta nunca
