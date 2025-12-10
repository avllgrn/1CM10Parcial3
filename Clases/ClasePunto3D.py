from os import system
from ClasePunto2D import *

class Punto3D (Punto2D):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        try:
            self.z = float(z)
        except:
            self.z = 0.0

    def __del__(self):
        pass

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        try:
            self.z = float(input('Dame mi z '))
        except:
            self.z = 0.0

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y, z):
        super().modificaTuEstado(x, y)
        try:
            self.z = float(z)
        except:
            self.z = 0.0

if __name__ == '__main__':
    system('cls')

    P1 = Punto3D()
    P1.muestraTuEstado()
    print(P1)
    print()

    P2 = Punto3D(1, 2, 3)
    P2.muestraTuEstado()
    print(P2)
    print()

    P3 = Punto3D('cuatro', 'cinco', 'seis')
    P3.muestraTuEstado()
    print(P3)
    print()

    P3.modificaTuEstado('siete', 'ocho', 'nueve')
    P3.muestraTuEstado()
    print(P3)
    print()
