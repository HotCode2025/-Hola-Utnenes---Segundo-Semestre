#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius
#a fahrenheit y viseversa.
#Investigar las formulas

# Función que convierte de Celsius a Fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32  # precedencia: multiplicación, división y suma

# Función que convierte de Fahrenheit a Celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # respetar la precedencia usando paréntesis

# Pedir valores al usuario
celsius = float(input('Digite el valor en Celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} °C a °F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor en Fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} °F a °C -> {resultado:.2f}')
