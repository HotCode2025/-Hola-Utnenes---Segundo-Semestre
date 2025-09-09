#Ejercicio 11. Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendra el siguiente menu de opciones:
#      1. Nuevo contacto
#      2. Borrar contacto
#      3. Ver contactos existentes
#      4. Salir

contactos = { }
salir = False
while not salir:
    print('-Agenda de contactos-')
    opcion = int(input('Elija una opcion: \n1. Nuevo contacto. \n2. Borrar contacto. \n3. Ver contactos existentes. \n4. Salir.\n'))
    #print('1. Nuevo contacto. \n2. Borrar contacto. \n3. Ver contactos existentes. \n4. Salir.')

    if opcion == 1:
        nombre = str(input('Nombre del contacto: '))
        telefono = int(input('Numero de telefono: '))
        contactos[nombre] = telefono

    elif opcion == 2:
            nombre = str(input('Nombre del contacto a borrar: '))
            if nombre in contactos:
                del contactos[nombre]
                print(f'Contacto {nombre} borrado.')
            else:
                print('El contacto no existe.')
    elif opcion == 3:
        if contactos:
            print('Lista de contactos:')
            for nombre, telefono in contactos.items():
                print(f'Nombre: {nombre} - Teléfono: {telefono}')
        else:
            print('La agenda esta vacia.')
    elif opcion == 4:
        salir = True
    else:
        print('Opción no válida. Ingrese un número entre 1 y 4.')