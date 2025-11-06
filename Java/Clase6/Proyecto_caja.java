
import java.util.Scanner;


public class Proyecto_caja {
    int ancho;
    int alto;
    int profundidad;

    public Proyecto_caja(int ancho, int alto, int profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }

    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el ancho: ");
        int ancho = sc.nextInt();
        System.out.print("Ingrese el alto: ");
        int alto = sc.nextInt();
        System.out.print("Ingrese la profundidad: ");
        int profundidad = sc.nextInt();
        Proyecto_caja caja = new Proyecto_caja(ancho, alto, profundidad);
        int volumen = caja.calcularVolumen();
        System.out.println("El volumen de la caja es: " + volumen);
        sc.close();
    }

}