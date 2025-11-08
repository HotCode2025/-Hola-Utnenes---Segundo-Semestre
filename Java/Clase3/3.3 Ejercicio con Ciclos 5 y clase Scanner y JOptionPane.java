/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello generar un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
*/

package Ciclos05;

public class Ciclos05 {
    
}
//Clase scanner
package Ciclos05;
import java.util.Scanner;
public class Ejercicio05Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeroAleatorio = (int)(Math.random() * 101);
        int numeroUsuario;
        int intentos = 0;

        System.out.print("Adivina el número (entre 0 y 100): ");
        numeroUsuario = entrada.nextInt();
        intentos++;

        while(numeroUsuario != numeroAleatorio){
            if(numeroUsuario < numeroAleatorio){
                System.out.println("Es mayor");
            }
            else{
                System.out.println("Es menor");
            }
            System.out.print("Intenta de nuevo: ");
            numeroUsuario = entrada.nextInt();
            intentos++;
        }
        System.out.println("¡Felicidades! Adivinaste el número " + numeroAleatorio + " en " + intentos + " intentos.");
        entrada.close();
    }
}
//_------------------------------------------------------------
package Ciclos05;
import javax.swing.JOptionPane;
public class Ejercicio05 {
    public static void main(String[] args) {
        int numeroAleatorio = (int)(Math.random() * 101);
        int numeroUsuario;
        int intentos = 0;

        numeroUsuario = Integer.parseInt(JOptionPane.showInputDialog("Adivina el número (entre 0 y 100): "));
        intentos++;

        while(numeroUsuario != numeroAleatorio){
            if(numeroUsuario < numeroAleatorio){
                JOptionPane.showMessageDialog(null, "Es mayor");
            }
            else{
                JOptionPane.showMessageDialog(null, "Es menor");
            }
            numeroUsuario = Integer.parseInt(JOptionPane.showInputDialog("Intenta de nuevo: "));
            intentos++;
        }
        JOptionPane.showMessageDialog(null, "¡Felicidades! Adivinaste el número " + numeroAleatorio + " en " + intentos + " intentos.");
    }
}
