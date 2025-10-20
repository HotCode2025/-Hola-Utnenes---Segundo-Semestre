class Persona {
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad) {
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get idPersona() { // ✅ sin guion bajo
        return this._idPersona;  
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(nombre) {
        this._nombre = nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }

    get edad() {
        return this._edad;
    }

    set edad(edad) {
        this._edad = edad;
    }

    toString() {
        return `${this._idPersona} ${this._nombre} ${this._apellido} ${this._edad}`;
    }
}


class Empleado extends Persona {

    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo) {
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado() {
        return this._idEmpleado;
    }

    get sueldo() {
        return this._sueldo;
    }

    set sueldo(sueldo) {
        this._sueldo = sueldo;
    }

    toString() {
        return `${super.toString()} ${this._idEmpleado} ${this._sueldo}`;
    }
}


class Cliente extends Persona {

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente() {
        return this._idCliente;
    }

    get fechaRegistro() {
        return this._fechaRegistro;
    }

    set fechaRegistro(fechaRegistro) {
        this._fechaRegistro = fechaRegistro;
    }

    toString() {
        return `${super.toString()} ${this._idCliente} ${this._fechaRegistro}`;
    }
}


//Prueba clase Persona
let persona1 = new Persona('Juan', 'Pérez', 32);
console.log(persona1.toString());

let persona2 = new Persona('Rosa', 'López', 35);
console.log(persona2.toString())
//Prueba clase Empleado
let empleado1 = new Empleado('Ana', 'López', 28, 50000);
console.log(empleado1.toString());

let empleado2 = new Empleado('Virginia', 'García', 55);
console.log(empleado2.toString());
//Prueba clase Cliente
let cliente1 = new Cliente('Luis', 'García', 45, '2025-10-15');
console.log(cliente1.toString());

let cliente2 = new Cliente('Juana', 'Chávez', 60);
console.log(cliente2.toString());