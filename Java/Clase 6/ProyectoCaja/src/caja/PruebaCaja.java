package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        // Usando constructor vacío
        Caja caja1 = new Caja();
        caja1.ancho = 3;
        caja1.alto = 2;
        caja1.profundidad = 6;
        System.out.println("Volumen caja1 = " + caja1.calcularVolumen());

        // Usando constructor con argumentos
        Caja caja2 = new Caja(4, 2, 5);
        System.out.println("Volumen caja2 = " + caja2.calcularVolumen());
    }
}
