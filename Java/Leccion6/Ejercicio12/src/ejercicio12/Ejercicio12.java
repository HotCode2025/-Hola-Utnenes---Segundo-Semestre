/*
 Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos clases, Scanner y joptionpane
 */
package ejercicio12;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio12 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Elige el metodo de entrada: ");
        System.out.println("1: Usar Scanner.");
        System.out.println("2. Usar JOptionPane.");
        int opcion = entrada.nextInt();
        int numero = 0;

        if (opcion == 1) {
            System.out.print("Digite un numero: ");
            numero = entrada.nextInt();
        } else if (opcion == 2) {       
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        } else {
            System.out.println("Opcion no valida.");
          
        }

    
        int factorial = 1;
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }

        
        if (opcion == 1) {
            System.out.println("El factorial de " + numero + " es: " + factorial);
        } else {
            JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
        }
        
    }
    
}
