#Ejercicio 8: Menu interactivo - Cajero automatico
#Hacer un programa que simule un cajero automatico con un saldo
#inicial de $1000 y tendra el siguiente menu de opciones:
#                1. Ingresar dinero en la cuenta
#                2. Retirar dinero de la cuenta
#                3. Mostrar dinero disponible
#                4. Salir

saldo = 1000
while True:
    print("1. Ingresar dinero en la cuenta.")
    print("2. Retirar dinero de la cuenta.")
    print("3. Mostrar dinero disponible.")
    print("4. Salir.")

    opcion = input("Elige una opcion ente 1 y 4: ")

    if opcion == "1":
        dinero = int(input("Cuanto deseas ingresar?: $"))
        if dinero > 0:
            saldo += dinero
            print(f"Has ingresado ${dinero: }. Saldo actual: ${saldo}")
        else:
            print("El monto debe ser mayor a $0.")
    elif opcion == "2":
        dinero = int(input("Cuanto deseas retirar?: $"))
        if dinero < saldo:
            saldo -= dinero
            print(f"Has retirado ${dinero: }. Saldo actual: ${saldo}")
        else:
            print("Fondos insuficientes.")
    elif opcion == "3":
        print(f"Tu saldo actual es: ${saldo:}")
    elif opcion == "4":
        print("Gracias por utilizar nuestro cajero.")
        break
    else:
        print("Opción no valida. Intentalo nuevamente.")