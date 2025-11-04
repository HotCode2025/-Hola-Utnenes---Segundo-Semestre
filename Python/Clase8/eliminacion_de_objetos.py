from metodo_getter_setter import Persona2

# Aca ejecutaremos solamente este archivo

if __name__ == '__main__':
    print('Creacion de objetos'.center(50, '-'))
    persona3 = Persona2('Raul', 'Gomez', 32)
    print(persona3.mostrar_detalles())
    print('Eliminacion de objetos'.center(50, '-'))
    del persona3
