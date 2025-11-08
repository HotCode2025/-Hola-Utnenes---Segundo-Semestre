/*
Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
*/

//Clase scanner

package Ciclos03;
import java.util.Scanner;
public class Ejercicio03Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;

        System.out.print("Digite un número: ");
        numero = entrada.nextInt();

        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El número ingresado " + numero + " es PAR");
            }
            else{
                System.out.println("El número ingresado " + numero + " es IMPAR");
            }
            System.out.print("Digite otro número: ");
            numero = entrada.nextInt();
        }
        System.out.println("El número ingresado es " + numero + " finaliza el programa");
        entrada.close();
    }
}

//_------------------------------------------------------------

package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado " + numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número ingresado es " + numero + " finaliza el programa");
    }
}
