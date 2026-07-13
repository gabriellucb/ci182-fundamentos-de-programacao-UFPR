"""Chaveamento da Copa: fases, grupos de dificuldade e as escalações reais dos adversários.

O adversário de cada fase é sorteado dentro do grupo de dificuldade daquela
fase (veja DIFICULDADES). As fases de elite sempre sorteiam seleções
diferentes entre si, então nunca se repete o mesmo rival de elite na mesma
Copa. A lista de fases muda com a dificuldade escolhida (veja montar_fases).

Nos times do grupo Fraco, a característica de cada batedor decide confiança
e estilo de chute juntos (arquétipo fixo, como sempre foi). Do grupo Médio
pra cima, a característica vira só o estilo de chute, e a confiança de cada
jogador vem do ranking real em CONFIANCA_INDIVIDUAL (jogadores.py).
"""

import random

from jogadores import Goleiro, Selecao, criar_jogador

# Chaveamento normal: cinco fases, dificuldade crescente do fraco ao elite.
FASES = [
    ("Dezesseis avos de final", "fraca"),
    ("Oitavas de final", "media"),
    ("Quartas de final", "forte"),
    ("Semifinal", "elite"),
    ("Final", "elite"),
]

# No fácil, você começa já nas oitavas (pula o grupo fraco).
FASES_FACIL = [
    ("Oitavas de final", "media"),
    ("Quartas de final", "forte"),
    ("Semifinal", "elite"),
    ("Final", "elite"),
]

# No difícil, o piso sobe: já começa contra o grupo médio e pega três
# seleções de elite seguidas nas quartas, semi e final.
FASES_DIFICIL = [
    ("Dezesseis avos de final", "media"),
    ("Oitavas de final", "forte"),
    ("Quartas de final", "elite"),
    ("Semifinal", "elite"),
    ("Final", "elite"),
]

PESO_PRESSAO = {
    "Dezesseis avos de final": 0,
    "Oitavas de final": 5,
    "Quartas de final": 10,
    "Semifinal": 15,
    "Final": 20,
}


def montar_fases(dificuldade):
    """Devolve a lista de fases do chaveamento conforme a dificuldade escolhida."""
    if dificuldade == "facil":
        return FASES_FACIL
    if dificuldade == "dificil":
        return FASES_DIFICIL
    return FASES

DIFICULDADES = {
    "fraca": ["Uruguai", "Colômbia", "México", "Estados Unidos", "Japão", "Suíça", "Cabo Verde"],
    "media": ["Holanda", "Bélgica", "Croácia", "Marrocos", "Noruega"],
    "forte": ["Alemanha", "Inglaterra", "Portugal"],
    "elite": ["Argentina", "França", "Espanha"],
}

BANDEIRAS = {
    "Brasil": "🇧🇷",
    "Argentina": "🇦🇷", "França": "🇫🇷", "Espanha": "🇪🇸",
    "Alemanha": "🇩🇪", "Inglaterra": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Portugal": "🇵🇹",
    "Holanda": "🇳🇱", "Bélgica": "🇧🇪", "Croácia": "🇭🇷", "Marrocos": "🇲🇦", "Noruega": "🇳🇴",
    "Uruguai": "🇺🇾", "Colômbia": "🇨🇴", "México": "🇲🇽", "Estados Unidos": "🇺🇸",
    "Japão": "🇯🇵", "Suíça": "🇨🇭", "Cabo Verde": "🇨🇻",
}

