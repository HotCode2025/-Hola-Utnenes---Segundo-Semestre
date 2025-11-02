class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = persona("joaquin","ybañez",20)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)