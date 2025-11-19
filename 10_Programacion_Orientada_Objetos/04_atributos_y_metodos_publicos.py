# atributos y metodos publicos en python 

class Persona:
    # atributo de clase o global (van fuera del constructor)
    especie = "Humano"

    def __init__(self, nombre, edad):
     self.nombre = nombre # atributos publicos o de instancia 
     self.edad = edad 

    # creamos un metodo publico 
    def trabajar(self):
       return f" {self.nombre} está trabajando muy duro"
    
    # creamos un metodo pero que recibe algo y con condiciones
    def comer(self, comida):
        if comida.lower() == 'empanadas':
          return "Las empanadas dan superpoderes !"
        else:
          return "A comido algo normal !"


# creamos una instancia (copia) de la clase o un objeto
persona1 = Persona('Alexander', 31)
print(persona1.trabajar())
print(persona1.comer('completo italiano'))