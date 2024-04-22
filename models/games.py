from models.avaliacoes import Avaliacao
from models.produtos.item_produto import ItemProduto
class GameStore:

    lojas = []
    
    def __init__(self, nome, ramo):
        self._avaliacao = []
        self._nome = nome
        self._ramo = ramo
        self._ativo = False
        self._produtos = []

        GameStore.lojas.append(self)

    def __str__ (self):

        return f'{self._nome.ljust(30)} | {self._ramo.ljust(30)} | {self.ativo}'
    @classmethod
    def listar_games (cls):

        for game in cls.lojas:

            print (f'{game._nome.ljust(17)} | {game._ramo.ljust(30)} | {str(game.media_avaliacoes).ljust(15)} | {game.ativo}')

    @property

    def ativo(self):
        return 'Aberta' if self._ativo else'Fechada'
    
    def alternar_disponibilidade (self):
        self._ativo = not self._ativo

    def avaliacoes_clientes (self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes (self):
        if not self._avaliacao:
            return 'Não Avaliado'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtd = len(self._avaliacao)
        media = round(soma_notas/ qtd, 1)
        return media
    
    def adicionar_produto (self, item):
        if isinstance (item, ItemProduto):
            self._produtos.append(item)
    
    @property
    def exibir_produtos (self):
        print (f'Produtos oferecidos pela loja {self._nome}: \n')
        for i, item in enumerate (self._produtos, start=1):
            if hasattr(item, 'memoria'):
                mensagem_console = f'**CONSOLE** Nome: {item._nome} | Preço: {item._preco} | Memória: {item.memoria} GB'
                print(mensagem_console)
            else:
                 mensagem_game = f'**GAME** Nome: {item._nome} | Preço: {item._preco} | Plataforma: {item._plataforma}'
                 print(mensagem_game)