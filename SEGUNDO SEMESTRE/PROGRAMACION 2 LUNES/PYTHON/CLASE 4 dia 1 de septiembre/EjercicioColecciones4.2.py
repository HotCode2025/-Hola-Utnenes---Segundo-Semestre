#dos listas de palabras
lista1 = ["perro", "gato", "ratón", "loro"]
lista2 = ["gato", "caballo", "perro", "conejo"]

#convertimos
set1 = set(lista1)
set2 = set(lista2)

#palabras que aparecen en las listas
union = list(set1 | set2)
print("1. Palabras que aparecen en las listas:", union)

#palabras que están en la primera lista pero no en la segunda
solo_primera = list(set1 - set2)
print("2. Solo en la primera lista:", solo_primera)

#palabras que están en la segunda lista pero no en la primera
solo_segunda = list(set2 - set1)
print("3. Solo en la segunda lista:", solo_segunda)

#palabras que aparecen en ambas listas
en_ambas = list(set1 & set2)
print("4. En ambas listas:", en_ambas)
