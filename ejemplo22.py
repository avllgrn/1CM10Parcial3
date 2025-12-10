from os import system
from Clases.ClasePunto2D import *

if __name__ == '__main__':
    system('cls')

    P1 = Punto2D(1, 2)
    P2 = Punto2D(3, 4)
    P3 = Punto2D(5, 6)
    P4 = Punto2D(7, 8)
    P5 = Punto2D(9, 10)

    P6 = add(add(add(add(P1, P2), P3), P4), P5)
    print(P6)

    P7 = P1.add(P2).add(P3).add(P4).add(P5)
    print(P7)

    P8 = P1.__add__(P2).__add__(P3).__add__(P4).__add__(P5)
    print(P8)

    P9 = P1+P2+P3+P4+P5
    print(P9)
