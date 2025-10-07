from figuraGeometrica import FiguraGeometrica
from color import Color

class Cuadrado (FiguraGeometrica,Color):
    def __init__(self,alto,ancho,color):
        Color.__init__(self,color)
        FiguraGeometrica.__init__(self,alto,ancho)
    
    def calcular_area(self):
        return (f'El area del cuadrado es de { self.alto * self.ancho} y es de color {self.color}')
        
    def __str__(self):
        return(f'Area : {self.calcular_area()}')