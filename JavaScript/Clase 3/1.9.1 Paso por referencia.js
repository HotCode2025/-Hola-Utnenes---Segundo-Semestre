//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k);   // 10


//Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}

console.log(persona);   // { nombre: 'Juan', apellido: 'Lepez' }

function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);   // { nombre: 'Ignacio', apellido: 'Perez' }
