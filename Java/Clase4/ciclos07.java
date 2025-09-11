package Clase4;
/*Ejericio 7 - Pedir numeros hasta que se introduzca uno negativo y mostrar la media 
Hacer con Scanner y JOptionPane
*/

import java.util.Scanner;

import javax.swing.JOptionPane;

public class ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Elegir opcion 1 para Scanner y opcion 2 paraJOptionPane: ");
        var opcion = entrada.nextInt();
        if (opcion == 1) {
            System.out.println("Has elegido la opcion 1 : Scanner");
            // Se crea la variale donde se guardara la opcion del usuario
            int numScanner;
            // Se crea variable donde se sumaran los numeros+
            int sum = 0;
            double media = 0;
            int cont = 0;
            do {
                System.out.println("Porfavor ingresar numeros, o un negativo para salir");
                numScanner = entrada.nextInt();
                // Se le pone ese IF para que no tome el numero negativo en la suma y el conteo
                if (numScanner >= 0) {
                    sum += numScanner;
                    cont++;
                    media = (double) sum / cont;
                    System.out.println("El numero ingresado es : " + numScanner);
                    System.out.println("La suma es: " + sum);
                    System.out.println("La cantidad de numeros ingresados es: " + cont);
                    System.out.println("La media es: " + media);
                }
            // 
            //Condicion de salida
            } while (numScanner >= 0);
            entrada.close();
        } else if (opcion == 2) {
            System.out.println("Has elegido la opcion 2 : JOptionPane");
            // Se crea la variale donde se guardara la opcion del usuario
            int numScanner;
            // Se crea variable donde se sumaran los numeros+
            int sum = 0;
            double media = 0;
            int cont = 0;
            do {
                String input = JOptionPane.showInputDialog("Porfavor ingresar numeros, o un negativo para salir");
                numScanner= Integer.parseInt(input);
                // Se le pone ese IF para que no tome el numero negativo en la suma y el conteo
                if (numScanner >= 0) {
                    sum += numScanner;
                    cont++;
                    media = (double) sum / cont;
                    System.out.println("El numero ingresado es : " + numScanner);
                    System.out.println("La suma es: " + sum);
                    System.out.println("La cantidad de numeros ingresados es: " + cont);
                    System.out.println("La media es: " + media);
                }
            // 
            //Condicion de salida
            } while (numScanner >= 0);
        } else {
            System.out.println("Opcion invalida");
        }
    }
}