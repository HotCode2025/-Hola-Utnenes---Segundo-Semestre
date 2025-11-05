# Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Método __str__ para representar la clase Persona como texto
    def __str__(self):
        return f'Persona: [Nombre: {self._nombre}, Edad: {self._edad}]'


# Clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    # Getter y setter para sueldo
    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    # Sobrescritura del método __str__
    def __str__(self):
        return f'Empleado: [Nombre: {self._nombre}, Edad: {self._edad}, Sueldo: {self._sueldo}]'


# --- Pruebas ---
empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1)  # Empleado: [Nombre: Ariel, Edad: 40, Sueldo: 75000]

empleado2 = Empleado('Liliana', 38, 70000)
print(empleado2)  # Empleado: [Nombre: Liliana, Edad: 38, Sueldo: 70000]
