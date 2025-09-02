# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10.

numero = int (input("Ingrese un número para ver su tabla de multiplicar: "))
tabla = [numero * i for i in range(1, 11)]
print(f"Tabla de multiplicar del {numero}: {tabla}")
