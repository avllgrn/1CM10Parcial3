from os import system
from Clases.ClaseFraccion import *

if __name__ == '__main__':
    system('cls')

    F1 = Fraccion()    
    F2 = Fraccion()    
    F3 = Fraccion()
    F4 = Fraccion()
    F5 = Fraccion()
    F6 = Fraccion()
    F7 = Fraccion()
    F8 = Fraccion()

    print('Fara F1')
    F1.pideleAlUsuarioTuEstado()
    print()
    print('Fara F2')
    F2.pideleAlUsuarioTuEstado()
    print()

    F3 = add(F1, F2)
    F4 = sub(F1, F2)
    F5 = mul(F1, F2)
    F6 = truediv(F1, F2)

    F7 = F1.add(F2)
    F8 = F1.sub(F2)
    F9 = F1.mul(F2)
    F10 = F1.truediv(F2)

    F11 = F1.__add__(F2)
    F12 = F1.__sub__(F2)
    F13 = F1.__mul__(F2)
    F14 = F1.__truediv__(F2)

    F15 = F1+F2
    F16 = F1-F2
    F17 = F1*F2
    F18 = F1/F2

    print(f'{F1} + {F2} = {F3}')
    print(f'{F1} - {F2} = {F4}')
    print(f'{F1} * {F2} = {F5}')
    print(f'{F1} / {F2} = {F6}')
    print()

    print(f'{F1} + {F2} = {F7}')
    print(f'{F1} - {F2} = {F8}')
    print(f'{F1} * {F2} = {F9}')
    print(f'{F1} / {F2} = {F10}')
    print()
    
    print(f'{F1} + {F2} = {F11}')
    print(f'{F1} - {F2} = {F12}')
    print(f'{F1} * {F2} = {F13}')
    print(f'{F1} / {F2} = {F14}')
    print()
    
    print(f'{F1} + {F2} = {F15}')
    print(f'{F1} - {F2} = {F16}')
    print(f'{F1} * {F2} = {F17}')
    print(f'{F1} / {F2} = {F18}')
    print()
    