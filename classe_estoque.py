from classe_produto import *

class Estoque:
    def __init__(self):
        self.listaCadastro = []
        self.listaCadastro.append(Produto(1, 'lapis', 'aa',0))
        


    def salvar_produtos(self):
        entrada_cod = input('Informe o código do produto: ')
        entrada_descricao = input('Informe a descrição do produto: ')
        entrada_fabricante = input('Informe o fabricante: ')
        entrada_quant = int(input('Informe a quantidade: '))
        self.listaCadastro.append(Produto(entrada_cod, entrada_descricao, entrada_fabricante, entrada_quant))
        print('Cadastro realizado com sucesso!')
        print('===================================')

    def listar_todos_produtos(self):
        entrada = input('Digite o código do produto:')
        for i in range(len(self.listaCadastro)):
            if entrada == self.listaCadastro[i].cod:
                print('Cod:',self.listaCadastro[i].cod,
                      '| Descrição:',self.listaCadastro[i].descricao,
                      '| fabricante:',self.listaCadastro[i].fabricante,
                      '| Quantidade:',self.listaCadastro[i].quant)
                print('===================================')
        if entrada == '':
            for i in range(len(self.listaCadastro)):
                print('Cod:',self.listaCadastro[i].cod,
                          '| Descrição:',self.listaCadastro[i].descricao,
                          '| fabricante:',self.listaCadastro[i].fabricante,
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