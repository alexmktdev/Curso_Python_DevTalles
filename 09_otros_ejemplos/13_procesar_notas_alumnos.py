def procesar_notas(lista_alumnos, nota_minima):
    aprobados = []
    reprobados = []
    suma_notas = 0
    mejor_alumno = ""
    nota_max = 0

    for alumno in lista_alumnos:
        nota = alumno["nota"]
        suma_notas += nota

        if nota >= nota_minima:
            aprobados.append(alumno)
        else:
            reprobados.append(alumno)

        if nota > nota_max:
            nota_max = nota
            mejor_alumno = alumno["nombre"]

    promedio_general = suma_notas / len(lista_alumnos)
    promedio_aprobados = (sum(a["nota"] for a in aprobados) / len(aprobados)) if aprobados else 0

    return aprobados, reprobados, promedio_general, promedio_aprobados, mejor_alumno, nota_max


alumnos = [
    {"nombre": "Ana", "nota": 5.5},
    {"nombre": "Luis", "nota": 3.9},
    {"nombre": "Carla", "nota": 6.2},
    {"nombre": "Pablo", "nota": 4.1}
]

print(procesar_notas(alumnos, 4.0))
