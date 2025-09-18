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
        return f"Estudiante: {self.nombre}, Carnet: {self.carnet}"
    
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
    
#clase plataforma general
class Plataforma:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}


    def registrar_usuario(self, tipo, id_usuario, nombre, correo, **kwargs):
        #Validación de formato de correo
        if "@" not in correo or "." not in correo:
            print("Error: El correo electrónico no tiene un formato válido.")
            return

        #Validación de que el ID de usuario sea numérico (usando try-except)
        try:
            int(id_usuario)
        except ValueError:
            print("Error: El ID de usuario debe contener solo números.")
            return

        #Validación de ID único
        if id_usuario in self.usuarios:
            print(f"Error: El ID de usuario '{id_usuario}' ya está en uso.")
            return

        #Creación del objeto según el tipo de usuario
        if tipo == "estudiante":
            carnet = kwargs.get('carnet')
            #Validación de carnet numérico
            try:
                int(carnet)
            except ValueError:
                print("Error: El carnet debe contener solo números.")
                return
            except TypeError:
                print("Error: El carnet no contiene nigun numero")
                return
            u = Estudiante(id_usuario, nombre, correo, **kwargs)
        elif tipo == "instructor":
            u = Instructor(id_usuario, nombre, correo, **kwargs)
        else:
            print("Tipo de usuario inválido.")
            return
        self.usuarios[id_usuario] = u
        print(f"Usuario {nombre} registrado exitosamente como {tipo}.")

    def crear_curso(self, codigo, nombre, id_instructor):
        if id_instructor not in self.usuarios or not isinstance(self.usuarios[id_instructor], Instructor):
            print("Instructor no encontrado o tipo de usuario inválido.")
            return
        
        instructor = self.usuarios[id_instructor]
        c = Curso(codigo, nombre, instructor)
        self.cursos[codigo] = c
        print(f"Curso {nombre} creado con éxito.")

    def inscribir(self, codigo_curso, id_estudiante):
        try:
            curso = self.cursos[codigo_curso]
            estudiante = self.usuarios[id_estudiante]
            if isinstance(estudiante, Estudiante):
                curso.inscribir_estudiante(estudiante)
            else:
                print("Solo se pueden inscribir estudiantes.")
        except KeyError:
            print("Curso o estudiante no encontrado.")

    def crear_evaluacion(self, codigo_curso, tipo, id_eval, titulo, ponderacion):
        try:
            curso = self.cursos[codigo_curso]
            if tipo == "examen":
                ev = Examen(id_eval, titulo, ponderacion)
            elif tipo == "tarea":
                ev = Tarea(id_eval, titulo, ponderacion)
            else:
                print("Tipo de evaluación no válido.")
                return
            curso.agregar_evaluacion(ev)
        except KeyError:
            print("Curso no encontrado.")

    def registrar_calificacion(self, codigo_curso, id_eval, id_estudiante, nota):
        try:
            curso = self.cursos[codigo_curso]
            evaluacion = next(ev for ev in curso.evaluaciones if ev.id_eval == id_eval)
            evaluacion.registrar_calificacion(id_estudiante, nota)
            print(f"Nota de {nota} registrada para el estudiante {id_estudiante} en la evaluación '{evaluacion.titulo}'.")
        except StopIteration:
            print("Evaluación no encontrada.")
        except KeyError:
            print("Curso o estudiante no encontrado.")

    def mostrar_cursos(self):
        print("--- Lista de Cursos ---")
        for curso in self.cursos.values():
            print(curso.mostrar_info())
        print("-----------------------")

    def mostrar_estudiantes(self, codigo_curso):
        try:
            curso = self.cursos[codigo_curso]
            print(f"--- Estudiantes en el curso '{curso.nombre}' ---")
            if not curso.estudiantes:
                print("No hay estudiantes inscritos.")
            for est in curso.estudiantes:
                print(f"- {est.mostrar_info()}")
            print("---------------------------------------------")
        except KeyError:
            print("Curso no encontrado.")
    #Reporte 1: Reporte de bajo rendimiento
    def generar_reporte_promedio_bajo(self):
        #genera un reporte de estudiantes con promedio bajo
        minimo = 65.0
        print(f"--- Reporte de Estudiantes con Promedio < {minimo} ---")
        encontrados = False
        for curso in self.cursos.values():
            print(f"Curso: {curso.nombre}")
            for estudiante in curso.estudiantes:
                promedio = curso.calcular_promedio_final(estudiante.id_usuario)
                if promedio < minimo:
                    encontrados = True
                    print(f"- {estudiante.mostrar_info()} | Promedio Final: {promedio:.2f}")
                    print("    Desglose de notas:")
                    for evaluacion in curso.evaluaciones:
                        nota_obtenida = evaluacion.calificaciones.get(estudiante.id_usuario, 0)
                        estado = "Entregada" if nota_obtenida > 0 else "No entregada"
                        print(f"    - {evaluacion.titulo} ({evaluacion.ponderacion*100:.0f}%): Nota: {nota_obtenida:.2f} ({estado})")
    
        if not encontrados:
            print("No se encontraron estudiantes con promedio bajo.")
        print("-------------------------------------------------------")

    #Reporte 2: Reporte general
    def generar_reporte_general(self):
        #Genera un reporte con el promedio de todos los estudiantes
        print("--- Reporte General de Estudiantes ---")
        encontrados = False
        for curso in self.cursos.values():
            print(f"Curso: {curso.nombre}")
            for estudiante in curso.estudiantes:
                encontrados = True
                #Llamamos a la función que calcula el promedio final del curso
                promedio_final = curso.calcular_promedio_final(estudiante.id_usuario)
                print(f"- {estudiante.mostrar_info()} | Promedio Final del Curso: {promedio_final:.2f}")
                print("    Desglose de notas:")
                for evaluacion in curso.evaluaciones:
                    nota_obtenida = evaluacion.calificaciones.get(estudiante.id_usuario, 0)
                    estado = "Entregada" if nota_obtenida > 0 else "No entregada"
                    print(f"    - {evaluacion.titulo} ({evaluacion.ponderacion*100:.0f}%): Nota: {nota_obtenida:.2f} ({estado})")

        if not encontrados:
            print("No hay estudiantes inscritos en ningún curso.")
        print("---------------------------------------")
