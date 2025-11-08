package inventario;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/*
 * AUTOR: Joaquin
 * PROPÓSITO: Construye un listado tipo tabla, ordenado por NOMBRE (y por CÓDIGO como desempate).
 * Uso: imprimir en consola o mostrar en JOptionPane.
 */
public class ListarProductos {

    public static String construirTabla(List<Producto> productos) {
        if (productos == null || productos.isEmpty()) {
            return "No hay productos cargados.";
        }

        List<Producto> ordenados = new ArrayList<>(productos);
        ordenados.sort(Comparator
                .comparing(Producto::getNombre, String.CASE_INSENSITIVE_ORDER)
                .thenComparing(Producto::getCodigo, String.CASE_INSENSITIVE_ORDER));

        StringBuilder sb = new StringBuilder();
        sb.append("=== LISTADO DE PRODUCTOS ===\n");
        sb.append(String.format("%-12s | %-20s | %-12s | %-8s | %-15s%n",
                "CÓDIGO", "NOMBRE", "PRECIO", "STOCK", "CATEGORÍA"));
        sb.append("--------------------------------------------------------------------------\n");

        for (Producto p : ordenados) {
            String cat = (p.getCategoria() == null) ? "SIN_CATEGORÍA" : p.getCategoria().getNombre();
            sb.append(String.format("%-12s | %-20s | %12.2f | %8d | %-15s%n",
                    p.getCodigo(), p.getNombre(), p.getPrecio(), p.getCantidad(), cat));
        }
        return sb.toString();
    }
}
