
# Operadores lógicos en Python


# Operador AND
# Devuelve True SOLO si ambas condiciones son verdaderas.
print("\n--- Operador AND ---")
edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("¿Tienes licencia de conducir? (s/n): ").lower() == "s"

if edad >= 18 and tiene_licencia:
    print("AND :Verdadero: puedes conducir.")
else:
    print("AND :Falso: no puedes conducir.")

# ------------------------------------------

# Operador OR
# Devuelve True si AL MENOS una condición es verdadera.
print("\n--- Operador OR ---")
edad = int(input("Ingresa tu edad nuevamente: "))
permiso_especial = input("¿Tienes permiso especial para conducir? (s/n): ").lower() == "s"

if edad >= 18 or permiso_especial:
    print("OR :Verdadero: puedes conducir con permiso o por edad.")
else:
    print("OR :Falso: no puedes conducir todavía.")

# ------------------------------------------

# Operador NOT
# Invierte el valor lógico (True → False / False → True)
print("\n--- Operador NOT ---")
llueve = input("¿Está lloviendo? (s/n): ").lower() == "s"

if not llueve:
    print("NOT : Verdadero: no llueve, puedes salir")
else:
    print("NOT : Falso: está lloviendo, mejor lleva paraguas.")

# ------------------------------------------

# 🔹 Combinando operadores
print("\n--- Combinación de operadores ---")
edad = int(input("Ingresa tu edad: "))
tiene_licencia = input("¿Tienes licencia de conducir? (s/n): ").lower() == "s"
llueve = input("¿Está lloviendo? (s/n): ").lower() == "s"

if (edad >= 18 and tiene_licencia) and not llueve:
    print("Puedes conducir y el clima está bien.")
else:
    print("No se cumplen todas las condiciones (revisa edad, licencia o clima).")

# ==========================================
#  Resumen teórico rápido:
# and → True si ambas condiciones son verdaderas.
# or  → True si al menos una condición es verdadera.
# not → Invierte el valor lógico de una condición.
# ==========================================
