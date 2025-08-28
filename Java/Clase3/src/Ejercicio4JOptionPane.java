/*Ejercicio 4 con JOption
*/


import javax.swing.JOptionPane;

public class Ejercicio4JOptionPane {
    public static void main(String[] args) {
        int numero;
        int contador = 0;
       
        do{
        String entrada = JOptionPane.showInputDialog("Ingresar un numero o uno negativo para finalizar): ");
        numero = Integer.parseInt(entrada);
        contador++;
            System.out.println("Se han introducido: " +contador+ " numeros");
        }while(numero > 0);
   
        

    }

    }

