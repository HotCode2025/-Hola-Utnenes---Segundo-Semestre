Orden orden1 = new Orden();
//Agregamos productos al arreglo
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.mostrarOrden();

//Tarea:
//Crear mas objetos de tipo Producto = 10
//Crear mas objetos de tipo Orden = 2
package ar.com.codesystem.ventas;
public double calcularTotal(){
    double total = 0; //Variable temporal
    for (int i = 0; i < this.contadorProductos; i++) {
        //Producto producto = this.productos[i];
        //total += producto.getPrecio();
        total += this.productos[i].getPrecio();
    }
    return total;
}package ar.com.codesystem.ventas;
public void mostrarOrden(){ 
    System.out.println("Id Orden: " + idOrden);
    double totalOrden = this.calcularTotal();
    System.out.println("El total de la oredén es: $" + totalOrden);
    System.out.println("Productos de la orden: ");
    for (int i = 0; i < this.contadorProductos; i++) {
        System.out.println(this.productos[i]);
    }
}
package ar.com.codesystem.ventas;
//Constructor vacío
public Orden() {
    this.idOrden = ++Orden.contadorOrdenes;
    this.productos = new Producto[Orden.MAX_PRODUCTOS];
}
public void agregarProducto(Producto producto){
    if(this.contadorProductos < Orden.MAX_PRODUCTOS){
        this.productos[this.contadorProductos++] = producto;
    }
    else{
        System.out.println("Se ha superado el maximo de productos: " + Orden.MAX_PRODUCTOS);
    }
}
package ar.com.codesystem.ventas;
public class Orden {
    private int idOrden;
    private Producto productos[];   //Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    //Constructor vacío
    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
}