#Ejercicio 7: Juego adivina el número
#Realizar un juego para adivinar un número. Para ello se debe
#generar un número aleatorio entre 1 - 100, y luego ir pidiendo
#números indicando "es mayor" o "es menor" segun sea mayor o menor
#con respecto a N. El proceso termina cuando el usuario acierta
#y alli se debe mostrar el número de intentos

numeros = list(range(1, 101))

numero_aleatorio = numeros[49]

intentos = 0
eleccion = 0

print("Adivina un número entre 1 y 100!")

while eleccion != numero_aleatorio:
    eleccion = int(input("Tu número: "))
    intentos += 1

    if eleccion < numero_aleatorio:
        print("El número secreto es mayor.")
    elif eleccion > numero_aleatorio:
        print("El número secreto es menor.")

print(f"¡Perfecto! Has adivinado en {intentos} intentos.")