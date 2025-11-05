#Utilizamos la clase persona (perteneciente a la clase 6) para utilizar la palabra reservada self
#Esta clase pertenece a la clase 6 (para que pueda correr el código) y más abajo agrego
#lo perteneciente a la clase 7.
class Persona: #Creamos una Clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    def mostrar_detalle(self): #self es igual a this
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')


persona1 = Persona('Ariel', 'Betancud', 30235633, '40') #Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 12653699, '45')
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')
#Tarea: Hacer lo mismo pero con persona1
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')
#Esta parte ya pertenece a la clase 7:
#Los atributos son: caracteristicas
#Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() #la referencia en este caso se pasa de manera automática
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dará error
persona1.telefono = '4465656456'
print(f'Este es el teléfono de: {persona1.nombre} {persona1.telefono}') #Hemos creado un atributo

#print(perosna2.telefono) el objeto persona2 no tiene este atributo, da error
persona3 = Persona('Rogelio', 'Romero', 5636333,'Teléfono', '4565652', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar en python,esto dice que lo desconocemos
#persona3.__nombre esta totalmente encapsulado