from models.produtos.item_produto import ItemProduto

class Consoles(ItemProduto):
    def __init__(self, nome, preco, memoria):
        super().__init__(nome, preco)
        self.memoria = memoria
    
    def __str__(self):
        return self._nome
    
