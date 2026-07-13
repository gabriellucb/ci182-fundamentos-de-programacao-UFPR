# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Repetição
# ────────────────────────────────────────────────────────────
#
# O programa exibe os primeiros N termos da sequência de
# Fibonacci, a soma de todos eles e quantos são pares.
# (Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13... — cada número é a
# soma dos dois anteriores.)
#
# Saída esperada (N = 7):
#
#   Termos: 0 1 1 2 3 5 8
#   Soma: 20
#   Pares: 3
#
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

n = int(input("Quantos termos da sequência de Fibonacci? "))

a = 1
b = 1
soma = 0
pares = 0

print("Termos: ", end="")
for i in range(n + 1):
    print(a, end=" ")
    soma += a
    if a % 2 != 0:
        pares += 1
    a, b = b, a + b

print()
print(f"Soma: {soma}")
print(f"Pares: {pares}")
