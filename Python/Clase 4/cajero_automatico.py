saldo = 1000  # saldo inicial

while True:
    print("\n--- Cajero Automático ---")
    print("1) Ingresar dinero")
    print("2) Retirar dinero")
    print("3) Mostrar saldo")
    print("4) Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        monto = float(input("Monto a ingresar: $"))
        saldo += monto
        print(f"Depósito ok. Saldo: ${saldo:.2f}")

    elif opcion == "2":
        monto = float(input("Monto a retirar: $"))
        if monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Retiro ok. Saldo: ${saldo:.2f}")

    elif opcion == "3":
        print(f"Saldo disponible: ${saldo:.2f}")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
