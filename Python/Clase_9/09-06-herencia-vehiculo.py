# Clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Vehículo [Color: {self.color}, Ruedas: {self.ruedas}]'


# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # en km/h

    def __str__(self):
        return f'Auto [Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} km/h]'


# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # urbana, montaña, etc.

    def __str__(self):
        return f'Bicicleta [Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}]'


# --- Crear un objeto de cada clase ---
vehiculo1 = Vehiculo('Rojo', 4)
print(vehiculo1)

auto1 = Auto('Negro', 4, 150)
print(auto1)

bicicleta1 = Bicicleta('Azul', 2, 'Montaña')
print(bicicleta1)
