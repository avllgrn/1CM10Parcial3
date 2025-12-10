import os
import math

def gradosAradianes(grados):
    return grados * math.pi / 180

def fDeXcoseno(xGrados):
    xRadianes = gradosAradianes(xGrados)                # Se convierte a radianes los grados recibidos
    return math.cos(xRadianes)                          # Se contesta el coseno de los radianes convertidos

def tabla1Ascendente(ini, fin, inc):
    print('\n x\t| f(x) = cos(x)\n')
    xGrados = ini                                       # Valor inicial de la variable contador
    while xGrados < fin:                                # Mientras el valor de xGrados sea menor al fin,
        print(f' {xGrados}\t| {fDeXcoseno(xGrados)} ')    # Se pinta el valor de la variable y su evaluacion en fDeXcoseno
        xGrados = xGrados+inc                           # Con cada vuelta del ciclo, la variable incrementa su valor en inc

def tabla1Descendente(ini, fin, dec):
    print('\n x\t| f(x) = cos(x)\n')
    xGrados = ini                                       # Valor inicial de la variable contador
    while xGrados > fin:                                # Mientras el valor de xGrados sea mayor al fin,
        print(f' {xGrados}\t| {fDeXcoseno(xGrados)} ')    # Se pinta el valor de la variable y su evaluacion en fDeXcoseno
        xGrados = xGrados-dec                           # Con cada vuelta del ciclo, la variable decrementa su valor en dec

def tabla():
    ini = float(input('Ingresa inicio de la tabla '))
    fin = float(input('Ingresa fin de la tabla '))
    
    if ini < fin:
        inc = float(input('Ingresa incremento de la tabla '))

        if inc>0:                                       # Si el incremento es positivo, 
            tabla1Ascendente(ini, fin, inc)             # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')

    else:
        dec = float(input('Ingresa decremento de la tabla '))

        if dec>0:                                       # Si el decremento es positivo, 
            tabla1Descendente(ini, fin, dec)            # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')

if __name__ == '__main__':
    os.system('cls')

    tabla()
