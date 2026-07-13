# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Listas
# ────────────────────────────────────────────────────────────
#
# O programa deve ler 5 notas, calcular a média e exibir
# quantas notas ficaram acima dela.
#
# Saída esperada (notas: 6, 8, 7, 5, 9):
#
#   Média: 7.00
#   Notas acima da média: 3
#
# Encontre e corrija o erro.
# ────────────────────────────────────────────────────────────

notas = []

for i in range(5):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")

acima = 0
for i in range(len(notas) + 1):
    if notas[i] > media:
        acima += 1

print(f"Notas acima da média: {acima}")
