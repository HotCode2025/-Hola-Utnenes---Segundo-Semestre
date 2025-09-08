#Ejercicio 3: Insertar elementos y ordenarlos
#pedir números y meterlos en una lista, cuando el usuario
#introduzca un número 0, nuestro programa dejaría de insertar.
#Por último, mostrarlos números ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Digite un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()#La lista está ordenada con esta funcion
print(f'\nLista ordenada: \n{lista}')