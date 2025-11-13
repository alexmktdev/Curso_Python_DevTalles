# ==========================================
# Operadores de comparación en Python
# ==========================================

print("\n--- Operadores de comparación ---")

# Pedimos dos números al usuario
a = float(input("Ingresa el primer número (a): "))
b = float(input("Ingresa el segundo número (b): "))

# 1. Igualdad (==)
# Devuelve True si ambos valores son iguales
print(f"\na == b -> {a == b}")

# 2. Desigualdad (!=)
# Devuelve True si los valores son diferentes
print(f"a != b -> {a != b}")

# 3. Mayor que (>)
# Devuelve True si el primer valor es mayor que el segundo
print(f"a > b -> {a > b}")

# 4. Menor que (<)
# Devuelve True si el primer valor es menor que el segundo
print(f"a < b -> {a < b}")

# 5. Mayor o igual que (>=)
# Devuelve True si el primer valor es mayor o igual al segundo
print(f"a >= b -> {a >= b}")

# 6. Menor o igual que (<=)
# Devuelve True si el primer valor es menor o igual al segundo
print(f"a <= b -> {a <= b}")

# ------------------------------------------

# Ejemplo práctico combinando operadores de comparación
print("\n--- Ejemplo práctico ---")

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida.")
elif edad < 18:
    print("Sos menor de edad.")
elif edad >= 18 and edad < 65:
    print("Sos adulto.")
else:
    print("Sos adulto mayor.")

# ==========================================
# Resumen teórico:
# ==  -> Igual a
# !=  -> Distinto de
# >   -> Mayor que
# <   -> Menor que
# >=  -> Mayor o igual que
# <=  -> Menor o igual que
# ==========================================
