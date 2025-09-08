#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le
#devolverá la misma frase pero sin espacios en blanc, y
#además un contador de cuantos caracteres tiene la frase
#sin contar los espacios en blanco)
#Ejemplo:       frase = vivir por siempre en paz
#               frase final = vivirposiempreenpaz
#               n° de caracteres = 20

frase = input('Escriba una frase: ')

frase_sin_espacios = frase.replace(' ', '')
caracteres = len(frase_sin_espacios)

print(f'Frase sin espacios: {frase_sin_espacios}')
print(f'Numero de caracteres sin espacio: {caracteres}')
