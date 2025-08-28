/*Ejercicio 5: Realizar un juego para adivinar un número al azar entre 0 y 100.
Luego ir pidiendo numeros indicando "es mayor o es menor" segu sea mayo o menor 
el número a adivinar. El proceso termina cuando se acierta el número y mostramos
el numero de intentos que ha llevado a acertar.
*/


import java.util.Random;
import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Random azar = new Random();
        int numero = azar.nextInt(101);
        int ingreso;
        int i = 0;
        System.out.println(numero);
        do {
            System.out.println("Digite un numero entre el 0 y el 100: ");
            ingreso = entrada.nextInt();
            i++;
            if(ingreso < numero){
                System.out.println("Es mayor vuelva a ingresar otro numero");
            }else if(ingreso > numero){
                System.out.println("Es menor vuelva a ingresar otro numero");
            }else{
                System.out.println("Felicitaciones!Adivinaste el numero: "+numero+ " en: "+i+ " intentos");
                break;
            }
        }while(ingreso != numero);
    }
   
}
