// 1️⃣ Mostrar los números del 1 al 10, uno debajo del otro
console.log(`\n📌 Ejercicio 1: Números del 1 al 10`);
let salida1 = '';
for (let i = 1; i <= 10; i++) {
  salida1 += `${i}\n`;
}
console.log(salida1);

// 2️⃣ Mostrar los números del 1 al 10, uno por línea
console.log(`\n📌 Ejercicio 2: Números del 1 al 10 (línea por línea)`);
let salida2 = [...Array(10)].map((_, i) => `${i + 1}`).join('\n');
console.log(salida2);

// 3️⃣ Promedio y nota más baja de estudiantes
console.log(`\n📌 Ejercicio 3: Promedio y nota más baja`);
let notas = [7, 4, 9, 6, 5];
let promedio = notas.reduce((a, b) => a + b, 0) / notas.length;
let notaMinima = Math.min(...notas);
console.log(`Promedio: ${promedio}\nNota más baja: ${notaMinima}`);

// 4️⃣ Salario individual y total de empleados
console.log(`\n📌 Ejercicio 4: Salarios individuales y total`);
let empleados = [1000, 1200, 950];
let total = empleados.reduce((a, b) => a + b, 0);
let detalle = empleados.map((salario, i) => `Empleado ${i + 1}: $${salario}`).join('\n');
console.log(`${detalle}\nTotal: $${total}`);

// 5️⃣ Suma de serie alternante
console.log(`\n📌 Ejercicio 5: Serie alternante 1 - 1/2 + 1/3 - ...`);
let n = 10;
let sumaAlternante = 0;
for (let i = 1; i <= n; i++) {
  sumaAlternante += (i % 2 === 0 ? -1 : 1) * (1 / i);
}
console.log(`Suma alternante hasta ${n} términos: ${sumaAlternante}`);

// 6️⃣ Número mayor y menor en una lista
console.log(`\n📌 Ejercicio 6: Mayor y menor en lista`);
let lista = [3, 8, 1, 9, 2];
console.log(`Mayor: ${Math.max(...lista)}\nMenor: ${Math.min(...lista)}`);

// 7️⃣ Verificar si un año es bisiesto
console.log(`\n📌 Ejercicio 7: Verificación de año bisiesto`);
let continuar = true;
while (continuar) {
  let año = parseInt(prompt("Ingrese un año:"));
  let bisiesto = (año % 4 === 0 && año % 100 !== 0) || (año % 400 === 0);
  alert(`${año} ${bisiesto ? "es" : "no es"} bisiesto`);
  continuar = confirm("¿Desea verificar otro año?");
}

// 8️⃣ Ingresar N números y encontrar mayor y menor
console.log(`\n📌 Ejercicio 8: Mayor y menor entre N números`);
let cantidad = parseInt(prompt("¿Cuántos números desea ingresar?"));
let numeros = [];
for (let i = 0; i < cantidad; i++) {
  numeros.push(parseFloat(prompt(`Número ${i + 1}:`)));
}
console.log(`Mayor: ${Math.max(...numeros)}\nMenor: ${Math.min(...numeros)}`);

// 9️⃣ Sumatoria con factorial y potencia
console.log(`\n📌 Ejercicio 9: Sumatoria con factorial y potencia`);
function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}
let suma = 0;
for (let i = 1; i <= 5; i++) {
  suma += Math.pow(i, 2) / factorial(i);
}
console.log(`Sumatoria: ${suma}`);

// 🔟 Factorial con while y do...while
console.log(`\n📌 Ejercicio 10: Factorial con while y do...while`);
let num = 5;
let fact1 = 1, i = 1;
while (i <= num) {
  fact1 *= i++;
}
console.log(`Factorial con while: ${fact1}`);

let fact2 = 1, j = 1;
do {
  fact2 *= j++;
} while (j <= num);
console.log(`Factorial con do...while: ${fact2}`);

// 1️⃣1️⃣ Números del 10 al 1 descendente
console.log(`\n📌 Ejercicio 11: Números del 10 al 1`);
let descendente = [...Array(10)].map((_, i) => `${10 - i}`).join('\n');
console.log(descendente);

// 1️⃣2️⃣ Sumar pares y promediar impares
console.log(`\n📌 Ejercicio 12: Suma de pares y promedio de impares`);
let datos = [2, 3, 4, 5, 6, 7];
let pares = datos.filter(n => n % 2 === 0);
let impares = datos.filter(n => n % 2 !== 0);
let sumaPares = pares.reduce((a, b) => a + b, 0);
let promedioImpares = impares.reduce((a, b) => a + b, 0) / impares.length;
console.log(`Suma pares: ${sumaPares}\nCantidad pares: ${pares.length}\nPromedio impares: ${promedioImpares}`);

// 1️⃣3️⃣ Suma de cuadrados de los primeros N números
console.log(`\n📌 Ejercicio 13: Suma de cuadrados`);
let N = 5;
let sumaCuadrados = 0;
for (let i = 1; i <= N; i++) {
  sumaCuadrados += i * i;
}
console.log(`Suma de cuadrados hasta ${N}: ${sumaCuadrados}`);