from tkinter import *

class Quadro:
    def __init__(self):
        self.circuitos = []

    def adicionar_circuito(self, circuito):
        self.circuitos.append(circuito)

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

def novo_circuito(quadro):

    def salva_circuito(quadro):
        # novo_nome = en_nome.get()
        novo_tensao = tensao.get()
        novo_tipo = finalidade.get()
        novo_potencia = en_potencia.get()
        circuito = Circuito(len(quadro.circuitos), novo_tipo, novo_tensao, novo_potencia)
        quadro.adicionar_circuito(circuito)
        adicionar_circuitos(quadro.circuitos)
        novo_raiz.destroy()


    novo_raiz = Tk()
    novo_raiz.title('Novo Circuito')

    metodos_instalacao = ['A1', 'A2', 'B1', 'B2', 'C', 'D']


    # ELEMENTOS

    frame1 = Frame(novo_raiz, width=500, height=500)
    frame1.grid(row=0, column=0)

    # Labels
    lb_titulo = Label(frame1, text='Criar Novo Circuito')
    lb_nome = Label(frame1, text='Nome: ')
    lb_tensao = Label(frame1, text='Tensão: ')
    lb_potencia = Label(frame1, text='Potência')
    lb_agrupados = Label(frame1, text='Número de cirucitos agrupados: ')
    lb_metodo = Label(frame1, text='Método de instalação: ')
    lb_tipo = Label(frame1, text='Tipo de alimentação: ')
    lb_finalidade = Label(frame1, text='Finalidade do circuito:')

    # Entrys
    en_nome = Entry(frame1)
    en_potencia = Entry(frame1)
    en_agrupados = Entry(frame1)

    # Caixas de opção
    tensao = StringVar(frame1)
    tensao.set('127')
    op_tensao = OptionMenu(frame1, tensao, '127', '220')

    finalidade = StringVar(frame1)
    finalidade.set('Alimentação')
    op_finalidade = OptionMenu(frame1, finalidade, 'Alimentação', 'Iluminação')

    alimentacao = StringVar(frame1)
    alimentacao.set('Monofásica')
    op_alimentacao = OptionMenu(frame1, alimentacao, 'Monofásica', 'Trifásica')

    metodo = StringVar(frame1)
    metodo.set('B1')
    op_metodo = OptionMenu(frame1, metodo, *metodos_instalacao)

    #Botões
    bot_salvar = Button(frame1, text='Salvar', command=lambda : salva_circuito(quadro))
    bot_cancelar = Button(frame1, text='Cancelar', command=novo_raiz.destroy)


    # POSICIONAMENTO

    # Labels
    lb_titulo.grid(row=0, column=0, sticky=W + E, columnspan=2)
    lb_nome.grid(row=1, column=0, sticky=W)
    lb_tensao.grid(row=2, column=0, sticky=W)
    lb_finalidade.grid(row=3, column=0, sticky=W)
    lb_tipo.grid(row=4, column=0, sticky=W)
    lb_potencia.grid(row=5, column=0, sticky=W)
    lb_agrupados.grid(row=6, column=0, sticky=W)
    lb_metodo.grid(row=7, column=0, sticky=W)

    # Entrys
    en_nome.grid(row=1, column=1, sticky=W)
    en_potencia.grid(row=5, column=1, sticky=W)
    en_agrupados.grid(row=6, column=1, sticky=W)

    # Caixas de opção
    op_tensao.grid(row=2, column=1, sticky=W)
    op_finalidade.grid(row=3, column=1, sticky=W)
    op_alimentacao.grid(row=4, column=1, sticky=W)
    op_metodo.grid(row=7, column=1, sticky=W)

    #Botões
    bot_salvar.grid(row=8, column=0)
    bot_cancelar.grid(row=8, column=1)

    novo_raiz.mainloop()

def criar_janela():

    bot_adicionar = Button(botoes, text='Novo Circuito', width=10, height=5, command=lambda : novo_circuito(quadro))
    bot_adicionar.grid(row=0, column=0)

    id_circuito = Label(tabela, text="Circuito", relief='solid', width=10)
    id_circuito.grid(row=0, column=0)

    tipo_circuito = Label(tabela, text='Tipo', relief='solid', width=10)
    tipo_circuito.grid(row=0, column=1)

    tensao_circuito = Label(tabela, text='Tensão(V)', relief='solid', width=10)
    tensao_circuito.grid(row=0, column=2)

    potencia_circuito = Label(tabela, text='Potência(VA)', relief='solid', width=15)
    potencia_circuito.grid(row=0, column=3)

    corrente_circuito = Label(tabela, text='Corrente(A)', relief='solid', width=15)
    corrente_circuito.grid(row=0, column=4)

    condutor_circuito = Label(tabela, text='Condutor(mm²)', relief='solid', width=15)
    condutor_circuito.grid(row=0, column=5)

    protecao_circuito = Label(tabela, text='Proteção(A)', relief='solid', width=15)
    protecao_circuito.grid(row=0, column=6)

def adicionar_circuitos(circuitos):
    ordem = 0
    for circuito in circuitos:
        id_circuito = Label(dados, text=str(circuito.ordem), relief='ridge', width=10 )
        id_circuito.grid(row=ordem, column=0)

        tipo_circuito = Label(dados, text=str(circuito.tipo), relief='ridge', width=10)
        tipo_circuito.grid(row=ordem, column=1)

        tensao_circuito = Label(dados, text=str(circuito.tensao), relief='ridge', width=10)
        tensao_circuito.grid(row=ordem, column=2)

        potencia_circuito = Label(dados, text=str(circuito.potencia), relief='ridge', width=15)
        potencia_circuito.grid(row=ordem, column=3)

        corrente_circuito = Label(dados, text=str(circuito.calc_corrente()), relief='ridge', width=15)
        corrente_circuito.grid(row=ordem, column=4)

        condutor_circuito = Label(dados, text=str(circuito.condutor), relief='ridge', width=15)
        condutor_circuito.grid(row=ordem, column=5)

        protecao_circuito = Label(dados, text=str(circuito.protecao), relief='ridge', width=15)
        protecao_circuito.grid(row=ordem, column=6)

        ordem = ordem + 1

if __name__ == '__main__':
    raiz = Tk()
    raiz.title('Quadro de cargas')

    botoes = Frame(raiz)
    botoes.grid(row=0,column=0, sticky=W)

    tabela = Frame(raiz)
    tabela.grid(row=1, column=0)

    dados = Frame(raiz)
    dados.grid(row=2, column=0)

    criar_janela()

    quadro = Quadro()
    # circuitos = criar_circuitos()

    adicionar_circuitos(quadro.circuitos)

    raiz.mainloop()