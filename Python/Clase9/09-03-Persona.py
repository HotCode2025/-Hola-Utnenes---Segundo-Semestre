class Persona:
    # Esta clase hereda de 'object' implícitamente
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Representación legible del objeto
    def __str__(self):
        return f'Persona: {self.nombre}, Edad: {self.edad}'


class Empleado(Persaona):  # <- si tu profe usa 'Persona', déjalo así: Empleado(Persona)
    # Esta clase es hija de Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.sueldo = sueldo

    # Sobrescribimos __str__ y reutilizamos el del padre
    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self.sueldo}'


# Pruebas rápidas
if __name__ == '__main__':
    persona1 = Persona('Carlos', 30)
    print(persona1)  # Persona: Carlos, Edad: 30

    empleado1 = Empleado('Ariel', 40, 75000)
    print(empleado1)  # Persona: Ariel, Edad: 40, Sueldo: 75000
