from operator import le
from classe_fabricante import *
from classe_produto import *

class Estoque:
    def __init__(self):
        self.listaCadastro = []
        self.listaFabri = []

    def salvar_produtos(self):
                entrada_cod = input('Informe o código do produto: ')
                entrada_descricao = input('Informe a descrição do produto: ')
                entrada_fabri = input('Digite o código do fabricante:')
                for i in range(len(self.listaFabri)):
                    if entrada_fabri == self.listaFabri[i].codi:
                        print('Fabricante:',self.listaFabri[i].nome)
                entrada_quant = int(input('Informe a quantidade: '))
                self.listaCadastro.append(Produto(entrada_cod, entrada_descricao,entrada_fabri,entrada_quant))
                print('Cadastro realizado com sucesso!')
                print('===================================')

    def listar_todos_produtos(self):
        entrada = input('Digite o código do produto:')
        for i in range(len(self.listaCadastro)):
            if entrada == self.listaCadastro[i].cod:
                print('Cod:',self.listaCadastro[i].cod,
                      '| Descrição:',self.listaCadastro[i].descricao,
                      '| fabricante:',self.listaFabri[i].nome,
                      '| Quantidade:',self.listaCadastro[i].quant)
                print('===================================')
        for i in range(len(self.listaCadastro)):
                if entrada == '':
                    print('Cod:',self.listaCadastro[i].cod,
                            '| Descrição:',self.listaCadastro[i].descricao,
                            '| fabricante:',self.listaFabri[i].nome,
                            '| Quantidade:',self.listaCadastro[i].quant)
                    print('===================================')
        else:
            print('esses são todos os produtos')
        
    def alterar_produto(self):
        entrada = input('Digite o código do produto: ')
        for i in range(len(self.listaCadastro)):
            if entrada == self.listaCadastro[i].cod:
                self.listaCadastro[i].descricao = input('Digite a nova descrição do produto:')
                print('Alteração realizada com sucesso!')
                print('===================================')

    def cadastrar_fabri(self):
        entrada_codi = input('Digite o código do fabricante:')
        entrada_nome = input('Digite o nome do fabricante:')
        self.listaFabri.append(Fabricante(entrada_codi,entrada_nome))
        print('Cadastro realizado com sucesso!')
        print('===================================')

    def listar_fabri(self):
        entrada = input('Digite o código do fabricante:')
        for i in range(len(self.listaFabri)):
            if entrada == self.listaFabri[i].codi:
                print('Código:',self.listaFabri[i].codi,
                      '| Nome:',self.listaFabri[i].nome)
                print('===================================')
        for i in range(len(self.listaFabri)):
            if entrada == '':
                print('Código:',self.listaFabri[i].codi,
                      '| Nome:',self.listaFabri[i].nome)
                print('===================================')

        else:
            print('esses são todos os fabricantes')
            print('===================================')



    