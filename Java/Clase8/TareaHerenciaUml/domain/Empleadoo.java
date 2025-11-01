package Clase8.TareaHerenciaUml.domain;


public class Empleadoo extends Personaa {
    private int idEmpleado;
    private double sueldo;

    public Empleadoo(String nombre, char genero, int edad, String direccion, int idEmpleado, double sueldo) {
        super(nombre, genero, edad, direccion);
        this.idEmpleado = idEmpleado;
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
}

