#La rectoria necesita un diagrama de clases que tenga las diferente funcionalidades.
#Alumnos, los alumnos tiene nombre apellido legajo , curso , notas y materias que cursa
#se quiere saber el promedio de cada materia
#Por otro lado la materia que esta compuesta por un nombre y los alumnos que la componen
#se quiere saber cual es el promedio del curso

class Alumnos():
 def __init__ (self, nombre, apellido, legajo, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.curso = curso
        self.alumnoMateriaNota = {}
        self.Aux = {}

 def añadirNotaMateria(self, materia, nota):
  if materia in self.alumnoMateriaNota and nota in self.alumnoMateriaNota :
       print("No se puede añadir")
  else:
   self.alumnoMateriaNota[materia] = nota
   self.Aux[materia.nombre] = nota
 def Mostarnotas(self):
       print(f"Las notas de {self.nombre} son {self.Aux}")

 def Devolvernotas(self, materia):
       return self.alumnoMateriaNota[materia]

class Materias():
 def __init__ (self, nombre, curso):
        self.nombre = nombre
        self.alumnosEn = []
        self.Aux2 = []
        self.curso = curso

 def agregarAlumno(self, alumnos):
       self.alumnosEn.append(alumnos)
       self.Aux2.append(alumnos.nombre)

 def MostaralumnosEn(self):
        print(f"Los alumnos que estan en la materia {self.nombre} son {self.Aux2}") 
 
 def materiaPromedio(self):
        promedioCurso = 0
        promedioMateria = 0
        for alumno in self.alumnosEn:
              promedioMateria += alumno.Devolvernotas(self)
              promedioCurso = promedioMateria/ len(self.alumnosEn)
        print(f"El promedio del curso en {self.nombre} es {promedioCurso}")
        return promedioCurso

class Curso():
 def __init__ (self,curso):
        self.curso = curso
        self.alumnos = []
        self.materiasEn = []
        self.Aux3 = []

 def agregarAlumnos(self, alumnos):
    self.alumnos.append(alumnos.nombre)

 def Mostaralumnos(self):
       print(f"Los Alumnos de {self.curso} son {self.alumnos}")  
 
 def AgregarMaterias(self, materia):
    self.materiasEn.append(materia)
    self.Aux3.append(materia.nombre)

 def MostaraMaterias(self):
       print(f"Las Materias de {self.curso} son {self.Aux3}")  
 
 def promedioGeneral(self):
        promedioMaterias = 0
        promedioGeneral = 0
        promedioMaterias += Materias.materiaPromedio(Matematica)
        promedioMaterias += Materias.materiaPromedio(Ingles)
        promedioMaterias += Materias.materiaPromedio(Historia)
        promedioGeneral = promedioMaterias/ len(self.materiasEn)
        print(f"El promedio general del curso es {promedioGeneral}")

Franco = Alumnos("Franco", "Masucco", 1,"Sexto")
Jose = Alumnos("Jose", "Mantas", 2,"Sexto")
Erick = Alumnos("erick", "Quispe", 3,"Sexto")

sexto = Curso("Sexto")
Matematica = Materias("Matematica",sexto)
Ingles = Materias("Ingles",sexto)
Historia = Materias("Historia",sexto)

sexto.AgregarMaterias(Matematica)
sexto.AgregarMaterias(Historia)
sexto.AgregarMaterias(Ingles)

sexto.MostaraMaterias()

Matematica.agregarAlumno(Franco)
Matematica.agregarAlumno(Jose)
Matematica.agregarAlumno(Erick)
Ingles.agregarAlumno(Franco)
Ingles.agregarAlumno(Jose)
Ingles.agregarAlumno(Erick)
Historia.agregarAlumno(Franco)
Historia.agregarAlumno(Jose)
Historia.agregarAlumno(Erick)

sexto.agregarAlumnos(Franco)
sexto.agregarAlumnos(Jose)
sexto.agregarAlumnos(Erick)

Franco.añadirNotaMateria(Matematica,8)
Franco.añadirNotaMateria(Ingles,7)
Franco.añadirNotaMateria(Historia,9)
Jose.añadirNotaMateria(Matematica,9)
Jose.añadirNotaMateria(Ingles,7)
Jose.añadirNotaMateria(Historia,9)
Erick.añadirNotaMateria(Matematica,7)
Erick.añadirNotaMateria(Ingles,9)
Erick.añadirNotaMateria(Historia,9)

Franco.Mostarnotas()
Jose.Mostarnotas()
Erick.Mostarnotas()

sexto.Mostaralumnos()

Matematica.MostaralumnosEn()
Ingles.MostaralumnosEn()
Historia.MostaralumnosEn()

Franco.Devolvernotas(Matematica)
Franco.Devolvernotas(Ingles)
Franco.Devolvernotas(Historia)
Jose.Devolvernotas(Matematica)
Jose.Devolvernotas(Ingles)
Jose.Devolvernotas(Historia)
Erick.Devolvernotas(Matematica)
Erick.Devolvernotas(Ingles)
Erick.Devolvernotas(Historia)

Matematica.materiaPromedio()
Ingles.materiaPromedio()
Historia.materiaPromedio()

sexto.promedioGeneral()
