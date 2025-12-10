class Cuadro:
    def __init__(self, lado=0.0):
        self.__lado = lado
        self.verificaTuEstado()

    @property
    def lado(self):
        return self.__lado
    
    @lado.setter
    def lado(self, lado):
        self.__lado = lado
        self.verificaTuEstado()

    def __str__(self):
        estado = f'Lado: {self.__lado}\n'
        estado += f'Área: {self.dameTuAtributoArea()}\n'
        estado += f'Perimetro: {self.dameTuAtributoPerimetro()}\n'
        return estado
    
    def __del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.__lado = input('Dame mi lado ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, lado):
        self.__lado = lado
        self.verificaTuEstado()

    def dameTuAtributoArea(self):
        return self.__lado**2

    def dameTuAtributoPerimetro(self):
        return self.__lado*4

    def verificaTuEstado(self):
        try:
            self.__lado = float(self.__lado)
        except:
            self.__lado = 0.0

        if self.__lado<0:
            self.__lado = 0.0
