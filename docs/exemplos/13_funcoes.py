"""
Jogo da Velha: você vs uma "IA" com estratégia real.

Esse é um dos exemplos que mais acho legal e também um dos que mais me bati,
não vou mentir. Mas é exatamente por isso que acho que funciona bem pra mostrar
funções: cada uma tem nome, faz uma coisa só, e quando você as encadeia,
o programa inteiro parece que raciocina.

A IA usa essa estratégia: antes de jogar, ela simula recursivamente todos os jogos
possíveis a partir do estado atual e escolhe o caminho que garante o melhor
resultado pra ela. Com isso, ela fica invencível (na teoria), o melhor que você consegue
é empate. Tente alcançar o empate, já é pra ser difícil o suficiente.
"""


def criar_tabuleiro():
    """Retorna um tabuleiro 3×3 com todas as células vazias (None)."""
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]


def exibir_tabuleiro(tab):
    """Imprime o estado atual do tabuleiro no terminal."""
    print("\n  1 2 3")
    for i, linha in enumerate(tab):
        simbolos = []
        for cel in linha:
            if cel is None:
                simbolos.append("·")
            else:
                simbolos.append(cel)
        print(f"{i + 1} {' '.join(simbolos)}")
    print()


def posicao_valida(tab, linha, col):
    """Retorna True se (linha, col) está dentro do tabuleiro e está livre."""
    if linha < 0 or linha > 2 or col < 0 or col > 2:
        return False
    return tab[linha][col] is None


def verificar_vitoria(tab, jogador):
    """Retorna True se jogador tiver três marcas em sequência."""
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True
    for j in range(3):
        if tab[0][j] == jogador and tab[1][j] == jogador and tab[2][j] == jogador:
            return True
    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True
    return False


def tabuleiro_cheio(tab):
    """Retorna True se não houver nenhuma célula vazia."""
    for linha in tab:
        if None in linha:
            return False
    return True


def avaliar(tab, vez_da_ia, profundidade):
    """
    Avalia o tabuleiro e retorna a pontuação da posição atual.

    Funciona como um jogador que pensa vários lances à frente: "se eu jogar
    aqui, o que ele responde, e daí o que eu faço...". Faz isso pra TODAS as
    possibilidades e retorna a pontuação do melhor caminho encontrado.

    +10 → IA vence, -10 → jogador vence, 0 → empate.
    Subtrair/somar a profundidade faz a IA preferir vitórias rápidas.
    """
    if verificar_vitoria(tab, "O"):
        return 10 - profundidade   # vitória mais cedo vale mais
    if verificar_vitoria(tab, "X"):
        return profundidade - 10   # derrota mais tarde é menos ruim
    if tabuleiro_cheio(tab):
        return 0

    if vez_da_ia:
        # Turno da IA: quer maximizar a pontuação.
        melhor = -100
        for i in range(3):
            for j in range(3):
                if posicao_valida(tab, i, j):
                    tab[i][j] = "O"
                    pontuacao = avaliar(tab, False, profundidade + 1)
                    tab[i][j] = None
                    if pontuacao > melhor:
                        melhor = pontuacao
        return melhor
    else:
        # Turno do jogador: quer minimizar a pontuação (do ponto de vista da IA).
        melhor = 100
        for i in range(3):
            for j in range(3):
                if posicao_valida(tab, i, j):
                    tab[i][j] = "X"
                    pontuacao = avaliar(tab, True, profundidade + 1)
                    tab[i][j] = None
                    if pontuacao < melhor:
                        melhor = pontuacao
        return melhor


def jogada_ia(tab):
    """
    Escolhe a melhor jogada possível e retorna (linha, col).

    Testa cada posição livre, simula o jogo inteiro a partir dali e escolhe
    a posição com a maior pontuação. A IA nunca perde.
    """
    melhor_pontuacao = -100
    melhor_lin, melhor_col = -1, -1

    for i in range(3):
        for j in range(3):
            if posicao_valida(tab, i, j):
                tab[i][j] = "O"
                pontuacao = avaliar(tab, False, 0)
                tab[i][j] = None
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_lin, melhor_col = i, j

    return melhor_lin, melhor_col


def pedir_jogada(tab):
    """
    Lê uma posição válida do jogador e retorna (linha, col) em índice 0.

    Repete até receber dois números dentro do tabuleiro e uma célula livre.
    """
    while True:
        entrada = input("Sua jogada (linha coluna, ex: 2 3): ").split()

        if len(entrada) != 2 or not entrada[0].isdigit() or not entrada[1].isdigit():
            print("Digite dois números separados por espaço.")
            continue

        linha = int(entrada[0]) - 1
        col   = int(entrada[1]) - 1

        if not posicao_valida(tab, linha, col):
            print("Posição já ocupada ou fora do tabuleiro.")
            continue

        return linha, col


def partida():
    """Executa uma partida completa de jogo da velha (jogador vs. IA)."""
    tab = criar_tabuleiro()

    print("\n  Você é X  |  IA é O")
    print("  Posições: linha e coluna de 1 a 3")

    while True:
        exibir_tabuleiro(tab)

        print("[ Seu turno ]")
        lin, col = pedir_jogada(tab)
        tab[lin][col] = "X"

        if verificar_vitoria(tab, "X"):
            exibir_tabuleiro(tab)
            print("Você venceu! Impressionante.")
            return

        if tabuleiro_cheio(tab):
            exibir_tabuleiro(tab)
            print("Empate! Você jogou bem.")
            return

        print("[ Turno da IA ]")
        lin_ia, col_ia = jogada_ia(tab)
        tab[lin_ia][col_ia] = "O"
        print(f"IA jogou em ({lin_ia + 1}, {col_ia + 1})")

        if verificar_vitoria(tab, "O"):
            exibir_tabuleiro(tab)
            print("IA venceu. Tenta de novo.")
            return

        if tabuleiro_cheio(tab):
            exibir_tabuleiro(tab)
            print("Empate! Você jogou bem.")
            return


def main():
    """Loop principal: joga partidas até o usuário sair."""
    print("=== JOGO DA VELHA ===")

    while True:
        partida()
        resposta = input("\nPressione qualquer tecla para jogar novamente ('n' para sair): ").strip().lower()
        if resposta.lower() == "n":
            print("Até mais.")
            break


main()
