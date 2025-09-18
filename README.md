# Proyecto_largo
Menú Principal
Al iniciar el programa, verás un menú con las siguientes opciones. Para usar el sistema, solo ingresa el número de la opción y presiona Enter.

Registrar usuario

Crear curso

Inscribir estudiante en curso

Crear evaluación

Registrar calificación

Mostrar cursos

Mostrar estudiantes de un curso

Generar Reportes

Salir

Funciones Clave del Sistema
1. Registrar Usuario
Permite añadir nuevos estudiantes o instructores.

Se solicita el tipo de usuario, un ID de usuario (solo números y único), nombre, y correo electrónico.

Si el usuario es un estudiante, se pedirá un carnet (solo números). Si es un instructor, se pedirá el departamento.

El sistema valida que el correo tenga un formato válido y que los IDs y carnets sean numéricos.

2. Crear Curso
Crea un curso nuevo y lo asocia a un instructor.

Debes ingresar un código y un nombre para el curso, y el ID del instructor ya registrado.

3. Inscribir Estudiante en Curso
Asocia a un estudiante con un curso existente.

Se necesita el código del curso y el ID del estudiante que se desea inscribir.

4. Crear Evaluación
Añade una evaluación (examen o tarea) a un curso, con un valor de ponderación.

Se solicita el código del curso, el tipo de evaluación (examen/tarea), un ID, un título y la ponderación (ej. 0.25 para 25% del total del curso).

5. Registrar Calificación
Permite asignar una nota a un estudiante para una evaluación.

Ingresa el código del curso, el ID de la evaluación, el ID del estudiante y la nota (un número entre 0 y 100).

Generación de Reportes
La opción 8 te lleva a un submenú para generar dos tipos de reportes:

A. Reporte de Bajo Rendimiento: Muestra a los estudiantes cuyo promedio final en el curso es menor a 65.

B. Reporte General de Estudiantes: Muestra a todos los estudiantes de todos los cursos, junto con su promedio final y un desglose detallado de las notas obtenidas en cada evaluación. Este desglose te permite ver si la nota en una tarea o examen fue baja o si no se entregó.

Salir
Selecciona la opción 0 para terminar el programa.