from classe_estoque import *


class Compra:
    def __init__(self):
        self.entrada = Estoque()


    def comprar_produtos(self):
        controle = int(input('informe o código do produto:'))
        for i in range(len(self.entrada.listaCadastro)):
            print('Error!')
            if controle == self.entrada.listaCadastro[i].cod:
                self.entrada.listaCadastro[i].quant += int((input('Informe a quantidade comprada:')))

            else:
                pass
        