# lista = Florencia, Ariel, Natalia

nombres = ['Naty','Osvaldo','Lily','Ariel']
print(nombres)

#print(nombres[0])
#print(nombres[1])
#print(nombres[3])
#print(nombres[-1])
#print(nombres[-2])
print(nombres[0:2]) #Solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #indice a mostrar 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #le pasamos como parametro la lista
nombres.append('Marcelo')
print(nombres)

#Insertar un elemento en un indice específico
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

#Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

#Eliminar el último elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete(eliminar)
print(nombres)

#Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
#print(nombres) #Aqui nos mostrara un error

#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])
#mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ('papa',) #una tupla necesita aunque sea de un elemento: la coma
#de lo contrario solo seria un tipo string(cadena)

#Recorremos los elementos de la tupla
for cocinar in cocina: #print esta usando \n para saltos de lineas
    print(cocinar, end= ' ') #Usamos end= para eliminar los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#del cocina esto es para eliminar una tupla
