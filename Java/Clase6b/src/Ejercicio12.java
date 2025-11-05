/*
Ejercicio 12: Pedir un número y calcular su factorial
Hacerlo con las dos clases, Scanner y JOptionPane
 */
 import java.util.Scanner;

public class Ejercicio12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese un número: ");
        int numero = entrada.nextInt();
        
        long factorial = 1;
        
        for (int i = 1; i <= numero; i++){
            factorial *= i;
        }
       
        System.out.println("El factorial de "+numero+ "es: " + factorial);
    }
}
