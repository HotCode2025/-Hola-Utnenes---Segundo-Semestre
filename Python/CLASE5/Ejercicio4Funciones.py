# Ejercicio 4: Calculadora de Impuestos
# Crear una función para calcular el total de un pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

def calcular_pago_total(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto / 100)
    return pago_total

# Solicitar datos al usuario
pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto (%): "))

# Calcular y mostrar el resultado
pago_con_impuesto = calcular_pago_total(pago_sin_impuesto, impuesto)
print(f"Pago con impuesto: {pago_con_impuesto:.2f}")