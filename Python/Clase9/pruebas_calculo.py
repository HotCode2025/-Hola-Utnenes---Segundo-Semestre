from rectangulo import Rectangulo
from cuadrado import Cuadrado

#Creadmos una instancia

cuadrado = Cuadrado(10 ,10, 'Verde')

# Mostramos los datos

print(cuadrado.calcular_area())

# Modificamos los datos 

cuadrado.alto = 5
cuadrado.ancho = 5
cuadrado.color = 'Azul'

# Mostramos los datos nuevos

print(cuadrado.calcular_area())

#Creadmos una instancia

rectangulo = Rectangulo(5 , 5 , 'Rojo')

# Mostramos los datos

print(rectangulo.calcular_area()) 

# Modificamos los datos 

rectangulo.alto = 10
rectangulo.ancho =  10
rectangulo.color = 'Blanco'

# Mostramos los datos nuevos

print(rectangulo.calcular_area())
