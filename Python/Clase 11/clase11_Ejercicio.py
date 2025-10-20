class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'{self.nombre} (${self.precio:.2f})'


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)  # Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0  # Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f'Orden: {self.id_orden}, \nProductos: {productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    productos1 = [producto1, producto2]  # Lista de productos
    orden1 = Orden(productos1)  # Primer objeto orden pasando la lista de productos
    print(orden1)
    producto4 = Producto('Jean', 140.00)
    producto5 = Producto('Cinturón', 1500.00)
    productos2 = [producto4, producto5]  # Lista de productos
    orden2 = Orden(productos2)
    print(orden2)
    # Tarea: Modificar la orden2, ingresando nuevos productos con sus nombres y precios,
    # crear una nueva lista de productos y agregarla a la orden2.
    
    # Plus: agregamos un una tercer orden con nuevos productos.
    producto6 = Producto('Zapatos', 250.00)
    producto7 = Producto('Sombrero', 80.00)
    productos3 = [producto6, producto7]  # Lista de productos
    orden3 = Orden(productos3)
    print(orden3)
    
    #Sumar ordenenes, calcular totales
    print(f'Total orden 1: ${orden1.calcular_total():.2f}')
    print(f'Total orden 2: ${orden2.calcular_total():.2f}')
    print(f'Total orden 3: ${orden3.calcular_total():.2f}')
    
    #total de todas las ordenes
    total_general = orden1.calcular_total() + orden2.calcular_total() + orden3.calcular_total()
    print(f'Total general de todas las ordenes: ${total_general:.2f}')