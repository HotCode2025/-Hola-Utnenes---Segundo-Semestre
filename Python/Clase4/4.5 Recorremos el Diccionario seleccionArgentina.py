#Diccionario para datos de la seleccion argentina
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70,'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di Maria', 'Edad': 34, 'Altura': 1.80,'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28 , 'Altura': 1.77,'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83,'Precio': '3.5 Millones', 'Posicion': 'Defensa'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89,'Precio': '3.5 Millones', 'Posicion': 'Portero'}
}

for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')