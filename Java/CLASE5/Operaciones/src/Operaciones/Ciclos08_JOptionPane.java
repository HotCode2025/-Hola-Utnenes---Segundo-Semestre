package Operaciones;


import javax.swing.JOptionPane; // Importante para usar ventanas

public class Ciclos08_JOptionPane {
    public static void main(String[] args) {
        int numero;

        // Pedimos el número usando una ventana
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número:"));

        // Usamos un StringBuilder para construir el texto final de forma eficiente
        StringBuilder numerosMostrados = new StringBuilder();
        numerosMostrados.append("Números del 1 al ").append(numero).append(":\n");

        for (int i = 1; i <= numero; i++) {
            numerosMostrados.append(i).append("\n"); // Agrega cada número y un salto de línea
        }

        // Mostramos el resultado final en una sola ventana
        JOptionPane.showMessageDialog(null, numerosMostrados.toString());
    }
}