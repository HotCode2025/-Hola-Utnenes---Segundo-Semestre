# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 y 100. Luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y se muestra el número de intentos.

import random

print("\t.:Juego Adivina el número:.")
aleatorio = random.randint(1, 100)  # Generamos un número aleatorio
contador = 0

while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("No es el número, digite un número menor")
    elif numero < aleatorio:
        print("No es el número, digite un número mayor")
    else:
        print(f"\n¡FELICIDADES! Adivinaste el número {aleatorio}")
        print(f"Número de intentos: {contador}")
        break
