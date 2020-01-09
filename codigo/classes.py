class Quadro:
    def __init__(self):
        self.nome = 'Novo Quadro'
        self.circuitos = []

    def adicionar_circuito(self, circuito):
        self.circuitos.append(circuito)

    def potecia_total(self):
        pass

class Circuito:
    def __init__(self, ordem, tipo, tensao, potencia):
        self.ordem = ordem
        self.tipo = tipo
        self.tensao = tensao
        self.potencia = potencia
        self.corrente = 0
        self.condutor = '2,5'
        self.protecao = '20'

    def calc_condutor(self):
        pass

    def calc_protecao(self):
        pass

    def calc_corrente(self):
        p = float(self.potencia)
        v = float(self.tensao)
        return round(p/v, 2)