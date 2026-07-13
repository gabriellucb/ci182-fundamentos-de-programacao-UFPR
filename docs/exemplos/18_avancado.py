"""Missão em Marte: zip, enumerate, compreensões, type hints e try/except.

Você assume o controle remoto de um rover pousado em Marte. A cada sol (dia
marciano) você escolhe uma ação, mede os sensores e decide se vale o risco de
perfurar o solo atrás de amostras, ou se é melhor recarregar antes que a
bateria acabe a 225 milhões de quilômetros de distância da tomada mais próxima.

Conceitos: zip, enumerate, compreensão de lista, compreensão de dicionário,
type hints, try/except com múltiplos except, raise, finally.
"""

import random

SENSORES: list[str] = ["Bateria", "Temperatura", "Oxigênio", "Pressão"]
LIMITES: dict[str, tuple[float, float]] = {
    "Bateria": (20.0, 100.0),
    "Temperatura": (-90.0, 20.0),
    "Oxigênio": (15.0, 100.0),
    "Pressão": (0.4, 0.9),
}
CUSTO_OXIGENIO_PERFURACAO: float = 4.0
META_AMOSTRAS: int = 3


def mostrar_status(sensores: list[str], leituras: list[float]) -> None:
    for nome, valor in zip(sensores, leituras):
        print(f"  {nome:<12}: {valor:6.1f}")


def sensores_criticos(
    sensores: list[str], leituras: list[float], limites: dict[str, tuple[float, float]]
) -> list[str]:
    return [
        nome
        for nome, valor in zip(sensores, leituras)
        if not (limites[nome][0] <= valor <= limites[nome][1])
    ]


def executar_acao(
    acao: str, bateria: float, temperatura: float, oxigenio: float, pressao: float
) -> tuple[float, float, float, float, int]:
    if acao == "m":
        bateria -= random.uniform(6, 10)
        temperatura += random.uniform(-3, 3)
        oxigenio -= random.uniform(1, 3)
        pressao += random.uniform(-0.03, 0.03)
        distancia = random.uniform(5, 15)
        print(f"  O rover avançou {distancia:.1f} metros pela superfície.")
        return bateria, temperatura, oxigenio, pressao, 0

    if acao == "e":
        bateria -= random.uniform(2, 4)
        oxigenio -= random.uniform(0, 1)
        if random.random() < 0.35:
            print("  O scanner encontrou um padrão mineral interessante nas rochas.")
        else:
            print("  Nada além de poeira vermelha no raio do scanner.")
        return bateria, temperatura, oxigenio, pressao, 0

    if acao == "p":
        if oxigenio < CUSTO_OXIGENIO_PERFURACAO:
            raise RuntimeError("oxigênio insuficiente para resfriar a broca")
        bateria -= random.uniform(10, 15)
        oxigenio -= CUSTO_OXIGENIO_PERFURACAO
        temperatura += random.uniform(2, 6)
        print("  A broca penetrou o solo marciano. Amostra coletada!")
        return bateria, temperatura, oxigenio, pressao, 1

    if acao == "r":
        bateria = min(100.0, bateria + random.uniform(15, 25))
        temperatura += random.uniform(-2, 1)
        print("  Painéis solares recarregando. Bateria em recuperação.")
        return bateria, temperatura, oxigenio, pressao, 0

    raise ValueError(f'ação "{acao}" não é reconhecida pelo painel de controle')


print("=== MISSÃO EM MARTE ===")
print("Você está no controle remoto do rover Curiosidade-BR, pousado no")
print("cráter Jezero. O sinal daqui até a Terra demora uns 15 minutos, então")
print("cada comando que você manda é definitivo: sem desfazer, sem recarregar")
print("um save. Sobreviva o quanto der e traga amostras pra casa.\n")

bateria: float = 100.0
temperatura: float = -60.0
oxigenio: float = 100.0
pressao: float = 0.6
amostras: int = 0
turno: int = 0
historico: list[tuple[int, str, float]] = []
desfecho: str = ""

while bateria > 0 and oxigenio > 0:
    turno += 1
    leituras: list[float] = [bateria, temperatura, oxigenio, pressao]

    print(f"\n--- Sol {turno} ---")
    mostrar_status(SENSORES, leituras)

    criticos = sensores_criticos(SENSORES, leituras, LIMITES)
    if criticos:
        print(f"  ALERTA: {', '.join(criticos)} fora da faixa segura!")

    escolha: str = ""
    sucesso_da_missao = False
    try:
        escolha = input(
            "\n  [m]over  [e]scanear  [p]erfurar  [r]ecarregar  [s]air > "
        ).strip().lower()

        if escolha == "s":
            desfecho = "interrompida"
            print("  Centro de controle confirma: encerrando a missão por aqui.")
            break

        bateria, temperatura, oxigenio, pressao, amostra_ganha = executar_acao(
            escolha, bateria, temperatura, oxigenio, pressao
        )
        amostras += amostra_ganha

        if amostras >= META_AMOSTRAS:
            desfecho = "sucesso"
            sucesso_da_missao = True
            print("\n  Amostras suficientes coletadas! Iniciando retorno à base.")
    except ValueError as erro:
        print(f"  Comando rejeitado: {erro}.")
    except RuntimeError as erro:
        print(f"  Falha de equipamento: {erro}.")
    finally:
        historico.append((turno, escolha, round(bateria, 1)))

    if sucesso_da_missao:
        break

if not desfecho:
    desfecho = "falha_bateria" if bateria <= 0 else "falha_oxigenio"

print("\n=== RELATÓRIO DA MISSÃO ===")
for numero, (turno_reg, acao_reg, bateria_reg) in enumerate(historico, start=1):
    comando = acao_reg if acao_reg else "-"
    print(f"  Sol {numero}: comando '{comando}', bateria em {bateria_reg}%")

leituras_finais: list[float] = [bateria, temperatura, oxigenio, pressao]
status_final: dict[str, bool] = {
    nome: not (LIMITES[nome][0] <= valor <= LIMITES[nome][1])
    for nome, valor in zip(SENSORES, leituras_finais)
}

print("\nDiagnóstico final dos sensores:")
for nome, critico in status_final.items():
    situacao = "CRÍTICO" if critico else "estável"
    print(f"  {nome:<12}: {situacao}")

print(f"\nAmostras coletadas: {amostras}/{META_AMOSTRAS}")
print(f"Total de sóis em operação: {turno}")

mensagens_finais: dict[str, str] = {
    "sucesso": "\nMissão cumprida. As amostras estão a caminho da Terra.",
    "interrompida": "\nMissão encerrada por decisão da equipe, com o rover ainda operante.",
    "falha_bateria": "\nA bateria esgotou. O rover perdeu contato com o centro de controle.",
    "falha_oxigenio": "\nA reserva de oxigênio zerou. Missão abortada por segurança.",
}
print(mensagens_finais[desfecho])
