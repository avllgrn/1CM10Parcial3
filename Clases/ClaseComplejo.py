from math import sqrt, pow

class Complejo:
    def __init__(self, real=0.0, imaginario=0.0):
        self.real = real
        self.imaginario = imaginario

    def __del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.real = float(input('Dame mi real '))
        self.imaginario = float(input('Dame mi imaginario '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, real, imaginario):
        self.real = float(real)
        self.imaginario = float(imaginario)

    def __str__(self):
        cadena = f'{self.real}'
        if self.imaginario<0:
            cadena = cadena + f'{self.imaginario}'
        else:
            cadena = cadena + f'+{self.imaginario}'
        cadena = cadena + 'i'
        return cadena

    def add(self, Derecho):
        S = Complejo()
        S.real = self.real + Derecho.real
        S.imaginario = self.imaginario + Derecho.imaginario
        return S

    def sub(self, Derecho):
        R = Complejo()
        R.real = self.real - Derecho.real
        R.imaginario = self.imaginario - Derecho.imaginario
        return R

    def mul(self, Derecho):
        M = Complejo()
        M.real = self.real * Derecho.real - self.imaginario* Derecho.imaginario
        M.imaginario = self.real* Derecho.imaginario + self.imaginario*Derecho.real
        return M

    def truediv(self, Derecho):
        M = Complejo()
        M.real = (self.real*Derecho.real + self.imaginario*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
        M.imaginario = (self.imaginario*Derecho.real - self.real*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
        return M

    def __add__(self, Derecho):
        S = Complejo()
        S.real = self.real + Derecho.real
        S.imaginario = self.imaginario + Derecho.imaginario
        return S

    def __sub__(self, Derecho):
        R = Complejo()
        R.real = self.real - Derecho.real
        R.imaginario = self.imaginario - Derecho.imaginario
        return R

    def __mul__(self, Derecho):
        M = Complejo()
        M.real = self.real * Derecho.real - self.imaginario* Derecho.imaginario
        M.imaginario = self.real* Derecho.imaginario + self.imaginario*Derecho.real
        return M
    
    def __truediv__(self, Derecho):
        M = Complejo()
        M.real = (self.real*Derecho.real + self.imaginario*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
        M.imaginario = (self.imaginario*Derecho.real - self.real*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
        return M

def add(Izquierdo, Derecho):
    S = Complejo()
    S.real = Izquierdo.real + Derecho.real
    S.imaginario = Izquierdo.imaginario + Derecho.imaginario
    return S

def sub(Izquierdo, Derecho):
    R = Complejo()
    R.real = Izquierdo.real - Derecho.real
    R.imaginario = Izquierdo.imaginario - Derecho.imaginario
    return R

def mul(Izquierdo, Derecho):
    M = Complejo()
    M.real = Izquierdo.real * Derecho.real - Izquierdo.imaginario* Derecho.imaginario
    M.imaginario = Izquierdo.real* Derecho.imaginario + Izquierdo.imaginario*Derecho.real
    return M

def truediv(Izquierdo, Derecho):
    M = Complejo()
    M.real = (Izquierdo.real*Derecho.real + Izquierdo.imaginario*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
    M.imaginario = (Izquierdo.imaginario*Derecho.real - Izquierdo.real*Derecho.imaginario) / (pow(Derecho.real,2) + pow(Derecho.imaginario,2))
    return M
