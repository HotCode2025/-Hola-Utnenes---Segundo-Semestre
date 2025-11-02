package domain;

public class Persona {
    // Atributos
    private String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;

    // Constructores
    public Persona() { }

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    // Getters / Setters
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public char getGenero() { return genero; }
    public void setGenero(char genero) { this.genero = genero; }

    public int getEdad() { return edad; }
    public void setEdad(int edad) { this.edad = edad; }

    public String getDireccion() { return direccion; }
    public void setDireccion(String direccion) { this.direccion = direccion; }

    // toString (generado con StringBuilder en el video 6)
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append('}');
        return sb.toString();
    }
}
