from os import system

class Fecha:
    def __init__(self, dia=1, mes=1, anio=2025):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__anio}'
    
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia
        self.verificaTuEstado()

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes
        self.verificaTuEstado()

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio
        self.verificaTuEstado()

    def pideleAlUsuarioTuEstado(self):
        self.__dia = input('Dame mi dia ')
        self.__mes = input('Dame mi mes ')
        self.__anio = input('Dame mi anio ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.verificaTuEstado()

    def verificaTuEstado(self):
        try:
            self.__dia = int(self.__dia)
        except:
            self.__dia = 1
        try:
            self.__mes = int(self.__mes)
        except:
            self.__mes = 1
        try:
            self.__anio = int(self.__anio)
        except:
            self.__anio = 2025

        if self.__anio<0:
            self.__anio=2025

        if self.__mes<1 or self.__mes>12:
            self.__mes=1
        
        if self.__dia<1 or self.__dia>31:
            self.__dia=1

if __name__ == '__main__':
    system('cls')

    print('Se intenta construir una instancia de Fecha con cadenas:')
    F = Fecha('cinco', 'mayo', 'dos mil veinte')
    print(f'F -> {F}\n')

    print('Se intenta modificar una instancia de Fecha con cadenas:')
    F.modificaTuEstado('primero', 'abril', 'dos mil veinticuatro')
    print(f'F -> {F}\n')

    print('Se intenta asignar cadenas a los atributos de una instancia de Fecha:')
    F.dia = 'cinco'
    F.mes = 'mayo'
    F.anio = 'dos mil ocho'
    print(f'F -> {F}\n')

    print('Si se intenta ingresar cadenas a los atributos de una instancia de Fecha:')
    F.pideleAlUsuarioTuEstado()
    print(f'F -> {F}\n')