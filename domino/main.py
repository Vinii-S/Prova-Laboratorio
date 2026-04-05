"""
Arquivo Principal: main.py
Controla o fluxo do jogo, turnos e interage com o usuário no terminal.
"""
# Importando o módulo criado com seu próprio namespace
import domino
import time

def imprimir_mesa(mesa):
    """Exibe o estado atual da mesa para o jogador de forma visual."""
    if not mesa:
        print("\nMesa: [ Vazia ]")
    else:
        mesa_str = " - ".join([f"[{p[0]}|{p[1]}]" for p in mesa])
        print(f"\n🪵  MESA: {mesa_str}")

def main():
    print("="*40)
    print("🎮 BEM-VINDO AO DOMINÓ DE SI 🎮")
    print("="*40)

    # Chamando as funções do nosso módulo
    pecas = domino.criar_pecas()
    jogadores = domino.distribuir_pecas(pecas)
    
    jogador_atual, peca_inicial = domino.encontrar_inicio(jogadores)
    print(f"\nSorteio feito! Quem começa é: {jogador_atual} com o duplo [{peca_inicial[0]}|{peca_inicial[1]}]")
    
    mesa = []
    ponta_esq = None
    ponta_dir = None
    
    # Controle de turnos
    ordem = ["Você", "NPC 1", "NPC 2", "NPC 3"]
    idx_turno = ordem.index(jogador_atual)
    passos_consecutivos = 0

    while True:
        nome_atual = ordem[idx_turno]
        mao = jogadores[nome_atual]
        
        imprimir_mesa(mesa)
        validas = domino.obter_jogadas_validas(mao, ponta_esq, ponta_dir)
        
        # Estrutura de Fluxo: Tratamento de passe e trancamento
        if not validas:
            print(f"❌ {nome_atual} não tem peças válidas e PASSOU A VEZ.")
            passos_consecutivos += 1
            if passos_consecutivos == 4:
                print("\n🔒 O JOGO TRANCOU! Ninguém tem mais jogadas.")
                break
        else:
            passos_consecutivos = 0 # Reseta o contador de passes
            
            # Lógica da primeira jogada (Mesa vazia)
            if not mesa:
                if peca_inicial in mao:
                    jogada = peca_inicial
                else:
                    jogada = validas[0]
                
                mao.remove(jogada) # Remove pelo valor
                mesa.append(jogada) # Adiciona no final
                ponta_esq, ponta_dir = jogada[0], jogada[1]
                print(f"🎯 {nome_atual} iniciou colocando [{jogada[0]}|{jogada[1]}].")
            
            else:
                if nome_atual == "Você":
                    print(f"\nSua vez! Suas peças: {mao}")
                    print(f"Peças válidas para jogar: {validas}")
                    
                    # Garantindo que o usuário digite um índice válido
                    escolha = -1
                    while escolha < 0 or escolha >= len(validas):
                        try:
                            # Conversão de Tipos string -> int
                            escolha = int(input(f"Escolha o índice da peça válida (0 a {len(validas)-1}): "))
                        except ValueError:
                            print("Por favor, digite um número inteiro válido!")
                            
                    jogada = validas[escolha]
                    mao.remove(jogada)
                    
                    # Verifica se a peça cabe nos dois lados
                    cabe_esq = (jogada[0] == ponta_esq or jogada[1] == ponta_esq)
                    cabe_dir = (jogada[0] == ponta_dir or jogada[1] == ponta_dir)
                    
                    lado = ''
                    if cabe_esq and cabe_dir and ponta_esq != ponta_dir:
                        while lado not in ['E', 'D']:
                            lado = input("Sua peça cabe nos dois lados. Jogar na Esquerda (E) ou Direita (D)? ").strip().upper()
                    elif cabe_esq:
                        lado = 'E'
                    else:
                        lado = 'D'
                        
                else:
                    # Lógica simples para os NPCs: eles jogam a primeira peça válida que encontram
                    jogada = validas[0]
                    mao.remove(jogada)
                    cabe_esq = (jogada[0] == ponta_esq or jogada[1] == ponta_esq)
                    lado = 'E' if cabe_esq else 'D'
                    print(f"🤖 {nome_atual} jogou a peça [{jogada[0]}|{jogada[1]}].")
                    time.sleep(1.5) # Dá uma pausa pequena para você conseguir ler o terminal

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
            
        # Pula para o próximo turno do jogador
        idx_turno = (idx_turno + 1) % 4
        print("-" * 50)
        
    print("\nPlacar final (peças restantes na mão):")
    for nome, mao_restante in jogadores.items():
        print(f"{nome}: {len(mao_restante)} peças")

# A 'porta principal' do seu programa
if __name__ == "__main__":
    main()