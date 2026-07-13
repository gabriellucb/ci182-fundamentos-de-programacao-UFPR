"""Copa do Mundo de Pênaltis: projeto grande com classes, nervosismo e disputa por pênaltis de verdade.

O Brasil por enquanto não avançou nem com pênaltis nessas últimas Copas.
Aqui você pode mudar isso e tornar o Brasil Hexacampeão (ou pelo menos tentar)!
Nesse projeto você escolhe a dificuldade, escala 5 batedores (na ordem que
quiser), bate os pênaltis do Brasil e defende como goleiro quando é o adversário
na bola. Cada jogador carrega uma característica que muda como ele bate ou defende,
e uma confiança que sobe com gol e desaba com erro, ficando mais frágil conforme
a fase aperta e viajando com o jogador pelo campeonato inteiro. Os adversários são
sorteados por dificuldade a cada Copa, então o caminho até a final não é igual duas
vezes. No fim, você vê o aproveitamento de cada batedor, e o resultado da campanha
fica salvo pra próxima vez que você jogar.

O projeto é dividido em módulos, cada um com uma responsabilidade:
- jogadores.py: as classes Jogador, Goleiro e Selecao
- campeonato.py: fases, grupos de dificuldade e as escalações dos adversários
- partida.py: as regras de uma disputa de pênaltis
- visual.py: cores, molduras, barra de confiança e o placar
- main.py (este arquivo): escalação do Brasil e o loop do chaveamento

Conceitos: class, __init__, self, atributos de instância, métodos, __str__, listas de
objetos, dicionários, condicionais, laços, funções, módulos, arquivos.
"""

import os

import visual
from jogadores import Goleiro, Selecao, criar_jogador
from campeonato import BANDEIRAS, PESO_PRESSAO, criar_selecao_rival, montar_fases, sortear_adversarios
from partida import disputa_penaltis, pausa

ARQUIVO_HISTORICO = os.path.join(os.path.dirname(__file__), "historico.txt")


def escolher_dificuldade():
    print(visual.cor("\n  Escolha a dificuldade:", visual.NEGRITO))
    print(f"    {visual.cor('1', visual.VERDE)}. Fácil    (começa já nas oitavas)")
    print(f"    {visual.cor('2', visual.AMARELO)}. Normal   (chaveamento completo, dos dezesseis avos à final)")
    print(f"    {visual.cor('3', visual.VERMELHO)}. Difícil  (só time forte desde cedo, três seleções de elite no fim)")
    opcoes = {"1": "facil", "2": "normal", "3": "dificil"}
    while True:
        entrada = input("  Opção: ").strip()
        if entrada in opcoes:
            return opcoes[entrada]
        print("    Digite 1, 2 ou 3.")


def ordenar_por_confianca(jogadores):
    """Devolve os jogadores do mais confiante ao menos confiante."""
    chaves = []
    for indice, jogador in enumerate(jogadores):
        chaves.append((-jogador.confianca, indice, jogador))
    chaves.sort()
    return [jogador for _, _, jogador in chaves]


def linha_escolha(numero, jogador):
    """Uma linha de opção com número colorido e barra de confiança do jogador."""
    etiqueta = visual.cor(f"{numero:>2}", visual.CIANO + visual.NEGRITO)
    nome = jogador.nome.ljust(20)
    return f"    {etiqueta}. {nome} {visual.barra(jogador.confianca)} {int(jogador.confianca)}%"


