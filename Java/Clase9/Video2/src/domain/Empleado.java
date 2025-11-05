package domain;

public class Empleado extends Persona {

    // Por ahora no agrega atributos ni métodos nuevos, solo hereda de Persona

    // Constructor vacío (usa el de Persona)
    public Empleado() {
        // Llama implícitamente al constructor vacío de Persona
        super();
    }

    // Si quisieras agregar un constructor con parámetros más adelante:
    // public Empleado(String nombre, char genero, int edad, String direccion) {
    //     super(nombre, genero, edad, direccion);
    // }

}
