from os import system
from Clases.ClaseComplejo import *

if __name__ == '__main__':
    system('cls')

    C1 = Complejo()    
    C2 = Complejo()    
    C3 = Complejo()
    C4 = Complejo()
    C5 = Complejo()
    C6 = Complejo()
    C7 = Complejo()
    C8 = Complejo()

    print('Cara C1')
    C1.pideleAlUsuarioTuEstado()
    print()
    print('Cara C2')
    C2.pideleAlUsuarioTuEstado()
    print()

    C3 = add(C1, C2)
    C4 = sub(C1, C2)
    C5 = mul(C1, C2)
    C6 = truediv(C1, C2)

    C7 = C1.add(C2)
    C8 = C1.sub(C2)
    C9 = C1.mul(C2)
    C10 = C1.truediv(C2)

    C11 = C1.__add__(C2)
    C12 = C1.__sub__(C2)
    C13 = C1.__mul__(C2)
    C14 = C1.__truediv__(C2)

    C15 = C1+C2
    C16 = C1-C2
    C17 = C1*C2
    C18 = C1/C2

    print(f'{C1} + {C2} = {C3}')
    print(f'{C1} - {C2} = {C4}')
    print(f'{C1} * {C2} = {C5}')
    print(f'{C1} / {C2} = {C6}')
    print()

    print(f'{C1} + {C2} = {C7}')
    print(f'{C1} - {C2} = {C8}')
    print(f'{C1} * {C2} = {C9}')
    print(f'{C1} / {C2} = {C10}')
    print()
    
    print(f'{C1} + {C2} = {C11}')
    print(f'{C1} - {C2} = {C12}')
    print(f'{C1} * {C2} = {C13}')
    print(f'{C1} / {C2} = {C14}')
    print()
    
    print(f'{C1} + {C2} = {C15}')
    print(f'{C1} - {C2} = {C16}')
    print(f'{C1} * {C2} = {C17}')
    print(f'{C1} / {C2} = {C18}')
    print()
    