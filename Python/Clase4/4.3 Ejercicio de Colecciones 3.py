# Ejercicio 3: Agregar personajes a una lista
# Escribir un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# TAREA

# Nombre: Gimli
# Clase: Guerrero/Herrero
# Raza: Enano

# Nombre: Frodo Bolsón
# Clase: Portador del anillo
# Raza: Hobbit

# Nombre: Boromir
# Clase: Capitán de Gondor
# Raza: Hombre (de Gondor)

personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P = {'Nombre': 'Aragon' , 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(P) # Agregamos a la lista un personaje
P = {'Nombre': 'Gandalf' , 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas' , 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase': 'Guerrero/Herrero' , 'Raza': 'Enano'}
personajes.append(P)
P = {'Nombre': 'Frodo Bolsón', 'Clase': 'Portador del anillo' , 'Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Boromir', 'Clase': 'Capitán de Gondor' , 'Raza': 'Hombre (de Gondor)'}
print(personajes)