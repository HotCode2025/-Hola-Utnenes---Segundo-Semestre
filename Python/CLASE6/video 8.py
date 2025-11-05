class persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(self.nombre, self.apellido, self.edad)


persona1 = persona("joaquin", "ybañez", 20)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = persona("maxi", "garcia", 21)
print(f"el objeto 2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}")

persona1.nombre = "nicolas"
persona1.apellido = "martini"
persona1.edad = 23
print(f"el objeto modificado de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}")

persona1.mostrar_detalle()
persona2.mostrar_detalle()