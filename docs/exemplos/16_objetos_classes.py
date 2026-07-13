"""Craque em Formação: carreira de um jogador de futebol contada em objetos.

Você cria um garoto de 17 anos saindo da base e acompanha a carreira dele
temporada após temporada: joga partidas, evolui (ou não), pode ser vendido
pra outro clube e, se a idade cobrar o preço, aposenta com a bola debaixo
do braço. Cada Jogador é um objeto com sua própria ficha e seus próprios gols.

Conceitos: class, __init__, self, atributos de instância e de classe,
métodos, __str__, dicionários, condicionais, laços, funções, módulo random.
"""

import random


class Jogador:
    OVERALL_MAXIMO = 99
    OVERALL_MINIMO = 40
    IDADE_DECLINIO = 30

    MULTIPLICADOR_GOL = {"Atacante": 0.6, "Meio-campo": 0.35, "Zagueiro": 0.15}
    MULTIPLICADOR_ASSISTENCIA = {"Atacante": 0.25, "Meio-campo": 0.45, "Zagueiro": 0.2}

    def __init__(self, nome, posicao, clube, overall=60, idade=17):
        self.nome = nome
        self.posicao = posicao
        self.clube = clube
        self.overall = overall
        self.idade = idade
        self.gols = 0
        self.assistencias = 0
        self.jogos = 0

    def jogar_partida(self):
        self.jogos += 1
        gols_partida = 0
        assistencias_partida = 0

        chance_gol = (self.overall / 100) * self.MULTIPLICADOR_GOL[self.posicao]
        if random.random() < chance_gol:
            gols_partida = random.randint(1, 2)
            self.gols += gols_partida

        chance_assistencia = (self.overall / 100) * self.MULTIPLICADOR_ASSISTENCIA[self.posicao]
        if random.random() < chance_assistencia:
            assistencias_partida = random.randint(1, 2)
            self.assistencias += assistencias_partida

        return gols_partida, assistencias_partida

    def evoluir(self, pontos):
        overall_antes = self.overall
        self.overall = min(self.overall + pontos, Jogador.OVERALL_MAXIMO)
        return self.overall - overall_antes

    def envelhecer(self):
        self.idade += 1
        if self.idade < 24:
            ganho = random.randint(1, 3)
            return self.evoluir(ganho)
        elif self.idade < self.IDADE_DECLINIO:
            ganho = random.randint(0, 1)
            return self.evoluir(ganho)
        else:
            perda = random.randint(1, 2)
            self.overall = max(self.overall - perda, self.OVERALL_MINIMO)
            return -perda

    def transferir(self, novo_clube):
        clube_antigo = self.clube
        self.clube = novo_clube
        return clube_antigo

    def aposentado(self):
        return self.overall <= self.OVERALL_MINIMO

    def __str__(self):
        proporcao = self.overall / Jogador.OVERALL_MAXIMO
        barra_cheia = int(proporcao * 20)
        barra = "█" * barra_cheia + "░" * (20 - barra_cheia)
        return (
            f"{self.nome} | {self.posicao} | {self.clube}\n"
            f"  OVR {self.overall} [{barra}] {self.idade} anos\n"
            f"  {self.jogos} jogos, {self.gols} gols, {self.assistencias} assistências"
        )


def escolher_posicao():
    posicoes = list(Jogador.MULTIPLICADOR_GOL.keys())
    print("Escolha a posição do seu jogador:\n")
    for i, posicao in enumerate(posicoes, start=1):
        print(f"  {i}. {posicao}")
    print()

    while True:
        entrada = input("Posição (número): ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(posicoes):
            return posicoes[int(entrada) - 1]
        print("Número inválido, tente de novo.")


def jogar_temporada(jogador, num_partidas=5):
    print(f"\n=== Temporada de {jogador.nome} pelo {jogador.clube} ===")
    gols_temporada = 0
    assistencias_temporada = 0

    for rodada in range(1, num_partidas + 1):
        gols, assistencias = jogador.jogar_partida()
        gols_temporada += gols
        assistencias_temporada += assistencias
        if gols > 0 or assistencias > 0:
            print(f"Rodada {rodada}: {gols} gol(s), {assistencias} assistência(s).")
        else:
            print(f"Rodada {rodada}: sem participação direta no gol.")

    print(f"\nFim de temporada: {gols_temporada} gols e {assistencias_temporada} assistências.")

    variacao = jogador.envelhecer()
    if variacao > 0:
        print(f"{jogador.nome} evoluiu! Overall subiu {variacao} ponto(s), agora {jogador.overall}.")
    elif variacao < 0:
        print(f"A idade começou a pesar. Overall caiu {abs(variacao)} ponto(s), agora {jogador.overall}.")
    else:
        print(f"Overall se manteve em {jogador.overall}.")


def main():
    print("=== CRAQUE EM FORMAÇÃO ===\n")
    nome = input("Nome do seu jogador: ").strip()
    if nome == "":
        nome = "Craque"

    posicao = escolher_posicao()
    clube = input("\nClube da base onde ele começa: ").strip()
    if clube == "":
        clube = "Base"

    jogador = Jogador(nome, posicao, clube)
    print(f"\n{jogador}\n")

    while True:
        print("O que fazer?")
        print("  1. Jogar temporada")
        print("  2. Ver ficha")
        print("  3. Transferir para outro clube")
        print("  4. Encerrar carreira")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            jogar_temporada(jogador)
            if jogador.aposentado():
                print(f"\n{jogador.nome} não aguenta mais o ritmo. Hora de pendurar as chuteiras.")
                break
        elif escolha == "2":
            print(f"\n{jogador}\n")
        elif escolha == "3":
            novo_clube = input("Nome do novo clube: ").strip()
            if novo_clube == "":
                print("Transferência cancelada.")
                continue
            clube_antigo = jogador.transferir(novo_clube)
            print(f"{jogador.nome} saiu do {clube_antigo} e assinou com o {novo_clube}!")
        elif escolha == "4":
            print(f"\n{jogador.nome} encerra a carreira por vontade própria.")
            break
        else:
            print("Opção inválida.\n")
            continue
        print()

    print("\n=== FIM DE CARREIRA ===")
    print(jogador)


if __name__ == "__main__":
    main()
