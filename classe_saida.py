from classe_estoque import *


class Saida:
    def __init__(self):
        self.entrada2 = Estoque()


    def sair_produtos(self):
        controle = int(input('informe o código do produto:'))
        for i in range(len(self.entrada2.listaCadastro)):
            if controle == self.entrada2.listaCadastro[i].cod:
                self.entrada2.listaCadastro[i].quant -= int((input('Informe a quantidade que foi comprada:')))
                print('Quantidade alterada!')
                print('===================================')

            else:
                pass