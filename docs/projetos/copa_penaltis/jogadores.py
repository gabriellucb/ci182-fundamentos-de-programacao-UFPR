"""Jogador, Goleiro e Seleção: as peças básicas da Copa de Pênaltis.

Guarda a lógica de confiança (o quanto cada característica sobe ou desaba com
a pressão da fase) e de escolha de direção/lado, usada tanto por quem bate
quanto por quem defende.

A característica de um batedor faz dois papéis diferentes dependendo de quem
é o jogador: pra quem não está em CONFIANCA_INDIVIDUAL, ela decide confiança
E estilo de chute juntos (arquétipo fixo). Pra quem está no ranking, ela vira
só o estilo de chute, e a confiança vem do valor individual, baseada na
qualidade real do jogador.
"""

import random

DIRECOES = ("esquerda", "meio", "direita")

CONFIANCA_BASE = {
    "Alta Confiança": 85,
    "Baixa Confiança": 50,
    "Finalizador Técnico": 72,
    "Chute Forte": 74,
    "Padrão": 68,
}

SENSIBILIDADE_PRESSAO = {
    "Alta Confiança": 0.3,
    "Baixa Confiança": 1.8,
    "Finalizador Técnico": 1.0,
    "Chute Forte": 0.8,
    "Padrão": 1.0,
}


def sensibilidade_por_confianca(confianca):
    """Quanto mais confiante o jogador, menos ele sente a pressão da fase."""
    bruta = 1.0 - (confianca - 55) * 0.0175
    return max(0.3, min(1.0, bruta))


# Confiança individual de batedores específicos, derivada de um ranking real
# de qualidade. Quem não está aqui usa o sistema de confiança fixa pela característica.
CONFIANCA_INDIVIDUAL = {
    "Neymar Jr": 95,
    "Harry Kane": 94,
    "Kylian Mbappé": 94,
    "Lionel Messi": 93,
    "Cristiano Ronaldo": 92,
    "Bruno Fernandes": 91,
    "Erling Haaland": 91,
    "Vinícius Jr": 89,
    "Bukayo Saka": 88,
    "Jude Bellingham": 88,
    "Rodri": 88,
    "Kevin De Bruyne": 87,
    "Raphinha": 87,
    "Lamine Yamal": 87,
    "Florian Wirtz": 86,
    "Jamal Musiala": 86,
    "Memphis Depay": 85,
    "Lautaro Martínez": 85,
    "Martin Ødegaard": 84,
    "Ousmane Dembélé": 84,
    "Federico Valverde": 83,
    "Alexis Mac Allister": 83,
    "Luka Modrić": 83,
    "Julián Álvarez": 82,
    "Vitinha": 82,
    "Enzo Fernández": 81,
    "Rafael Leão": 81,
    "Michael Olise": 80,
    "Nico Williams": 80,
    "Fabián Ruiz": 79,
    "Kai Havertz": 79,
    "Cody Gakpo": 78,
    "Xavi Simons": 78,
    "Romelu Lukaku": 78,
    "Bradley Barcola": 78,
    "Declan Rice": 77,
    "Brahim Díaz": 77,
    "Mikel Oyarzabal": 77,
    "Leroy Sané": 76,
    "Tijjani Reijnders": 76,
    "Youri Tielemans": 75,
    "Anthony Gordon": 75,
    "Achraf Hakimi": 74,
    "Mateo Kovačić": 74,
    "Jérémy Doku": 73,
    "Alexander Sørloth": 73,
    "Jeremie Frimpong": 73,
    "Youssef En-Nesyri": 73,
    "Andrej Kramarić": 71,
    "Leandro Trossard": 70,
    "Bilal El Khannouss": 70,
    "Aleksandar Pavlović": 70,
    "Adrien Rabiot": 69,
    "Francisco Conceição": 69,
    "Abde Ezzalzouli": 69,
    "Antonio Nusa": 68,
    "Ante Budimir": 67,
    "Petar Sučić": 65,
    "Patrick Berg": 64,
}


def criar_jogador(nome, caracteristica):
    """Cria um Jogador, usando a confiança do ranking quando o nome está nele."""
    return Jogador(nome, caracteristica, CONFIANCA_INDIVIDUAL.get(nome))


