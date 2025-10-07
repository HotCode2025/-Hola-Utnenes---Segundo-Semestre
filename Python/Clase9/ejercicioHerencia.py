class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad= edad
        
    @property
    def nombre(self): # Metodo Getter
        return self._nombre
    @property
    def edad(self): # Metodo Getter
        return self._edad

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self._sueldo = sueldo
    
    @property
    def sueldo(self): # Metodo Getter
        print('-------------------------------')
        print('UTILIZANDO EL GETTER')
        print('-------------------------------')
        return self._sueldo
    
    @sueldo.setter
    def nuevo_sueldo(self,sueldo): # Metodo Setter
        print('-------------------------------')
        print('UTILIZANDO EL SETTER')
        print('-------------------------------')
        self._sueldo = sueldo
        print(f'El nuevo sueldo es de U$S{self._sueldo}')
        
    def mostrar_datos(self):
        print(f'Mi nombre es {self.nombre}. Tengo {self.edad} años de edad, y mi sueldo es de U$S{self._sueldo}')


# Creando empleado

empleado = Empleado('Otar', 35, 3500)

# Mostrando datos

empleado.mostrar_datos()

# Modificando datos

empleado.nuevo_sueldo = 5000

# Mostrando datos nuevos


empleado.mostrar_datos()