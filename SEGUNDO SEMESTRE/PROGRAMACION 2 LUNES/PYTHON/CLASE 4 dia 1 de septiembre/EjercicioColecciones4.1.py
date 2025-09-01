lista = [1, 2, 2, 3, 4, 4, 5, 6, 1, 2, 2 ,4 ,4]

resultado = []
for elemento in lista:
    if elemento not in resultado:
        resultado.append(elemento)

print("Lista sin duplicados (orden original):", resultado)

