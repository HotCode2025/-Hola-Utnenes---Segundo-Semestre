/*
Ejercicio 10: Pedir 10 numeros y escribir la suma total
Hacerlo con la clase scanner y JOptionPane
*/
package ejercicio10;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ejercicio10 {

    
    public static void main(String[] args) {
       
        Scanner entrada = new Scanner(System.in);
        
        
        System.out.println("Elige el metodo de entrada: ");
        System.out.println("1: Usar Scanner.");
        System.out.println("2. Usar JOptionPane.");
        int opcion = entrada.nextInt();
        int suma = 0;
        if (opcion == 1) {
            
            for (int i = 1; i <= 10; i++) {
                System.out.print("Digite un numero: ");
                int numero = entrada.nextInt();
                suma += numero;
            }
            System.out.println("La suma total es: " + suma);

        } else if (opcion == 2) {
            
            for (int i = 1; i <= 10; i++) {
                int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
                suma += numero;
            }
            JOptionPane.showMessageDialog(null, "La suma total es: " + suma);

        } else {
            System.out.println("Elija una opcion valida.");
        }
    }
    
}
