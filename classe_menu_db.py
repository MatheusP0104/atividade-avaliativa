from classe_db import  DBestoque
from classe_compras import *
from classe_saida import *


class Menu:
    def __init__(self):
        DB = DBestoque()
        compra = Compra()
        saida = Saida()
        compra.entrada = DB
        saida.entrada2 = DB

        while True:
            entrada_fab = input('Informe a opção desejada:\n1 - Cadastrar Fabricante\n2 - Ja tenho um Fabricante\n3 - Encerrar Programa\nEntrada:')
            if entrada_fab == '1':
                codi = None
                nome = input('Digite o nome do fabricante:')
                DB.cadastrar_fabri(codi, nome)
            elif entrada_fab == '2':
                while entrada_fab == '2':
                    entrada2 = input('Informe a opção desejada:\n1 - Cadastrar Produto\n2 - Listar todos\n3 - Alterar Produto\n4 - Comprar do estoque \
                                    \n5 - Saida do produto\n6 - Histórico de compra\n7 - Histórico de saída\n8 - Listar todos os Fabricantes\n0 - Sair\nEntrada:')
                    if entrada2 == '1':
                        cod = int(input('Digite o código do produto: '))
                        descricao = input('Digite o nome do produto: ')
                        codigo_fabri = input('Digite o codigo do Fabricante: ')
                        quantidade = input('Digite a quantidade: ')
                        DB.salvar_produtos(cod, descricao,codigo_fabri,quantidade)
                    elif entrada2 == '2':
                        DB.listar_produtos()
                    elif entrada2 == '3':
                        cod = int(input('Digite o código do produto:'))
                        valor = input('Digite a nova descricao: ')
                        atributo = 'descricao'
                        DB.alterar_produtos(atributo, valor, cod)
                    elif entrada2 == '4':
                        cod = int(input('digite o código do produto:'))
                        var = int(input('Digite a quantidade que será comprada:'))
                        atributo = 'quantidade'
                        compra.comprar_produtos(cod,var,atributo)
                    elif entrada2 == '5':
                        cod = int(input('digite o código do produto:'))
                        var = int(input('Digite a quantidade que irá sair:'))
                        atributo = 'quantidade'
                        saida.sair_produtos(cod,var,atributo)
                    elif entrada2 == '6':
                        compra.imprimir_hist()
                    elif entrada2 == '7':
                        saida.imprimir_hist_saida()
                    elif entrada2 == '8':
                        DB.listar_fabri()
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
