#Ejercicio:
'''Definir una clase padre llamada Vehículo y dos clases hijas llamadas
Auto y Bicicleta, las cuales heredan de la clase padre Vehículo. La
clase padre debe tener los siguientes atributos y métodos:'''
#Clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"
# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def _str_(self):
        return f"Auto -> {super().__str__()}, Velocidad: {self.velocidad} km/h"

# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta -> {super().__str__()}, Tipo: {self.tipo}"

# Crear objetos de cada clase
auto1 = Auto("Azul", 4, 100)
bici1 = Bicicleta("Negra", 2, "Montaña")

print(auto1)
print(bici1)