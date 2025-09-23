class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f'El área del rectángulo es: {area} m2')


# Usuario 1
print('--------USUARIO 1---------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo1 = Rectangulo(base, altura)
rectangulo1.calcular_area()

# Usuario 2
print('--------USUARIO 2---------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo2 = Rectangulo(base, altura)
rectangulo2.calcular_area()

# Usuario 3
print('--------USUARIO 3---------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo3 = Rectangulo(base, altura)
rectangulo3.calcular_area()

