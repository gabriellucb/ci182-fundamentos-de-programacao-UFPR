"""Truco - random, datetime, math.

Intervalo entre aulas, pessoal no Centro Academico. Voce vs. Amigo, primeiro
a 12 pontos vence. Voce pode pedir truco, seis, nove e doze - e o amigo
tambem pede quando acha que tem mão boa. Blefe por sua conta e risco.

Conceitos: import, import ... as, random.shuffle, random.randrange,
datetime.now(), strftime, math.floor, funcoes, listas, dicionarios.
"""

import random
import math
import datetime as dt

CARTAS = ["4", "5", "6", "7", "Q", "J", "K", "A", "2", "3"]
NAIPES = ["♣", "♥", "♦", "♠"]
PONTOS_PARA_VENCER = 12

FORCA_BASE = {
    "4": 1, "5": 2, "6": 3, "7": 4,
    "Q": 5, "J": 6, "K": 7, "A": 8, "2": 9, "3": 10,
}

# Manilhas tem hierarquia propria (paus > copas > espadas > ouros)
FORCA_MANILHA = {"♣": 14, "♥": 13, "♠": 12, "♦": 11}

NIVEIS = [1, 3, 6, 9, 12]
NOMES = {3: "Truco", 6: "Seis", 9: "Nove", 12: "Doze"}


# Baralho e forcas

def criar_baralho():
    baralho = []
    for carta in CARTAS:
        for naipe in NAIPES:
            baralho.append(carta + naipe)
    return baralho


def manilha_da_vira(vira):
    valor_vira = vira[:-1]
    idx = CARTAS.index(valor_vira)
    return CARTAS[(idx + 1) % len(CARTAS)]


def forca_carta(carta, manilha):
    valor = carta[:-1]
    naipe = carta[-1]
    if valor == manilha:
        return FORCA_MANILHA[naipe]
    return FORCA_BASE[valor]


def forca_mao(mao, manilha):
    total = 0
    for carta in mao:
        total += forca_carta(carta, manilha)
    return total


def comparar(c1, c2, manilha):
    """Retorna 1 se c1 vence, -1 se c2 vence, 0 se empata."""
    f1 = forca_carta(c1, manilha)
    f2 = forca_carta(c2, manilha)
    if f1 > f2:
        return 1
    if f2 > f1:
        return -1
    return 0


# Exibicao e input

def label_carta(carta, manilha):
    marcador = "★" if carta[:-1] == manilha else " "
    return marcador + carta


def exibir_mao(mao, manilha):
    partes = []
    for i, carta in enumerate(mao):
        partes.append(f"[{i + 1}]{label_carta(carta, manilha)}")
    return "  ".join(partes)


def escolher_carta(mao, manilha):
    while True:
        try:
            idx = int(input(f"Escolha (1-{len(mao)}): ")) - 1
            if 0 <= idx < len(mao):
                return mao.pop(idx)
        except ValueError:
            pass
        print(f"Opcao invalida. Sua mao: {exibir_mao(mao, manilha)}")


# Negociacao de truco

def pode_subir(valor):
    return NIVEIS.index(valor) + 1 < len(NIVEIS)


def ia_responde(mao_ia, manilha, tem_proximo):
    """IA decide aceitar, relancar ou fugir com base na forca da mao."""
    forca = forca_mao(mao_ia, manilha)
    dado = random.randint(1, 10)
    if forca >= 25:
        return "r" if tem_proximo and dado >= 8 else "a"
    if forca >= 15:
        return "a" if dado >= 3 else "f"
    return "f" if dado >= 4 else "a"


def player_responde(tem_proximo):
    opcoes = "a=aceitar / r=relancar / f=fugir" if tem_proximo else "a=aceitar / f=fugir"
    while True:
        r = input(f"  ({opcoes}): ").strip().lower()
        if r in ("a", "f"):
            return r
        if r == "r" and tem_proximo:
            return r
        print("  Opcao invalida.")


def negociar(nivel, chamador, mao_ia, manilha):
    """
    Conduz a negociacao de apostas a partir de 'nivel', com 'chamador' iniciando.
    Retorna (pontos, "continua" | "voce_vence" | "amigo_vence").
    """
    idx = NIVEIS.index(nivel) + 1

    while idx < len(NIVEIS):
        prox_valor = NIVEIS[idx]
        penalidade = NIVEIS[idx - 1]
        tem_proximo = idx + 1 < len(NIVEIS)

        nome_chamador = "Voce" if chamador == "voce" else "Amigo"
        print(f"  {nome_chamador}: {NOMES[prox_valor]}!")

        respondedor = "amigo" if chamador == "voce" else "voce"

        if respondedor == "amigo":
            resp = ia_responde(mao_ia, manilha, tem_proximo)
        else:
            resp = player_responde(tem_proximo)

        if resp == "f":
            if respondedor == "amigo":
                print(f"  Amigo correu. Voce leva {penalidade} ponto(s).")
                return penalidade, "voce_vence"
            print(f"  Voce correu. Amigo leva {penalidade} ponto(s).")
            return penalidade, "amigo_vence"

        if resp == "a":
            if respondedor == "amigo":
                print(f"  Amigo aceitou. Mao vale {prox_valor} ponto(s).")
            else:
                print(f"  Aceito. Mao vale {prox_valor} ponto(s).")
            return prox_valor, "continua"

        chamador = respondedor
        idx += 1

    return NIVEIS[-1], "continua"


