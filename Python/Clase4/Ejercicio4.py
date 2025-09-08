#Ejercicio 4: Sumar números pares dentro de un rango
#Hacer un programa para sumar números pares dentro
#de un rango, por ejemplo:
#                           suma de números pares del 2 al 30
#                           suma = 240
lista = range(1, 31)
suma = 0
for i in range(1, 31):
    if i % 2 == 0:
        suma += i
print('La suma de los numeros pares es: ',suma)



