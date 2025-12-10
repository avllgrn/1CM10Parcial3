from os import system
from math import pi
from ClasePunto2D import *

class CirculoP:
    def __init__(self, C = Punto2D(), P = Punto2D()):
        self.__C = C
        self.__P = P
        self.verificaTuEstado()

    def __del__(self) -> None:
        pass

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, C):
        self.__C = C
        self.verificaTuEstado()
    
    @property
    def P(self):
        return self.__P

    @P.setter
    def P(self, P):
        self.__P = P
        self.verificaTuEstado()
    
    def __str__(self) -> str:
        datos = f'C{self.__C}\n'
        datos += f'P{self.__P}\n'
        datos += f'Radio: {self.dameTuRadio()}\n'
        datos += f'Diametro: {self.dameTuDiametro()}\n'
        datos += f'Área: {self.dameTuArea()}\n'
        datos += f'Perímetro: {self.dameTuPerimetro()}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        print('Dame mi C')
        self.__C.pideleAlUsuarioTuEstado()
        print('Dame mi P')
        self.__P.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, C, P):
        self.__C = C
        self.__P = P
        self.verificaTuEstado()

    def dameTuRadio(self):
        return distanciaEntre(self.__C, self.__P)    

    def dameTuDiametro(self):
        return 2*self.dameTuRadio()

    def dameTuArea(self):
        return pi*self.dameTuRadio()**2

    def dameTuPerimetro(self):
        return 2*pi*self.dameTuRadio()

    def verificaTuEstado(self):
        if not isinstance(self.__C, Punto2D):
            self.__C = Punto2D()

        if not isinstance(self.__P, Punto2D):
            self.__P = Punto2D()

if __name__ == '__main__':
    system('cls')

    Q1 = CirculoP()
    print(f'Q1\n{Q1}')

    A = Punto2D(1,1)
    B = Punto2D(2,2)
    Q2 = CirculoP(A, B)
    print(f'Q2')
    Q2.muestraTuEstado()


    print(f'Q1')
    Q1.pideleAlUsuarioTuEstado()
    print(f'Q1\n{Q1}')

    print('Se intenta construir un objeto con dos cadenas:')
    Q3 = CirculoP('unaCadena', 'otraCadena')
    print(f'Q3\n{Q3}')

    print('Se intenta asignar una cadena al C de un objeto:')
    Q3.C = '(1.2, 3.4)'
    print(f'Q4\n{Q3}')
    print('Se intenta asignar una cadena al P de un objeto:')
    Q3.P = '(5.6, 7.8)'
    print(f'Q4\n{Q3}')
