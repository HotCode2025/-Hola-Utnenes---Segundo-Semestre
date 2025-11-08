package inventario;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


/*
 * AUTORES: Integración de varias tareas
 *   - Fernando: agregarProducto()
 *   - Serena: búsquedas (por código y por nombre)
 *   - Fernanda: modificarProducto()
 *   - Emma: eliminarProducto()
 * PROPÓSITO: Gestiona la lista de productos/categorías y operaciones CRUD por consola (Scanner).
 * Notas: Tiene helpers para lectura robusta y selección de categoría por ID.
 */
public class Inventario {

    // Estado
    private final List<Producto> listaProductos;
    private final List<Categoria> listaCategorias;

    // Un único scanner para toda la clase (evita conflictos con nextLine)
    private final Scanner entrada = new Scanner(System.in);

    // --- Constructores ---
    public Inventario(List<Producto> listaProductos, List<Categoria> listaCategorias) {
        this.listaProductos = (listaProductos != null) ? listaProductos : new ArrayList<>();
        this.listaCategorias = (listaCategorias != null) ? listaCategorias : new ArrayList<>();
    }

    public Inventario() {
        this(new ArrayList<>(), new ArrayList<>());
    }

    // ===================== TAREA 3 — Agregar (Fernando) =====================
    public void agregarProducto() {
        System.out.println("\n=== AGREGAR NUEVO PRODUCTO ===");

        // Código único
        String codigo;
        do {
            System.out.print("Ingrese el CÓDIGO (único): ");
            codigo = entrada.nextLine().trim();
            if (codigo.isEmpty()) {
                System.out.println(" El código no puede estar vacío.");
            } else if (codigoYaExiste(codigo)) {
                System.out.println(" Ya existe un producto con ese código.");
                codigo = "";
            }
        } while (codigo.isEmpty());

        // Nombre
        String nombre;
        do {
            System.out.print("Ingrese el NOMBRE: ");
            nombre = entrada.nextLine().trim();
            if (nombre.isEmpty()) System.out.println("El nombre no puede estar vacío.");
        } while (nombre.isEmpty());

        // Precio y cantidad
        double precio = leerDoubleNoNegativo("Ingrese el PRECIO (>= 0): ");
        int cantidad = leerEnteroNoNegativo("Ingrese la CANTIDAD (>= 0): ");

        // Categoría (opcional)
        Categoria categoriaElegida = seleccionarCategoria();

        // Alta
        Producto nuevo = new Producto(codigo, nombre, precio, cantidad, categoriaElegida);
        listaProductos.add(nuevo);
        System.out.println("Producto agregado: " + nuevo);
    }

    // ===================== TAREA 5 — Buscar (Serena) =====================
    public Producto buscarProductoPorCodigo(String codigo) {
        if (codigo == null) return null;
        for (Producto p : listaProductos) {
            if (p.getCodigo().equalsIgnoreCase(codigo.trim())) {
                return p;
            }
        }
        return null;
    }

    public List<Producto> buscarProductosPorNombre(String texto) {
        List<Producto> res = new ArrayList<>();
        if (texto == null) return res;
        String q = texto.trim().toLowerCase();
        for (Producto p : listaProductos) {
            if (p.getNombre().toLowerCase().contains(q)) {
                res.add(p);
            }
        }
        return res;
    }

    // ===================== TAREA 6 — Modificar (Fernanda) =====================
    public void modificarProducto() {
        System.out.println("\n=== MODIFICAR PRODUCTO ===");

        if (listaProductos.isEmpty()) {
            System.out.println("No hay productos cargados.");
            return;
        }

        System.out.print("Ingrese el CÓDIGO del producto a modificar: ");
        String codigoBuscado = entrada.nextLine().trim();

        Producto productoAModificar = buscarProductoPorCodigo(codigoBuscado);
        if (productoAModificar == null) {
            System.out.println(" No existe producto con código '" + codigoBuscado + "'.");
            return;
        }

        System.out.println("Producto: " + productoAModificar);
        System.out.println("¿Qué desea modificar?");
        System.out.println("  1) Precio");
        System.out.println("  2) Cantidad");
        System.out.println("  3) Categoría");
        System.out.print("Opción: ");
        String option = entrada.nextLine().trim();

        switch (option) {
            case "1" -> {
                double nuevo = leerDoubleNoNegativo("Nuevo PRECIO (>= 0): ");
                productoAModificar.setPrecio(nuevo);
            }
            case "2" -> {
                int nuevo = leerEnteroNoNegativo("Nueva CANTIDAD (>= 0): ");
                productoAModificar.setCantidad(nuevo);
            }
            case "3" -> {
                Categoria nueva = seleccionarCategoria(); // null = SIN CATEGORÍA
                productoAModificar.setCategoria(nueva);
            }
            default -> {
                System.out.println("Opción inválida. No se realizaron cambios.");
                return;
            }
        }
        System.out.println("✅ Producto modificado: " + productoAModificar);
    }

