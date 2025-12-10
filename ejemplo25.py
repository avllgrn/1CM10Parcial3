from os import system
from Clases.ClaseComplejo import *

if __name__ == '__main__':
    system('cls')

    P = Complejo()

    P.pideleAlUsuarioTuEstado()
    P.muestraTuEstado()
    print()

    P.modificaTuEstado(5.6, 7.8)
    P.muestraTuEstado()
    print()
