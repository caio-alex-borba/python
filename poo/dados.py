class BaseDeDados():
    def __init__(self):
        self.__dados = {}

    def novo_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def litar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    #getter
    #@property recebe

    #setter
    #@__dados.setter retorna
