# -Hola-Utnenes---Segundo-Semestre
Repositorio principal de ('Hola Utnenes')
#########################################################
# 🚨 ATENCIÓN HOLAUTNenes 🚨
# NO MODIFICAR NADA EN LA RAMA MAIN !!!
# SOLO TRABAJAR EN SUS PROPIAS RAMAS
# EL QUE TOQUE MAIN SE GANA UNA PATADA VIRTUAL ⚡
#########################################################

# 1) Clonar el repo en una carpeta llamada HolaUTNenes
git clone https://github.com/HotCode2025/-Hola-Utnenes---Segundo-Semestre.git HolaUTNenes
cd HolaUTNenes

# 2) Crear una nueva rama (cada uno la suya, con su nombre)
git checkout -b rama_tunombre

# 3) Ver ramas disponibles
git branch -a

# 4) Cambiar a otra rama
git checkout rama_tunombre

#########################################################
# 🚨 ANTES DE SUBIR CAMBIOS 🚨
# HACER PULL PARA TRAER LO ÚLTIMO Y EVITAR CONFLICTOS
#########################################################
git pull origin main

# 5) Agregar y confirmar cambios en TU rama
git add .
git commit -m "mensaje claro del cambio"

# 6) Subir cambios (NUNCA A MAIN)
git push origin rama_tunombre

#########################################################
# 🚨 COMANDOS ÚTILES DE CARPETAS Y ARCHIVOS 🚨
#########################################################

# Crear carpeta
mkdir NombreCarpeta

# Entrar en carpeta
cd NombreCarpeta

# Volver un nivel atrás
cd ..

# Eliminar archivo
rm archivo.txt

# Eliminar carpeta (⚠ cuidado, borra todo adentro)
rm -rf Carpeta
