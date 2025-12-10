from os import system
from Clases.ClasePunto2D import *

if __name__ == '__main__':
    system('cls')

    P1 = Punto2D()    
    P2 = Punto2D()    
    P3 = Punto2D()
    P4 = Punto2D()
    P5 = Punto2D()
    P6 = Punto2D()
    P7 = Punto2D()
    P8 = Punto2D()

    print('Para P1')
    P1.pideleAlUsuarioTuEstado()
    print('Para P2')
    P2.pideleAlUsuarioTuEstado()

    P3 = add(P1, P2)
    P4 = sub(P1, P2)
    P5 = P1.add(P2)
    P6 = P1.sub(P2)
    P7 = P1.__add__(P2)
    P8 = P1.__sub__(P2)
    P9 = P1+P2 # P1.__add__(P2)
    P10 = P1-P2 # P1.__sub__(P2)


    print(f'{P1} + {P2} = {P3}')
    print(f'{P1} - {P2} = {P4}')
    print()

    print(f'{P1} + {P2} = {P5}')
    print(f'{P1} - {P2} = {P6}')
    print()

    print(f'{P1} + {P2} = {P7}')
    print(f'{P1} - {P2} = {P8}')
    print()

    print(f'{P1} + {P2} = {P9}')
    print(f'{P1} - {P2} = {P10}')
    print()

    print(f'Distancia entre {P1} y {P2}: {distanciaEntre(P1,P2)}')
    print()

    print(f'Pendiente dados {P1} y {P2}: {pendienteDados(P1,P2)}')
    print()