def escolher_escalacao(elenco):
    print("\n" + visual.moldura("ESCALE SEUS 5 BATEDORES", visual.VERDE))
    print(visual.cor("  A lista vem por confiança, do mais confiante ao menos.\n", visual.CINZA))

    restantes = list(elenco)
    escalados = []
    while len(escalados) < 5:
        ordenados = ordenar_por_confianca(restantes)
        faltam = 5 - len(escalados)
        verbo = "Falta" if faltam == 1 else "Faltam"
        print(visual.cor(f"  {verbo} {faltam} pra escalar. Disponíveis:", visual.NEGRITO))
        for i, jogador in enumerate(ordenados, start=1):
            print(linha_escolha(i, jogador))

        entrada = input(f"\n  {len(escalados) + 1}º cobrador (número): ").strip()
        if not entrada.isdigit():
            print("    Digite um número válido.\n")
            continue
        indice = int(entrada) - 1
        if indice < 0 or indice >= len(ordenados):
            print("    Número fora da lista.\n")
            continue

        escolhido = ordenados[indice]
        escalados.append(escolhido)
        restantes.remove(escolhido)
        print(visual.cor(f"  ✔ {escolhido.nome} confirmado como {len(escalados)}º cobrador!\n", visual.VERDE))

    return escalados, restantes


def escolher_goleiro(opcoes):
    print(visual.moldura("ESCOLHA O GOLEIRO", visual.AZUL))
    for i, goleiro in enumerate(opcoes, start=1):
        etiqueta = visual.cor(f"{i:>2}", visual.CIANO + visual.NEGRITO)
        print(f"    {etiqueta}. 🧤 {goleiro.nome} ({goleiro.caracteristica})")
    while True:
        entrada = input("\n  Goleiro (número): ").strip()
        if not entrada.isdigit():
            print("    Digite um número válido.")
            continue
        indice = int(entrada) - 1
        if 0 <= indice < len(opcoes):
            escolhido = opcoes[indice]
            print(visual.cor(f"  ✔ {escolhido.nome} no gol!\n", visual.VERDE))
            return escolhido
        print("    Número fora da lista.")


def registrar_campanha(dificuldade, resultado, detalhe):
    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{dificuldade};{resultado};{detalhe}\n")


