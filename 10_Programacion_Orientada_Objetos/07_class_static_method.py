# ***********************************************
# Ejemplo completo de métodos en Python (POO)
# ***********************************************

class Persona:
    # ----------------------------------------------------
    # Atributo de clase:
    # Es compartido por TODOS los objetos de esta clase.
    # ----------------------------------------------------
    especie = "Humano"

    # ----------------------------------------------------
    # Constructor (__init__):
    # Se ejecuta al crear un objeto. Recibe "self" (el objeto).
    # ----------------------------------------------------
    def __init__(self, nombre, edad):
        # Atributos de instancia (propios del objeto)
        self.nombre = nombre
        self.edad = edad

    # ----------------------------------------------------
    # MÉTODO NORMAL (usa self)
    # ----------------------------------------------------
    # Este método SÍ necesita acceder a los datos del OBJETO.
    # Por eso recibe "self".
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    # ----------------------------------------------------
    # MÉTODO DE CLASE (usa cls)
    # ----------------------------------------------------
    # Este método NO usa datos del objeto, sino de la CLASE completa.
    # Recibe "cls", que representa la clase "Persona".
    @classmethod
    def cambiar_especie(cls, nueva_especie):
        # Cambia el atributo de clase para todos los objetos
        cls.especie = nueva_especie

    # ----------------------------------------------------
    # CONSTRUCTOR ALTERNATIVO usando @classmethod
    # ----------------------------------------------------
    # Sirve para crear objetos desde otro tipo de dato o formato.
    @classmethod
    def desde_cadena(cls, texto):
        # Por ejemplo: "Alex-25"
        nombre, edad = texto.split("-")
        # cls(...) es equivalente a Persona(...)
        return cls(nombre, int(edad))

    # ----------------------------------------------------
    # MÉTODO ESTÁTICO (NO usa ni self ni cls)
    # ----------------------------------------------------
    # Es como una función "normal", pero ubicada dentro de la clase
    # porque tiene relación lógica con ella.
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


# ***********************************************
# Uso de los métodos
# ***********************************************

# 1) Crear un objeto normalmente
persona1 = Persona("Alex", 25)

print(persona1.presentarse())        # Método normal

# 2) Usar el método de clase para cambiar la especie de TODOS
Persona.cambiar_especie("Mutante")
print("Nueva especie:", Persona.especie)

# 3) Crear un objeto usando el constructor alternativo
persona2 = Persona.desde_cadena("Carla-30")
print(persona2.presentarse())

# 4) Usar el método estático
print("¿Carla es mayor de edad?:", Persona.es_mayor_de_edad(persona2.edad))