TIMES = {
    "Argentina": {
        "batedores": [
            ("Lionel Messi", "Finalizador Técnico"),
            ("Enzo Fernández", "Padrão"),
            ("Alexis Mac Allister", "Chute Forte"),
            ("Julián Álvarez", "Finalizador Técnico"),
            ("Lautaro Martínez", "Chute Forte"),
        ],
        "goleiro": ("Emiliano Martínez", "Parede"),
    },
    "França": {
        "batedores": [
            ("Kylian Mbappé", "Chute Forte"),
            ("Adrien Rabiot", "Padrão"),
            ("Ousmane Dembélé", "Chute Forte"),
            ("Michael Olise", "Finalizador Técnico"),
            ("Bradley Barcola", "Padrão"),
        ],
        "goleiro": ("Mike Maignan", "Parede"),
    },
    "Espanha": {
        "batedores": [
            ("Rodri", "Padrão"),
            ("Fabián Ruiz", "Chute Forte"),
            ("Lamine Yamal", "Finalizador Técnico"),
            ("Nico Williams", "Padrão"),
            ("Mikel Oyarzabal", "Chute Forte"),
        ],
        "goleiro": ("Unai Simón", "Parede"),
    },
    "Alemanha": {
        "batedores": [
            ("Jamal Musiala", "Finalizador Técnico"),
            ("Florian Wirtz", "Padrão"),
            ("Kai Havertz", "Padrão"),
            ("Leroy Sané", "Chute Forte"),
            ("Aleksandar Pavlović", "Padrão"),
        ],
        "goleiro": ("Manuel Neuer", "Antecipa"),
    },
    "Inglaterra": {
        "batedores": [
            ("Harry Kane", "Padrão"),
            ("Jude Bellingham", "Padrão"),
            ("Declan Rice", "Chute Forte"),
            ("Bukayo Saka", "Finalizador Técnico"),
            ("Anthony Gordon", "Padrão"),
        ],
        "goleiro": ("Jordan Pickford", "Antecipa"),
    },
    "Portugal": {
        "batedores": [
            ("Cristiano Ronaldo", "Chute Forte"),
            ("Vitinha", "Padrão"),
            ("Bruno Fernandes", "Chute Forte"),
            ("Francisco Conceição", "Padrão"),
            ("Rafael Leão", "Finalizador Técnico"),
        ],
        "goleiro": ("Diogo Costa", "Antecipa"),
    },
    "Holanda": {
        "batedores": [
            ("Memphis Depay", "Chute Forte"),
            ("Xavi Simons", "Finalizador Técnico"),
            ("Cody Gakpo", "Chute Forte"),
            ("Jeremie Frimpong", "Padrão"),
            ("Tijjani Reijnders", "Padrão"),
        ],
        "goleiro": ("Bart Verbruggen", "Lado Preferido"),
    },
    "Bélgica": {
        "batedores": [
            ("Kevin De Bruyne", "Finalizador Técnico"),
            ("Jérémy Doku", "Chute Forte"),
            ("Romelu Lukaku", "Padrão"),
            ("Youri Tielemans", "Padrão"),
            ("Leandro Trossard", "Padrão"),
        ],
        "goleiro": ("Thibaut Courtois", "Parede"),
    },
    "Croácia": {
        "batedores": [
            ("Luka Modrić", "Finalizador Técnico"),
            ("Andrej Kramarić", "Chute Forte"),
            ("Mateo Kovačić", "Padrão"),
            ("Ante Budimir", "Padrão"),
            ("Petar Sučić", "Padrão"),
        ],
        "goleiro": ("Dominik Livaković", "Antecipa"),
    },
    "Marrocos": {
        "batedores": [
            ("Brahim Díaz", "Finalizador Técnico"),
            ("Achraf Hakimi", "Chute Forte"),
            ("Bilal El Khannouss", "Padrão"),
            ("Abde Ezzalzouli", "Padrão"),
            ("Youssef En-Nesyri", "Padrão"),
        ],
        "goleiro": ("Yassine Bounou", "Antecipa"),
    },
    "Noruega": {
        "batedores": [
            ("Erling Haaland", "Chute Forte"),
            ("Martin Ødegaard", "Finalizador Técnico"),
            ("Alexander Sørloth", "Padrão"),
            ("Patrick Berg", "Padrão"),
            ("Antonio Nusa", "Padrão"),
        ],
        "goleiro": ("Ørjan Nyland", "Lado Preferido"),
    },
    "Uruguai": {
        "batedores": [
            ("Federico Valverde", "Finalizador Técnico"),
            ("Darwin Núñez", "Chute Forte"),
            ("Rodrigo Bentancur", "Padrão"),
            ("Facundo Pellistri", "Baixa Confiança"),
            ("Maximiliano Araújo", "Baixa Confiança"),
        ],
        "goleiro": ("Fernando Muslera", "Lado Preferido"),
    },
    "Colômbia": {
        "batedores": [
            ("James Rodríguez", "Finalizador Técnico"),
            ("Luis Díaz", "Chute Forte"),
            ("Luis Suárez", "Padrão"),
            ("Jhon Arias", "Padrão"),
            ("Gustavo Puerta", "Baixa Confiança"),
        ],
        "goleiro": ("Camilo Vargas", "Inseguro"),
    },
    "México": {
        "batedores": [
            ("Julián Quiñones", "Finalizador Técnico"),
            ("Raúl Jiménez", "Padrão"),
            ("Erik Lira", "Baixa Confiança"),
            ("Brian Gutiérrez", "Baixa Confiança"),
            ("Roberto Alvarado", "Baixa Confiança"),
        ],
        "goleiro": ("Raúl Rangel", "Inseguro"),
    },
    "Estados Unidos": {
        "batedores": [
            ("Christian Pulisic", "Finalizador Técnico"),
            ("Timothy Weah", "Padrão"),
            ("Weston McKennie", "Baixa Confiança"),
            ("Yunus Musah", "Baixa Confiança"),
            ("Folarin Balogun", "Baixa Confiança"),
        ],
        "goleiro": ("Matt Turner", "Inseguro"),
    },
    "Japão": {
        "batedores": [
            ("Takefusa Kubo", "Finalizador Técnico"),
            ("Kaoru Mitoma", "Padrão"),
            ("Hidemasa Morita", "Baixa Confiança"),
            ("Daichi Kamada", "Baixa Confiança"),
            ("Ayase Ueda", "Baixa Confiança"),
        ],
        "goleiro": ("Zion Suzuki", "Inseguro"),
    },
    "Suíça": {
        "batedores": [
            ("Ruben Vargas", "Finalizador Técnico"),
            ("Breel Embolo", "Padrão"),
            ("Remo Freuler", "Baixa Confiança"),
            ("Dan Ndoye", "Baixa Confiança"),
            ("Ardon Jashari", "Baixa Confiança"),
        ],
        "goleiro": ("Gregor Kobel", "Lado Preferido"),
    },
    "Cabo Verde": {
        "batedores": [
            ("Bebé", "Finalizador Técnico"),
            ("Jamiro Monteiro", "Padrão"),
            ("Kenny Rocha Santos", "Baixa Confiança"),
            ("Garry Rodrigues", "Baixa Confiança"),
            ("Dailon Livramento", "Baixa Confiança"),
        ],
        "goleiro": ("Vozinha", "Inseguro"),
    },
}


def criar_selecao_rival(nome):
    dados = TIMES[nome]
    batedores = [criar_jogador(nome_jogador, caracteristica) for nome_jogador, caracteristica in dados["batedores"]]
    nome_goleiro, caracteristica_goleiro = dados["goleiro"]
    goleiro = Goleiro(nome_goleiro, caracteristica_goleiro)
    return Selecao(nome, batedores, goleiro, bandeira=BANDEIRAS.get(nome, "🏳️"))


def sortear_adversarios(fases):
    sorteio = {}
    quantas_elite = sum(1 for _, dificuldade in fases if dificuldade == "elite")
    elites = random.sample(DIFICULDADES["elite"], quantas_elite)
    indice_elite = 0
    for fase, dificuldade in fases:
        if dificuldade == "elite":
            sorteio[fase] = elites[indice_elite]
            indice_elite += 1
        else:
            sorteio[fase] = random.choice(DIFICULDADES[dificuldade])
    return sorteio
