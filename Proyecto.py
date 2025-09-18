#clase base usuario
class Usuario:
    def __init__(self, id_usuario, nombre, correo, **kwargs):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        #Usa setattr para asignar cualquier otro atributo pasado en kwargs
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

    def mostrar_info(self):
        return f"{self.id_usuario} - {self.nombre} - {self.correo}"

#clase estudiante hereda de usuario
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, correo, **kwargs):
        #Extrae 'carnet' de kwargs antes de pasarlo a la clase base
        self.carnet = kwargs.pop('carnet', None)
        super().__init__(id_usuario, nombre, correo, **kwargs)

    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Carnet: {self.carnet}"
    
    #clase instructor hereda de usuario
class Instructor(Usuario):
    def __init__(self, id_usuario, nombre, correo, **kwargs):
        #Extrae 'departamento' de kwargs antes de pasarlo a la clase base
        self.departamento = kwargs.pop('departamento', None)
        super().__init__(id_usuario, nombre, correo, **kwargs)

    def mostrar_info(self):
        return f"Instructor: {self.nombre}, Depto: {self.departamento}"
    
    #clase base evaluacion
class Evaluacion:
    def __init__(self, id_eval, titulo, ponderacion):
        self.id_eval = id_eval
        self.titulo = titulo
        self.ponderacion = ponderacion
        self.calificaciones = {}

    def registrar_calificacion(self, id_estudiante, nota):
        try:
            if not 0 <= nota <= 100:
                raise ValueError("La nota debe estar en el rango de 0 a 100.")
            self.calificaciones[id_estudiante] = nota
        except ValueError as e:
            print(f"Error: {e}")

    def mostrar_calificaciones(self):
        return self.calificaciones

    def calcular_nota_ponderada(self, id_estudiante):
        # Calcula la nota del estudiante ponderada por la ponderacion de la evaluación.
        return self.calificaciones.get(id_estudiante, 0) * self.ponderacion
    
    #clase examen hereda de evaluacion
class Examen(Evaluacion):
    def __init__(self, id_eval, titulo, ponderacion):
        super().__init__(id_eval, titulo, ponderacion)

#clase tarea hereda de evaluacion
class Tarea(Evaluacion):
    def __init__(self, id_eval, titulo, ponderacion):
        super().__init__(id_eval, titulo, ponderacion)

#clase curso
class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} inscrito en el curso {self.nombre}.")
        else:
            print(f"Este estudiante ya está inscrito en el curso {self.nombre}.")

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación '{evaluacion.titulo}' agregada al curso {self.nombre}.")

    def mostrar_info(self):
        return f"{self.codigo} - {self.nombre} - Instructor: {self.instructor.nombre}"
    
    def calcular_promedio_final(self, id_estudiante):
        #Calcula el promedio final de un estudiante en el curso.
        total_promedio_ponderado = 0
        total_ponderacion = 0
        for evaluacion in self.evaluaciones:
            total_promedio_ponderado += evaluacion.calcular_nota_ponderada(id_estudiante)
            total_ponderacion += evaluacion.ponderacion
        
        return (total_promedio_ponderado / total_ponderacion) if total_ponderacion > 0 else 0