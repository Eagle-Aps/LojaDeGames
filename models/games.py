from models.avaliacoes import Avaliacao

class GameStore:

    lojas = []
    
    def __init__(self, nome, ramo):
        self._avaliacao = []
        self._nome = nome
        self.ramo = ramo

        self._ativo = False

        GameStore.lojas.append(self)

    def __str__ (self):

        return f'{self._nome.ljust(30)} | {self.ramo.ljust(30)} | {self.ativo}'
    @classmethod
    def listar_games (cls):

        for game in cls.lojas:

            print (f'{game._nome.ljust(17)} | {game.ramo.ljust(30)} | {str(game.media_avaliacoes).ljust(15)} | {game.ativo}')

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