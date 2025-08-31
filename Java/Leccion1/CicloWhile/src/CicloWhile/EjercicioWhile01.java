
package CicloWhile;

import java.util.Scanner;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo < 3){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en 1 la variable
        }
    
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador <= 7);
        //Uso de las palabras break y continue junto a las etiquetas(Labels)
        inicio:
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 == 0){
                System.out.println("contando = " + contando);
                break inicio;
        }
       }
        for(var contando = 0; contando < 7; contando++ ){
            if(contando % 2 != 0){
                continue;
            }
            System.out.println("contando = " + contando);
        }
    }
}


