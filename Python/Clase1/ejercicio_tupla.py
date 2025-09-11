# Data la siguiente tupla
tupla = (13,1,8,3,2,5,8) 
# Crear una lista que solo incluya los numeros menores a 5  y los imprima en pantalla
menores_a_5 = []
for num in tupla:
    if num < 5:
        menores_a_5.append(num)
print(menores_a_5)