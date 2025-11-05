class Aritmetica:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del método será calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres
    """

    class Rectangulo:
        def __init__(self, base, altura):
            self.base = base
            self.altura = altura

        def calcular_area(self):
            return self.base * self.altura

    # Pedimos los datos al usuario
    base = int(input('Digite el número para la base del rectángulo: '))
    altura = int(input('Digite el número para la altura del rectángulo: '))

    # Creamos el objeto
    rectangulo1 = Rectangulo(base, altura)

    # Mostramos el resultado
    print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')