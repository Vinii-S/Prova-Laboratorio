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
    # Estruturas de repetição 'for' iterando sobre a faixa de valores (range)
    for i in range(7):
        for j in range(i, 7):
            pecas.append((i, j)) # append() insere no final da lista
    return pecas

def distribuir_pecas(pecas, numero_jogadores, nome_do_player, npc1, npc2, npc3):
    """
    Embaralha e distribui as peças para os jogadores com base no número de jogadores
    
    ARGS:
    - pecas: Lista de todas as peças do dominó
    - numero_jogadores: Quantidade de jogadores (2, 3 ou 4)
    - nome_do_player: Nome do jogador humano
    - npc1, npc2, npc3: Nomes dos NPCs (dependendo do tema escolhido)
    
    RETORNA: 
    - jogadores: Dicionário com os jogadores e suas respectivas mãos de peças representasdas por listas de tuplas.
    
    """
    random.shuffle(pecas)

    if numero_jogadores == 2:
        jogadores = {
            nome_do_player: pecas[0:7],
            npc1: pecas[7:14],
            "MONTE": pecas[14:28]
        }
    elif numero_jogadores == 3:
        jogadores = {
            nome_do_player: pecas[0:7],
            npc1: pecas[7:14],
            npc2: pecas[14:21],
            "MONTE": pecas[21:28]
        }
    elif numero_jogadores == 4:
        jogadores = {
            nome_do_player: pecas[0:7],
            npc1: pecas[7:14],
            npc2: pecas[14:21],
            npc3: pecas[21:28]
        }
    # Criamos um Dicionário (Chave:Valor) para armazenar os jogadores
    return jogadores

def comprar_peca(numero_jogadores, jogadores, nome_atual):
    """
    Realiza a compra de uma peça do monte para o jogador atual quando ele não tem jogadas válidas.
    
    ARGS:
    - numero_jogadores: Quantidade total de jogadores (2 a 4)
    - jogadores: Dicionário contendo os jogadores e suas mãos de peças
    - nome_atual: Nome do jogador que precisa comprar
    
    RETORNA: 
    - Modifica o estado do dicionário 'jogadores' e imprime mensagens informativas)
    """
    if numero_jogadores <= 3:
        if jogadores["MONTE"]:
            comprada = jogadores["MONTE"].pop()
            jogadores[nome_atual].append(comprada)
            print(f"\n❌ {nome_atual} não tem peças válidas, comprou do monte e PASSOU A VEZ.")
        else:
            print(f"\n⚠️ O MONTE ESTÁ VAZIO! {nome_atual} não pode comprar.")
        

    elif numero_jogadores == 4:
        print(f"\n❌ {nome_atual} não tem peças válidas e PASSOU A VEZ.")

def encontrar_inicio(jogadores):
    """
    Procura qual jogador possui a maior bucha (6,6 ; 5,5; ...).
    
    ARGS:
    - jogadores: Dicionário contendo os jogadores e suas mãos de peças
    
    RETORNA:
    - nome: Nome do jogador que possui a maior bucha
    - bucha: A peça da maior bucha encontrada (tupla)
    """
    for i in range(6, -1, -1):
        bucha = (i, i)
        # Para cada bucha, verifica quem a possui
        for nome, mao in jogadores.items():
            if nome != "MONTE" and bucha in mao:
                return nome, bucha
        
def obter_jogadas_validas(mao, ponta_esq, ponta_dir):
    """
    Verifica quais peças da mão do jogador podem ser jogadas nas pontas atuais.
    
    ARGS:
    - mao: Lista de tuplas representando as peças na mão do jogador
    - ponta_esq: O número na ponta esquerda da mesa (ou None se a mesa estiver vazia)
    - ponta_dir: O número na ponta direita da mesa (ou None se a mesa estiver vazia)
    
    RETORNA:
    - validas: Lista de peças (tuplas) que podem ser jogadas nas pontas atuais
    
    """
    validas = []
    # Se for a primeira jogada (mesa vazia)
    if ponta_esq is None and ponta_dir is None:
        return mao.copy()
        
    for peca in mao:
        if peca[0] == ponta_esq or peca[1] == ponta_esq or peca[0] == ponta_dir or peca[1] == ponta_dir:
            validas.append(peca)
            
    return validas # Função devolve um resultado que pode ser guardado em variável