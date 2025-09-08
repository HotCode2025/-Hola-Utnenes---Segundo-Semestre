#SOLICITAMOS DATOS AL USUARIO

pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el impuesto: "))

#CALCULAMOS EL IMPUESTO

pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

print(f"El pago con impuesto es: {pago_total}")