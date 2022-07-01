class Produto:
    def __init__(self, cod, descrição, fabricante=str, quantidade=0):
        self.cod = cod
        self.descricao = descrição
        self.fabricante = fabricante.nome
        self.quant = quantidade

        