# Set

planetas = {"Venus", "Tierra", "Marte"}
print(planetas) # en cada iteracion cambie el orden

print(len(planetas)) # 3
print("Tierra" in planetas) # True
print("Jupiter" in planetas) # False
print("Jupiter" not in planetas) # True
print("Marte" not in planetas) # False
print(type(planetas)) # <class 'set'>

# No se pueden tener elementos repetidos
planetas.add("Tierra") # No hace nada
print(planetas) # {'Venus', 'Tierra', 'Marte'}
planetas.add("Jupiter") # Agrega el elemento
print(planetas) # {'Venus', 'Tierra', 'Marte', 'Jupiter'}
planetas.remove("Venus") # Elimina el elemento
print(planetas) # {'Tierra', 'Marte', 'Jupiter'}
# planetas.remove("Venus") # Arroja error porque no existe el elemento
planetas.discard("Venus") # No hace nada porque no existe el elemento
print(planetas) # {'Tierra', 'Marte', 'Jupiter'}
planetas.discard("Marte") # Elimina el elemento
print(planetas) # {'Tierra', 'Jupiter'}
planetas.clear() # Elimina todos los elementos
print(planetas) # set()
planetas = {"Venus", "Tierra", "Marte"}
print(planetas) # {'Venus', 'Tierra', 'Marte'}
# No se puede acceder a un elemento por su indice
# print(planetas[0]) # Arroja error
for planeta in planetas:
    print(planeta) # Imprime los elementos en orden aleatorio

# Operaciones de conjuntos
planetas_a = {"Venus", "Tierra", "Marte"}
planetas_b = {"Marte", "Jupiter", "Saturno"}
print(planetas_a | planetas_b) # Union {'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno'}
print(planetas_a & planetas_b) # Interseccion {'Marte'}
print(planetas_a - planetas_b) # Diferencia {'Venus', 'Tierra'}
print(planetas_b - planetas_a) # Diferencia {'Jupiter', 'Saturno'}
print(planetas_a ^ planetas_b) # Diferencia simetrica {'Venus', 'Tierra', 'Jupiter', 'Saturno'}
print(planetas_a <= planetas_b) # Subconjunto False
print(planetas_a >= planetas_b) # Superconjunto False
print(planetas_a.isdisjoint(planetas_b)) # Disjuntos False
print(planetas_a.issubset(planetas_b)) # Subconjunto False
print(planetas_a.issuperset(planetas_b)) # Superconjunto False
print(planetas_a.union(planetas_b)) # Union {'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno'}
print(planetas_a.intersection(planetas_b)) # Interseccion {'Marte'}
print(planetas_a.difference(planetas_b)) # Diferencia {'Venus', 'Tierra'}
print(planetas_a.symmetric_difference(planetas_b)) # Diferencia simetrica {'Venus', 'Tierra', 'Jupiter', 'Saturno'}


#Eliminar un set
del planetas_a
# print(planetas_a) # Arroja error porque el set fue eliminado