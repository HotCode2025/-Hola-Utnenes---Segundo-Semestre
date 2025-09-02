numeros = list(range(1, 51))
for numero in numeros:
    if numero != 50:
        print(f"{numero}-", end="")
    else:
        print(numero)