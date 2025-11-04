# Getter : Nos permiten obtener los atributros privados
# Setter : Nos permite modificar el atributo

class Persona2:
    def __init__(self,nombre, apellido,edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    def mostrar_detalles(self):
        return (f'Los datos a mostrar son :\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}')
    
    @property
    def nombre(self): # Metodo Getter
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    def __del__(self):
        print(f'Eliminando: \nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Adrian', 'Kebadze', 35)
    print(persona1.nombre) # Llamamos al Getter
    persona1.nombre = 'Otar' # Accede al Setter
    print(persona1.nombre) # Llamamos al Getter
    print(persona1.mostrar_detalles()) # Llamamos al metodo mostrar_detalles()

