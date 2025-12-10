from os import system

class Fraccion:
    def __init__(self, numerador=0, denominador=1):
        self.__numerador = numerador
        self.__denominador = denominador
        self.verificaTuEstado()

    @property
    def numerador(self):
        return self.__numerador
    
    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador
        self.verificaTuEstado()

    @property
    def denominador(self):
        return self.__denominador
    
    @denominador.setter
    def denominador(self, denominador):
        self.__denominador = denominador
        self.verificaTuEstado()

    def __str__(self):
        estado = f'{self.__numerador}/'
        estado += f'{self.__denominador}'
        return estado
    
    def __del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.__numerador = input('Dame mi numerador ')
        self.__denominador = input('Dame mi denominador ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__numerador = int(self.__numerador)
        except:
            self.__numerador = 0
            self.__denominador = 1

        try:
            self.__denominador = int(self.__denominador)
        except:
            self.__numerador = 0
            self.__denominador = 1

        if self.__denominador==0:
            self.__numerador = 0
            self.__denominador = 1

        if self.__denominador<0:
            self.__numerador *= -1
            self.__denominador *= -1

        self.reduceTuEstado()

    def reduceTuEstado(self):
        pass

    def add(self, Derecho):
        S = Fraccion()
        S.__numerador = self.__numerador*Derecho.__denominador + self.__denominador*Derecho.__numerador
        S.__denominador = self.denominador * Derecho.denominador
        return S

    def sub(self, Derecho):
        R = Fraccion()
        R.__numerador = self.__numerador*Derecho.__denominador - self.__denominador*Derecho.__numerador
        R.__denominador = self.denominador * Derecho.denominador
        return R

    def mul(self, Derecho):
        M = Fraccion()
        M.__numerador = self.__numerador*Derecho.__numerador
        M.__denominador = self.denominador * Derecho.denominador
        return M

    def truediv(self, Derecho):
        M = Fraccion()
        M.__numerador = self.__numerador*Derecho.denominador
        M.__denominador = self.denominador * Derecho.__numerador
        return M

    def __add__(self, Derecho):
        S = Fraccion()
        S.__numerador = self.__numerador*Derecho.__denominador + self.__denominador*Derecho.__numerador
        S.__denominador = self.denominador * Derecho.denominador
        return S

    def __sub__(self, Derecho):
        R = Fraccion()
        R.__numerador = self.__numerador*Derecho.__denominador - self.__denominador*Derecho.__numerador
        R.__denominador = self.denominador * Derecho.denominador
        return R

    def __mul__(self, Derecho):
        M = Fraccion()
        M.__numerador = self.__numerador*Derecho.__numerador
        M.__denominador = self.denominador * Derecho.denominador
        return M

    def __truediv__(self, Derecho):
        M = Fraccion()
        M.__numerador = self.__numerador*Derecho.denominador
        M.__denominador = self.denominador * Derecho.__numerador
        return M

def add(Izquierdo, Derecho):
    S = Fraccion()
    S.numerador = Izquierdo.numerador*Derecho.denominador + Izquierdo.denominador*Derecho.numerador
    S.denominador = Izquierdo.denominador * Derecho.denominador
    return S

def sub(Izquierdo, Derecho):
    R = Fraccion()
    R.numerador = Izquierdo.numerador*Derecho.denominador - Izquierdo.denominador*Derecho.numerador
    R.denominador = Izquierdo.denominador * Derecho.denominador
    return R

def mul(Izquierdo, Derecho):
    M = Fraccion()
    M.numerador = Izquierdo.numerador*Derecho.numerador
    M.denominador = Izquierdo.denominador * Derecho.denominador
    return M

def truediv(Izquierdo, Derecho):
    M = Fraccion()
    M.numerador = Izquierdo.numerador*Derecho.denominador
    M.denominador = Izquierdo.denominador * Derecho.numerador
    return M
