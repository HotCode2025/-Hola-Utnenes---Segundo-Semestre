/*
Clase anterior para poder ejecutar codigo de esta clase
 */


public class PruebaAritmetica {

    public static void main(String[] args) {
        var a = 10; // variable local (memoria stack)
        int b = 7;  // variable local (memoria stack)

        miMetodo(); // Llamamos al método estático

        // Creación de un objeto usando el constructor vacío
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros(); // Llamada a método sin retorno

        // Uso de método con retorno
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        // Uso de método con argumentos
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando Argumentos = " + resultado);

        // Mostrar valores del primer objeto
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        // Creación de otro objeto con constructor con argumentos
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 a: " + aritmetica2.a);
        System.out.println("aritmetica2 b: " + aritmetica2.b);
        
        Persona persona = new Persona("Florencia", "Martini");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }

    // Método estático adicional
    public static void miMetodo() {
        System.out.println("Aquí hay otro método");
    }
}
/*
Esto si perteneces a la 6b
Donde creamos una clase dentro de otra (Una clase llamada persona
dentro de la clase de PruebaAritmetica.
*/

class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ //Constructor
        super(); //Llamada al constructor de la clase Padre object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para reservar memoria
    }
public void imprimir(Persona persona){
    System.out.println("Persona desde la clase imprimir: "+persona);
    System.out.println("Impresión del objeto actual (this). "+this);
    }
}
        