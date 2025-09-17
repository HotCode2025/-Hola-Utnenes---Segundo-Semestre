# Arguments, variables en funciones
def listarNombres(*nombres):  # Normalmente se utiliza: *args
    for nombre in nombres:  # Se va a convertir en una tupla
        print(nombre)

listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'Maria')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos):  # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): #kwars significa key word arguments
        print(f'{llave} : {valor}')

listarTerminos()  # No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy Key')
listarTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres([10, 11] # No es un objeto iterable
desplegarNombres([10, 11])# La convertimos a una taula, en un solo elemento no olvidar la coma
desplegarNombres([22, 55])# La convertimos en una lista

#Funciones Recursivas
def factorial(numero):
    if numero == 1: #Caso base
        return 1
    else:
        return numero * factorial(numero-1)#Caso recursivo

resultado = factorial(5) #Lo hacemos en codigo duro
print(f'El factorial del número 5 es: {resultado}')