#Ejercicio 8: Menú interactivo - Cajero automático
#Hacer un programa que simule un cajero automático con un saldo
#inicial de 1000$ y tendrá el siguiente menú de opciones:
#                  1. Ingresar dinero en la cuenta
#                  2. Retirar dinero de la cuenta
#                  3. Mostrar dinero disponible
#                  4. Salir

saldo = 1000
while True:
    print('\n1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')

    opcion = input('Elegir una opcion: ')

    if opcion == '1':
        ingreso = float(input('¿Cuánto dinero desea ingresar?: '))
        saldo += ingreso
        print(f'Ingresaste ${ingreso}. Tu saldo ahora es ${saldo}')

    elif opcion == '2':
        retiro = float(input('¿Cuánto dinero desea retirar?: '))
        if retiro > saldo:
            print('Saldo insuficiente.')
        else:
            saldo -= retiro
            print(f'Su retiro es de ${retiro}. Su nuevo saldo es de: ${saldo}')

    elif opcion == '3':
        print(f'Su saldo disponible es de: ${saldo}')

    elif opcion == '4':
        print('Gracias por elegirnos!')
        break  # salimos del bucle

    else:
        print('Opción inválida, intente de nuevo.')
