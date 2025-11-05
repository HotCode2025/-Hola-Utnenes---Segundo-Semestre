package Operaciones;

//Ejercicio 8 con scanner

import java.util.Scanner; // Importante para poder leer desde la consola

public class Ciclos08_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;

        System.out.print("Digite un número: "); // Pide el número al usuario
        numero = entrada.nextInt();

        System.out.println("Mostrando los números del 1 al " + numero + ":");

        // El bucle 'for' se encargará de contar
        // Inicia en 1; se repite mientras i <= numero; aumenta i en 1 cada vez.
        for (int i = 1; i <= numero; i++) {
            System.out.println(i);
        }
    }
}
