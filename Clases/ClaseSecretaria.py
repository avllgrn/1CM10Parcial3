from ClaseEmpleado import *
from os import system

class Secretaria (Empleado):
    def __init__(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroJefes=0,golpesMinuto=250.0,Taquigrafia='Pitman'):
            super().__init__(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self._numeroJefes = numeroJefes
            self._golpesMinuto = golpesMinuto
            self._Taquigrafia = Taquigrafia
            self.verificaSecretaria()

    def __del__(self):
        pass

    @property
    def numeroJefes(self):
        return self._numeroJefes

    @numeroJefes.setter
    def numeroJefes(self, numeroJefes):
        self._numeroJefes = numeroJefes
        self.verificaSecretaria()

    @property
    def golpesMinuto(self):
        return self._golpesMinuto

    @golpesMinuto.setter
    def golpesMinuto(self, golpesMinuto):
        self._golpesMinuto = golpesMinuto
        self.verificaSecretaria()

    @property
    def Taquigrafia(self):
        return self._Taquigrafia

    @Taquigrafia.setter
    def Taquigrafia(self, Taquigrafia):
        self._Taquigrafia = Taquigrafia
        self.verificaSecretaria()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de grupos: {self._numeroJefes}\n'
        datos += f'Golpes por minuto: {self._golpesMinuto}\n'
        datos += f'Taquigrafía: {self._Taquigrafia}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self._numeroJefes = input('Dame mi número de jefes ')
        self._golpesMinuto = input('Dame mi golpes por minuto ')
        self._Taquigrafia = input('Dame mi taquigrafía ')
        self.verificaSecretaria()

    def muestraTuSecrestado(self):
        print(self)

    def modificaSecretaria(self, Nombre='',Paterno='',Materno='',Genero='',estatura=1.65,FechaNacimiento=Evento(),numeroEmpleado=0,sueldo=7467.9,Puesto='Trabajador',numeroJefes=0,golpesMinuto=0.0,Taquigrafia='Física'):
            super().modificaEmpleado(  Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento, numeroEmpleado, sueldo, Puesto )
            self._numeroJefes = numeroJefes
            self._golpesMinuto = golpesMinuto
            self._Taquigrafia = Taquigrafia
            self.verificaSecretaria()

    def verificaSecretaria(self):
        if not isinstance(self._Taquigrafia,str):
            self._Taquigrafia = 'Pitman'

        try:
            self._numeroJefes = int(self._numeroJefes)
        except:
            self._numeroJefes = 0
        try:
            self._golpesMinuto = float(self._golpesMinuto)
        except:
            self._golpesMinuto = 0.0

        if self._numeroJefes < 0:
            self._numeroJefes = 0

        if self._golpesMinuto < 0.0 and self._golpesMinuto > 300.0:
            self._golpesMinuto = 0.0

if __name__ == '__main__':
    system('cls')

    Secre1 = Secretaria()
    print(f'Secre1')
    Secre1.muestraTuSecrestado()

    FN = Evento(Fecha(1,2,2003),Hora(4,5,6))
    Secre2 = Secretaria('Juan','Perez','Lopez','m',1.82,FN,2,4967.6,'Secretaria Ejecutiva', 1, 234.5, 'Garriga')
    print(f'Secre2\n{Secre2}')

    Secre3 = Secretaria(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'siete', 'Diez punto cinco', 3.1416)
    print(f'Secre3\n{Secre3}')

    print(f'Secre1\n{Secre1}')
    print(f'Secre1')
    Secre1.pideleAlUsuarioTuEstado()
    print(f'\nSecre1\n{Secre1}')    

    print('Se intenta P1.modificaSecretaria()')
    Secre1.modificaSecretaria()
    print(f'\nSecre1\n{Secre1}')

    print('Se intenta Secre1.modificaSecretaria(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'mil\', \'un millón\', 56.78, \'dos\', \'tres\', 2.71)')
    Secre1.modificaSecretaria(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'dos', 'tres', 2.71)
    print(f'\nSecre1\n{Secre1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    Secre1.Nombre = 1
    Secre1.Paterno = 2.3
    Secre1.Materno = 4
    Secre1.Genero = 5.6
    Secre1.estatura = 'uno ochenta'
    Secre1.FechaNacimiento = 789
    Secre1.numeroEmpleado = 'uno dos tres cuatro'
    Secre1.sueldo = 'siete mil cuatrocientos sesenta y siete punto nueve'
    Secre1.Puesto = 456.654
    Secre1.numeroJefes = 'cinco'
    Secre1.golpesMinuto = 'siete punto cinco'
    Secre1.Taquigrafia = 9.81
    print(f'\nSecre1\n{Secre1}')