def sortear_direcao(pesos):
    total = sum(pesos.values())
    sorteio = random.uniform(0, total)
    acumulado = 0
    for direcao, peso in pesos.items():
        acumulado += peso
        if sorteio <= acumulado:
            return direcao
    return DIRECOES[-1]


def pedir_direcao(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada in DIRECOES:
            return entrada
        print("  Digite esquerda, meio ou direita.")


class Jogador:
    def __init__(self, nome, caracteristica, confianca_individual=None):
        self.nome = nome
        self.caracteristica = caracteristica
        self.confianca_individual = confianca_individual
        self.confianca = self.confianca_inicial()
        self.cobrancas = 0
        self.gols = 0
        self.gols_decisivos = 0

    def confianca_inicial(self):
        if self.confianca_individual is not None:
            return self.confianca_individual
        return CONFIANCA_BASE.get(self.caracteristica, 55)

    def sensibilidade(self):
        if self.confianca_individual is not None:
            return sensibilidade_por_confianca(self.confianca_individual)
        return SENSIBILIDADE_PRESSAO.get(self.caracteristica, 1.0)

    def taxa_de_acertar_o_alvo(self, peso_pressao, decisiva):
        taxa = self.confianca - peso_pressao * self.sensibilidade()
        if decisiva:
            taxa -= 10 * self.sensibilidade()
        teto = max(95, self.confianca_inicial())
        return max(30, min(teto, taxa))

    def escolher_direcao(self):
        if self.caracteristica == "Finalizador Técnico":
            pesos = {"esquerda": 25, "meio": 50, "direita": 25}
        elif self.caracteristica == "Chute Forte":
            pesos = {"esquerda": 45, "meio": 10, "direita": 45}
        else:
            pesos = {"esquerda": 33, "meio": 34, "direita": 33}
        return sortear_direcao(pesos)

    def atualizar_confianca(self, marcou):
        teto = max(95, self.confianca_inicial())
        if marcou:
            self.confianca = min(teto, self.confianca + 8)
        else:
            self.confianca = max(20, self.confianca - 15)

    def descansar(self):
        self.confianca = (self.confianca + self.confianca_inicial()) / 2

    def registrar_cobranca(self, marcou, decisiva):
        self.cobrancas += 1
        if marcou:
            self.gols += 1
            if decisiva:
                self.gols_decisivos += 1

    def aproveitamento(self):
        if self.cobrancas == 0:
            return 0.0
        return self.gols / self.cobrancas * 100

    def __str__(self):
        return f"{self.nome} ({self.caracteristica}), confiança: {int(self.confianca)}%"


class Goleiro:
    def __init__(self, nome, caracteristica):
        self.nome = nome
        self.caracteristica = caracteristica
        self.confianca_base = 55
        self.confianca = 55
        self.defesas_seguidas = 0
        self.caracteristica_revelada = False

    def escolher_lado(self):
        if self.caracteristica == "Lado Preferido":
            pesos = {"esquerda": 50, "meio": 10, "direita": 40}
        elif self.caracteristica == "Antecipa":
            # Lê a tendência do batedor e quase nunca fica parado no meio,
            # então cai mais vezes no lado pra onde a bola costuma ir.
            pesos = {"esquerda": 45, "meio": 10, "direita": 45}
        else:
            pesos = {"esquerda": 33, "meio": 34, "direita": 33}
        return sortear_direcao(pesos)

    def chance_de_defender(self):
        base = {"Parede": 60, "Antecipa": 50, "Lado Preferido": 47, "Inseguro": 40}
        chance = base.get(self.caracteristica, 45)
        return chance + (self.confianca - 55) * 0.3

    def atualizar_confianca(self, defendeu):
        if defendeu:
            self.confianca = min(90, self.confianca + 10)
            self.defesas_seguidas += 1
        else:
            self.confianca = max(30, self.confianca - 8)
            self.defesas_seguidas = 0

    def descansar(self):
        self.confianca = (self.confianca + self.confianca_base) / 2

    def __str__(self):
        return f"{self.nome} ({self.caracteristica}), confiança: {int(self.confianca)}%"


class Selecao:
    def __init__(self, nome, batedores, goleiro, reservas=None, bandeira="🏳️"):
        self.nome = nome
        self.batedores = batedores
        self.goleiro = goleiro
        self.reservas = reservas if reservas is not None else []
        self.bandeira = bandeira
