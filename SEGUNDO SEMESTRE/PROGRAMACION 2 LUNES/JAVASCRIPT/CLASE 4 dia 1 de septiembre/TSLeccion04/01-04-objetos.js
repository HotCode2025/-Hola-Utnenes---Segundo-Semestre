let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){ //Método o funcion en JS
        return this.nombre+' '+this.apellido;
    }

}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5491618282821';
console.log(persona2.telefono)
console.log('Creamos un nuevo objeto');

console.log(persona['apellido']);//Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//for in y accedemos al objeto como si fuera arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad])
}
console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud';//Cambiamos dinamicamente el vaor de un objeto
delete persona.apellida;//Eliminamos el error
console.log(persona)

//Distinta forma de imprimir un objeto
//Número 1: la más sencilla: concatenar cada valor de cada propiedad
console.log('Distinta forma de imprimir un objeto: forma 1');
console.log(persona.nombre+' '+persona.apellido);

//Número 2: A través del ciclo for in
console.log('Distinta forma de imprimir un objeto: forma 3');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: La funcion Object.values()
console.log('Distinta forma de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray)

//Número 4: Utilizaremos el metodo JSON.stringify
console.log('Distinta forma de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);