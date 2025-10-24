class Persona {
    static contadorPersonas = 0; // Atributo Estatico

    static get MAX_OBJ() { // Simula una constante
        return 5
    }

    // Clase Padre
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
        if (Persona.contadorPersonas < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersonas;
            console.log(`Se incrementa el contador : ${Persona.contadorPersonas}`);
        } else {
            console.log('SE HA EXCEEDIDO DEL MAXIMO DE OBJETOS PERMITIDOS')
        }
    }
}

// Intentamos crear 6 objetos persona
let persona1 = new Persona('Ana', 'García');
let persona2 = new Persona('Carlos', 'Rodríguez');
let persona3 = new Persona('María', 'López');
let persona4 = new Persona('Juan', 'Martínez');
let persona5 = new Persona('Laura', 'Sánchez');
let persona6 = new Persona('Pedro', 'González');

console.log('\nMáximo de objetos permitidos:', Persona.MAX_OBJ);
console.log('Contador actual de personas:', Persona.contadorPersonas);