def mostrar_historico():
    try:
        with open(ARQUIVO_HISTORICO, encoding="utf-8") as arquivo:
            linhas = [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        return

    # Ignora linhas fora do formato "dificuldade;resultado;detalhe" (por
    # exemplo, se o arquivo for editado à mão), em vez de quebrar.
    campanhas = [partes for partes in (linha.split(";") for linha in linhas) if len(partes) == 3]
    if not campanhas:
        return

    titulos = sum(1 for partes in campanhas if partes[1] == "campeao")
    print(visual.cor(f"  🗂  Campanhas anteriores: {len(campanhas)}   🏆 Títulos: {titulos}", visual.CINZA))
    for dificuldade, _, detalhe in campanhas[-3:]:
        print(visual.cor(f"     [{dificuldade}] {detalhe}", visual.CINZA))
    print()


def mostrar_estatisticas(brasil):
    usados = [jogador for jogador in brasil.batedores + brasil.reservas if jogador.cobrancas > 0]
    if not usados:
        return

    print("\n" + visual.moldura("APROVEITAMENTO DOS BATEDORES", visual.CIANO))
    ranking = []
    for indice, jogador in enumerate(usados):
        ranking.append((jogador.aproveitamento(), jogador.gols, indice, jogador))
    ranking.sort(reverse=True)
    for taxa, _, _, jogador in ranking:
        nome = jogador.nome.ljust(20)
        print(f"    {nome} {visual.barra(taxa)} {jogador.gols}/{jogador.cobrancas} ({taxa:.0f}%)")

    melhor = None
    for jogador in usados:
        atual = (jogador.gols_decisivos, jogador.gols)
        if melhor is None or atual > (melhor.gols_decisivos, melhor.gols):
            melhor = jogador
    if melhor is not None and melhor.gols_decisivos > 0:
        print(visual.cor(f"\n    ⭐ Cara da Copa: {melhor.nome}, {melhor.gols_decisivos} gol(s) decisivo(s)", visual.AMARELO + visual.NEGRITO))


def main():
    print(visual.cor("\n  🏆⚽ ================================== ⚽🏆", visual.VERDE + visual.NEGRITO))
    print(visual.cor("       C O P A   D E   P Ê N A L T I S", visual.AMARELO + visual.NEGRITO))
    print(visual.cor("  🏆⚽ ================================== ⚽🏆", visual.VERDE + visual.NEGRITO))
    print("  O Brasil só está avançando nos pênaltis nessa Copa.")
    print("  Escale seus batedores, escolha o goleiro e boa sorte.\n")
    mostrar_historico()

    dificuldade = escolher_dificuldade()

    elenco_brasil = [
        criar_jogador("Gabriel Magalhães", "Padrão"),
        criar_jogador("Marquinhos", "Alta Confiança"),
        criar_jogador("Danilo", "Padrão"),
        criar_jogador("Douglas Santos", "Finalizador Técnico"),
        criar_jogador("Casemiro", "Alta Confiança"),
        criar_jogador("Bruno Guimarães", "Padrão"),
        criar_jogador("Lucas Paquetá", "Finalizador Técnico"),
        criar_jogador("Vinícius Jr", "Chute Forte"),
        criar_jogador("Neymar Jr", "Finalizador Técnico"),
        criar_jogador("Raphinha", "Alta Confiança"),
    ]
    goleiros_brasil = [
        Goleiro("Alisson", "Parede"),
        Goleiro("Ederson", "Antecipa"),
        Goleiro("Bento", "Lado Preferido"),
    ]

    batedores_brasil, reservas_brasil = escolher_escalacao(elenco_brasil)
    goleiro_brasil = escolher_goleiro(goleiros_brasil)
    brasil = Selecao("Brasil", batedores_brasil, goleiro_brasil, reservas_brasil, bandeira=BANDEIRAS["Brasil"])

    fases = montar_fases(dificuldade)
    sorteio = sortear_adversarios(fases)

    for fase, _ in fases:
        nome_rival = sorteio[fase]
        rival = criar_selecao_rival(nome_rival)
        peso_pressao = PESO_PRESSAO[fase]

        print("\n" + visual.moldura(fase.upper(), visual.AMARELO))
        print(f"   {brasil.bandeira} Brasil   x   {rival.bandeira} {nome_rival}")
        pausa(1.5)

        vencedor = disputa_penaltis(brasil, rival, peso_pressao)

        if vencedor is not brasil:
            pausa()
            if fase == "Final":
                print("\n" + visual.cor("  🥈 VICE-CAMPEÃO", visual.CINZA + visual.NEGRITO))
                print(f"  O Brasil chegou à final, mas perdeu pra {rival.bandeira} {nome_rival} nos pênaltis.")
                print("  Tão perto. Fica pra próxima Copa.")
                registrar_campanha(dificuldade, "vice", f"Vice (perdeu a final pra {nome_rival})")
            else:
                print("\n" + visual.cor(f"  ❌ ELIMINADO na {fase.lower()}", visual.VERMELHO + visual.NEGRITO))
                print(f"  O Brasil caiu pra {rival.bandeira} {nome_rival}. Fim de jogo.")
                registrar_campanha(dificuldade, "eliminado", f"Eliminado na {fase.lower()} pra {nome_rival}")
            mostrar_estatisticas(brasil)
            return

        pausa()
        print(visual.cor("\n  ✅ Brasil vence e avança! Próxima fase.", visual.VERDE + visual.NEGRITO))
        for batedor in brasil.batedores + brasil.reservas:
            batedor.descansar()
        goleiro_brasil.descansar()

    pausa(1.5)
    print(visual.cor("\n  🏆🏆🏆 ============================== 🏆🏆🏆", visual.AMARELO + visual.NEGRITO))
    print(visual.cor("     BRASIL É CAMPEÃO DO MUNDO NOS PÊNALTIS!", visual.VERDE + visual.NEGRITO))
    print(visual.cor("     🇧🇷 HEXA! 🇧🇷", visual.AMARELO + visual.NEGRITO))
    print(visual.cor("  🏆🏆🏆 ============================== 🏆🏆🏆", visual.AMARELO + visual.NEGRITO))
    registrar_campanha(dificuldade, "campeao", "Campeão do mundo")
    mostrar_estatisticas(brasil)


if __name__ == "__main__":
    main()