def ia_quer_chamar(valor_mao, mao_ia, manilha):
    if not pode_subir(valor_mao):
        return False
    forca = forca_mao(mao_ia, manilha)
    dado = random.randint(1, 10)
    return dado >= (4 if forca >= 20 else 8)


# Mao e jogo 

def jogar_mao(placar_voce, placar_amigo):
    print(f"\n=== MAO -- Placar: Voce {placar_voce} x Amigo {placar_amigo} ===\n")

    baralho = criar_baralho()
    random.shuffle(baralho)

    vira = baralho[0]
    manilha = manilha_da_vira(vira)
    print(f"Vira: {vira}   ->   Manilha: {manilha} (★)")
    hierarquia = f"{manilha}♣ > {manilha}♥ > {manilha}♦ > {manilha}♠"
    print(f"Hierarquia: {hierarquia}\n")

    mao_voce = baralho[1:4]
    mao_amigo = baralho[4:7]

    print(f"\nSua mao: {exibir_mao(mao_voce, manilha)}\n")

    valor_mao = 1
    vitorias_voce = 0
    vitorias_amigo = 0
    primeira_rodada = None

    for num_rodada in range(1, 4):
        print(f"--- Rodada {num_rodada} (mao vale {valor_mao} pt) ---")
        print(f"Sua mao: {exibir_mao(mao_voce, manilha)}")

        if ia_quer_chamar(valor_mao, mao_amigo, manilha):
            valor_mao, res = negociar(valor_mao, "amigo", mao_amigo, manilha)
            if res == "voce_vence":
                return placar_voce + valor_mao, placar_amigo
            if res == "amigo_vence":
                return placar_voce, placar_amigo + valor_mao
        elif pode_subir(valor_mao):
            r = input("Pedir truco? (s/n): ").strip().lower()
            if r == "s":
                valor_mao, res = negociar(valor_mao, "voce", mao_amigo, manilha)
                if res == "voce_vence":
                    return placar_voce + valor_mao, placar_amigo
                if res == "amigo_vence":
                    return placar_voce, placar_amigo + valor_mao

        carta_voce = escolher_carta(mao_voce, manilha)
        carta_amigo = mao_amigo.pop(random.randrange(len(mao_amigo)))

        print(f"Voce jogou:  {label_carta(carta_voce, manilha)}")
        print(f"Amigo jogou: {label_carta(carta_amigo, manilha)}")

        res = comparar(carta_voce, carta_amigo, manilha)
        if res == 1:
            vitorias_voce += 1
            if primeira_rodada is None:
                primeira_rodada = "voce"
            print("-> Voce venceu a rodada!\n")
        elif res == -1:
            vitorias_amigo += 1
            if primeira_rodada is None:
                primeira_rodada = "amigo"
            print("-> Amigo venceu a rodada.\n")
        else:
            print("-> Empate na rodada.\n")

        if vitorias_voce == 2 or vitorias_amigo == 2:
            break

    if vitorias_voce > vitorias_amigo:
        print(f"Voce venceu a mao! ({vitorias_voce}-{vitorias_amigo})")
        return placar_voce + valor_mao, placar_amigo
    if vitorias_amigo > vitorias_voce:
        print(f"Amigo venceu a mao. ({vitorias_amigo}-{vitorias_voce})")
        return placar_voce, placar_amigo + valor_mao
    if primeira_rodada == "voce":
        print("Empate em rodadas -- voce leva por ter vencido a primeira.")
        return placar_voce + valor_mao, placar_amigo
    if primeira_rodada == "amigo":
        print("Empate em rodadas -- amigo leva por ter vencido a primeira.")
        return placar_voce, placar_amigo + valor_mao
    print("Todas as rodadas empataram -- ninguem pontua.")
    return placar_voce, placar_amigo


def main():
    inicio = dt.datetime.now()
    print(f"=== TRUCO NO CENTRO ACADÊMICO -- {inicio.strftime('%d/%m/%Y %H:%M')} ===")
    print(f"Primeiro a {PONTOS_PARA_VENCER} pontos vence.\n")

    placar_voce = 0
    placar_amigo = 0
    total_maos = 0

    while placar_voce < PONTOS_PARA_VENCER and placar_amigo < PONTOS_PARA_VENCER:
        total_maos += 1
        placar_voce, placar_amigo = jogar_mao(placar_voce, placar_amigo)
        print(f"Placar: Voce {placar_voce} x Amigo {placar_amigo}")
        if placar_voce < PONTOS_PARA_VENCER and placar_amigo < PONTOS_PARA_VENCER:
            input("\n[Enter para proxima mao]")

    duracao = math.floor((dt.datetime.now() - inicio).total_seconds() / 60)

    print("\n" + "=" * 36)
    if placar_voce >= PONTOS_PARA_VENCER:
        print("VOCE VENCEU O JOGO!")
    else:
        print("Amigo venceu o jogo.")
    print(f"Placar final: Voce {placar_voce} x Amigo {placar_amigo}")
    print(f"Duracao: ~{duracao} min  |  {total_maos} maos jogadas")
    print(f"Aproveitamento: {math.floor(placar_voce * 100 / total_maos)}%")


main()
