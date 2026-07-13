"""Regras de uma disputa de pênaltis: cada cobrança, o fim antecipado e a morte súbita."""

import random
import time

import visual
from jogadores import pedir_direcao

# Vários jeitos de narrar cada desfecho, sorteados a cada cobrança pra que uma
# disputa longa não fique repetitiva. Os campos {batedor}, {goleiro} e {lugar}
# são preenchidos na hora ({lugar} vira "no meio", "no canto esquerdo" ou
# "no canto direito", veja local_do_chute).
FRASES_GOL_LADO_ERRADO = [
    "{batedor} deslocou o goleiro e mandou {lugar}. Sem chance pro {goleiro}!",
    "{goleiro} foi pro outro lado e {batedor} mandou {lugar}, no fundo do gol!",
    "Frieza total: {batedor} esperou o {goleiro} escolher o lado e bateu {lugar}.",
    "No contrapé! {batedor} bateu {lugar} e o {goleiro} pulou pro lado oposto.",
    "{goleiro} adivinhou errado e {batedor} não perdoou: bola mansa {lugar}.",
]
FRASES_GOL_NAO_ALCANCOU = [
    "{batedor} carimbou {lugar}. O {goleiro} até foi no lugar certo, mas não segurou!",
    "Golaço do {batedor} {lugar}! O {goleiro} adivinhou, encostou, e não deu.",
    "{goleiro} foi no lugar certo, mas {batedor} bateu firme demais {lugar}. No fundo!",
    "Que categoria do {batedor} {lugar}, onde nem o {goleiro} no lugar certo alcança.",
]
FRASES_DEFESA = [
    "DEFENDAÇA! {goleiro} adivinhou {lugar} e espalmou a batida do {batedor}!",
    "{goleiro} sentiu o {batedor}, foi {lugar} e pegou! Paredão.",
    "Muralha! {goleiro} foi {lugar} e agarrou a cobrança do {batedor}.",
    "{batedor} bateu {lugar}, mas achou o {goleiro} inspirado. Defendeu!",
]
FRASES_FORA = [
    "{batedor} pegou embaixo demais e mandou por cima do gol. A pressão pesou.",
    "Isolou! {batedor} tentou {lugar}, mas jogou a bola nas nuvens.",
    "Que desperdício do {batedor}! A bola foi parar lá na arquibancada.",
    "{batedor} exagerou na força e mandou raspando a trave, pra fora. Perdeu!",
]


def pausa(segundos=0.8):
    time.sleep(segundos)


def celebrar():
    print(visual.cor("     ⚽  G O O O O L !  ⚽", visual.VERDE + visual.NEGRITO))


def local_do_chute(direcao):
    """Vira o texto certo pra narração: 'meio' não é canto."""
    if direcao == "meio":
        return "no meio"
    if direcao == "esquerda":
        return "no canto esquerdo"
    return "no canto direito"


def narrar(frases, batedor, goleiro, direcao, codigo, icone):
    frase = random.choice(frases).format(
        batedor=batedor.nome,
        goleiro=goleiro.nome,
        lugar=local_do_chute(direcao),
    )
    print(visual.cor(f"     {icone} {frase}", codigo))


