from ClaseEmpleado import *
from os import system

class Profesor (Empleado):
    def __init__(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroGrupos=0,carga=0.0,Academia='Física'):
            super().__init__(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self._numeroGrupos = numeroGrupos
            self._carga = carga
            self._Academia = Academia
            self.verificaProfesor()

    def __del__(self):
        pass

    @property
    def numeroGrupos(self):
        return self._numeroGrupos

    @numeroGrupos.setter
    def numeroGrupos(self, numeroGrupos):
        self._numeroGrupos = numeroGrupos
        self.verificaProfesor()

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def carga(self, carga):
        self._carga = carga
        self.verificaProfesor()

    @property
    def Academia(self):
        return self._Academia

    @Academia.setter
    def Academia(self, Academia):
        self._Academia = Academia
        self.verificaProfesor()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de grupos: {self._numeroGrupos}\n'
        datos += f'Carga: {self._carga}\n'
        datos += f'Academia: {self._Academia}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self._numeroGrupos = input('Dame mi número de grupos ')
        self._carga = input('Dame mi carga ')
        self._Academia = input('Dame mi academia ')
        self.verificaProfesor()

    def muestraTuProfstado(self):
        print(self)

    def modificaProfesor(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroGrupos=0,carga=0.0,Academia='Física'):
            super().modificaEmpleado(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self._numeroGrupos = numeroGrupos
            self._carga = carga
            self._Academia = Academia
            self.verificaProfesor()

    def verificaProfesor(self):
        if not isinstance(self._Academia,str):
            self._Academia = 'Computación'

        try:
            self._numeroGrupos = int(self._numeroGrupos)
        except:
            self._numeroGrupos = 0
        try:
            self._carga = float(self._carga)
        except:
            self._carga = 0.0

        if self._numeroGrupos < 0:
            self._numeroGrupos = 0

        if self._carga < 0.0 and self._carga > 24.0:
            self._carga = 0.0

if __name__ == '__main__':
    system('cls')

    Prof1 = Profesor()
    print(f'Prof1')
    Prof1.muestraTuProfstado()

    FN = Evento(Fecha(1,2,2003),Hora(4,5,6))
    Prof2 = Profesor('Juan','Perez','Lopez','m',1.82,FN,2,4967.6,'Docente', 1, 1.5, 'Humanidades')
    print(f'Prof2\n{Prof2}')

    Prof3 = Profesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'siete', 'Diez punto cinco', 3.1416)
    print(f'Prof3\n{Prof3}')

    print(f'Prof1\n{Prof1}')
    print(f'Prof1')
    Prof1.pideleAlUsuarioTuEstado()
    print(f'\nProf1\n{Prof1}')    

    print('Se intenta P1.modificaProfesor()')
    Prof1.modificaProfesor()
    print(f'\nProf1\n{Prof1}')

    print('Se intenta Prof1.modificaProfesor(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'mil\', \'un millón\', 56.78, \'dos\', \'tres\', 2.71)')
    Prof1.modificaProfesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'dos', 'tres', 2.71)
    print(f'\nProf1\n{Prof1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    Prof1.Nombre = 1
    Prof1.Paterno = 2.3
    Prof1.Materno = 4
    Prof1.Genero = 5.6
    Prof1.estatura = 'uno ochenta'
    Prof1.FechaNacimiento = 789
    Prof1.numeroEmpleado = 'uno dos tres cuatro'
    Prof1.sueldo = 'siete mil cuatrocientos sesenta y siete punto nueve'
    Prof1.Puesto = 456.654
    Prof1.numeroGrupos = 'cinco'
    Prof1.carga = 'siete punto cinco'
    Prof1.Academia = 9.81
    print(f'\nProf1\n{Prof1}')
