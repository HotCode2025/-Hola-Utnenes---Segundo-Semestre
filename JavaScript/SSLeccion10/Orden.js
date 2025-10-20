import Producto from './Producto.js';

export default class Orden {
    static contadorOrdenes = 0;
    static get MAX_PRODUCTOS() { return 5; }

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
    }

    agregarProducto(producto) {
        if (this._productos.length < Orden.MAX_PRODUCTOS) {
        this._productos.push(producto);
    }   else {
        console.log('Límite de productos alcanzado.');
    }
}

    calcularTotal() {
        return this._productos.reduce((total, p) => total + p.precio, 0);
    }

    mostrarOrden() {
    const productosOrden = this._productos
        .map(p => p.toString())
        .join('\n');

    console.log(
    `Orden N°: ${this._idOrden}

    ${productosOrden}

    Total: $${this.calcularTotal()}`);

    }
}