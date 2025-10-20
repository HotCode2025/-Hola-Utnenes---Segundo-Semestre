import Producto from './Producto.js';
import Orden from './Orden.js';

//Creamos los productos
const producto1 = new Producto('Remera', 40000);
const producto2 = new Producto('Pantalón', 80000);
const producto3 = new Producto('Zapatilla', 150000);
const producto4 = new Producto('Pollera', 50000);
const producto5 = new Producto('Musculosa', 8000);
const producto6 = new Producto('Short', 50000 );


// Creamos la orden de productos
const orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
orden1.agregarProducto(producto6);

orden1.mostrarOrden();
