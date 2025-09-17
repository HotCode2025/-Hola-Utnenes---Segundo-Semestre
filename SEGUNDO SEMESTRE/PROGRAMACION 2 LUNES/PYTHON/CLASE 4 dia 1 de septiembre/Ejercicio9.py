# Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, y se le
# devolverá la misma frase pero sin espacios en blanco, y además
# un contador de cuántos caracteres tiene la frase (sin contar los espacios).

# Ejemplo: frase = "vivir por siempre en paz"
# Resultado: "vivirporsiempreenpaz"
# Nº de caracteres = 21

frase1 = input("Digite una frase: ")
frase2 = ""

for i in frase1:
    if i != " ":
        frase2 += i

print(f"\nFrase final: {frase2}")
print(f"Nº de caracteres: {len(frase2)}")
