/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo, y mostrar cuantos numeros 
se han introducido.
Lo hacemos primero con la clase Scanner
*/
import java.util.Scanner;

public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        int contador = 0;
       
        do{ 
        System.out.println("Digite un numero o un negativo para finalizar): ");
        numero = entrada.nextInt();
        contador++;
            System.out.println("Se han introducido: " +contador+ " numeros");
        }while(numero > 0);
   
        

    }

