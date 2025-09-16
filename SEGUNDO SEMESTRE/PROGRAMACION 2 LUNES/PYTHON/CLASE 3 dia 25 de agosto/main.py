# Repaso de set o conjunto
# Para definir un conjunto
conjunto2 = set()
conjunto1 = {'Bye',}

conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)

conjunto1.add('Hola')
print(conjunto1)

print(3 not in conjunto1) #Preguntamos si el número 3 NO esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) #Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que esta n el conjuntp1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #Elementos que no comparte o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #Aqui preguntamos su un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto 1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) #Si es verdadero quiere decir que el conjunto3 es un super conjunto
print(conjunto2.issuperset(conjunto3))

#Como saber su ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))#No hay cosas en comun

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso de diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

#Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel' : {'edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')


# Colas con listas
# Estructura de datos de tipo fifo (first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)














