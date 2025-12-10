from math import sqrt, pow

class Punto2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.x = float(input('Dame mi x '))
        self.y = float(input('Dame mi y '))

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def add(self, Derecho):
        S = Punto2D()
        S.x = self.x + Derecho.x
        S.y = self.y + Derecho.y
        return S

    def sub(self, Derecho):
        R = Punto2D()
        R.x = self.x - Derecho.x
        R.y = self.y - Derecho.y
        return R

    def __add__(self, Derecho):
        S = Punto2D()
        S.x = self.x + Derecho.x
        S.y = self.y + Derecho.y
        return S

    def __sub__(self, Derecho):
        R = Punto2D()
        R.x = self.x - Derecho.x
        R.y = self.y - Derecho.y
        return R

def add(Izquierdo, Derecho):
    S = Punto2D()
    S.x = Izquierdo.x + Derecho.x
    S.y = Izquierdo.y + Derecho.y
    return S

def sub(Izquierdo, Derecho):
    R = Punto2D()
    R.x = Izquierdo.x - Derecho.x
    R.y = Izquierdo.y - Derecho.y
    return R

def distanciaEntre(P1, P2):
    return sqrt(pow(P2.y-P1.y,2) + pow(P2.x-P1.x,2))

def pendienteDados(P1, P2):
    try:
        return (P2.y-P1.y) / (P2.x-P1.x)
    except:
        return None
