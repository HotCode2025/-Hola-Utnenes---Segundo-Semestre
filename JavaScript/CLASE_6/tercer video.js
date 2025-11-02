class Persona{
    constructor(nombre, apellido){
       this._nombre = nombre;
       this._apellido = apellido; 
    }

get nombre(){
    return this._nombre
}

}

let persona1 = new Persona("Joaquin", "Ybañez");
console.log(persona1.nombre)
//console.log(persona1);
let persona2 = new Persona("nicolas", "Martini");
console.log(persona2.nombre)
//console.log(persona2);