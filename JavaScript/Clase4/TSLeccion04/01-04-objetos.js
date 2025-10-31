let x = 10; //variable de tipo primitiva
console.log(x.length); // undefined

//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){//metodo o funcion en JavaScript 
        return this.nombre + ' ' + this.apellido;
    }
}

console.log(persona.nombre); // Carlos
console.log(persona.apellido); // Gil
console.log(persona.email); // cgil@gmail.com
console.log(persona.edad); // 30
console.log(persona); // { nombre: 'Carlos', apellido: 'Gil', email: 'cgil@gmail.com', edad: 30 }
console.log(persona.nombreCompleto());// Carlos Gil
console.log('Ejecutando con un objeto');
let persona2 = new Object();//Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono); // 5492618282821
console.log(persona['apellido']); //Accedemos como si fuera un arreglo Gill
console.log(persona['apellido']); //Usamos el ciclo for in
console.log('Usamos el ciclo for in');
//for in
for(propiedad in persona){
    console.log(propiedad); 
    console.log(persona[propiedad]);
}
console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Bentancud'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distinta formas de imprimir un objeto
//Número 1: la más sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre + ','+ persona.apellido);

//Número 2: A través del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(propiedad in persona){
    console.log(persona[propiedad]);
}

//Número 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Número 4: Utilizando el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);