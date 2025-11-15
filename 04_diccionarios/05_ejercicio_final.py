
Estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}

# Agregar nuevo estudiante
# Sacar el promedio de un estudiante existente
# El promedio del estudiante nuevo


# 1. Agregar nuevo estudiante 
Estudiantes["Ricardo"] = [5, 6, 6]


# 2. sacar el promedio de un estudiante existente

# pidamos el nombre por entrada
nombre = str(input("ingrese el nombre del estudiante que quiere evaluar: ")).strip() # ingrese el nombre tal cual

if nombre in Estudiantes:
    student_grades = Estudiantes[nombre]
    #total_grade = (student_grades[0]+student_grades[1]+student_grades[2]) / 3
    promedio = sum(student_grades)/len(student_grades)

    if promedio >= 6.0:
        print(f"{nombre} aprobó con un promedio de: {promedio:.2f}")
    else:
        print(f"{nombre} reprobó con un promedio de: {promedio:.2f}")

else:
    print("El estudiante no está registrado.")