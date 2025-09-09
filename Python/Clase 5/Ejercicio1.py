#Ejercicio 1: Crear una función para sumar los valores recibidos de tipos
#numéricos, utilizando argumentos variables *args como parametro de la
#función y agregar como resultado la suma de todos los valores pasados
#como argumentos.

def sumar(*args): #creamos función para sumar
    total = 0
    for numero in args: #recorremos los argumentos
        total += numero #sumamos cada uno
    return total
resultado = sumar(1, 2, 3, 4, 5)
print("La suma es: ", resultado)