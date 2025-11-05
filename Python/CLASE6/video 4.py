class persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = persona("joaquin","ybañez",20)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = persona("maxi","garcia",21)
print(f"el objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}")