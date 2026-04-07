import random

def criar_pecas():
    """
    Gera as 28 peças do dominó duplo-6 usando tuplas dentro de uma lista.
    
    Args:
        Nenhum.
        
    Returns:
        list: Uma lista contendo as peças do dominó como tuplas (ex: [(0,0), (0,1), ..., (6,6)]).
    """
    pecas = []
    for i in range(7):
        for j in range(i, 7):
            pecas.append((i, j)) 
    return pecas

def distribuir_pecas(pecas):
    """
    Embaralha e distribui 7 peças para 4 jogadores usando fatiamento (slicing).

    Args:
        pecas (list): A lista de peças do dominó.

    Returns:
        dict: Um dicionário com os nomes dos jogadores como chaves e suas respectivas mãos como valores.
    """
    random.shuffle(pecas)
    
    jogadores = {
        "Você": pecas[0:7],
        "NPC 1": pecas[7:14],
        "NPC 2": pecas[14:21],
        "NPC 3": pecas[21:28]
    }
    return jogadores

def encontrar_inicio(jogadores):
    """
    Procura qual jogador possui a peça (6,6).
    
    Args:
        jogadores (dict): O dicionário contendo os jogadores e suas mãos.
        
    Returns:
        tuple: O nome do jogador que começa e a peça inicial (6,6).
    """
    for nome, mao in jogadores.items():
        if (6, 6) in mao:
            return nome, (6, 6)
        
def obter_jogadas_validas(mao, ponta_esq, ponta_dir):
    """
    Verifica quais peças da mão do jogador podem ser jogadas nas pontas atuais.
    
    Args:
        mao (list): A lista de peças na mão do jogador.
        ponta_esq (int): O valor da ponta esquerda da mesa.
        ponta_dir (int): O valor da ponta direita da mesa.
        
    Returns:
        list: Uma lista contendo as peças válidas que podem ser jogadas.
    """
    validas = []
    # Se for a primeira jogada (mesa vazia)
    if ponta_esq is None and ponta_dir is None:
        return mao.copy()
        
    for peca in mao:
        if peca[0] == ponta_esq or peca[1] == ponta_esq or peca[0] == ponta_dir or peca[1] == ponta_dir:
            validas.append(peca)
            
    return validas # Função devolve um resultado que pode ser guardado em variável