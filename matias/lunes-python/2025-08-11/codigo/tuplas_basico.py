# Tuplas: inmutables
t = ("a", "b", "c")
print("Tupla:", t)

# convertir a lista para “modificar”
lista = list(t)
lista.append("d")
t2 = tuple(lista)
print("Tupla modificada (vía lista):", t2)

# tupla de un solo elemento: OJO coma
uno = (42,)
print("Tupla de un elemento:", uno, type(uno))
