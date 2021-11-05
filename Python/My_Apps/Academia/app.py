
class Alumno:

    #atributos
    #constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #sobre-escritura
    def __str__(self):
        return "Alumno de clase"


def cargar_alumnos(num):
    als = []
    for i in range(num):
        als.append(Alumno())
    return als

def mostrar_alumnos(l_alumnos):
    for al in l_alumnos:
        print(al)

if __name__ == "__main__":
    alumnos = None
    profesores = list()
    examenes = list()

    alumnos = cargar_alumnos()
    mostrar_alumnos(alumnos)
