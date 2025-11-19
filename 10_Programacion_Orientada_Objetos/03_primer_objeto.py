# objetos en python 

class Persona:
    def __init__(self, nombre, edad):
     self.nombre = nombre
     self.edad = edad 


# creamos una instancia (copia) de la clase o un objeto
persona1 = Persona('Alexander', 31)

print(persona1.nombre) # accedemos al atributo nombre del objeto persona1 
print(persona1.edad) # lo mismo con la edad

print(f"La persona 1 se llama {persona1.nombre} y tiene {persona1.edad} años")

# creamos otro objeto 
persona2 = Persona('Fernando', 32)


