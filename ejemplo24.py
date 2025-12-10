from os import system
from Clases.ClaseComplejo import *

if __name__ == '__main__':
    system('cls')

    P1 = Complejo()    
    P2 = Complejo()    
    P3 = Complejo()
    P4 = Complejo()
    P5 = Complejo()

    print('Para P1')
    P1.pideleAlUsuarioTuEstado()
    print()
    print('Para P2')
    P2.pideleAlUsuarioTuEstado()
    print()

    P3 = P1 + P2*P1 - P2/P1 + P2*P1 - P2 

    print(f'P1 + P2*P1 - P2/P1 + P2*P1 - P2 = {P3}')
