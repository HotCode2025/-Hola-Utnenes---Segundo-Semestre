package Clase4;
/* Ejercicio 6 : Pedir numeros hasta que se teclee un 0, mostrar la suma de los numeros introducidos
 con Scanner y JOptionPane
 */

import java.util.Scanner;

import javax.swing.JOptionPane;

public class ciclos06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Elegir opcion 1 para Scanner y opcion 2 paraJOptionPane: ");
        var opcion = entrada.nextInt();
        if (opcion == 1) {
            System.out.println("Has elegido la opcion 1 : Scanner");
            // Se crea la variale donde se guardara la opcion del usuario
            int numScanner;
            // Se crea variable donde se sumaran los numeros
            var sum = 0;
            do {
                System.out.println("Porfavor ingresar numeros a sumar o 0 para salir");
                numScanner = entrada.nextInt();
                sum += numScanner;
                System.out.println("El numero ingresado es : " + numScanner);
                System.out.println("La suma es: " + sum);
                // Condicion de salida
            } while (numScanner != 0);
            entrada.close();
        } else if (opcion == 2) {
            System.out.println("Has elegido la opcion 2 : JOptionPane");
            int numScanner2;
            var sum2 = 0;
            do {
                // Se solicita iopcion, pero este se guarda como String
                String input = JOptionPane.showInputDialog("Ingrese un número:");
                // Convierto el string en numero
                numScanner2 = Integer.parseInt(input);
                sum2 += numScanner2;
                System.out.println("El numero ingresado es : " + numScanner2);
                System.out.println("La suma es: " + sum2);
            } while (numScanner2 != 0);
        } else {
            System.out.println("Opcion invalida");
        }
        
    }
}
