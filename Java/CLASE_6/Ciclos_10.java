

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos_10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0;
        int contador = 0;

        while (contador < 10) {
            System.out.print("Introduce el número " + (contador + 1) + " (entre el 5 y el 15): ");
            int numero = entrada.nextInt();

            if (numero >= 5 && numero <= 15) {
                suma += numero;
                contador++;
            } else {
                System.out.println("Número fuera de rango, intente de nuevamente");
            }
        }

        JOptionPane.showMessageDialog(null, "La suma total de estos números es: " + suma);
    }
}