    // ===================== TAREA 7 — Eliminar (Emma) =====================
    public void eliminarProducto() {
        System.out.println("\n=== ELIMINAR PRODUCTO ===");

        if (listaProductos.isEmpty()) {
            System.out.println("No hay productos cargados.");
            return;
        }

        System.out.print("Ingrese el CÓDIGO del producto a eliminar: ");
        String codigo = entrada.nextLine().trim();

        Producto p = buscarProductoPorCodigo(codigo);
        if (p == null) {
            System.out.println(" No se encontró un producto con ese código.");
            return;
        }

        System.out.println("Se eliminará: " + p);
        System.out.print("¿Confirmar? (s/n): ");
        String conf = entrada.nextLine().trim();
        if (conf.equalsIgnoreCase("s")) {
            listaProductos.remove(p);
            System.out.println("✅ Producto eliminado.");
        } else {
            System.out.println("Operación cancelada.");
        }
    }

    // ===================== Helpers =====================
    private boolean codigoYaExiste(String codigo) {
        return buscarProductoPorCodigo(codigo) != null;
    }

    private double leerDoubleNoNegativo(String prompt) {
        Double valor = null;
        while (valor == null || valor < 0) {
            System.out.print(prompt);
            if (entrada.hasNextDouble()) {
                valor = entrada.nextDouble();
                entrada.nextLine(); // limpiar salto
                if (valor < 0) System.out.println(" No puede ser negativo.");
            } else {
                System.out.println(" Ingrese un número válido (use punto decimal).");
                entrada.nextLine(); // descartar
            }
        }
        return valor;
    }

    private int leerEnteroNoNegativo(String prompt) {
        Integer valor = null;
        while (valor == null || valor < 0) {
            System.out.print(prompt);
            if (entrada.hasNextInt()) {
                valor = entrada.nextInt();
                entrada.nextLine(); // limpiar salto
                if (valor < 0) System.out.println("❌ No puede ser negativo.");
            } else {
                System.out.println(" Ingrese un entero válido.");
                entrada.nextLine(); // descartar
            }
        }
        return valor;
    }

    /**
     * Muestra categorías y permite elegir por ID (o 0 para SIN CATEGORÍA).
     * Retorna la categoría elegida o null.
     */
    private Categoria seleccionarCategoria() {
        if (listaCategorias.isEmpty()) {
            System.out.println("No hay categorías cargadas. El producto quedará SIN CATEGORÍA.");
            return null;
        }

        System.out.println("\nCategorías disponibles:");
        for (Categoria c : listaCategorias) {
            System.out.println("  " + c);
        }
        System.out.println("  [0] SIN CATEGORÍA");

        Integer idElegido = null;
        while (idElegido == null) {
            System.out.print("Ingrese ID de la categoría: ");
            if (entrada.hasNextInt()) {
                idElegido = entrada.nextInt();
                entrada.nextLine(); // limpiar
            } else {
                System.out.println("Ingrese un entero válido.");
                entrada.nextLine(); // descartar
            }
        }

        if (idElegido == 0) return null;

        for (Categoria c : listaCategorias) {
            if (c.getId() == idElegido) return c;
        }

        System.out.println("⚠️ ID no encontrado. Se guardará SIN CATEGORÍA.");
        return null;
    }

    // Getters para integración
    public List<Producto> getListaProductos() { return listaProductos; }
    public List<Categoria> getListaCategorias() { return listaCategorias; }
}
