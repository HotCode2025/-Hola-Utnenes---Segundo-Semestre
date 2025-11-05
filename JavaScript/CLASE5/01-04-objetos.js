//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase();//convierte las minúsculas a mayúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },

    nombreCompleto: function(){
        //método o función en JavaScript
        return this.nombre + ' ' + this.apellido;
    },
    get nombreEdad() { //Éste es el método get
        return 'El nombre es: ' + this.nombre + ', Edad: ' + this.edad;
    }

};

console.log('comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el método get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang)

function Persona3(nombre ,apellido,email){//constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Leo','Lopez','lopez@gmail.com');
padre.nombre = 'Luis';//modificamos el nombre

padre.telefono = '2345623456';//una propiedad exclusiva del objeto padre

console.log(padre)

console.log(padre.nombreCompleto());//utilizamos la funcion

let madre = new Persona3('Laura','Contrera','contrera@gmail.com');
console.log(madre);

console.log(madre.telefono);//la propiedad no esta definida

console.log(madre.nombreCompleto());

//Diferentes formas de crear objetos
//caso número 1
let miObjeto = new Object();
//caso número 2
let miObjeto2 = {};//Esta opcion es brve y recomendada

//Caso string 1
let miCadena1 = new String('Hola');
//caso string 2
let miCadena2 = 'Hola';//Esta es la sintaxis simplificada y recomendada 

//caso con numeros 1
let miNumero = new Number(1);//Es formal no recomendable
//caso con numeros 2
let miNumero2 = 1;//sintaxis recomendada

//caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//caso boolean 2
let miBoolean2 = false; //sintaxis recomendada

//caso arreglos 1
let miArreglo1 = new Array();//formal
//caso arreglo 2
let miArreglo2 = []; //Sintaxis recomendada

//caso function 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//caso function 2
let miFuncion2 = function(){};//Notacion simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '2618383832'
console.log(padre);
console.log(madre.telefono);
madre.telefono = '2613434342';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Lic.', '5492618484845'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492618585856'));

//Método Apply
let arreglo = ['Ing.' , '5492618686865'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));