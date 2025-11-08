package inventario;

import java.util.Objects;

/*
 * AUTOR: Matías
 * PROPÓSITO: Modelo de producto con código único, nombre, precio, cantidad y categoría (opcional).
 * Notas: valida que código/nombre no estén vacíos y que precio/cantidad no sean negativos.
 */
public class Producto {
    private String codigo;        // clave única (no vacío)
    private String nombre;        // no vacío
    private double precio;        // >= 0
    private int cantidad;         // >= 0
    private Categoria categoria;  // puede ser null

    public Producto(String codigo, String nombre, double precio, int cantidad, Categoria categoria) {
        setCodigo(codigo);
        setNombre(nombre);
        setPrecio(precio);
        setCantidad(cantidad);
        setCategoria(categoria);
    }

    public Producto(String codigo, String nombre, double precio, int cantidad) {
        this(codigo, nombre, precio, cantidad, null);
    }

    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public int getCantidad() { return cantidad; }
    public Categoria getCategoria() { return categoria; }

    public void setCodigo(String codigo) {
        if (codigo == null || codigo.trim().isEmpty()) {
            throw new IllegalArgumentException("El código no puede estar vacío.");
        }
        this.codigo = codigo.trim();
    }

    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre no puede estar vacío.");
        }
        this.nombre = nombre.trim();
    }

    public void setPrecio(double precio) {
        if (precio < 0) {
            throw new IllegalArgumentException("El precio no puede ser negativo.");
        }
        this.precio = precio;
    }

    public void setCantidad(int cantidad) {
        if (cantidad < 0) {
            throw new IllegalArgumentException("La cantidad no puede ser negativa.");
        }
        this.cantidad = cantidad;
    }

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria; // puede ser null
    }

    public double getValorTotal() {
        return precio * cantidad;
    }

    @Override
    public String toString() {
        String cat = (categoria == null) ? "SIN_CATEGORÍA" : categoria.getNombre();
        return String.format(
            "Producto{codigo='%s', nombre='%s', precio=%.2f, cantidad=%d, categoria=%s}",
            codigo, nombre, precio, cantidad, cat
        );
    }

    // Igualdad y hash por "codigo" (clave de negocio)
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Producto)) return false;
        Producto producto = (Producto) o;
        return codigo.equalsIgnoreCase(producto.codigo);
    }

    @Override
    public int hashCode() {
        return Objects.hash(codigo.toLowerCase());
    }
}
