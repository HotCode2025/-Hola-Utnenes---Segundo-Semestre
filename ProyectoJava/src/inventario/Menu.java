package inventario;

import javax.swing.JOptionPane;
import java.util.ArrayList;
import java.util.List;

/*
 * AUTORA: Florencia
 * PROPÓSITO: Menú con JOptionPane (Swing) que ejecuta las operaciones reales:
 * agregar, listar, buscar, modificar y eliminar productos usando el modelo unificado.
 */
public class Menu {

    // Estado en memoria (independiente del Scanner de consola)
    private static final List<Producto> productos = new ArrayList<>();
    private static final List<Categoria> categorias = new ArrayList<>();

    public static void main(String[] args) {
        // Semillas de categorías
        categorias.add(new Categoria(1, "Limpieza"));
        categorias.add(new Categoria(2, "Alimentos"));
        categorias.add(new Categoria(3, "Bebidas"));

        int opcion = 0;
        do {
            String texto = """
            ===== MENÚ =====
            1. Agregar producto
            2. Listar productos
            3. Buscar producto
            4. Modificar producto
            5. Eliminar producto
            0. Salir

            Elija una opción:""";

            String input = JOptionPane.showInputDialog(null, texto, "Menú", JOptionPane.QUESTION_MESSAGE);

            if (input == null) {
                JOptionPane.showMessageDialog(null, "Programa cerrado...");
                break;
            }

            try {
                opcion = Integer.parseInt(input.trim());
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Ingresar un número válido.");
                continue;
            }

            switch (opcion) {
                case 1 -> agregarProductoJop();
                case 2 -> listarProductosJop();
                case 3 -> buscarProductoJop();
                case 4 -> modificarProductoJop();
                case 5 -> eliminarProductoJop();
                case 0 -> JOptionPane.showMessageDialog(null, "Programa finalizado.");
                default -> JOptionPane.showMessageDialog(null, "Opción inválida.");
            }
        } while (opcion != 0);
    }

    // ====== Opción 1: Agregar ======
    private static void agregarProductoJop() {
        String codigo = leerNoVacio("Ingrese el CÓDIGO (único):");
        if (codigo == null) return;
        if (buscarPorCodigo(codigo) != null) {
            JOptionPane.showMessageDialog(null, " Ya existe un producto con ese código.");
            return;
        }

        String nombre = leerNoVacio("Ingrese el NOMBRE:");
        if (nombre == null) return;

        Double precio = leerDoubleNoNegativo("Ingrese el PRECIO (>= 0):");
        if (precio == null) return;

        Integer cantidad = leerEnteroNoNegativo("Ingrese la CANTIDAD (>= 0):");
        if (cantidad == null) return;

        Categoria cat = elegirCategoriaJop(); // puede ser null (= SIN CATEGORÍA)

        productos.add(new Producto(codigo, nombre, precio, cantidad, cat));
        JOptionPane.showMessageDialog(null, " Producto agregado.");
    }

    // ====== Opción 2: Listar ======
    private static void listarProductosJop() {
        JOptionPane.showMessageDialog(null, ListarProductos.construirTabla(productos));
    }

    // ====== Opción 3: Buscar ======
    private static void buscarProductoJop() {
        if (productos.isEmpty()) {
            JOptionPane.showMessageDialog(null, "No hay productos cargados.");
            return;
        }
        String[] opciones = {"Por CÓDIGO (exacto)", "Por NOMBRE (contiene)"};
        int sel = JOptionPane.showOptionDialog(
                null, "Elija tipo de búsqueda", "Buscar",
                JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE,
                null, opciones, opciones[0]
        );
        if (sel == 0) {
            String codigo = leerNoVacio("Ingrese CÓDIGO:");
            if (codigo == null) return;
            Producto p = buscarPorCodigo(codigo);
            JOptionPane.showMessageDialog(null, p == null ? "No encontrado." : p.toString());
        } else if (sel == 1) {
            String texto = leerNoVacio("Texto en NOMBRE:");
            if (texto == null) return;
            StringBuilder sb = new StringBuilder("Resultados:\n");
            int count = 0;
            for (Producto p : productos) {
                if (p.getNombre().toLowerCase().contains(texto.toLowerCase())) {
                    sb.append(p).append('\n');
                    count++;
                }
            }
            JOptionPane.showMessageDialog(null, count == 0 ? "Sin resultados." : sb.toString());
        }
    }

