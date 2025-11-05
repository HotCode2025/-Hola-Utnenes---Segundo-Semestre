/*
Ejercicio 12 pero con JOption Pane
 */

import javax.swing.JOptionPane;

public class Ejercicio12JOption {
    public static void main(String[] args) {
        int numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese un número: ")
        );
        
        long factorial = 1;
        
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        
        JOptionPane.showInternalMessageDialog(null, "El factorial de "+numero+ "es: "+ factorial);
                
    }
}
