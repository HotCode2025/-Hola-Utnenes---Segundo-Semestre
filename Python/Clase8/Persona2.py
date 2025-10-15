class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get para nombre')
        return self._nombre

    @property
    def apellido(self):  # Método Getter
        print('Estamos utilizando el método get para apellido')
        return self._apellido

    @property
    def edad(self):  # Método Getter
        print('Estamos utilizando el método get para edad')
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el método set para nombre')
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el método set para apellido')
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        print('Estamos utilizando el método set para edad')
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':

    persona1 = Persona2('Ariel', 'Betancud', 41)

    # Usamos getters
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    # Usamos setters
    persona1.nombre = 'Natalia'
    persona1.apellido = 'Lucero'
    persona1.edad = 35

    # Mostramos los nuevos datos
    persona1.mostrar_detalles()
    #Tarea crear tres objetos más, utilizando los métodos getter and setter
    #para modificar, y mostrar los cambios con el método mostrar detalles

    #Objeto numero 1:

    persona2 = Persona2('Flor', 'Romero', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22

    print(persona2.mostrar_detalles())

    #Objeto numero 2:

    persona3 = Persona2('Caro', 'Felisa',21 )
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Carolina'
    persona3.apellido = 'Felix'
    persona3.edad = 31

    print(persona3.mostrar_detalles())

    #Objeto numero 3:

    persona4 = Persona2('Naty', 'Lucer', 35)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Natalia'
    persona4.apellido = 'Lucero'
    persona4.edad = 36

    print(persona4.mostrar_detalles())

    print(__name__)