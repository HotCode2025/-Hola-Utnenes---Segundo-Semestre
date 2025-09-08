#Ejercicio 5: Factorial de un número positivo
#Hacer un programa para calcular el factorial de un número positivo

numero = int(input('Ingresa un número positivo: '))
while numero <0:
    print('Error, el número tiene que ser positivo')
    numero = int(input('Digite un numero nuevamente: '))
factorial = 1
for i in range(1, numero+ 1):
    factorial *= i
print(f'El factorial de {numero} es {factorial}')
