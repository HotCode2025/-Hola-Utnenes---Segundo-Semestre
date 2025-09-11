# Tupla ( son inmmutrables )

cocina = ("cuchara", "tenedor", "cuchillo")
print(cocina)

print(cocina[0])  # Acceder al primer elemento
print(cocina[-1]) # Acceder al último elemento

print(cocina[0:2]) # Acceder a un rango de elementos
# cocina[0] = "plato"  # Esto generará un error porque las tuplas son inmutables

# Iterar una tupla
for utensilio in cocina:
    print(utensilio, end="#") # con el end, agregeo algo al final de cada elemento 
    

# Obtener la longitud de la tupla
print(len(cocina))
# Eliminar la tupla
del cocina

# print(cocina)  # Esto generará un error porque la tupla ya no existe
# Una tupla con un solo elemento debe llevar una coma al final, sino tiene el tipo de la variable (str,num, etc)
tupla_un_elemento = (5,)
no_tupla_un_elemento = (5)
print(tupla_un_elemento)
print(type(tupla_un_elemento))
print(type(no_tupla_un_elemento))

# Una tupla sin paréntesis también es válida
otra_tupla = 1, 2, 3, 4
print(otra_tupla)
print(type(otra_tupla))
# Convertir una lista en una tupla
lista = [1, 2, 3, 4]
tupla_desde_lista = tuple(lista)
print(tupla_desde_lista)
print(type(tupla_desde_lista))
# Convertir una tupla en una lista
tupla = (5, 6, 7, 8)
lista_desde_tupla = list(tupla)
print(lista_desde_tupla)
print(type(lista_desde_tupla))
print(type(tupla))
# Desempaquetado de tuplas
frutas = ("manzana", "banana", "cereza")
a, b, c = frutas
print(a)
print(b)
print(c)
# a, b = frutas  # Esto generará un error porque no coinciden las cantidades de variables y elementos
# Si no se sabe cuántos elementos hay, se puede usar el asterisco
a, *b = frutas
print(a)
print(b)


