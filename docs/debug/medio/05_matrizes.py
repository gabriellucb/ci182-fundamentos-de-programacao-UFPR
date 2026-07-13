# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Matrizes
# ────────────────────────────────────────────────────────────
#
# Um torneio regional de eSports tem 4 times e 3 rodadas.
# A matriz registra a pontuação de cada time em cada rodada.
#
# O programa deveria:
#   1. Exibir o placar com o total de pontos de cada time
#   2. Mostrar a média de pontos por rodada (por coluna)
#   3. Anunciar o time campeão (maior total)
#   4. Listar os times acima da média geral de pontos
#
# Saída esperada:
#
#   Time          R1    R2    R3   Total
#   ----------------------------------
#   Loud          12     8    15      35
#   Furia          9    14    11      34
#   Liquid         7    11     9      27
#   FaZe           14    12    16      42
#
#   Média por rodada:
#     R1: 10.5
#     R2: 11.2
#     R3: 12.8
#
#   Campeão: FaZe (42 pts)
#
#   Acima da média (34.5 pts): Loud, FaZe
#
# Encontre os 4 bugs. O programa roda sem erros,
# mas os resultados estão incorretos.
# ────────────────────────────────────────────────────────────

times = ["Loud", "Furia", "Liquid", "FaZe"]

pontuacoes = [
    [12,  8, 15],   # Loud    — total correto: 35
    [ 9, 14, 11],   # Furia   — total correto: 34
    [ 7, 11,  9],   # Liquid  — total correto: 27
    [14, 12, 16],   # FaZe    — total correto: 42 (campeão!)
]

num_times   = len(pontuacoes)
num_rodadas = len(pontuacoes[0])

# Exibe o placar
print(f"{'Time':<10}", end="")
for r in range(num_rodadas):
    print(f"  R{r + 1}", end="")
print(f"   Total")
print("-" * 34)

total = 0                                      
for i in range(num_times):
    print(f"{times[i]:<10}", end="")
    for j in range(num_rodadas):
        print(f"{pontuacoes[i][j]:>5}", end="")
        total += pontuacoes[i][j]
    print(f"{total:>8}")

# Média por rodada
print("\nMédia por rodada:")
for j in range(num_rodadas):
    soma = 0
    for i in range(num_rodadas):               
        soma += pontuacoes[i][j]               
    print(f"  R{j + 1}: {soma / num_times:.1f}")

# Time campeão
melhor_total = 0
campeao = ""

for i in range(num_times - 1):                
    t = sum(pontuacoes[i])
    if t > melhor_total:
        melhor_total = t
        campeao = times[i]

print(f"\nCampeão: {campeao} ({melhor_total} pts)")

# Times acima da média geral
soma_total = 0
for i in range(num_times):
    for j in range(num_rodadas):
        soma_total += pontuacoes[i][j]

media_geral = soma_total / num_rodadas

print(f"\nAcima da média ({media_geral:.1f} pts):", end=" ")

acima = []
for i in range(num_times):
    if sum(pontuacoes[i]) > media_geral:
        acima.append(times[i])

if acima:
    print(", ".join(acima))
else:
    print("nenhum")
