/*
Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)

function validatePassword(password) {
    // Tu código aquí
}

console.log(validatePassword("Abc12345")); // true
console.log(validatePassword("weak")); // false

// Ejercicio 2: Crear un sistema simple de gestión de tareas
function createTaskManager() {
    let tasks = [];
    
    return {
        addTask: function(task) {
            // Tu código aquí
        },
        completeTask: function(taskId) {
            // Tu código aquí
        },
        listTasks: function() {
            // Tu código aquí
        }
    };
}

// Uso:
const myTasks = createTaskManager();
myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");

Tarea: hacer los ejercicios sin tener el video, estos ejercicios se los muestro después 
de la entrega de la tarea, se debe enviar el enlace desde el repositorio de Github, 
es un trabajo grupal, si se entrega antes de las 23 horas y los ejercicios estan bien 
resueltos, tendrán la mejor nota, después de las 23 horas la nota baja, aprueban con 7.
*/


/* ejercicio 1 */
function validatePassword(contrasenia) {
    const minLength = 8;
    const hasNumber = /\d/;
    const hasUpperCase = /^[^A-Z]*$/;

    if (contrasenia.length < minLength) return false;
    if (!hasNumber.test(contrasenia)) return false;
    if (!hasUpperCase.test(contrasenia)) return false;
    return true;
}

console.log(validatePassword("abc12345")); // true
console.log(validatePassword("utn")); // false
console.log(validatePassword("UTNENES")); // false
console.log(validatePassword("UTNENES12")); // false


/* Ejercicio 2 */
function createTaskManager() {
    let tasks = [];
    
    return {
        addTask: function(task) {
            
            tasks.push({ id: tasks.length + 1, description: task, completed: false });
        },
        completeTask: function(taskId) {
            
            const task = tasks.find(t => t.id === taskId);
            if (task) {
                task.completed = true;
            }
        },
        listTasks: function() {
            return tasks;
        }
    };
}

// Uso:
const myTasks = createTaskManager();
myTasks.addTask("Aprender JavaScript");
myTasks.addTask("Hacer ejercicio");
console.log(myTasks.listTasks())