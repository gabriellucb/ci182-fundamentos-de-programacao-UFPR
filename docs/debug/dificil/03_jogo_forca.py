# ────────────────────────────────────────────────────────────
# Nível: Difícil │ Tema: Desafio final (strings, sets, dicionários,
#                        classes, arquivos, try/except, compreensões)
# ────────────────────────────────────────────────────────────
#
# Jogo da forca com categorias, dificuldade escolhida pelo jogador e
# placar salvo em arquivo entre execuções. O programa deve:
#   - sortear uma categoria e uma palavra dela
#   - dar um número de erros permitidos de acordo com a dificuldade
#   - não aceitar letra repetida
#   - detectar vitória (todas as letras da palavra descobertas) e
#     derrota (erros esgotados) corretamente
#   - somar pontos por vitória (mais pontos quanto maior a palavra) e
#     descontar pontos por derrota
#   - carregar e salvar o placar em arquivo texto, por jogador
#   - exibir um ranking dos jogadores do maior pro menor placar ao sair
#
# Não há saída fixa (a palavra é sorteada, e o placar depende de
# quantas vezes você já jogou). Jogue até vencer, jogue até perder, e
# rode o programa DUAS vezes seguidas, para testar o placar salvo.
#
# Mistura de bugs silenciosos com pelo menos um que só aparece na
# SEGUNDA execução, depois que o placar já existe em arquivo.
# Corrigir um bug pode expor outro. Encontre e corrija todos.
# ────────────────────────────────────────────────────────────

import random

CATEGORIAS = {
    "linguagens": ["python", "javascript", "kotlin", "ruby", "golang"],
    "estruturas": ["lista", "dicionario", "conjunto", "tupla", "matriz"],
    "poo": ["heranca", "polimorfismo", "encapsulamento", "abstracao", "construtor"],
}

ERROS_POR_DIFICULDADE = {"facil": 8, "medio": 6, "dificil": 4}

ARQUIVO_PLACAR = "docs/debug/dificil/placar_forca.txt"


class Rodada:
    def __init__(self, palavra, categoria, max_erros):
        self.palavra = palavra
        self.categoria = categoria
        self.max_erros = max_erros
        self.acertadas = set()
        self.erradas = set()

    def tentar(self, letra):
        if letra in self.categoria:
            self.acertadas.add(letra)
            return True
        else:
            self.erradas.add(letra)
            return False

    def erros_restantes(self):
        return self.max_erros - len(self.acertadas)

    def venceu(self):
        for letra in self.palavra:
            if letra not in self.acertadas:
                return False
        return True

    def perdeu(self):
        return self.erros_restantes() <= 0

    def visivel(self):
        letras = [letra if letra in self.acertadas else "_" for letra in self.palavra]
        return " ".join(letras)


def sortear_rodada(dificuldade):
    categoria = random.choice(list(CATEGORIAS.keys()))
    palavra = random.choice(CATEGORIAS[categoria])
    max_erros = ERROS_POR_DIFICULDADE[dificuldade]
    return Rodada(palavra, categoria, max_erros)


def carregar_placar():
    placar = {}
    try:
        with open(ARQUIVO_PLACAR, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, pontos = linha.strip().split(",")
                placar[nome] = pontos
    except FileNotFoundError:
        pass
    return placar


def salvar_placar(placar):
    with open(ARQUIVO_PLACAR, "w", encoding="utf-8") as arquivo:
        for nome, pontos in placar.items():
            arquivo.write(f"{nome},{pontos}\n")


def exibir_ranking(placar):
    print("\n=== RANKING ===")
    ranking = sorted(placar.items(), key=lambda item: item[0], reverse=True)
    for posicao, (nome, pontos) in enumerate(ranking, start=1):
        print(f"  {posicao}. {nome}: {pontos} pontos")


def jogar_rodada(rodada):
    while not rodada.venceu() and not rodada.perdeu():
        print(f"\nCategoria: {rodada.categoria}")
        print(f"Palavra:    {rodada.visivel()}")
        print(f"Erradas:    {sorted(rodada.erradas) or 'nenhuma'}")
        print(f"Tentativas: {rodada.erros_restantes()}")

        chute = input("Letra: ").strip().lower()

        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra.")
            continue

        if chute in rodada.acertadas or chute in rodada.erradas:
            print("Você já tentou essa letra.")
            continue

        if rodada.tentar(chute):
            print("Certo!")
        else:
            print("Errou.")

    if rodada.venceu():
        print(f"\nVocê venceu! A palavra era '{rodada.palavra}'.")
        return True
    else:
        print(f"\nVocê perdeu. A palavra era '{rodada.palavra}'.")
        return False


def main():
    print("=== JOGO DA FORCA: DESAFIO FINAL ===")
    nome = input("Seu nome: ").strip()
    dificuldade = input("Dificuldade (facil/medio/dificil): ").strip().lower()

    placar = carregar_placar()
    if nome not in placar:
        placar[nome] = 0

    jogando = True
    while jogando:
        rodada = sortear_rodada(dificuldade)
        venceu = jogar_rodada(rodada)

        if venceu:
            placar[nome] += len(rodada.categoria) * 10
        else:
            placar[nome] -= 5

        print(f"Pontuação de {nome}: {placar[nome]}")

        continuar = input("\nJogar de novo? (s/n): ").strip().lower()
        if continuar != "s":
            jogando = False

    salvar_placar(placar)
    exibir_ranking(placar)


if __name__ == "__main__":
    main()
