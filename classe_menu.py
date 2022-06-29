from classe_estoque import *
from classe_controle import *


class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        compra.entrada = estoque

        while True:
            entrada = input('Informe a opção desejada:\n1 - Cadastrar\n2 - Listar todos\n3 - Alterar Produto\n4 - Comprar\n0 - Sair\nEntrada:')
            if entrada == '1':
                estoque.salvar_produtos()
            elif entrada == '2':
                estoque.listar_todos_produtos()
            elif entrada == '3':
                estoque.alterar_produto()
            elif entrada == '4':
                compra.comprar_produtos()
            elif entrada == '0':
                print('Saindo...')
                break
            else:
                print('Opção escolhida não existe')
                print('===================================')
