/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/

package Ciclos04;

public class Ciclos04 {

}
//Clase scanner
package Ciclos04;
import java.util.Scanner;
public class Ejercicio04Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        int contador = 0;

        System.out.print("Digite un número: ");
        numero = entrada.nextInt();

        while(numero >= 0){
            contador++;
            System.out.print("Digite otro número: ");
            numero = entrada.nextInt();
        }
        System.out.println("Se han introducido " + contador + " números positivos.");
        entrada.close();
    }
}
//_------------------------------------------------------------
package Ciclos04;
import javax.swing.JOptionPane;
public class Ejercicio04 {
    public static void main(String[] args) {
        int numero;
        int contador = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "Se han introducido " + contador + " números positivos.");
    }
}