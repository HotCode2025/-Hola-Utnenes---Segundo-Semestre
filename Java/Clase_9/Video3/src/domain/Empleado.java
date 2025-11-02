package domain;

public class Empleado extends Persona {

    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados; // Para incrementar IDs automáticamente

    // Constructor
    public Empleado(String nombre, double sueldo) {
        super(nombre); // Llama al constructor de Persona que recibe 'nombre'
        this.idEmpleado = ++Empleado.contadorEmpleados;
        this.sueldo = sueldo;
    }

    // Getters y Setters
    public int getIdEmpleado() {
        return idEmpleado;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    // Método toString sobrescrito
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString()); // Llama al toString() de Persona
        sb.append('}');
        return sb.toString();
    }
}
