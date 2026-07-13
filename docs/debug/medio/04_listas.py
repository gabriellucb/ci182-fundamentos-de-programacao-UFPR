# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Listas                    (4 erros)
# ────────────────────────────────────────────────────────────
#
# O programa recebe pontuações de um torneio de games,
# gera o ranking do melhor ao pior, e calcula a média do grupo.
#
# Saída esperada (entradas: 85, 42, 97, 63, 78):
#
#   Pontuações registradas: [85, 42, 97, 63, 78]
#   Ranking (1º ao último): [97, 85, 78, 63, 42]
#   Melhor pontuação: 97
#   Pior pontuação:   42
#   Média do grupo:   73.00
#
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

print("Torneio de Games — informe as pontuações:")

pontuacoes = []
while True:
    entrada = input("  Pontuação (Enter para encerrar): ").strip()
    if entrada == "":
        break
    pontuacoes.append(int(entrada))

ranking = pontuacoes
ranking.sort()

media = sum(pontuacoes) / (len(pontuacoes) - 1)

print(f"\nPontuações registradas: {pontuacoes}")
print(f"Ranking (1º ao último): {ranking}")
print(f"Melhor pontuação: {ranking[0]}")
print(f"Pior pontuação:   {ranking[-1]}")
print(f"Média do grupo:   {media:.0f}")
