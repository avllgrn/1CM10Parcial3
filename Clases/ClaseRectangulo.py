class Rectangulo:
    def __init__(self, base=0.0, altura=0.0):
        self.__base = base
        self.__altura = altura
        self.verificaTuEstado()

    @property
    def base(self):
        return self.__base
    
    @base.setter
    def base(self, base):
        self.__base = base
        self.verificaTuEstado()

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        self.verificaTuEstado()

    def __str__(self):
        estado = f'Base: {self.__base}\n'
        estado += f'Altura: {self.__altura}\n'
        estado += f'Área: {self.dameTuAtributoArea()}\n'
        estado += f'Perimetro: {self.dameTuAtributoPerimetro()}\n'
        return estado
    
    def __del__(self):
        pass

    def pideleAlUsuarioTuEstado(self):
        self.__base = input('Dame mi base ')
        self.__altura = input('Dame mi altura ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, base, altura):
        self.__base = base
        self.__altura = altura
        self.verificaTuEstado()

    def dameTuAtributoArea(self):
        return self.__base*self.__altura

    def dameTuAtributoPerimetro(self):
        return self.__base*2 + self.__altura*2

    def verificaTuEstado(self):
        try:
            self.__base = float(self.__base)
        except:
            self.__base = 0.0

        try:
            self.__altura = float(self.__altura)
        except:
            self.__altura = 0.0

        if self.__base<=0 or self.__altura<=0:
            self.__base = 0.0
            self.__altura = 0.0
