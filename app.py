from models.games import GameStore
from models.produtos.console import Consoles
from models.produtos.game import GameProduto

gamepoint = GameStore('Gamepoint', 'Jogos e Consoles')
ps_store = GameStore('PlayStation Store', 'Jogos de Playstation')
ps_5 = Consoles('Playstation 5', 3500, 870)
gamepoint.adicionar_produto(ps_5)
God_of_War = GameProduto('God Of War', 200, 'PS2')
ps_store.adicionar_produto(God_of_War)
# gamepoint.avaliacoes_clientes('Igor', 10)
# gamepoint.avaliacoes_clientes('Wendell', 9)
# ps_store.avaliacoes_clientes('Igor', 10)
# ps_store.avaliacoes_clientes('Nathalia', 3)
# ps_store.avaliacoes_clientes('Simone', 9)
# ps_store.alternar_disponibilidade()
# point_do_hardware = GameStore('Point do Hardware', 'Hardware para Games em Geral')

def main ():
    gamepoint.exibir_produtos
    ps_store.exibir_produtos

if __name__ == '__main__':
    main()