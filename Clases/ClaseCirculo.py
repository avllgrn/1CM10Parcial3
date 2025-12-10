from math import pi

class Circulo:
    def __init__(self, radio=0.0):
        self.__radio = radio
        self.verificaTuEstado()

    @property
    def radio(self):
        return self.__radio
    
    @radio.setter
    def radio(self, radio):
        self.__radio = radio
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        estado = f'Radio: {self.__radio}\n'
        estado += f'Diametro: {self.dameTuAtributoDiametro()}\n'
        estado += f'Area: {self.dameTuAtributoArea()}\n'
        estado += f'Perímetro: {self.dameTuAtributoPerimetro()}\n'
        return estado

    def pideleAlUsuarioTuEstado(self):
        self.__radio = input('Dame mi radio ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)
    
    def modificaTuEstado(self, radio):
        self.__radio = radio
        self.verificaTuEstado()

    def dameTuAtributoDiametro(self):
        return self.__radio*2

    def dameTuAtributoPerimetro(self):
        return 2*pi*self.__radio

    def dameTuAtributoArea(self):
        return pi*self.__radio**2

    def verificaTuEstado(self):
        try:
            self.__radio = float(self.__radio)
        except:
            self.__radio = 0.0

        if self.__radio<0:
            self.__radio = 0.0
