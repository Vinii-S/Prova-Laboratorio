import random

def criar_pecas():
    """Gera as 28 peças do dominó duplo-6 usando tuplas dentro de uma lista."""
    pecas = []
    # Estruturas de repetição 'for' iterando sobre a faixa de valores (range)
    for i in range(7):
        for j in range(i, 7):
            pecas.append((i, j)) # append() insere no final da lista
    return pecas

def distribuir_pecas(pecas):
    """Embaralha e distribui 7 peças para 4 jogadores usando fatiamento (slicing)."""
    random.shuffle(pecas)
    
    # Criamos um Dicionário (Chave:Valor) para armazenar os jogadores
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
    Como as 28 peças foram distribuídas entre 4 jogadores, é garantido que alguém a tem.
    """
    for nome, mao in jogadores.items():
        if (6, 6) in mao:
            return nome, (6, 6)
        
def obter_jogadas_validas(mao, ponta_esq, ponta_dir):
    """Verifica quais peças da mão do jogador podem ser jogadas nas pontas atuais."""
    validas = []
    # Se for a primeira jogada (mesa vazia)
    if ponta_esq is None and ponta_dir is None:
        return mao.copy()
        
    for peca in mao:
        if peca[0] == ponta_esq or peca[1] == ponta_esq or peca[0] == ponta_dir or peca[1] == ponta_dir:
            validas.append(peca)
            
    return validas # Função devolve um resultado que pode ser guardado em variável