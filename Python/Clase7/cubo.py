# Crear clase cubo con los atributos, ancho, alto, profundidad
# Con el metodo calcular_volumen que usara la formula ancho * altura * profundidad
# con los datos que el usuario ingrese.

class Cubo:
    
    def __init__(self,ancho,alto,profundo):
        self.alto = alto
        self.ancho = ancho
        self.profundo = profundo
    
    def volumen(self):
        vol = self.profundo * self.alto * self.ancho
        print(f'El volumen del cubo es de {vol} m3') 

# Usuario 1

print('-----------------------USUARIO 1---------------------------------')
ancho = int(input('Ingresar el ancho deseado: '))
alto = int(input('Ingresar el alto deseado: '))
profundo = int(input('Ingresar la profundidad deseada: '))
cubo = Cubo(ancho, alto , profundo)
cubo.volumen()


# Usuario 2

print('-----------------------USUARIO 2---------------------------------')
ancho = int(input('Ingresar el ancho deseado: '))
alto = int(input('Ingresar el alto deseado: '))
profundo = int(input('Ingresar la profundidad deseada: '))
cubo = Cubo(ancho, alto , profundo)
cubo.volumen()

# Usuario 3

print('-----------------------USUARIO 3---------------------------------')
ancho = int(input('Ingresar el ancho deseado: '))
alto = int(input('Ingresar el alto deseado: '))
profundo = int(input('Ingresar la profundidad deseada: '))
cubo = Cubo(ancho, alto , profundo)
cubo.volumen()