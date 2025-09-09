# Ejercicio 5: Convertidor de temperaturas

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("--- Convertidor de Temperaturas ---")
    print("1) Celsius a Fahrenheit")
    print("2) Fahrenheit a Celsius")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        c = float(input("Ingresá la temperatura en °C: "))
        f = celsius_a_fahrenheit(c)
        print(f"{c:.2f} °C equivalen a {f:.2f} °F")
    elif opcion == "2":
        f = float(input("Ingresá la temperatura en °F: "))
        c = fahrenheit_a_celsius(f)
        print(f"{f:.2f} °F equivalen a {c:.2f} °C")
    else:
        print("⚠️ Opción inválida")