//let persona3 = new Persona('Carla', 'Ponce')ESTO NO SE DEBE HACER

class Persona{ //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
//get y set para nombre
    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }
//get y set para apellido
    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
    //Sobreescribiendo el método de la clase padre (objetc)
    toString(){//Regresa un string
        //Se aplica el polimorfismo = multiple orma en tiempo de ejecucion
        //El metodo que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }
}

class Empleado extends Persona{//Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido)
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
    }

    toString(){
        return this.nombreCompleto();
    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1._nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre +' '+persona1.apellido)

//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2._nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre +' '+persona2._apellido);
//console.log(persona2);


//Tarea hecha.

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1)
console.log(empleado1.nombreCompleto());

//Object.prototype.toString Esta es la manera de acceder a atributos y metodos de manera dinamica 
console.log(empleado1.toString());
console.log(persona1.toString());
