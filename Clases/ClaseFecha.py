

class Fecha:
    def __init__(self, dia= 1,mes= 1,anio= 2025):
        self.dia= int(dia)
        self.mes= int(mes)
        self.anio= int(anio)
        self.verificaTuEstado()
        
        
    def __del__(self):
        pass
    
    
    def pideleAlUsuarioTuEstado (self):
        self.dia=int(input('Dame el dia: '))
        self.mes=int(input('Dame el mes: '))
        self.anio=int(input('Dame el anio: '))
        self.verificaTuEstado()
        
    def muestraTuEstado(self):
        print(self)
        

    def __str__(self):
        estado= f'Dia: {self.dia} / Mes: {self.mes} / Anio: {self.anio}'
    
        return estado
    
    def modificaTuEstado(self, dia ,mes ,anio):
        self.dia=int(dia) 
        self.mes=int(mes)
        self.anio=int(anio)
        self.verificaTuEstado()
        
    def verificaTuEstado(self):
        if self.dia<1 or self.dia>=32:
            self.dia= 1

        if self.mes<1 or self.mes>=13:
            self.mes= 1

        if self.anio<1:
            self.anio=2025
        
    
        
        