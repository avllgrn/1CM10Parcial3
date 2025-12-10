from os import system
from ClaseFecha import *
from ClaseHora import *

class Evento:
    def __init__(self, F = Fecha(), H = Hora()):
        self.__F = F
        self.__H = H
        self.verificaTuEstado()

    def __del__(self):
        pass

    @property
    def F(self):
        return self.__F
    
    @F.setter
    def F(self, F):
        self.__F = F
        self.verificaTuEstado()

    @property
    def H(self):
        return self.__H
    
    @H.setter
    def H(self, H):
        self.__H = H
        self.verificaTuEstado()

    def __str__(self) -> str:
        return f'{self.__F} {self.__H}'

    def pideleAlUsuarioTuEstado(self):
        print('Dame mi F ')
        self.__F.pideleAlUsuarioTuEstado()
        print('Dame mi H')
        self.__H.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, F, H):
        self.__F = F
        self.__H = H
        self.verificaTuEstado()

    def verificaTuEstado(self):
        if not isinstance(self.__F, Fecha):
            self.__F = Fecha()

        if not isinstance(self.__H, Hora):
            self.__H = Hora()


if __name__ == '__main__':
    system('cls')

    print('Se intenta construir una instancia de Evento con dos cadenas:')
    UnaFecha = 'Fecha(1, 2, 3)'
    UnaHora = 'Hora(4, 5, 6)'
    E1 = Evento(UnaFecha, UnaHora)
    print(f'E1 -> {E1}\n')

    print('Se intenta modificar una instancia de Evento con dos cadenas:')
    E1.modificaTuEstado(UnaFecha, UnaHora)
    print(f'E1 -> {E1}\n')

    print('Se intenta asignar cadenas a los atributos de una instancia de Evento:')
    E1.F = 'Fecha(1, 2, 3)'
    E1.H = 'Hora(4, 5, 6)'
    print(f'E1 -> {E1}\n')