from ClaseEvento import *
from os import system

class Persona:
    def __init__(self, Nombre='', Paterno='', Materno='', Genero='', estatura=0.24, FechaNacimiento=Evento()):
        self._Nombre = Nombre
        self._Paterno = Paterno
        self._Materno = Materno
        self._Genero = Genero
        self._estatura = estatura
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __del__(self):
        pass

    @property
    def Nombre(self):
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre
        self.verificaPersona()

    @property
    def Paterno(self):
        return self._Paterno
    
    @Paterno.setter
    def Paterno(self, Paterno):
        self._Paterno = Paterno
        self.verificaPersona()

    @property
    def Materno(self):
        return self._Materno
    
    @Materno.setter
    def Materno(self, Materno):
        self._Materno = Materno
        self.verificaPersona()

    @property
    def Genero(self):
        return self._Genero
    
    @Genero.setter
    def Genero(self, Genero):
        self._Genero = Genero
        self.verificaPersona()

    @property
    def estatura(self):
        return self._estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura
        self.verificaPersona()

    @property
    def FechaNacimiento(self):
        return self._FechaNacimiento
    
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento):
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def __str__(self) -> str:
        datos = f'Nombre: {self._Nombre}\n'
        datos += f'Paterno: {self._Paterno}\n'
        datos += f'Materno: {self._Materno}\n'
        datos += f'Genero: {self._Genero}\n'
        datos += f'estatura: {self._estatura}\n'
        datos += f'FechaNacimiento: {self._FechaNacimiento}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        self._Nombre = input('Dame mi Nombre ')
        self._Paterno = input('Dame mi Paterno ')
        self._Materno = input('Dame mi Materno ')
        self._Genero = input('Dame mi Genero ')
        self._estatura = input('Dame mi estatura ')
        print('Dame mi Fecha de Nacimiento')
        self._FechaNacimiento.pideleAlUsuarioTuEstado()
        self.verificaPersona()
    
    def muestraTuEstado(self):
        print(self)

    def modificaPersona(self, Nombre, Paterno, Materno, Genero, estatura, FechaNacimiento):
        self._Nombre = Nombre
        self._Paterno = Paterno
        self._Materno = Materno
        self._Genero = Genero
        self._estatura = estatura
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

    def verificaPersona(self):
        if not isinstance(self._Nombre,str):
            self._Nombre = ''

        if not isinstance(self._Paterno,str):
            self._Paterno = ''

        if not isinstance(self._Materno,str):
            self._Materno = ''

        if not isinstance(self._Genero,str):
            self._Genero = ''

        try:
            self._estatura = float(self._estatura)
        except:
            self._estatura = 0.24

        if self._estatura<0.24 or self._estatura>2.72:
            self._estatura = 0.24

        if not isinstance(self._FechaNacimiento, Evento):
            self._FechaNacimiento = Evento()


if __name__ == '__main__':
    system('cls')

    P1 = Persona()
    print(f'P1\n{P1}')

    E = Evento( Fecha(2,12,2024), Hora(7,10,32) )
    P2 = Persona('Juan','Perez','Lopez','Masculino',1.65, E)
    print(f'P2')
    P2.muestraTuEstado()

    print(f'P1\n{P1}')
    P1.pideleAlUsuarioTuEstado()
    print(f'\nP1\n{P1}')

    print('Se realiza P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)')
    P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)
    print(f'P2\n{P2}')
    print(f'P1\n{P1}')

    print('Se intenta Persona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P3 = Persona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P3\n{P3}')

    print('Se intenta P3.modificaPersona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P3.modificaPersona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P3\n{P3}')

    print('Se intenta asignar valores incorrectos a los atributos de P3')
    P3.Nombre = 12.3
    P3.Paterno = 45.6
    P3.Materno = 78.9
    P3.Genero = 8.76
    P3.estatura = 'uno sesenta'
    P3.FechaNacimiento = 123
    print(f'P3\n{P3}')
