from os import system
from Clases.ClaseRectangulo import *

if __name__ == '__main__':
    system('cls')

    R1 = Rectangulo()
    print(f'R1:\n{R1}')

    R2 = Rectangulo(1, 2)
    print(f'R2:\n{R2}')
    R2.pideleAlUsuarioTuEstado()
    print(f'R2:\n{R2}')

    R3 = Rectangulo(4, 5)
    print(f'R3:\n{R3}')
    R3.base = 6
    print(f'R3:\n{R3}')
    R3.altura = 7
    print(f'R3:\n{R3}')

    R3.base = -6
    print(f'R3:\n{R3}')
    R3.altura = -7
    print(f'R3:\n{R3}')

    R4 = Rectangulo(-6, -7)
    print(f'R4:\n{R4}')
    R4.modificaTuEstado(8, 9)
    print(f'R4:\n{R4}')

    R4.modificaTuEstado(-8, 9)
    print(f'R4:\n{R4}')

    R4.modificaTuEstado(8, -9)
    print(f'R4:\n{R4}')
