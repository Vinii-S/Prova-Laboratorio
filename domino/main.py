"""
Arquivo Principal: main.py
Controla o fluxo do jogo, turnos e interage com o usuário no terminal.
"""
# Importando o módulo criado com seu próprio namespace
import domino
import themas
import time

def configurar_jogatina():
    """
    Configura o jogo perguntando o nome do jogador, a dificuldade e o número de jogadores.
    
    ARGS:
    - Nenhum
    
    RETORNA:
    - nome_do_player: O nome do jogador humano
    - npc1, npc2, npc3: Nomes dos NPCs baseados no tema escolhido
    - dificuldade: 'C' para Casual ou 'H' para Hard
    - numero_jogadores: Quantidade total de jogadores (2 a 4)
    """
    nome_do_player = input("Digite o seu nome: ").strip() 
    if nome_do_player == "":
        nome_do_player = 'Você'
        npc1='NPC1' 
        npc2='NPC2' 
        npc3='NPC3'
    else:
        nome_do_player = nome_do_player[0].upper() + nome_do_player[1:].lower()
        npc1, npc2, npc3 = themas.estilizar_jogo(nome_do_player)

    dificuldade = ''
    while dificuldade not in ['C', 'H']:
        dificuldade = input("Temos dois modos de jogo o Casual(C) e Hard(H). Qual você deseja jogar? ").strip().upper()

    numero_jogadores = obter_input_int("Quantos jogadores vão jogar (2 a 4): ", minimo=2, maximo=4)

    return nome_do_player, npc1, npc2, npc3, dificuldade, numero_jogadores 

def imprimir_mesa(mesa):
    """
    Exibe o estado atual da mesa para o jogador de forma visual.
    
    ARGS:
    - mesa: Lista de tuplas representando as peças na mesa
    
    RETORNA:
    - Nenhum (apenas imprime no terminal)
    """
    if not mesa:
        print("\nMesa: [ Vazia ]")
    else:
        mesa_str = " - ".join([f"[{p[0]}|{p[1]}]" for p in mesa])
        print(f"\n🪵  MESA: {mesa_str}")
        
def obter_input_int(mensagem, minimo, maximo):
    """
    Solicita ao usuário que digite um número inteiro dentro de um intervalo específico.
    
    ARGS:
    - mensagem: Mensagem a ser exibida ao usuário
    - minimo: Valor mínimo permitido
    - maximo: Valor máximo permitido
    
    RETORNA:
    - valor: Número inteiro digitado pelo usuário
    """
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Erro: Digite um número inteiro entre {minimo} e {maximo}.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número inteiro.")

def verificar_lados(jogada, ponta_esq, ponta_dir):
    """
    Verifica se a peça jogada pode ser colocada na ponta esquerda, direita ou em ambas.
    Se a peça for válida para ambos os lados, solicita ao jogador que escolha onde colocá
    
    ARGS:
    - jogada: A peça que o jogador deseja jogar (tupla)
    - ponta_esq: O número na ponta esquerda da mesa
    - ponta_dir: O número na ponta direita da mesa
    
    RETORNA:
    - lado: 'E' para esquerda ou 'D' para direita, dependendo de onde a peça pode ser colocada
    """
    cabe_esq = (jogada[0] == ponta_esq or jogada[1] == ponta_esq)
    cabe_dir = (jogada[0] == ponta_dir or jogada[1] == ponta_dir)
    
    if cabe_esq and cabe_dir and ponta_esq != ponta_dir:
        lado = ''
        while lado not in ['E', 'D']:
            lado = input("Sua peça cabe nos dois lados. Jogar na Esquerda(E) ou Direita(D)? ").strip().upper()
        return lado
    
    return 'E' if cabe_esq else 'D'

def dificultar_jogo(validas, mao, ponta_esq, ponta_dir):
    """
    Se o usuario escolher a dificuldade Hard, essa função é chamada para forçar o jogador a escolher uma peça válida.
    
    ARGS:
    - validas: Lista de peças válidas para jogar
    - mao: Lista de peças na mão do jogador
    - ponta_esq: O número na ponta esquerda da mesa
    - ponta_dir: O número na ponta direita da mesa
    
    RETORNA:
    - jogada: A peça escolhida para jogar (tupla)
    - lado: 'E' para esquerda ou 'D' para direita, dependendo de onde a peça pode ser colocada
    """
    escolha = obter_input_int(f"Escolha o índice da peça a ser jogada (0 a {len(mao)-1}): ", minimo=0, maximo = len(mao)-1)
    
    if mao[escolha] in validas:
        jogada = mao[escolha]
    else:
        while mao[escolha] not in validas: 
            escolha = obter_input_int(f"Escolha o índice da peça que combine com a da mesa (0 a {len(mao)-1}): ", minimo=0, maximo = len(mao)-1)
        jogada = mao[escolha]
    
    lado = verificar_lados(jogada, ponta_esq, ponta_dir)
            
    return jogada, lado
    

