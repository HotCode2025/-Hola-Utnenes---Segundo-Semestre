from Empleado import Empleado

def imprimir_detalles(objeto):
    print(objeto) #De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto)) # Esto es para saber el tipo de dato que recibe


empleado = Empleado('Ariel', 50000)
imprimir_detalles(empleado)
