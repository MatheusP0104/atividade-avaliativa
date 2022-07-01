from classe_estoque import *


class Saida:
    def __init__(self):
        self.entrada2 = Estoque()
        self.listaHistSaida = []


    def sair_produtos(self):
        controle = int(input('informe o código do produto:'))
        for i in range(len(self.entrada2.listaCadastro)):
            if controle == int(self.entrada2.listaCadastro[i].cod):
                var = int((input('Informe a quantidade que irá sair:')))
                self.entrada2.listaCadastro[i].quant -= var
                self.listaHistSaida.append(f'Produto:{self.entrada2.listaCadastro[i].descricao} | Quantidade que foi retirada: {var}')
                print('Quantidade alterada!')
                print('===================================')

            else:
                pass
    
    def imprimir_hist_saida(self):
        for i in range(len(self.listaHistSaida)):
            print(self.listaHistSaida[i])
            print('===================================')