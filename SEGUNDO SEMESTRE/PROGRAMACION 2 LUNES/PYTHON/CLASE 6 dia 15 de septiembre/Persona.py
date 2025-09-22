class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Ariel', 'Betancud', 40) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2 = Persona('Osvaldo','Giordanini', 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es:{persona2.edad}')

#Tarea:

persona3 = Persona('Ariel','Betancud', 40)
print(f'El objeto3 de la clase persona: {persona3.nombre} {persona3.apellido} Su edad es:{persona3.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccela'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es:{persona1.edad}')

#Los atributos son: caracteristicas
#Los atributos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()
