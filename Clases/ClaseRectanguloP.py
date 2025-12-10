from os import system
from math import fabs
from ClasePunto2D import *

class RectanguloP:
    def __init__(self, P1 = Punto2D(), P2 = Punto2D()):
        self.__P1 = P1
        self.__P2 = P2
        self.verificaTuEstado()
    
    def __del__(self) -> None:
        pass

    @property
    def P1(self):
        return self.__P1

    @P1.setter
    def P1(self, P1):
        self.__P1 = P1
        self.verificaTuEstado()
    
    @property
    def P2(self):
        return self.__P2

    @P2.setter
    def P2(self, P2):
        self.__P2 = P2
        self.verificaTuEstado()
    
    def __str__(self) -> str:
        datos = f'P1{self.__P1}\n'
        datos += f'P2{self.__P2}\n'
        datos += f'Base: {self.dameTuBase()}\n'
        datos += f'Altura: {self.dameTuAltura()}\n'
        datos += f'Área: {self.dameTuArea()}\n'
        datos += f'Perímetro: {self.dameTuPerimetro()}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        print('Dame mi P1')
        self.__P1.pideleAlUsuarioTuEstado()
        print('Dame mi P2')
        self.__P2.pideleAlUsuarioTuEstado()
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, P1, P2):
        self.__P1 = P1
        self.__P2 = P2
        self.verificaTuEstado()

    def dameTuBase(self):
        return fabs(self.__P1.x - self.__P2.x)

    def dameTuAltura(self):
        return fabs(self.__P1.y - self.__P2.y)

    def dameTuArea(self):
        return self.dameTuBase() * self.dameTuAltura()

    def dameTuPerimetro(self):
        return 2*self.dameTuBase() + 2*self.dameTuAltura()

    def verificaTuEstado(self):
        if not isinstance(self.__P1, Punto2D):
            self.__P1 = Punto2D()

        if not isinstance(self.__P2, Punto2D):
            self.__P2 = Punto2D()

        if self.__P1.x == self.__P2.x or self.__P1.y == self.__P2.y:
            self.__P1.x = 0.0
            self.__P1.y = 0.0
            self.__P2.x = 0.0
            self.__P2.y = 0.0
            
if __name__ == '__main__':
    system('cls')

    R1 = RectanguloP()
    print(f'R1\n{R1}')

    A = Punto2D(1,1)
    B = Punto2D(4,5)
    R2 = RectanguloP(A, B)
    print(f'R2')
    R2.muestraTuEstado()

    print(f'R1')
    R1.pideleAlUsuarioTuEstado()
    print(f'R1\n{R1}')

    print('Se intenta construir un objeto con dos cadenas:')
    R3 = RectanguloP('unaCadena', 'otraCadena')
    print(f'R3\n{R3}')

    print('Se intenta asignar una cadena al P1 de un objeto:')
    R3.P1 = '(1.2, 3.4)'
    print(f'R3\n{R3}')
    print('Se intenta asignar una cadena al P2 de un objeto:')
    R3.P2 = '(5.6, 7.8)'
    print(f'R3\n{R3}')
