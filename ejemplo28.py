from os import system
from Clases.ClaseCuadro import *

if __name__ == '__main__':
    system('cls')

    C1 = Cuadro(-1)
    print(C1)
    print()
    
    C1.pideleAlUsuarioTuEstado()
    print(C1)
    print()
   
    C1.modificaTuEstado(-3)
    print(C1)
    print()
   
    C1.radio = -4
    print(C1)
    print()
