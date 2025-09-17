#Ejercicio 3: Agregar personajes a una lista
#Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragorn
# Clase: Guerrero
# Raza: Dúnadan del Norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Nombre: Frodo
# Clase: Portador del Anillo
# Raza: Hobbit

# Nombre: Gimli
# Clase: Guerrero
# Raza: Enano

# Nombre: Boromir
# Clase: Guerrero
# Raza: Hombre de Gondor


# Creamos una lista vacía
personajes = []

# Creamos diccionarios y los agregamos a la lista
p = {'Nombre': 'Aragorn', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(p)

p = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p)

p = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(p)

p = {'Nombre': 'Frodo', 'Clase': 'Portador del Anillo', 'Raza': 'Hobbit'}
personajes.append(p)

p = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}
personajes.append(p)

p = {'Nombre': 'Boromir', 'Clase': 'Guerrero', 'Raza': 'Hombre de Gondor'}
personajes.append(p)

# Imprimir la lista completa
print(personajes)

