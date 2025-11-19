class Person:

    def __init__(self, name):
        self.name = name  # atributos de instancia
        self._energy = 100 # por convencion, para que otros programadores sepan que es protegido, se le pone el _
        # esto no quiere decir que efectivamente sea protegido y oculto , es una convencion 

    def _waste_energy(self, quantity):
        self._energy -= quantity


person1 = Person('Ricardo', )
print(person1.name)
person1._waste_energy(20)