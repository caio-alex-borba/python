class Escritor():
    def __init__(self, nome):
        self.__nome = nome
        self.__feramenta = None
    @property
    def nome(self):
        return self.__nome
    @property
    def feramenta(self):
        return self.__feramenta
    @feramenta.setter
    def feramenta(self, feramenta):
        self.__feramenta = feramenta

class Caneta():
    def __init__(self, marca):
        self.__nome = marca
    @property
    def marca(self):
        return self.__marca
    def escrever(self):
        print('caneta esta escrevendo')

class Maquinadeescrever():
    def __init__(self, modelo):
        self.__modelo = modelo
    @property
    def modelo(self):
        return self.__modelo
    def escrever(self):
        print('caneta esta escrevendo')