def cobranca(batedor, goleiro, peso_pressao, decisiva, controla_direcao, controla_goleiro, rotulo=""):
    if rotulo:
        print(visual.cor(f"\n   ┈┈┈ {rotulo} ┈┈┈", visual.CINZA))

    etiqueta = visual.cor("   [ DECISIVA ]", visual.AMARELO + visual.NEGRITO) if decisiva else ""
    print(f"\n  {visual.cor('⚽ ' + batedor.nome, visual.CIANO + visual.NEGRITO)}{etiqueta}")
    print(f"     {visual.barra(batedor.confianca)} {int(batedor.confianca)}% de confiança")

    if goleiro.defesas_seguidas > 0:
        print(visual.cor(f"     🔥 {goleiro.nome} está embalado: {goleiro.defesas_seguidas} defesa(s) seguida(s)!", visual.AMARELO))

    # Chance real de acertar o alvo nesta cobrança, já com a pressão da fase,
    # o extra de cobrança decisiva e o goleiro embalado descontados. Só aparece
    # quando a pressão realmente derruba a confiança de fundo do jogador.
    pressao_do_goleiro = goleiro.defesas_seguidas * 5
    taxa_alvo = batedor.taxa_de_acertar_o_alvo(peso_pressao + pressao_do_goleiro, decisiva)
    if int(taxa_alvo) < int(batedor.confianca):
        print(visual.cor(f"     🎯 com a pressão, {int(taxa_alvo)}% de acerto no alvo nesta cobrança", visual.AMARELO))

    if controla_direcao:
        direcao_bola = pedir_direcao(visual.cor("     → Pra onde você bate? (esquerda/meio/direita): ", visual.AZUL))
    else:
        direcao_bola = batedor.escolher_direcao()

    if controla_goleiro:
        lado_goleiro = pedir_direcao(visual.cor(f"     → Pra que lado o {goleiro.nome} pula? (esquerda/meio/direita): ", visual.AZUL))
    else:
        lado_goleiro = goleiro.escolher_lado()

    pausa()

    if random.uniform(0, 100) > taxa_alvo:
        narrar(FRASES_FORA, batedor, goleiro, direcao_bola, visual.VERMELHO, "😖")
        marcou = False
    elif direcao_bola != lado_goleiro:
        celebrar()
        narrar(FRASES_GOL_LADO_ERRADO, batedor, goleiro, direcao_bola, visual.VERDE, "⚽")
        marcou = True
    elif random.uniform(0, 100) <= goleiro.chance_de_defender():
        narrar(FRASES_DEFESA, batedor, goleiro, direcao_bola, visual.VERMELHO, "🧤")
        marcou = False
    else:
        celebrar()
        narrar(FRASES_GOL_NAO_ALCANCOU, batedor, goleiro, direcao_bola, visual.VERDE, "⚽")
        marcou = True

    batedor.registrar_cobranca(marcou, decisiva)
    batedor.atualizar_confianca(marcou)
    goleiro.atualizar_confianca(not marcou)

    # O adversário só mostra o tipo de goleiro depois da primeira cobrança
    # contra ele: você joga a primeira às cegas e aprende com o que viu.
    if controla_direcao and not goleiro.caracteristica_revelada:
        goleiro.caracteristica_revelada = True
        print(visual.cor(f"     🔎 Deu pra sentir: {goleiro.nome} é um goleiro do tipo {goleiro.caracteristica}.", visual.CINZA))

    return marcou


def partida_decidida(placar_a, placar_b, restantes_a, restantes_b):
    if placar_a > placar_b + restantes_b:
        return True
    if placar_b > placar_a + restantes_a:
        return True
    return False


def eh_decisiva(placar_batedor, placar_adversario, restantes_batedor_apos, restantes_adversario):
    """Cobrança decisiva: marcar já fecha o jogo, ou errar já entrega o jogo."""
    marcando = partida_decidida(placar_batedor + 1, placar_adversario, restantes_batedor_apos, restantes_adversario)
    errando = partida_decidida(placar_batedor, placar_adversario, restantes_batedor_apos, restantes_adversario)
    return marcando or errando


def escolher_reserva(reservas):
    print(visual.cor("     Escolha o próximo cobrador (reservas que ainda não bateram):", visual.AZUL))
    for i, jogador in enumerate(reservas, start=1):
        print(f"       {i}. {jogador}")
    while True:
        entrada = input("     Número do cobrador: ").strip()
        if not entrada.isdigit():
            print("       Digite um número válido.")
            continue
        indice = int(entrada) - 1
        if indice < 0 or indice >= len(reservas):
            print("       Número fora da lista.")
            continue
        return reservas.pop(indice)


