class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre
        this._apellido = apellido
    }
    //get y set nombre
    get nombre(){
        return this._name
    }
    set nombre(newName){
        return this._nombre = newName
    }
    
    get apellido(){
        return this._apellido
    }
    set apelldio(newApellido){
        return this._apellido = newApellido
    }
}


class Obrero extends Persona{
    constructor (departamento, nombre, apellido){
        
        super(nombre, apellido)
        this._departamento = departamento
    }
    get departamento(){
        return this._departamento
    }
    set departamento(newDepartamento){
        return this._departamento = newDepartamento
    }
}
const laburante = new Obrero("piso 5", "Franco", "Giraudo")
console.log(laburante);


console.log(laburante._nombre);