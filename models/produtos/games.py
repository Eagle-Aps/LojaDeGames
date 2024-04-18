from models.produtos.item_produto import ItemProduto

class GameProduto (ItemProduto):
    def __init__ (self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

    def __str__(self):
        return self.nome