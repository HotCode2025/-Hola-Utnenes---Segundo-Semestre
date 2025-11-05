# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a Fahrenheit y viseversa.
# Investigar las formulas

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplos de uso
print("Conversiones de temperatura:")
print(f"20°C a Fahrenheit: {celsius_a_fahrenheit(20):.2f}°F")
print(f"68°F a Celsius: {fahrenheit_a_celsius(68):.2f}°C")
print(f"0°C a Fahrenheit: {celsius_a_fahrenheit(0):.2f}°F")
print(f"100°C a Fahrenheit: {celsius_a_fahrenheit(100):.2f}°F")
print(f"32°F a Celsius: {fahrenheit_a_celsius(32):.2f}°C")