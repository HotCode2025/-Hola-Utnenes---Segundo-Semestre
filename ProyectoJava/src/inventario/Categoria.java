package inventario;

/*
 * AUTOR: Amelia
 * PROPÓSITO: Crear categoria para cada producto del inventario
 * Uso: Recibe un string que lo asigna como categoria un producto creado.
 */

public class Categoria {
    private int id;
    private String nombre;

    public Categoria() {}

    public Categoria(int id, String nombre) {
        if (id < 0) throw new IllegalArgumentException("El id no puede ser negativo.");
        if (nombre == null || nombre.trim().isEmpty())
            throw new IllegalArgumentException("El nombre no puede estar vacío.");
        this.id = id;
        this.nombre = nombre.trim();
    }

    public int getId() { return id; }
    public String getNombre() { return nombre; }

    
    public void setId(int id) {
        if (id < 0) throw new IllegalArgumentException("El id no puede ser negativo.");
        this.id = id;
    }
    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty())
            throw new IllegalArgumentException("El nombre no puede estar vacío.");
        this.nombre = nombre.trim();
    }

    @Override public String toString() { return "[" + id + "] " + nombre; }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Categoria c = (Categoria) o;
        return id == c.id;
}

    @Override public int hashCode(){ return Integer.hashCode(id); }
}
