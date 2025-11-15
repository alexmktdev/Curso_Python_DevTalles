# Conjuntos (sets) de estudiantes inscritos en cada curso
python_course = {'Ana', 'Luis', 'Maria', 'Pedro'}
java_course = {'Pepito', 'Pedro', 'Carlos', 'Ricardo'}

# intersection(): devuelve los elementos que están en ambos conjuntos
two_courses = python_course.intersection(java_course)
# print(two_courses)  # Resultado: {'Pedro'} porque es el único en ambos cursos

# difference(): devuelve los elementos que están en python_course pero NO en java_course
only_python = python_course.difference(java_course)
# print(only_python)  # Resultado: {'Ana', 'Luis', 'Maria'}

# union(): une ambos conjuntos SIN repetir elementos
all_students = python_course.union(java_course)
print(all_students)  
# Resultado:
# {'Ana', 'Luis', 'Maria', 'Pedro', 'Pepito', 'Carlos', 'Ricardo'}
