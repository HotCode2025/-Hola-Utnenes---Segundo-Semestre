import java.util.Scanner;

public class Ejercicio_ciclos_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long producto = 1;

        System.out.println("calculando el producto de los primeros 10 números impares:");

        for (int i = 1, contador = 0; contador < 10; i += 2, contador++) {
            producto *= i;
            System.out.println("impar #" + (contador + 1) + ": " + i);
        }

        System.out.println("resultado final: " + producto);
    }
}