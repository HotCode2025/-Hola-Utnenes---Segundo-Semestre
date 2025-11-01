#lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily','Ariel']
print(nombres)
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
#er del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #indices a mostrar 0,1,2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar nuestra lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)

else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene
print(len(nombres)) #le pasamos como parametro la lista

#agregamos un elemento
nombres.append('Marcelo')
print(nombres)

#insertar un elemento en un indice especifico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)


#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)



# Definimos una tupla
cocina =('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))


#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])


#acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ('papa',) #una tupla necesita una coma aunque sea de 1 elemento
#de lo contrario solo seria un tipo str cadena


#recorremos los elementos de la tupla
for cocinar in cocina:#print esta usando \n para saltos de lineas
    print(cocinar, end=' ') #usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina # esto es para eliminar una tupla

 #tipo set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) #Usamos la funcion len = length significa largo

#revisar si un elemento existe dentro del set
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') #Add es una funcion
print(planetas)

#eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') #Esta funcion ante un mal ingreso u inexistencia del elemento da  error
print(planetas)
planetas.discard('Tierra') #Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set
planetas.clear()
print(planetas)

#Eliminar  o conjunto
del planetas
#print(planetas) #al eliminar nos muestra un error

# 'Maradona':10 un diccionario esta compuesto por dos elementos
#UNA LLAVE Y UN VALOR
#DICT(KEY,VALUE)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administacion de Base de Datos'
}
#verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)


#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])


#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))


#Modificar elementos
diccionario['IDE'] = 'Entorno desarollo integrado'
print(diccionario)

#como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)
 #necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #Estamos usando una funcion
    print(termino)#Muestra solo las llaves


for valor in diccionario.values(): #Usamos una funcion para acceder al valor
    print(valor)


#Comprobar la existencia de algun elemento
print('IDE' in diccionario)


#Agregar un elemento
diccionario['PK'] = 'Pimary Key'
print(diccionario)


#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #el diccionario se borro

#Concateamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 #Concatenamos
print(lista3)

lista3.extend([7, 8, 9, 1]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) #Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0)) #Esto daria un error por no ser el elemento parte de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de la lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)


#Metodos de ordenamiento
lista3.sort() #Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente
print(lista3)
#Repaso de tuplas
tupla = (4, 'Hola', 6.78, [1, 2, 78],4, 'Hola') #Puede tener diferentes tipos de datos dentro
print(tupla)


print(4 in tupla) #Accion booleana, su respuesta es de tipo booleana
#Lo que podemos usar dentro de tuplas son: index c# ount, len
#En tuplas se puede convertir de tupla a lista y de lista a tupla