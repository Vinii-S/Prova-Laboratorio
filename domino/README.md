# Jogo de Dominó em Python

## Descrição do Projeto
Este é um jogo clássico de dominó desenvolvido totalmente em Python para ser jogado via terminal. O projeto simula partidas interativas de 2 a 4 jogadores, onde o usuário enfrenta NPCs (bots). Uma curiosidade divertida é o sistema de temas: dependendo do nome que o jogador escolher (ex: *Batman*, *Sonic*, *Bob Esponja*, *Python*), os NPCs recebem automaticamente nomes de rivais ou personagens do mesmo universo!

## Instruções de Execução
Para rodar o jogo, você precisa ter o Python 3 instalado em sua máquina.

1. Baixe ou clone os arquivos do projeto.
2. Abra o terminal ou prompt de comando.
3. Navegue até a pasta `domino` onde os arquivos estão localizados.
4. Execute o arquivo principal com o seguinte comando:
   ```bash
   python main.py
   ```
5. Siga as instruções apresentadas no terminal para inserir seu nome, escolher a dificuldade e a quantidade de jogadores.

## Principais Funcionalidades
- **Partidas Customizáveis**: Possibilidade de configurar a mesa para 2, 3 ou 4 competidores.
- **Sistema de Temas (`themas.py`)**: NPCs (bots) com nomes dinâmicos e divertidos baseados na cultura pop e programação.
- **Níveis de Dificuldade**:
  - **Casual (C)**: Auxilia o jogador exibindo uma lista clara das peças válidas que podem ser jogadas no turno.
  - **Hard (H)**: Desafia o jogador a escolher o índice correto da peça diretamente da sua mão, sem filtros facilitadores.
- **Lógica do Dominó (`domino.py`)**: 
  - Geração e distribuição aleatória das 28 peças padrão (duplo-6).
  - Identificação de quem inicia a partida procurando o jogador com a maior peça/bucha.
  - Validação inteligente de regras (encaixe nas pontas direita `D` e esquerda `E`).
  - Sistema de "Monte" para compra de peças quando um jogador não tem jogadas válidas (disponível em partidas de 2 ou 3 jogadores).
  - Detecção automática de condições de vitória (bater) ou de jogo trancado (quando ninguém mais tem jogadas possíveis após 4 turnos sem avançar).
