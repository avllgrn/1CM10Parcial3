from os import system

class Monomio:
    def __init__(self, coeficiente=0.0, exponente=0):
        self.coeficiente = coeficiente
        self.exponente = exponente

    def __str__(self) -> str:
        return f'{self.coeficiente}x^{self.exponente}'

    def muestraTuEstado(self):
        print(self)

if __name__ == '__main__':
    system('cls')

    # Ejemplo de cómo se ve una instancia de la clase monomio
    print(Monomio(2,3))
