#Ejercicio 2: Modificar los elemento de una lista
#Llenar una lista con los números del 1 al 10, luego modificar
#los elementos de la lista multiplicandolos por un valor
#ingresado por el usuario
import math

lista = list(range(1, 11))
for i in lista:
    print (i , end = ", " )
multiplicador = int(input("Digite un numero para multiplicar la lista: "))
for i in range(len(lista)):
    lista[i] *= multiplicador
print("Lista modificaa:", lista)