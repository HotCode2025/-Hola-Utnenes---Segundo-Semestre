#Ejercicio 10. No repetir caracteres
#Hacer un programa que pida una cadena por teclado, luego
#meter los caracteres en una lista sin repetir caracteres

lista = []
salir = False
while not salir: #mientras sea verdadero
    cadena = str(input('Digite su cadena: '))
    if cadena in lista:
        salir = True
    else:
        lista.append(cadena)
print('Esa cadena ya se encuentra en la lista.')
print(f'Lista completa: {lista}')