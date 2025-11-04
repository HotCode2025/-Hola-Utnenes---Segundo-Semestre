class Persona {
    static contadorPersonas = 0; // Atributo Estatico
    email = 'Valor Default Email'; // Atributo No Estatico
    // Clase Padre
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        this.idPersona = ++Persona.contadorPersonas;
        console.log(`Se incrementa el contador : ${Persona.contadorPersonas}`);
    }
    nombreCompleto(){
        return `${this._nombre} ${this._apellido} con un id: ${this.idPersona}`;
    }
     toString() {
        //Regresa un String
        //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        // El metodo que se ejecuta depende si es una referencia del tipo padre o hija
        return this.nombreCompleto();
    }
}

class Empleado extends Persona {
    constructor(nombre, apellido, departamento) {
        super(nombre, apellido);
        this._departamento = departamento;
    }

    // Getter
    get departamento() {
        return this._departamento;
    }
    // Setter
    set departamento(departamento) {
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Otar','Kebadze');

console.log(persona1.email);

let empleado1 = new Empleado("Alberto", "Gomez", "Sistemas");

console.log(empleado1.email);

let persona2 = new Persona('Marco','Segui');

console.log(Persona.email); // Da UNDEFINED porque es no estatico

let persona3 = new Persona('Adrian','Alvarez');

// Vemos los tosTring, para probar el ID

console.log(persona1.toString()); // Primer objetoi creado
console.log(empleado1.toString()); // Segundo objetoi creado
console.log(persona2.toString()); // Tercer objetoi creado
console.log(persona3.toString()); // Cuarto objetoi creado