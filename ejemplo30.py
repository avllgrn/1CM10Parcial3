from os import system
from math import *

if __name__ == '__main__':
    system('cls')

    try:
        a = float(input('Ingresa a '))
        b = float(input('Ingresa b '))
        c = float(input('Ingresa c '))
        try:
            x1 = (-b + sqrt(pow(b,2)-4*a*c))/(2*a)
            x2 = (-b - sqrt(pow(b,2)-4*a*c))/(2*a)
            print(f'a  = {a}')
            print(f'b  = {b}')
            print(f'c  = {c}')
            print(f'x1 = {x1}')
            print(f'x2 = {x2}')
        except ValueError:
            print('Error! Raíces imaginarias')
        except ZeroDivisionError:
            print('Error! Raíces indeterminadas')
    except ValueError:
        print('Error! Ingresa solo números')
