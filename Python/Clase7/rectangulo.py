# Crear clase rectanguloi, que debe tener dos atributos, altura y base
# Debe tener un metodo calcular Area con la formula base* altura
# Los datos deben ser ingresados por el usuario ( debe3n ser 3 )

class Rectangulo:

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        area = self.base * self.altura
        print(f'El area del rectangulo es: {area} m2')


# Usuario 1
print('-----------------------USUARIO 1---------------------------------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo1 = Rectangulo(altura, base)
rectangulo1.calcular_area()


# Usuario 2

print('-----------------------USUARIO 2---------------------------------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo1 = Rectangulo(altura, base)
rectangulo1.calcular_area()

# Usuario 3

print('-----------------------USUARIO 3---------------------------------')
altura = int(input('Ingresar la altura deseada: '))
base = int(input('Ingresar la base deseada: '))
rectangulo1 = Rectangulo(altura, base)
rectangulo1.calcular_area()
