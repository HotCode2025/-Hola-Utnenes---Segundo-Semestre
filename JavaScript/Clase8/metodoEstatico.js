class Persona {
    // Clase Padre
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    // Getters
    get nombre() {
        return this._nombre;
    }

    get apellido() {
        return this._apellido;
    }

    // Setters
    set nombre(nombre) {
        this._nombre = nombre;
    }

    set apellido(apellido) {
        this._apellido = apellido;
    }
    nombreCompleto() {
        return `Me llamo ${this._nombre} ${this.apellido}`;
    }
    // Sobreescribiendo el metodo de la clase padre
    toString() {
        //Regresa un String
        //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecucion
        // El metodo que se ejecuta depende si es una referencia del tipo padre o hija
        return this.nombreCompleto();
    }
    static saludar() {
        console.log("Saludos desde el metodo static");
    }
    static saludar2(persona) {
        console.log(`${persona.nombre} ${persona.apellido}`);
        console.log(
            `Saludos desde el metodo static , me llamo ${persona.nombre} ${persona.apellido}`
        );
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

let persona1 = new Persona("Otar", "Kebadze");
// persona1.saludar(); No se puede usar, porque los metodos estaticos son de la Clase en si, no de los objetos
Persona.saludar2(persona1);

let empleado1 = new Empleado("Alberto", "Gome", "Sistemas");
Empleado.saludar2(empleado1);