def facilitar_jogo(validas, ponta_esq, ponta_dir):
    """
    Se o usuario escolher a dificuldade Casual, essa função é chamada para mostrar apenas as peças válidas e forçar o jogador a escolher entre elas.
    
    ARGS:
    - validas: Lista de peças válidas para jogar
    - ponta_esq: O número na ponta esquerda da mesa
    - ponta_dir: O número na ponta direita da mesa
    
    RETORNA:
    - jogada: A peça escolhida para jogar (tupla)
    - lado: 'E' para esquerda ou 'D' para direita, dependendo de onde a peça pode ser colocada
    
    """
    print(f"Peças válidas para jogar: {validas}")
    escolha = obter_input_int(f"Escolha o índice da peça válida (0 a {len(validas)-1}): ", minimo=0, maximo = len(validas)-1)
    
    jogada = validas[escolha]

    lado = verificar_lados(jogada, ponta_esq, ponta_dir)

    return jogada, lado

def main():
    print("="*40)
    print("🎮 BEM-VINDO AO DOMINÓ DE SI 🎮")
    print("="*40)
    
    #CONFIGURAÇÕES DA PARTIDA
    nome_do_player, npc1, npc2, npc3, dificuldade, numero_jogadores = configurar_jogatina()
    

    #CRIAR PEÇAS, DIVIDIR PARA JOGADORES DE FROMA ALEATORIA e ENCONTRAR QUEM COMEÇA 
    pecas = domino.criar_pecas()
    jogadores = domino.distribuir_pecas(pecas, numero_jogadores, nome_do_player, npc1, npc2, npc3)
    jogador_atual, peca_inicial = domino.encontrar_inicio(jogadores)


    print(f"\nSorteio feito! Quem começa é: {jogador_atual} com o duplo [{peca_inicial[0]}|{peca_inicial[1]}]")
    
    mesa = []
    ponta_esq = None
    ponta_dir = None
    
    #CONTROLE DE TURNOS
    ordem = list(jogadores)
    idx_turno = ordem.index(jogador_atual)    
    passos_consecutivos = 0

    while True:
        #DEFINE MAO, JOGADOR ATUAL e MOSTRA A MESA
        nome_atual = ordem[idx_turno]
        mao = jogadores[nome_atual]
        imprimir_mesa(mesa)
        
        validas = domino.obter_jogadas_validas(mao, ponta_esq, ponta_dir)
        
        # Estrutura de Fluxo: Tratamento de passe e trancamento
        if not validas:
            domino.comprar_peca(numero_jogadores, jogadores, nome_atual)
            passos_consecutivos += 1

            if passos_consecutivos == 4:
                print("\n🔒 O JOGO TRANCOU! Ninguém tem mais jogadas.")
                break
        else:
            passos_consecutivos = 0 # Reseta o contador de passes
            
            #LÓGICA PARA VERIFICAR SE É A PRIMEIRA JOGADA E JOGA A MAIOR BUCHA NA MESA
            if not mesa:
                if peca_inicial in mao:
                    jogada = peca_inicial
                else:
                    jogada = validas[0]
                
                mao.remove(jogada) # Remove pelo valor
                mesa.append(jogada) # Adiciona no final
                ponta_esq, ponta_dir = jogada[0], jogada[1]
                print(f"\n🎯 {nome_atual} iniciou colocando [{jogada[0]}|{jogada[1]}].")
            
            #LOGICA PARA AS JOGADAS SEGUINTES 
            else:
                #LOGICA PARA A JOGADA DO PLAYER COM BASE NA DIFICULDADE
                if nome_atual == nome_do_player:
                    print(f"\nSua vez! Sua mão: {mao}")
                    if dificuldade == 'H':
                        jogada, lado = dificultar_jogo(validas, mao, ponta_esq, ponta_dir)

                    elif dificuldade == 'C':
                        jogada, lado = facilitar_jogo(validas, ponta_esq, ponta_dir)
                
                #LOGICA PARA A JOGADA DO NPC 
                else:
                    # Lógica simples para os NPCs: eles jogam a primeira peça válida que encontram
                    jogada = validas[0]
                    cabe_esq = (jogada[0] == ponta_esq or jogada[1] == ponta_esq)
                    lado = 'E' if cabe_esq else 'D'
                    print(f"\n🤖 {nome_atual} jogou a peça [{jogada[0]}|{jogada[1]}].")
                    time.sleep(1.5) # Dá uma pausa pequena para você conseguir ler o terminal

                #REMOÇÃO DA PEÇA JOGADA
                mao.remove(jogada)

                # Inserindo a peça na mesa (Modificando as Listas)
                if lado == 'E':
                    if jogada[0] == ponta_esq:
                        mesa.insert(0, (jogada[1], jogada[0])) # insert(0) adiciona na primeira posição
                        ponta_esq = jogada[1]
                    else:
                        mesa.insert(0, jogada)
                        ponta_esq = jogada[0]
                else: 
                    if jogada[0] == ponta_dir:
                        mesa.append(jogada)
                        ponta_dir = jogada[1]
                    else:
                        mesa.append((jogada[1], jogada[0]))
                        ponta_dir = jogada[0]

        # Verifica condição de vitória
        if len(mao) == 0:
            print(f"\n🏆 FIM DE JOGO! {nome_atual} BATEU E VENCEU!")
            break
            
        # Pula para o próximo turno do jogador.
        idx_turno = (idx_turno + 1) % numero_jogadores
        
        print("-" * 50)
        
    print("\nPlacar final (peças restantes na mão):")
    for nome, mao_restante in jogadores.items():
        print(f"{nome}: {len(mao_restante)} peças")

# A 'porta principal' do seu programa
if __name__ == "__main__":
    main()