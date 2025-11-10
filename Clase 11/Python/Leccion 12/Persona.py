class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(sel, other): #Other significa = otro
        return self.nombre + other.nombre
    
    def __sub__(self, otro): #Sub significa = substraccion (resta)
        return self.edad - otro.edad


persona1 = Perona('Ariel',40)
persona2 = Persona('Betancud',5)

# persona1.__add__(persona2) sintaxis interna y automatica

print(persona1 + persona2)
print(persona1 - persona2)