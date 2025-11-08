package inventario;

import java.util.Scanner;

/*
 * AUTOR: Gabriel Moya
 * PROPÓSITO: Punto de entrada por consola. Integra Inventario (CRUD) y ListarProductos (tabla).
 */
public class MainApp {

    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        // Categorías semilla (editables)
        inventario.getListaCategorias().add(new Categoria(1, "Limpieza"));
        inventario.getListaCategorias().add(new Categoria(2, "Alimentos"));
        inventario.getListaCategorias().add(new Categoria(3, "Bebidas"));

        Scanner menuScanner = new Scanner(System.in);
        String opcion;

        do {
            System.out.println("""
                    \n===== MENÚ (Consola) =====
                    1. Agregar producto
                    2. Listar productos
                    3. Buscar producto
                    4. Modificar producto
                    5. Eliminar producto
                    0. Salir
                    """);
            System.out.print("Elija una opción: ");
            opcion = menuScanner.nextLine().trim();

            switch (opcion) {
                case "1" -> inventario.agregarProducto();

                case "2" -> System.out.println("\n" +
                        ListarProductos.construirTabla(inventario.getListaProductos()));

                case "3" -> {
                    System.out.println("""
                            \n--- Buscar Producto ---
                            1) Por CÓDIGO (exacto)
                            2) Por NOMBRE (contiene)
                            """);
                    System.out.print("Opción: ");
                    String opBusq = menuScanner.nextLine().trim();

                    if (opBusq.equals("1")) {
                        System.out.print("Ingrese CÓDIGO: ");
                        String codigo = menuScanner.nextLine().trim();
                        Producto p = inventario.buscarProductoPorCodigo(codigo);
                        System.out.println(p != null ? ("Encontrado:\n" + p)
                                : "No existe producto con código '" + codigo + "'.");
                    } else if (opBusq.equals("2")) {
                        System.out.print("Texto a buscar en NOMBRE: ");
                        String texto = menuScanner.nextLine().trim();
                        var res = inventario.buscarProductosPorNombre(texto);
                        if (res.isEmpty()) {
                            System.out.println("Sin resultados.");
                        } else {
                            System.out.println("Resultados:");
                            for (Producto p : res) System.out.println(p);
                        }
                    } else {
                        System.out.println("Opción inválida.");
                    }
                }

                case "4" -> inventario.modificarProducto();

                case "5" -> inventario.eliminarProducto();

                case "0" -> System.out.println("Programa finalizado. ¡Gracias!");

                default -> System.out.println("Opción inválida. Intente de nuevo.");
            }
        } while (!opcion.equals("0"));
        menuScanner.close();
        
    }
}
