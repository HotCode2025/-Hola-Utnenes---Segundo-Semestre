# Lista (son mutables)

nombres = ["Ana", "Luis", "Carlos", "Marta"]
print(nombres)
print(nombres[0])  # Acceder al primer elemento
print(nombres[-1]) # Acceder al último elemento
print(nombres[1:3]) # Acceder a un rango de elementos
# Agregamos diferentes tipos de datos
nombres.append(25)
nombres.append(True)
nombres.append(3.14)
nombres.append([1, 2, 3])
print(nombres)
# Modificar un elemento
nombres[1] = "Luis Miguel"
print(nombres)
# Agregar un elemento al final
nombres.append("Sofía")
print(nombres)
# Insertar un elemento en una posición específica
nombres.insert(2, "Pedro")
print(nombres)
# Eliminar un elemento por valor
nombres.remove("Carlos")
print(nombres)
# Eliminar un elemento por índice
del nombres[0]
print(nombres)
# Eliminar el último elemento y obtener su valor
ultimo = nombres.pop()
print(ultimo)
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("Fin de la iteración")    
# Obtener la longitud de la lista
print(len(nombres))
# Eliminar todos los elementos
nombres.clear()
print(nombres)
# Eliminar la lista
del nombres
# print(nombres)  # Esto generará un error porque la lista ya no existe