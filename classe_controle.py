from platform import java_ver
from classe_estoque import *


class Compra:
    def __init__(self):
        self.entrada = Estoque()
        self.listaHist = []

    def comprar_produtos(self):
        controle = int(input('informe o código do produto:'))
        for i in range(len(self.entrada.listaCadastro)):
            if controle == int(self.entrada.listaCadastro[i].cod):
                variavel = int((input('Informe a quantidade comprada:')))
                self.entrada.listaCadastro[i].quant += variavel
                self.listaHist.append(f'Produto:{self.entrada.listaCadastro[i].descricao} | Quantidade Comprada:{variavel}')
                print('Quantidade alterada!')
                print('===================================')

            else:
                pass


    def imprimir_hist(self):
        for i in range(len(self.listaHist)):
            print(self.listaHist[i])
            print('===================================')
            