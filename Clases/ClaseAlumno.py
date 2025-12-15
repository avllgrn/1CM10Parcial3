from ClasePersona import *
from os import system

class Alumno (Persona):
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=1.65, FechaNacimiento=Evento(), semestre=1, promedio=0.0, Carrera='ICE'):
            super().__init__( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self._semestre = semestre
            self._promedio = promedio
            self._Carrera = Carrera
            self.verificaAlumno()

    def __del__(self):
        pass

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, semestre):
        self._semestre = semestre
        self.verificaAlumno()

    @property
    def promedio(self):
        return self._promedio

    @promedio.setter
    def promedio(self, promedio):
        self._promedio = promedio
        self.verificaAlumno()

    @property
    def Carrera(self):
        return self._Carrera

    @Carrera.setter
    def Carrera(self, Carrera):
        self._Carrera = Carrera
        self.verificaAlumno()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Semestre: {self._semestre}\n'
        datos += f'Promedio: {self._promedio}\n'
        datos += f'Carrera: {self._Carrera}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self._semestre = input('Dame mi semestre ')
        self._promedio = input('Dame mi promedio ')
        self._Carrera = input('Dame mi carrera ')
        self.verificaAlumno()

    def muestraTuEstado(self):
        print(self)

    def modificaAlumno(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, semestre, promedio, Carrera):
            super().__init__( Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento )
            self._semestre = semestre
            self._promedio = promedio
            self._Carrera = Carrera
            self.verificaAlumno()

    def verificaAlumno(self):
        if not isinstance(self._Carrera,str):
            self._Carrera = 'ICE'

        try:
            self._semestre = int(self._semestre)
        except:
            self._semestre = 1
        try:
            self._promedio = float(self._promedio)
        except:
            self._promedio = 0.0

        if self._semestre < 1:
            self._semestre = 1

        if self._promedio < 0.0:
            self._promedio = 0.0

if __name__ == '__main__':
    system('cls')

    A1 = Alumno()
    print(f'A1')
    A1.muestraTuEstado()

    FN = Evento( Fecha(1,2,2003),Hora(4,5,6) )
    A2 = Alumno('Juan','Perez','Lopez','m',1.82,FN,2,7.6,'ICA')
    print(f'A2\n{A2}')

    A3 = Alumno(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'cuarto', 'ocho punto cinco', 56.78)
    print(f'A5\n{A3}')

    print(f'A1\n{A1}')
    print(f'A1')
    A1.pideleAlUsuarioTuEstado()
    print(f'\nA1\n{A1}')    

    print('Se intenta A1.modificaAlumno(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'cuarto\', \'ocho punto cinco\', 56.78)')
    A1.modificaAlumno(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'cuarto', 'ocho punto cinco', 56.78)
    print(f'\nA1\n{A1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    A1.Nombre = 1
    A1.Paterno = 2.3
    A1.Materno = 4
    A1.Genero = 5.6
    A1.estatura = 'uno ochenta'
    A1.FechaNacimiento = 789
    A1.semestre = 'cuarto'
    A1.promedio = 'ocho punto cinco'
    A1.Carrera = 56.78
    print(f'\nA1\n{A1}')
