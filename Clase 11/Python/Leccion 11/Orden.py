class Orden:
    contador_ordenes = 0

    def __init__(self,productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto) #Esto es para agregar un nuevo producto

    def calcular_total(self):
        total = 0 #Variable temporal para almacenar el total temporal
        for producto in self._productos:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f'Orden ID: {self.id_orden}, \nProducto: {productos_str}'
    
if __name__ == '__main__': 
    from Producto import Producto
producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
productos1 = [producto1, producto2] #Lista de productos
Orden1 = Orden(productos1) #Primer objeto orden pasando la lista de productos
print(Orden1)
Orden2 = Orden(productos1)
print(Orden2)
# Tarea: Modificar la orden2 ingresando nuevos productos con sus nombres y precios
# Crear una nueva lista de productos y agregarla a la orden2

producto3 = Producto('Zapatillas', 300.00)
producto4 = Producto('Gorra', 80.00)
productos2 = [producto3, producto4] #Lista de nuevos productos
for producto in productos2:
    Orden2.agregar_producto(producto) #Agregamos los nuevos productos a la orden2

print('\nOrden 2 modificada con nuevos productos:')
print(Orden2)
print(f'Total de la orden 2: ${Orden2.calcular_total()}')