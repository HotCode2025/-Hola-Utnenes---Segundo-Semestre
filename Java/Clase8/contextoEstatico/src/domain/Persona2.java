package domain;

import domain.Persona2;

public class Persona2 {
    private int idPersona;
    private static int contadorPersona;
    private String nombre;

    // Constructor
    public Persona2(String nombre){
        this.nombre = nombre;
        // Incrementar el contador por cada objeto nuevo
        Persona2.contadorPersona++; // No utilizar this, debe referencierase
        // a traves de la clase, porque es estatico
        this.idPersona = Persona2.contadorPersona;
    }

    // Getters y setters (encapsulados)
    // idPersona: solo getter (no se debe modificar externamente)
    public int getIdPersona() {
        return this.idPersona;
    }

    // nombre: getter y setter
    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    @Override
    public String toString() {
        return "Persona { idPersona=" + idPersona + ", nombre='" + nombre + "', contadorPersona=" + contadorPersona + " }";
    }

}
