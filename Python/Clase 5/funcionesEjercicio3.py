def numero_descendente(num):
    if num <= 0: #Si el numero es igual o menor a 0 no hace nada
        return
    print(num)
    numero_descendente(num - 1)

numero = int(input("Ingresa un numero positivo: "))
numero_descendente(numero)


