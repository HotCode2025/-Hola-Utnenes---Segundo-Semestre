package Operaciones;

import javax.swing.JOptionPane;

public class Ciclos09_JOptionPane {
    public static void main(String[] args) {
        int dia, mes, anio;

        dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día:"));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes:"));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año:"));

        if ((anio != 0) && (mes >= 1 && mes <= 12) && (dia >= 1 && dia <= 30)) {
            JOptionPane.showMessageDialog(null, "La fecha " + dia + "/" + mes + "/" + anio + " es CORRECTA.");
        } else {
            JOptionPane.showMessageDialog(null, "La fecha ingresada es INCORRECTA.");
        }
    }
}