from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
producto2 = Producto('Pantalon', 150.00)
producto3 = Producto('Meidas', 45.00)
producto4 = Producto('Campera', 250.00)
producto5 = Producto('Sweter', 95.00)
producto6 = Producto('Blusa',75.00)

productos1 = [producto1, producto2] #Lista de productos
Orden1 = Orden(productos1) #Primer objeto orden pasando la lista de productos
orden1.agregar_producto(producto5)
orden1.agregar_producto(producto3)
print(Orden1)
print(f'Total de la orden 1: ${Orden1.calcular_total()}')
productos2 = [producto3, producto4]
Orden2 = Orden(productos2)
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(Orden2)
print(f'Total de la orden 2: ${Orden2.calcular_total()}')