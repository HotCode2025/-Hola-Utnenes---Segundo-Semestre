// Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta.
// Suponiendo que todos los meses son de 30 dias
package Clase5;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Elegir opcion 1 para Scanner y opcion 2 paraJOptionPane: ");
        var opcion = entrada.nextInt();
        if (opcion == 1) {
            System.out.println("Porfavor ingresar un dia ( del 1 al 30)");
            var dia = entrada.nextInt();
            System.out.println("Porfavor ingresar un mes ( del 1 al 12)");
            var mes = entrada.nextInt();
            System.out.println("Porfavor ingresar un año (ingresar numero positivo)");
            var anio = entrada.nextInt();
            if ((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (anio > 0)) {
                System.out.println(String.format("La fecha ingresada es: %d/%d/%d", dia, mes, anio));
            } else {
                System.out.println("Akgun dato ingresado es invalido");
            }
            entrada.close();
        } else if (opcion == 2) {
            System.out.println("Has elegido la opcion 2 : JOptionPane");
            String input = JOptionPane.showInputDialog("Porfavor ingresar un dia ( del 1 al 30)");
            var dia= Integer.parseInt(input);
            String input2 = JOptionPane.showInputDialog("Porfavor ingresar un mes ( del 1 al 12)");
            var mes= Integer.parseInt(input2);
            String input3 = JOptionPane.showInputDialog("Porfavor ingresar un año (ingresar numero positivo)");
            var anio= Integer.parseInt(input3);
            if ((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (anio > 0)) {
                System.out.println(String.format("La fecha ingresada es: %d/%d/%d", dia, mes, anio));
            } else {
                System.out.println("Akgun dato ingresado es invalido");
            }
        } else {
            System.out.println("Opcion invalida");
        }
    }
}
