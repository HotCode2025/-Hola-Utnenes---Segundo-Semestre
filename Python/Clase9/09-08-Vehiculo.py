# Clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)


# Clase hija Auto
class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad  # km/hr

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)


# Clase hija Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # urbana, montaña, etc.

    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo


# --- Objetos de cada clase ---

# Objeto 1: clase padre Vehículo
vehiculo = Vehiculo('Blanco', 4)
print(vehiculo)
# Salida: Color: Blanco, Ruedas: 4

# Objeto 2: clase hija Auto
auto = Auto('Amarillo', 4, 120)
print(auto)
# Salida: Color: Amarillo, Ruedas: 4, Velocidad(km/hr): 120

# Objeto 3: clase hija Bicicleta
bici = Bicicleta('Azul', 2, 'Urbana')
print(bici)
# Salida: Color: Azul, Ruedas: 2, Tipo: Urbana
