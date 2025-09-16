seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 25, 'Altura': 1.70, 'Precio': '90 Millones', 'Posicion': 'Delantero Centro'},
    24: {'Nombre': 'Enzo Fernandez', 'Edad': 24, 'Altura': 1.78, 'Precio': '81 Millones', 'Posicion': 'Mediocampista'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 31, 'Altura': 1.83, 'Precio': '3.3 Millones', 'Posicion': 'Mediocampista'},
    3: {'Nombre': 'Valentin Barco', 'Edad': 21, 'Altura': 1.70, 'Precio': '10 Millones', 'Posicion': 'Lateral Izquierdo'},
}

for llave, valor in seleccionArgentina.items():
    print(f'El jugador {valor["Nombre"]} usa la numero {llave}')
