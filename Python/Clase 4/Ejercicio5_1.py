#SUMAS NUMEROS PARES DENTRO DE UN RANGO
inicio = int(input("Ingrese el primer numero del rango: "))
final = int(input("Ingrese el ultimo numero del rango: "))

suma = 0
for i in range(inicio, final + 1):
    if i % 2 == 0:
        suma += i

print(f"La suma de los números pares entre {inicio} al {final} es:", suma)