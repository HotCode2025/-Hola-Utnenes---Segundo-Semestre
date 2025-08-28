/*
Ejercicio 3: Leer numeros hasta que se introduzca un cero 
Para cada uno indicar si es par o impar.
*/
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        do{System.out.println("Introduzca un numero: ");
        numero = entrada.nextInt();
           if(numero == 0){
               break;
           }else if(numero % 2 != 0){
             
               System.out.println("El numero "+numero+ " es impar.");
           }else {
               System.out.println("El numero "+numero+ " es par.");
           }
        }while(numero != 0);
        
    }
    
}
