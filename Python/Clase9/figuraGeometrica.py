class FiguraGeometrica:
    def __init__(self,alto,ancho):
        self._alto = alto
        self._ancho = ancho
    
    @property
    def alto(self):
        return self._alto
    
    @property
    def ancho(self):
            return self._ancho
    
    @alto.setter
    def alto(self, nuevoAlto):
        self._alto = nuevoAlto
        return(f'El nuevo alto es de {self._alto}')
    
    @ancho.setter
    def ancho(self, nuevoAncho):
        self._ancho = nuevoAncho
        return(f'El nuevo ancho es de {self._ancho }')
    
    def __str__(self):
        return(f'El ancho es de {self._ancho} y el alto es de {self._alto}')