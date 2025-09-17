# Ejercicio de matematicas
# Para sacar la raíz cuadrada de un número positivo

import math

numero = int(input('Digite un número positivo: '))

while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))

print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')