    // ====== Opción 4: Modificar ======
    private static void modificarProductoJop() {
        if (productos.isEmpty()) {
            JOptionPane.showMessageDialog(null, "No hay productos cargados.");
            return;
        }
        String codigo = leerNoVacio("Ingrese CÓDIGO a modificar:");
        if (codigo == null) return;

        Producto p = buscarPorCodigo(codigo);
        if (p == null) {
            JOptionPane.showMessageDialog(null, " No se encontró un producto con ese código.");
            return;
        }

        String[] ops = {"Precio", "Cantidad", "Categoría"};
        int sel = JOptionPane.showOptionDialog(
                null, "¿Qué desea modificar?\n" + p,
                "Modificar",
                JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE,
                null, ops, ops[0]
        );
        if (sel == 0) {
            Double nuevo = leerDoubleNoNegativo("Nuevo PRECIO (>= 0):");
            if (nuevo == null) return;
            p.setPrecio(nuevo);
        } else if (sel == 1) {
            Integer nuevo = leerEnteroNoNegativo("Nueva CANTIDAD (>= 0):");
            if (nuevo == null) return;
            p.setCantidad(nuevo);
        } else if (sel == 2) {
            p.setCategoria(elegirCategoriaJop()); // puede ser null
        }
        JOptionPane.showMessageDialog(null, "Producto modificado:\n" + p);
    }

    // ====== Opción 5: Eliminar ======
    private static void eliminarProductoJop() {
        if (productos.isEmpty()) {
            JOptionPane.showMessageDialog(null, "No hay productos cargados.");
            return;
        }
        String codigo = leerNoVacio("Ingrese CÓDIGO a eliminar:");
        if (codigo == null) return;

        Producto p = buscarPorCodigo(codigo);
        if (p == null) {
            JOptionPane.showMessageDialog(null, "No se encontró un producto con ese código.");
            return;
        }
        int conf = JOptionPane.showConfirmDialog(null, "¿Eliminar?\n" + p, "Confirmar", JOptionPane.YES_NO_OPTION);
        if (conf == JOptionPane.YES_OPTION) {
            productos.remove(p);
            JOptionPane.showMessageDialog(null, "Producto eliminado.");
        }
    }

    // ====== Helpers ======
    private static Producto buscarPorCodigo(String codigo) {
        if (codigo == null) return null;
        for (Producto p : productos) {
            if (p.getCodigo().equalsIgnoreCase(codigo.trim())) return p;
        }
        return null;
    }

    private static String leerNoVacio(String prompt) {
        while (true) {
            String s = JOptionPane.showInputDialog(null, prompt);
            if (s == null) return null; // cancelado
            s = s.trim();
            if (!s.isEmpty()) return s;
            JOptionPane.showMessageDialog(null, "El valor no puede estar vacío.");
        }
    }

    private static Double leerDoubleNoNegativo(String prompt) {
        while (true) {
            String s = JOptionPane.showInputDialog(null, prompt);
            if (s == null) return null;
            try {
                double v = Double.parseDouble(s.trim());
                if (v < 0) JOptionPane.showMessageDialog(null, "Debe ser >= 0.");
                else return v;
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Ingrese un número válido (use punto decimal).");
            }
        }
    }

    private static Integer leerEnteroNoNegativo(String prompt) {
        while (true) {
            String s = JOptionPane.showInputDialog(null, prompt);
            if (s == null) return null;
            try {
                int v = Integer.parseInt(s.trim());
                if (v < 0) JOptionPane.showMessageDialog(null, "Debe ser >= 0.");
                else return v;
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Ingrese un entero válido.");
            }
        }
    }

    private static Categoria elegirCategoriaJop() {
        if (categorias.isEmpty()) {
            JOptionPane.showMessageDialog(null, "No hay categorías. Se guardará SIN CATEGORÍA.");
            return null;
        }
        StringBuilder sb = new StringBuilder("Categorías disponibles:\n");
        for (Categoria c : categorias) sb.append("  ").append(c).append('\n');
        sb.append("\nIngrese ID (0 = SIN CATEGORÍA):");

        Integer id = leerEnteroNoNegativo(sb.toString());
        if (id == null) return null;        // cancelado
        if (id == 0) return null;           // sin categoría

        for (Categoria c : categorias) {
            if (c.getId() == id) return c;
        }
        JOptionPane.showMessageDialog(null, "ID no encontrado. Se guardará SIN CATEGORÍA.");
        return null;
    }
}
