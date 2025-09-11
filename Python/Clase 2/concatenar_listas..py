# Concatenar listas

lista1 = [1, 2, 3,1]
lista2 = [4, 5, 6,1]
lista3 = lista1 + lista2
print(lista3) # [1, 2, 3, 1, 4, 5, 6, 1]
lista4 = lista1 * 3
print(lista4) # [1, 2, 3, 1, 1, 2, 3, 1, 1, 2, 3, 1]

# Verificar si un elemento está en la lista
print(3 in lista3) # True
print(7 in lista3) # False

# Contar cuántas veces aparece un elemento en la lista
print(lista3.count(1)) # 3
print(lista3.count(7)) # 0
# Obtener el índice de la primera aparición de un elemento
print(lista3.index(5)) # 5
# print(lista3.index(7)) # Arroja error porque el elemento no está en la lista
# Lista de forma descendente
lista3.sort(reverse=True)
print(lista3) # [6, 5, 4, 3, 1, 1, 1, 2]
# Lista de forma ascendente
lista3.sort()
print(lista3) # [1, 1, 1, 2, 3, 4, 5, 6]
# Invertir el orden de la lista
lista3.reverse()
print(lista3) # [6, 5, 4, 3, 2, 1, 1, 1]
# Copiar una lista
lista5 = lista3.copy()
print(lista5) # [6, 5, 4, 3, 2
# Agregar varios elementos a la lista
lista5.extend([7, 8, 9])
print(lista5) # [6, 5, 4, 3, 2, 1, 1, 1, 7, 8, 9]
# Agregar varios elementos a la lista con +
lista5 = lista5 + [10, 11, 12]
print(lista5) # [6, 5, 4, 3, 2, 1, 1, 1, 7, 8, 9, 10, 11, 12]