# Diccionarios

diccionario = {
    'IDE' : 'Integrated Development Environment',
    'POO' : 'Programacion Orientada a Objetos',
    'SABD' : 'Sistema de Administracion de Base de Datos'
}

print(diccionario) # Imprime el diccionario completo
print(len(diccionario)) # 3
print(type(diccionario)) # <class 'dict'>
print(diccionario['POO']) # Programacion Orientada a Objetos, accedemos pcon la llave
print(diccionario.get('IDE')) # Integrated Development Environment , accedemos pcon la llave
# print(diccionario['SGBD']) # Arroja error porque la clave no existe
print(diccionario.get('SGBD')) # None
print(diccionario.get('SGBD', 'No existe la clave')) # No existe la clave
print('IDE' in diccionario) # True
print('SGBD' in diccionario) # False
# Modificar un elemento
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario) # {'IDE': 'Entorno de Desarrollo Integrado', 'POO': 'Programacion Orientada a Objetos', 'SABD': 'Sistema de Administracion de Base de Datos'}
# Mostrar solo llaves
print(diccionario.keys()) # dict_keys(['IDE', 'POO', 'SABD'])
# Mostrar solo valores
print(diccionario.values()) # dict_values(['Entorno de Desarrollo Integrado', 'Programacion Orientada a Objetos', 'Sistema de Administracion de Base de Datos'])

# Lo mismo pero con un for

for termino in diccionario.keys():
    print(termino) # Imprime las llaves

for definicion in diccionario.values():
    print(definicion) # Imprime los valores
    
for termino, definicion in diccionario.items():
    print(termino, definicion) # Imprime las llaves y los valores
    
# Agregar un elemento
diccionario['SGBD'] = 'Sistema de Gestion de Base de Datos'

#Comprobar la existencia de un elemento
if 'SGBD' in diccionario:
    print('Existe el termino SGBD') # Existe el termino SGBD
# o sino tambien puede hacerse
print('IDE' in diccionario) # True

# Eliminar un elemento
diccionario.pop('SABD') # Elimina el elemento con la llave 'SABD'
print(diccionario) # {'IDE': 'Entorno de Desarrollo Integrado', 'POO': 'Programacion Orientada a Objetos', 'SGBD': 'Sistema de Gestion de Base de Datos'}
del diccionario['POO'] # Elimina el elemento con la llave 'POO'
print(diccionario) # {'IDE': 'Entorno de Desarrollo Integrado', 'SGBD': 'Sistema de Gestion de Base de Datos'}
diccionario.clear() # Elimina todos los elementos
print(diccionario) # {}
del diccionario # Elimina el diccionario