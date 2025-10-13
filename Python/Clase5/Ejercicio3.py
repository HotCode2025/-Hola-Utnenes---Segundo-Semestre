#Ejercicio : Funcion Recursiva
#Imprimir números de  a de manera descendente usando funciones recursivas
#Puede ser cualquier valor positivo, por ejemplo, si pasamos el
#valor de 5, debe imprimir:
#5
#4
#3
#2
#1
#En caso de ser el número 3 debe imprimir:
#3
#2
#1
#Si se ingresan números negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor ingresado incorrecto')

# Pedir el número al usuario
num = int(input("Ingresa un número: "))

imprimir_numeros_recursivos(num)
