import os

def fDeXigualX(x):
    return x

def tablaAscendente(ini, fin, inc):
    print('\n x\t| f(x) = x\n')
    x = ini                                     # Valor inicial de la variable contador
    while x < fin:                              # Mientras el valor de x sea menor al fin,
        print(f' {x}\t| {fDeXigualX(x)} ')      # Se pinta el valor de la variable y su evaluacion en fDeXigualX
        x = x+inc                               # Con cada vuelta del ciclo, la variable incrementa su valor en inc

def tablaDescendente(ini, fin, dec):
    print('\n x\t| f(x) = x\n')
    x = ini                                     # Valor inicial de la variable contador
    while x > fin:                              # Mientras el valor de x sea mayor al fin,
        print(f' {x}\t| {fDeXigualX(x)} ')      # Se pinta el valor de la variable y su evaluacion en fDeXigualX
        x = x-dec                               # Con cada vuelta del ciclo, la variable decrementa su valor en dec

def tabla():
    ini = float(input('Ingresa inicio del contador '))
    fin = float(input('Ingresa fin del contador '))
    
    if ini < fin:
        inc = float(input('Ingresa incremento del contador '))

        if inc>0:                               # Si el incremento es positivo, 
            tablaAscendente(ini, fin, inc)     # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')

    else:
        dec = float(input('Ingresa decremento del contador '))

        if dec>0:                               # Si el decremento es positivo, 
            tablaDescendente(ini, fin, dec)    # se invoca la funcion que cuenta
        else:
            print('Error! Se genera ciclo infinito')

if __name__ == '__main__':
    os.system('cls')

    tabla()
