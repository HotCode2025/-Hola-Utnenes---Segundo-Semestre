//Clase 7, la cual le agrego la clase 6 para que el código pueda funcionar correctamente.

class Persona{ //Clase padre

    static contadorPersonas = 0; //Atributo estático
    //email = 'Valor default email'; //Atributo no estático
    
    static get MAX_OBJ(){ //Este método simula una constante
        return 5;    
    }
    
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;
        }
        else{
            console.log('Se ha superado el máximo de objetos permitidos');
        }
        this.idPersona = ++Persona.contadorPersonas;
        //console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
    }
    
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        this._apellido = apellido;
    }
    //Estos pertenece a la clase 7, la cual agregamos un método a la clase padre
    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido;
    }
    //Sobreescribiendo el método de la clase padre(Object) Pertenece a la clase 7
    toString(){ //Regresa un String
        //Se aplica el polimorfismo que significa = múltiples formas en tiempo de ejecución
        //El método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }
    static saludar(){
        console.log('Saludos desde este método static');
    }
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
    }
}

class Empleado extends Persona{ //Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this.de = this.departamento;
    }

    //Sobreescritura pertenece a la clase 7. 
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;

        }

}   


let persona1 = new Persona('Martín', 'Pérez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
persona1.apellido = 'Suárez';
console.log(persona1.apellido);
//console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'María Laura';
console.log(persona2.nombre);
persona2.apellido = 'García';
console.log(persona2.apellido);
//console.log(persona2);


let empleado1 = new Empleado('María', 'Jimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto()); 

//Object.prototype.toString Esta  es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());
console.log(persona1.toString());