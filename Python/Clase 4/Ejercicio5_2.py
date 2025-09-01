#FACTORIAL DE UN NUMERO POSITIVO
num = int(input("Ingrese un numero entero positivo: "))

factorial = 1
for i in range(1 , num + 1):
    factorial *= i


print(f"El factorial de {num} es = {factorial}")