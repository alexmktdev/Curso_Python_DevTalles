def comparar_numeros(x, y):
    if x > y:
        return f"{x} es mayor que {y}"
    elif y > x:
        return f"{y} es mayor que {x}"
    else:
        return "Ambos números son iguales"

# ejemplo
print(comparar_numeros(8, 3))
