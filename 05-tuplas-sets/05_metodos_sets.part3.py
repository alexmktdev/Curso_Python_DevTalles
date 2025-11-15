# ============================================
# DEMOSTRACIÓN DE MÉTODOS DE SETS EN PYTHON
# ============================================

# ---------- symmetric_difference ----------
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# symmetric_difference():
# Devuelve los elementos que están en uno de los sets,
# pero NO en ambos al mismo tiempo (excluye los comunes).
symmetric_difference = set1.symmetric_difference(set2)
print("symmetric_difference:", symmetric_difference)
# Resultado: {1, 2, 5, 6}


# ---------- issubset ----------
set1 = {1, 2}
set2 = {1, 2, 3, 4}

# issubset():
# Devuelve True si TODOS los elementos de set1
# están contenidos dentro de set2.
resultado_issubset = set1.issubset(set2)
print("set1 es subconjunto de set2:", resultado_issubset)
# Resultado: True (porque 1 y 2 están en set2)


# ---------- issuperset ----------
set1 = {1, 2, 3, 4}
set2 = {1, 2}

# issuperset():
# Devuelve True si set1 contiene TODOS los elementos de set2.
resultado_issuperset = set1.issuperset(set2)
print("set1 es superconjunto de set2:", resultado_issuperset)
# Resultado: True (set1 contiene 1 y 2)
