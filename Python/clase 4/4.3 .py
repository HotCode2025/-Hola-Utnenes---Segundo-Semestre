personajes = []
personajes.append({
    "Nombre": "Aragorn",
    "Clase": "Guerrero",
    "Raza": "Dúnadan del norte"})
personajes.append({
    "Nombre": "Gandalf",
    "Clase": "Mago",
    "Raza": "Istar"})
personajes.append({
    "Nombre": "Legolas",
    "Clase": "Arquero",
    "Raza": "Elfo Sindar"})
for personaje in personajes:
    print(f"Nombre:{personaje['Nombre']}, Clase:{personaje['Clase']}, Raza:{personaje['Raza']}")
