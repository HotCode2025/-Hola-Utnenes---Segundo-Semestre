#Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas)) #Usamos la función len = length signifit largo

#Revisar si un elemnto existe dentro de set
print('Júpiter' not in planetas)
#Agregar un elemento
planetas.add('Tierra') # add es una función
print(planetas)
#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') #Esta funcion ante un mal ingreso u inexistencia del elemento da como resultado error
print(planetas)
planetas.discard('tierra') #Esta funcion no nos presenta ningún error, no elimina el elemento tampoco
print(planetas)
#Limpiar set
planetas.clear()
print(planetas)
#Eliminar el conjunto
del planetas
#print(planetas) #al eliminar nos muestra fun error

# 'Maradona':10 un diccionario esta compuesto por dos elementos:
#una llave y un valor
#dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
     'POO':'Programación Orientada a Objetos',
     'SABD': 'Sistema de Administración de Base de Datos'
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)
#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))
#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como reccorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)
#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves
for valor in diccionario.values():#Usamos una funcion para acceder al valor
    print(valor)
#Comproamos la existencia de algun elemento
print('IDE' in diccionario) #devuelve un booleano

#Agregamos un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)
#Vaciar un diccionario
diccionario.clear()
print(diccionario)
#Eliniar diccionario
del diccionario #el diccionario se borro

#Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 #Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) #Funcion para agregar varios elementos a una lista
print(lista3)
print(lista3.index(5)) #Funciona para ubicar varios elementos en una lista
#print(lista3.index(0))#estos daria un error por no ser el elemento que es parte de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay en la lista
#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)
lista3 = lista3 * 2
print(lista3)

#Metodos de ordenamiento
lista3.sort() #Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente
print(lista3)

tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo booleana
#Lo que podemos usar dentro de tuplas son: index, count, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla
