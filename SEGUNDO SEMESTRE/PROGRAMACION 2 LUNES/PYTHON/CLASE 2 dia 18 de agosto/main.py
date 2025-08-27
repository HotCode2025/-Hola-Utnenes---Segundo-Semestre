#Tipo ser
planetas = {'Marte','Júpiter','Venus'}
print(len(planetas))#Usamos la funcion len = length significa largo

#REvisar si un elemento existe dentro del set
print('Júpiter' in planetas)

#Agregar un elemento
planetas.add('Tierra') #Add es una funcion
print(planetas)

#Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove('Júpiter')#Esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)
planetas.discard('Tierra')#Esta funcion no nos presenta nignun error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#eliminar set o conjunto
del planetas
#print(planetas) #Al eliminar nos muestra un error

#Diccionario

#'Maradona':10 Un diccionario esta compuesto por dos elementos
#una LLAVE y un VALOR
#dick(key,value)
diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Recorrer los elementos
for termino in diccionario:#Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():#Estamos usando una funcion
    print(termino)#Muestra solo las llaves

for valor in diccionario.values():#Usamos una funcion para acceder al valor
    print(valor)

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)#Devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar el diccionario
del diccionario #El diccionario se borró

#Concatenamos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1+lista2 #Concatenacion
print(lista3)

lista3.extend([7,8,9,1]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) #Esto daria un error por no ser el elemento parte de la lista

#Como saber cuantos valores hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner nuestra lista al reves
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento, en python es una funcion
lista3.sort() #Ordena los lementos de forma ascendente
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente
print(lista3)

#Repaso de tuplas

tupla = (4, 'Hola', 6.78,[1,2,78], 4, 'Hola')#Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es tipo booleana
#Lo que podemos usar dentro de tuplas son: index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla







