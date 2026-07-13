# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Repetição
# ────────────────────────────────────────────────────────────
#
# O programa deve exibir a tabuada de um número de 1 até 10.
#
# Saída esperada (número: 3):
#
#   3 x 1 = 3
#   3 x 2 = 6
#   ...
#   3 x 10 = 30
#
# Encontre e corrija o erro.
# ────────────────────────────────────────────────────────────

numero = int(input("Digite um número: "))
soma = numero

for i in range(1, 11):
    soma += numero
    print(f"{numero} x {i} = {soma}")
