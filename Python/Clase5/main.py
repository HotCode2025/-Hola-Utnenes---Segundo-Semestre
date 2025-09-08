#Desempaquetado de listas o list unpacking

def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la función
show(*person)#Esto e slo mismo que lo anterior pero lo pasamos todo junto
person2 = ('Osvaldo', 'Giodanini') #desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}#desempaquetamos a travez de un diccionario
show(*person3)

numbers = [1, 2, 3, 4, 5] #Aun con la lista vacia se va a ejercutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #sta es la unica manera para que no se ejecute el else
else:
    print('Esto se termina')
#list comprehension, lista de comprensión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de Argumentos (funciones)
def mi_funcion(name, lastName):
    print("Saludos a todos los que ven a través del canal de Youtube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion("Jorge", "Lucero")
mi_funcion("Ariel", "Betancud")
mi_funcion("Analia", "Pedrosa")

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a, b):
    return a +b
#resultado = sumar(78, 22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0): #Le damos un valor por default
    return a +b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #Normalmente se utiliza: *args
    for nombre in nombres: #se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosa', 'María')
listarNombres('MArcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos') #se van agregando los elementos como argumentos
