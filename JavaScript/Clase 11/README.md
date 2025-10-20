Funciones descriptivas
1. Funciones de Manipulación de Datos
Estas funciones se encargan de transformar, limpiar o verificar la información.
•	calculateTotalPrice() (Calcular Precio Total): Esta función hace un cálculo matemático para sumar los precios y obtener el total. Es fundamental en cualquier carrito de compra y debe devolver un valor numérico. El nombre es muy explícito sobre su propósito.
•	formatUserInput() (Formatear Entrada del Usuario): Indica que la función va a modificar los datos ingresados por el usuario. Se usa para la limpieza inicial, como quitar espacios extra o convertir todo a minúsculas, lo cual ayuda a mantener la consistencia de la información.
•	validateEmailAddress() (Validar Dirección de Correo): El verbo validate (validar) comunica que la función va a comprobar si la dirección tiene el formato correcto. Es una validación esencial en formularios y devuelve un valor booleano (true o false).
•	convertToCamelCase() (Convertir a Camel Case): Su nombre indica una transformación de texto muy específica: cambiar una cadena (como mi_variable) al formato estándar de JavaScript (miVariable). Es clave para mantener la coherencia del código.
•	filterActiveUsers() (Filtrar Usuarios Activos): El verbo filter (filtrar) muestra que la función tomará una lista grande de usuarios, aplicará una condición (ser activo) y devolverá una lista más pequeña, solo con los usuarios que cumplen el criterio.
________________________________________
2. Funciones de Eventos e Interacción
Estas funciones se ejecutan en respuesta a una acción del usuario o a un cambio de estado en la interfaz.
•	handleButtonClick() (Manejar el Clic de un Botón): El prefijo handle (manejar/gestionar) es la convención estándar en JavaScript para las funciones que responden a un evento específico, en este caso, el clic en un botón.
•	onFormSubmit() (Al Enviar el Formulario): El prefijo on (al/cuando) es otra convención para handlers de eventos. Esta función se dispara justo cuando el usuario intenta enviar un formulario, permitiendo revisar los datos antes de que se envíen al servidor.
•	toggleDarkMode() (Alternar Modo Oscuro): El verbo toggle significa cambiar entre dos estados (ON u OFF). Es ideal para funciones que activan o desactivan una característica, como cambiar entre el tema claro y el oscuro de una interfaz.
•	updateProgressBar() (Actualizar la Barra de Progreso): El verbo update (actualizar) deja claro que la función modificará un elemento visual (ProgressBar) en la pantalla. Es común en procesos largos para mostrar el estado actual de una tarea.
•	initializeApp() (Inicializar la Aplicación): El verbo initialize (inicializar) indica una función de inicio o preparación. Esta función se ejecuta típicamente una sola vez al cargar la página para establecer configuraciones, cargar datos iniciales o preparar el sistema.
________________________________________
3. Operaciones CRUD
Estas funciones son esenciales para la gestión de datos persistentes (la base de datos o el servidor).
•	createNewUser() (Crear Nuevo Usuario): Representa la 'C' (Create) de CRUD. Esta función se encarga de agregar un nuevo registro (una cuenta o un usuario) al sistema.
•	fetchUserData() (Obtener Datos del Usuario): Representa la 'R' (Read) de CRUD. El verbo fetch es muy usado en JS para solicitar o traer datos existentes desde una fuente externa (API o servidor).
•	updateUserProfile() (Actualizar Perfil del Usuario): Representa la 'U' (Update) de CRUD. El verbo update comunica que la función modificará o editará un registro de usuario que ya existe en el sistema.
•	deleteUserAccount() (Eliminar Cuenta de Usuario): Representa la 'D' (Delete) de CRUD. La función elimina de forma permanente un registro del sistema, por lo que es una acción crítica y sensible.
________________________________________
4. Funciones de Utilidad
Estas son tareas genéricas, reusables y de soporte que se usan en muchas partes de la aplicación.
•	generateRandomId() (Generar ID Aleatorio): El verbo generate (generar) indica que la función crea un valor nuevo (un identificador único) de forma automática y aleatoria, lo cual es útil para dar identidad a nuevos objetos o registros.
•	formatCurrency() (Formatear Moneda): Esta función de utilidad se usa para cambiar el formato de un número para que se vea como dinero, añadiendo el símbolo monetario, comas y decimales (ej. $1.500,00).
•	debounceSearch() (Retrasar Búsqueda): El término debounce se refiere a una técnica de optimización. La función controla el tiempo para evitar ejecutar la búsqueda repetidamente mientras el usuario está escribiendo, mejorando el rendimiento.
•	sanitizeInput() (Sanear Entrada): El verbo sanitize (sanear/limpiar) es clave para la seguridad. La función elimina código o caracteres potencialmente peligrosos de la entrada del usuario antes de que se procese, previniendo vulnerabilidades.
•	checkPermissions() (Comprobar Permisos): El verbo check (comprobar/revisar) es sencillo y directo. La función se encarga de verificar si el usuario tiene los derechos para realizar una acción, siendo esencial para el control de acceso en el sistema.

