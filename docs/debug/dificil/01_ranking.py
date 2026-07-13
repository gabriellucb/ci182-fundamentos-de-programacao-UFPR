# ────────────────────────────────────────────────────────────
# Nível: Difícil  │  Tema: Listas e dicionários    (3 erros)
# ────────────────────────────────────────────────────────────
#
# Sistema de ranking para uma competição de programação.
# O programa deve calcular a média de cada participante,
# exibir o ranking do maior para o menor e a média geral.
#
# Saída esperada (dados fixos no código):
#
#   === RANKING ===
#     1º  Diana      8.83
#     2º  Carlos     8.17
#     3º  Ana        7.50
#     4º  Bruno      6.33
#
#   Pódio: Diana, Carlos, Ana
#   Média geral da competição: 7.71
#
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

participantes = [
    {"nome": "Ana",    "pontos": [7.0, 8.5, 7.0]},
    {"nome": "Bruno",  "pontos": [5.0, 7.0, 7.0]},
    {"nome": "Carlos", "pontos": [9.0, 8.0, 7.5]},
    {"nome": "Diana",  "pontos": [8.5, 9.0, 9.0]},
]

for p in participantes:
    p["media"] = sum(p["pontos"]) / len(p["pontos"])

for i in range(len(participantes)):
    for j in range(len(participantes) - 1 - i):
        if participantes[j]["media"] > participantes[j + 1]["media"]:
            temp = participantes[j]
            participantes[j] = participantes[j + 1]
            participantes[j + 1] = temp

print("=== RANKING ===")
for i in range(len(participantes)):
    print(f"  {i + 1}º  {participantes[i]['nome']:<10} {participantes[i]['media']:.2f}")

podio = ""
for i in range(3):
    podio = participantes[i]["nome"]
    if i < 2:
        podio = podio + ", "

print(f"\n  Pódio: {podio}")

todas_medias = []
for p in participantes:
    todas_medias.append(p["pontos"][0])

media_geral = sum(todas_medias) / len(participantes)

print(f"  Média geral da competição: {media_geral:.2f}")
