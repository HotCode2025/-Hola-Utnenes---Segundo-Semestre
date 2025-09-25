/* 
Desarrollar un programa que muestre el producto de los primeros 
10 numeros impares
 */
package ejercicio11;

import javax.swing.JOptionPane;

public class Ejercicio11{
     public static void main(String[] args) {
        String respuesta = (JOptionPane.showInputDialog("Le gustaria ver el producto de los primeros 10 impares?(SI O NO)")).toUpperCase();
        System.out.println(respuesta);
        if (respuesta.equals("SI")) {
            int num = 1;
            long res = 1;
            int i = 0;
            while(i < 10){
                res *= num;
                num += 2;
                i++;
            };
            System.out.println("El resultado es : " + res);
        }else{
            System.out.println("Decidiste ingresar no");
        }
        }
}