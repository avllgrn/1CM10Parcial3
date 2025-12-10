import os
import tablaFdeXIgualX
import tablaFdeXcuadrada
import tablaFdeXseno
import tablaFdeXcoseno
import tablaFdeXtangente

def selecciona(opcion):
    match opcion:
        case '1':
            tablaFdeXIgualX.tabla()
        case '2':
            tablaFdeXcuadrada.tabla()
        case '3':
            tablaFdeXseno.tabla()
        case '4':
            tablaFdeXcoseno.tabla()
        case '5':
            tablaFdeXtangente.tabla()
        case '6':
            print('Adiós! =)')
        case _:
            print('Opción invalida... =(')











def menu():
    os.system('cls')
    print('1. f(x) = x')
    print('2. f(x) = x^2')
    print('3. f(x) = sen(x)')
    print('4. f(x) = cos(x)')
    print('5. f(x) = tan(x)')
    print('6. Salir')
    opcion = input('¿Cuál es tu opción? ')
    os.system('cls')
    selecciona(opcion)
    return opcion

if __name__ == '__main__':
    os.system('cls')

    while menu() != '6':
        input('\n\nPresiona una tecla para continuar...')
