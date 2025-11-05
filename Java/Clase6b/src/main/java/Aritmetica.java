/*
Copio una parte de la clase anterior para poder ejecutar correctamente el código
ya que sobre la misma se agregan otras funciones y nueva clase.
 */

public class Aritmetica {

    // Atributos de la clase
    int a;
    int b;

    // Constructor vacío
    public Aritmetica() {
        System.out.println("Ejecutando constructor vacío");
    }

    // Constructor con argumentos
    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Ejecutando constructor con argumentos");
    }

    // Método sin retorno ni argumentos
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado de sumar sin retorno = " + resultado);
    }

    // Método con retorno pero sin argumentos
    public int sumarConRetorno() {
        return a + b;
    }

    // Método con retorno y con argumentos
    public int sumarConArgumentos(int a, int b) {
        return a + b;
    }
}

