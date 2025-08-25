seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones' , 'Posicion': 'Extremo Derecho'},
    9: {'Nombre': 'Julian alvarez', 'Edad': 25, 'Altura': 1.70, 'Precio': '90 Millones' , 'Posicion': 'Delantero Centro'},
    24: {'Nombre': 'Enzo Fernandez', 'Edad': 24 , 'Altura': 1.78, 'Precio': '81 Millones' , 'Posicion': 'Mediocampista'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 31, 'Altura': 1.82, 'Precio': '3.3 Millones' , 'Posicion': 'Mediocampista'},
    3: {'Nombre': 'Valentin Barco', 'Edad': 21, 'Altura': 1.70, 'Precio': '10 Millones' , 'Posicion': 'Lateral Izquierdo'},
}

for llave, valor  in seleccionArgentina.items():
    print (f'El jugador {valor['Nombre']} usa la numero {llave}\n')

# Agregando un nuevo jugador
seleccionArgentina[23] = {'Nombre': 'Emiliano Martinez', 'Edad': 32, 'Altura': 1.95, 'Precio': '20 Millones' , 'Posicion': 'Arquero'}
seleccionArgentina[14] = {'Nombre': 'Exequiel Palacios', 'Edad': 26, 'Altura': 1.77, 'Precio': '40 Millones' , 'Posicion': 'Mediocampista'}
seleccionArgentina[20] = {'Nombre': 'Franco Mastantuono', 'Edad': 18, 'Altura': 1.77, 'Precio': '30 Millones' , 'Posicion': 'Extremo Derecho'}
seleccionArgentina[11] = {'Nombre': 'Thiago Almada', 'Edad': 24, 'Altura': 1.71, 'Precio': '25 Millones' , 'Posicion': 'Extremo Izquierdo'}


for llave, valor  in seleccionArgentina.items():
    print (f'El jugador {valor["Nombre"]} usa la numero {llave}\n')