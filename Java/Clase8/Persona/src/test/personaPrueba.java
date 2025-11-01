package test;

import dominio.Persona;

public class personaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Otar",57000, false);
        System.out.println("Nombre es: "+ persona1.getNombre());     
        // Modificamos a traves de los metodos

        persona1.setNombre("Alberto");
        System.out.println("Nombre modificado es: "+ persona1.getNombre());
        System.out.println("El sueldo es: "+ persona1.getSueldo());
        System.out.println("Eliminado? : "+ persona1.isEliminado());
        
        // Tarea : Crear otro objeto de tipo Persona, asignar valores aleatorios y
        // luego imprimir , modificar sus valores y volver a imprimir

        Persona persona2 = new Persona("María", 45000, true);

        System.out.println(persona2.toString());

        // Modificamos valores de persona2

        persona2.setNombre("Mariana");
        persona2.setSueldo(48000);
        persona2.setEliminado(false);

        // Volvemos a imprimir para verificar los cambios
        
        System.out.println(persona2); // Accede sautomaticamente al toString, por mas que no lo ponga
    }
}
