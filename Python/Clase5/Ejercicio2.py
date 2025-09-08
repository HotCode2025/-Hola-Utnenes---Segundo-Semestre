#Ejercicio 2: Función con *args para multiplicar
#Crear una función para multiplicar los valores recibidos
#de tipo numérico, utilizando argumentos variables *args
#como parámetro de la función y regresar como resultado
#la multiplicación de todos los valores pasados como argumento

def multiplicar(*args): #creamos función para multiplicar
    resultado = 1
    for numero in args: #recorremos los argumentos
        resultado *= numero #multiplicamos cada número
    return resultado #devolvemos el resultado
lista_numeros = [2, 3, 4, 5] #creamos lista de números
#usamos para desempacar la lista y pasarlos como argumentos
print(f'El total es: ', multiplicar(*lista_numeros)) #resultado final de la multiplicación de cada número de la lista al resultado
