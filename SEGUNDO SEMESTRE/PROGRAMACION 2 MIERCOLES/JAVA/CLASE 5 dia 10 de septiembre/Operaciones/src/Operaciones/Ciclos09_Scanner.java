package Operaciones;

import java.util.Scanner;

public class Ciclos09_Scanner {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite el día: ");
        int dia = entrada.nextInt();

        System.out.print("Digite el mes: ");
        int mes = entrada.nextInt();

        System.out.print("Digite el año: ");
        int anio = entrada.nextInt();

        // Verificamos las condiciones con 'if'
        if ((anio != 0) && (mes >= 1 && mes <= 12) && (dia >= 1 && dia <= 30)) {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es correcta.");
        } else {
            System.out.println("La fecha es incorrecta.");
        }
    }
}
