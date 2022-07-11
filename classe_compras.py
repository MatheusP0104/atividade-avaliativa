from classe_db import DBestoque
from datetime import datetime

class Compra:
    def __init__(self):
        self.entrada = DBestoque()


    def comprar_produtos(self,cod,var,atributo):
        comando_sql = 'select cod from Produtos'
        self.entrada.mycursor.execute(comando_sql)
        lista = self.entrada.mycursor.fetchall()
        for i in lista:
            if int(cod) == i[0]:
                self.entrada.mycursor.execute(
                    f'update Produtos set {atributo} = {atributo} + {int(var)} where cod = {cod}')
                self.entrada.conexao.commit()