def morte_subita(brasil, rival, peso_pressao, marcas_brasil=None, marcas_rival=None):
    if marcas_brasil is None:
        marcas_brasil = []
    if marcas_rival is None:
        marcas_rival = []

    print("\n" + visual.moldura("MORTE SÚBITA", visual.VERMELHO))
    pausa()

    # Regra real: os jogadores que ainda não bateram cobram primeiro. Você
    # escolhe as reservas uma a uma; quando elas acabam, o rodízio recomeça
    # pelos 5 escalados do início.
    reservas_disponiveis = list(brasil.reservas)
    indice_escalados = 0
    indice_rival = 0
    rodada = 0

    while True:
        rodada += 1

        if reservas_disponiveis:
            batedor_brasil = escolher_reserva(reservas_disponiveis)
        else:
            batedor_brasil = brasil.batedores[indice_escalados % len(brasil.batedores)]
            indice_escalados += 1

        batedor_rival = rival.batedores[indice_rival % len(rival.batedores)]
        indice_rival += 1

        gol_brasil = cobranca(batedor_brasil, rival.goleiro, peso_pressao, True, True, False,
                              rotulo=f"Morte súbita {rodada}: {brasil.nome} na bola")
        marcas_brasil.append("gol" if gol_brasil else "erro")
        gol_rival = cobranca(batedor_rival, brasil.goleiro, peso_pressao, True, False, True,
                             rotulo=f"Morte súbita {rodada}: {rival.nome} na bola")
        marcas_rival.append("gol" if gol_rival else "erro")

        print("\n" + visual.placar(brasil, marcas_brasil, rival, marcas_rival))

        if gol_brasil and not gol_rival:
            return brasil
        if gol_rival and not gol_brasil:
            return rival


def disputa_penaltis(brasil, rival, peso_pressao):
    print("\n" + visual.moldura("DISPUTA DE PÊNALTIS", visual.AMARELO))
    print(f"   {brasil.bandeira} {visual.cor(brasil.nome, visual.NEGRITO)}   x   {rival.bandeira} {visual.cor(rival.nome, visual.NEGRITO)}")
    pausa()

    placar_brasil = 0
    placar_rival = 0
    feitas_brasil = 0
    feitas_rival = 0
    marcas_brasil = []
    marcas_rival = []

    for rodada in range(5):
        if partida_decidida(placar_brasil, placar_rival, 5 - feitas_brasil, 5 - feitas_rival):
            break

        decisiva = eh_decisiva(placar_brasil, placar_rival, 4 - rodada, 5 - rodada) or rodada == 4
        gol = cobranca(brasil.batedores[rodada], rival.goleiro, peso_pressao, decisiva, True, False,
                       rotulo=f"{rodada + 1}ª cobrança do Brasil")
        if gol:
            placar_brasil += 1
        marcas_brasil.append("gol" if gol else "erro")
        feitas_brasil += 1
        print("\n" + visual.placar(brasil, marcas_brasil, rival, marcas_rival))

        if partida_decidida(placar_brasil, placar_rival, 5 - feitas_brasil, 5 - feitas_rival):
            break

        decisiva = eh_decisiva(placar_rival, placar_brasil, 4 - rodada, 4 - rodada) or rodada == 4
        gol = cobranca(rival.batedores[rodada], brasil.goleiro, peso_pressao, decisiva, False, True,
                       rotulo=f"{rodada + 1}ª cobrança do {rival.nome}")
        if gol:
            placar_rival += 1
        marcas_rival.append("gol" if gol else "erro")
        feitas_rival += 1
        print("\n" + visual.placar(brasil, marcas_brasil, rival, marcas_rival))

    if placar_brasil == placar_rival:
        return morte_subita(brasil, rival, peso_pressao, marcas_brasil, marcas_rival)
    if placar_brasil > placar_rival:
        return brasil
    return rival
