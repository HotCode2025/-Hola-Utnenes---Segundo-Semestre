# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada

def imprimir_descendente(n):
    if n <= 0:
        return
    print(n)
    imprimir_descendente(n - 1)

# Ejemplos de uso:
print("Números del 5 al 1:")
imprimir_descendente(5)

print("\nNúmeros del 3 al 1:")
imprimir_descendente(3)

print("\nNúmero negativo (no debe imprimir nada):")
imprimir_descendente(-2)