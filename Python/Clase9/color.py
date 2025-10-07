class Color:
    def __init__(self,color):
        self._color=color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,nuevoColor):
        self._color = nuevoColor
        return(f'El nuevo color seleccionado es {self._color}')
    
    def __str__(self):
        return(f'Color : {self._color}')