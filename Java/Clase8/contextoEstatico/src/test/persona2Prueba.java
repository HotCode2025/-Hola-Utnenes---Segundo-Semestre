package test;

import domain.Persona2;

public class persona2Prueba {
    private int contador;
    public static void main(String[] args) {
        
        Persona2 persona1 = new Persona2("Ariel");
        System.out.println(" Nombre: " + persona1);

        Persona2 persona2 = new Persona2("Otar");
        System.out.println(" Nombre: " + persona2);

        Persona2 persona3 = new Persona2("Marco");
        System.out.println(" Nombre: " + persona3);
        
        imprimir(persona1); // Ejecuta el metodo de abajo, que debe ser static, sino da error
        imprimir(persona2); // Ejecuta el metodo de abajo, que debe ser static, sino da error
        imprimir(persona3); // Ejecuta el metodo de abajo, que debe ser static, sino da error

        // this.contador = contador; no puede referenciarse con this, porque esta en un contexto estatico

    // Creamos una instancia de esta misma clase para poder llamar a getContador()
    persona2Prueba personaP1 = new persona2Prueba();
    System.out.println("Contador desde personaP1: " + personaP1.getContador());

    }
    public static void imprimir(Persona2 persona){
        System.out.println("Persona: "+ persona);
    }

    public int getContador(){
        imprimir(new Persona2("Liliana"));
        return this.contador;
    }
}
