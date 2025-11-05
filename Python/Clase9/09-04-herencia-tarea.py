# Clase padre
class Persona:
    # Esta clase hereda de Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter y setter para nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Getter y setter para edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


# Clase hija
class Empleado(Persona):
    # Esta clase es hija de Persona
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


# --- PRUEBA DEL CÓDIGO ---
empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

# Crear otro objeto y mostrar datos
empleado2 = Empleado('Liliana', 38, 70000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

# Modificar los datos
empleado2.nombre = 'Natalia'
empleado2.edad = 35
empleado2.sueldo = 75000

# Mostrar nuevamente los datos modificados
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
