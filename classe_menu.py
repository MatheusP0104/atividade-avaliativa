from classe_estoque import *
from classe_controle import *
from classe_saida import *
from classe_fabricante import *


class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        saida = Saida()
        compra.entrada = estoque
        saida.entrada2 = estoque

        while True:
            entrada_fab = input('Informe a opção desejada:\n1 - Cadastrar Fabricante\n2 - Ja tenho um Fabricante\n3 - Encerrar Programa\nEntrada:')
            if entrada_fab == '1':
                estoque.cadastrar_fabri()
            elif entrada_fab == '2':
                while entrada_fab == '2':
                    entrada2 = input('Informe a opção desejada:\n1 - Cadastrar Produto\n2 - Listar todos\n3 - Alterar Produto\n4 - Comprar do estoque \
                                    \n5 - Saida do produto\n6 - Histórico de compra\n7 - Histórico de saída\n8 - Listar todos os Fabricantes\n0 - Sair\nEntrada:')
                    if entrada2 == '1':
                        estoque.salvar_produtos()
                    elif entrada2 == '2':
                        estoque.listar_todos_produtos()
                    elif entrada2 == '3':
                        estoque.alterar_produto()
                    elif entrada2 == '4':
                        compra.comprar_produtos()
                    elif entrada2 == '5':
                        saida.sair_produtos()
                    elif entrada2 == '6':
                        compra.imprimir_hist()
                    elif entrada2 == '7':
                        saida.imprimir_hist_saida()
                    elif entrada2 == '8':
                        estoque.listar_fabri()
                    elif entrada2 == '0':
                        print('Saindo...')
                        break
                    else:
                        print('Opção escolhida não existe')
                        print('===================================')
            elif entrada_fab == '3':
                print('Encerrando o Programa...')
                break
            else:
                    print('Opção escolhida não existe')
                    print('===================================')
