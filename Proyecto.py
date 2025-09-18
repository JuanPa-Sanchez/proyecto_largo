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