import java.util.Scanner;

public class Ciclos_12 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese un número para calcular su factorial: ");
        int numScanner = sc.nextInt();
        System.out.println("El factorial de " + numScanner + " es: " + calcularFactorial(numScanner));
        
    }

    // Método para calcular el factorial
    public static long calcularFactorial(int n) {
        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        return factorial;
    }
}