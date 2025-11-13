# Ejemplos de valores Truthy y Falsey en Python

# --- Valores Falsey (se comportan como False) ---
falsy_values = [0, 0.0, "", [], {}, set(), None, False]

print("=== Valores Falsey ===")
for valor in falsy_values:
    if valor:
        print(f"{repr(valor)} -> Truthy")
    else:
        print(f"{repr(valor)} -> Falsey")

# --- Valores Truthy (se comportan como True) ---
truthy_values = [1, -5, 0.1, "hola", [1, 2], {"a": 1}, (0,), True]

print("\n=== Valores Truthy ===")
for valor in truthy_values:
    if valor:
        print(f"{repr(valor)} -> Truthy")
    else:
        print(f"{repr(valor)} -> Falsey")

# --- Uso práctico ---
print("\n=== Ejemplo práctico ===")

nombre = input("Ingresa tu nombre: ")

# Si el usuario no escribe nada, el string será "" (que es Falsey)
mensaje = f"Hola, {nombre} 👋" if nombre else "No ingresaste tu nombre ❌"

print(mensaje)
