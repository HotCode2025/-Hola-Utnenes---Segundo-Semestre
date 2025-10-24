class Persona2:
    
    def __init__(self,nombre,apellido,edad): # Datois encapsulador
        
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
        
    def mostrar_detalles(self):
        return (f'Los datos a mostrar son :\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}')
    
    @property
    def nombre(self): # Metodo Getter
        print('-------------------------------')
        print('UTILIZANDO EL GETTER')
        print('-------------------------------')
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre): # Metodo Setter
        print('-------------------------------')
        print('UTILIZANDO EL SETTER')
        print('-------------------------------')
        self._nombre = nombre
    
    @property
    def apellido(self): # Metodo Getter
        print('-------------------------------')
        print('UTILIZANDO EL GETTER')
        print('-------------------------------')
        return self._apellido
    
    @apellido.setter
    def nomapellidobre(self,apellido): # Metodo Setter
        print('-------------------------------')
        print('UTILIZANDO EL SETTER')
        print('-------------------------------')
        self.apellido = apellido
    
    @property
    def edad(self): # Metodo Getter
        print('-------------------------------')
        print('UTILIZANDO EL GETTER')
        print('-------------------------------')
        return self._edad
    
    @edad.setter
    def edad(self,edad): # Metodo Setter
        print('-------------------------------')
        print('UTILIZANDO EL SETTER')
        print('-------------------------------')
        self._edad = edad

persona1 = Persona2('Otar', 'Kebadze' , 35)
# print(persona1._nombre) 
# print(persona1._nombre) Se puede acceder, pero NO SE DEBE, ES UNA MALA PRACTICA+

print(persona1.nombre)

#    TAREA 
#    CREANDO 3 PERSONAS MAS

#    PERSONA 2 
#    Creacion

persona2 = Persona2('Raul', 'Betancud' , 35)

print(persona2.nombre)

#    Modificando con el setter

persona2.nombre = 'Ariel'

print(persona2.mostrar_detalles())

#    PERSONA 3

persona3 = Persona2('Javier', 'Segui' , 35)

print(persona3.nombre)


#    Modificando con el setter

persona2.nombre = 'Marco'

print(persona3.mostrar_detalles())

#    PERSONA 4

persona4 = Persona2('Amanda', 'Villar' , 40)

print(persona4.nombre)


#    Modificando con el setter

persona4.nombre = 'Amelia'

print(persona4.mostrar_detalles())

