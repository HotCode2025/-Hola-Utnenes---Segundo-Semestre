/*
Ejercicio3: JOption*/

import javax.swing.JOptionPane;

public class Ejercicio3JOptionPane {
    public static void main(String[] args) {
        
        int numero;
        
        do{
           String entrada = JOptionPane.showInputDialog("Ingresar un numero: ");
           numero = Integer.parseInt(entrada);
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

    

