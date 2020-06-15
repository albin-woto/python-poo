# Definición
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'

if __name__ == '__main__':
    # Creación de instancias
    david = Persona('Ayrton', 35)
    erika = Persona('Erica', 33)

    # Uso de método
    saludo = david.saluda(erika)
    print(saludo)
    # Como se si es una instancia
    print('Es david instancia de Persona:', isinstance(david, Persona))