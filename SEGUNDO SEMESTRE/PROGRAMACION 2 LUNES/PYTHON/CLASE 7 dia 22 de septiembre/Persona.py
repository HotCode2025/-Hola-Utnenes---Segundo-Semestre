class Persona: # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args,**kwargs ):
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido}{self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud',2345678, 40) #Necesitamos enviar argumentos
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

persona2 = Persona('Osvaldo','Giordanini', 2345678,  45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es:{persona2.edad}')

#Tarea:

persona3 = Persona('Ariel','Betancud', 23456789, 40)
print(f'El objeto3 de la clase persona: {persona3.nombre} {persona3.apellido} Su edad es:{persona3.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccela'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es:{persona1.edad}')

#Los atributos son: caracteristicas
#Los atributos son: el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle() #La referencia en estos casos se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar.detalle(persona1) #Debemos pasarle una referencia para el self o dará error
persona1.telefono = '44445555289'
print(f'Este es el teléfono de: {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

persona3 = Persona('Rogelio', 'Romero ', 23456456,22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Cfavorito='Azul', Auto= 'Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni)esto no se debe utilizar(esta encapsulado) en python, esto dice que desconocemos python

#persona3.__nombre #esta totalmente encapsulado


