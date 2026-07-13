# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Funções
# ────────────────────────────────────────────────────────────
#
# O programa usa duas funções:
#   calcular_media(notas)  →  retorna a média de uma lista
#   classificar(media)     →  retorna "Aprovado", "Recuperação"
#                             ou "Reprovado"
#
# Saída esperada (notas: 6, 8, 7):
#
#   Média: 7.00 — Aprovado
#
# Encontre e corrija o erro.
# ────────────────────────────────────────────────────────────

def calcular_media(notas):
    total = sum(notas) / len(notas)


def classificar(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


notas = []
for i in range(3):
    n = float(input(f"Nota {i + 1}: "))
    notas.append(n)

media = calcular_media(notas)
resultado = classificar(media)

print(f"Média: {media:.2f} — {resultado}")
