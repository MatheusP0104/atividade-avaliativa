from classe_estoque import *
from classe_controle import *

estoque_tarde = Estoque()
compra = Compra()


compra.entrada = estoque_tarde

compra.comprar_produtos()

estoque_tarde.listar_todos_produtos()