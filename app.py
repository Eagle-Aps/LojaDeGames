from models.games import GameStore
from models.produtos.consoles import Consoles
from models.produtos.games import GameProduto

# gamepoint = GameStore('Gamepoint', 'Jogos e Consoles')
ps_5 = Consoles('Playstation 5', 3500, 870)
# gamepoint.avaliacoes_clientes('Igor', 10)
# gamepoint.avaliacoes_clientes('Wendell', 9)
# ps_store = GameStore('PlayStation Store', 'Jogos de Playstation')
# ps_store.avaliacoes_clientes('Igor', 10)
# ps_store.avaliacoes_clientes('Nathalia', 3)
# ps_store.avaliacoes_clientes('Simone', 9)
# ps_store.alternar_disponibilidade()
# point_do_hardware = GameStore('Point do Hardware', 'Hardware para Games em Geral')

def main ():
    # GameStore.listar_games()
    print (ps_5)

if __name__ == '__main__':
    main()