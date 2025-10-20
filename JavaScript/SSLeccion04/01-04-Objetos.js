let x = 10; //Variable de tipo primitivo
console.log(x.length);
console.log('Tipos primitivos');
//Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 28,
    idioma: 'es',

    get lang(){
        return this.idioma.toUpperCase();//Convierte las mínusculas a mayúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },

    nombreCompleto: function(){ //Metodo o funcionen JS
        return this.nombre+' '+this.apellido;

    },
    get nombreEdad(){ //Este es el método get
        return 'El nombre es: '+this.nombre+' ,Edad: '+this.edad;

    }


}
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5461546514653';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');

console.log(persona['apellido']); //Accedemos como si fuera un arreglo
console.log('Usamos el ciclo for in');
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);

}
console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud';//Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distintas formas de imprimir un objeto
//Número 1: la más sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un obejeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

//Número 2: A través del ciclo for in
console.log('Distintas formas de imprimir un obejeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Número 3: La función Object.value()
console.log('Distintas formas de imprimir un obejeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: Utilizaremos el método JSON.stringify
console.log('Distintas formas de imprimir un obejeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el método get')
console.log(persona.nombreEdad);
console.log('Comenzamos con el método get y set para idioma');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre = 'Luis', apellido, email){//consltructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+apellido;
    }
}
let padre = new Persona3('Leo', 'López', 'lopezl@gmail.com');
padre.nombre = 'Luis'
padre.telefono = '5465641'; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto());
let madre = new Persona3('Laura', 'Contreras', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //La propuedad no esta definida
console.log(madre.nombreCompleto());


//Uso de prototype
Persona3.prototype.telefono = '564646464';
console.log(padre);
console.log(madre);
madre.telefono = '64564564654654';
console.log(madre.telefono);


//Uso de call
let Persona4 = {
    nombre: 'Juan',
    apellido: 'Pérez',
    nombreCompleto2: function(título, teléfono){
        return título+': '+this.nombre+' '+this.apellido+' '+teléfono;
        //return this.nombre+' '+this.apellido;
    }

}

let Persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara',
    
}
console.log(Persona4.nombreCompleto2('Lic.', '65456465'));
console.log(Persona4.nombreCompleto2.call(Persona5, 'Ing.', '654564564'));

//Método Apply
let arreglo = ['Ing.', '5456464'];
console.log(Persona4.nombreCompleto2.apply(Persona5, arreglo));
