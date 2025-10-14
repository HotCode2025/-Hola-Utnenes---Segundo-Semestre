class Cubo:
    """
    Crear una clase llamada Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la fórmula:
    volumen = ancho * altura * profundidad con los valores que el usuario ingrese.
    """

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad
ancho = int(input('Digite el ancho del cubo: '))
altura = int(input('Digite el alto del cubo: '))
profundidad = int(input('Digite la profundidad del cubo: '))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')