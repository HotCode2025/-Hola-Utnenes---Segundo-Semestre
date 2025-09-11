//Pedir un numero N, y mostrar todos los numeros de 1 a N

package Clase5;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio8 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Elegir opcion 1 para Scanner y opcion 2 paraJOptionPane: ");
        var opcion = entrada.nextInt();
        if (opcion == 1) {
            System.out.println("Porfavor ingresar la cantidad de numeros a mostrar");
            var num = entrada.nextInt();
            for (int i = 1; i <= num; i++) { 
                System.out.println("Los numeros a mostrar son: " + i);
            }
            entrada.close();
        } else if (opcion == 2) {
            System.out.println("Has elegido la opcion 2 : JOptionPane");
            String input = JOptionPane.showInputDialog("Porfavor ingresar la cantidad de numeros a mostrar");
            var num= Integer.parseInt(input);
             for (int i = 1; i <= num; i++) { 
                System.out.println("Los numeros a mostrar son: " + i);
            }
        } else {
            System.out.println("Opcion invalida");
        }
    }
}
