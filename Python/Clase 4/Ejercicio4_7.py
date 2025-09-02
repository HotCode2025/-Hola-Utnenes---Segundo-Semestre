# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10, luego modificar los
# elementos de la lista multiplicándolos por un valor ingresado por el usuario
numeros = list(range(1, 11))  # Declara una lista llamada "numeros" con números del 1 al 10
print("Lista original:", numeros)  # Muestra la lista original
factor = int(input("Ingrese un valor para multiplicar los elementos de la lista: "))  # Solicita un valor al usuario
numeros = [x * factor for x in numeros]  # Modifica los elementos de "numeros"
print("Lista modificada:", numeros)  # Muestra la lista modificada
