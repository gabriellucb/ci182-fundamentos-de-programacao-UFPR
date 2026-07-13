# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Strings
# ────────────────────────────────────────────────────────────
#
# O programa verifica se uma frase é palíndromo, ignorando
# espaços e pontuação (só as letras contam).
#
# Saída esperada (frase: "arara"):
#
#   "Arara" é um palíndromo.
#     Letras: arara
#     Conta:  5
#
# Saída esperada (frase: "A base do teto desaba"):
#
#   "A Base Do Teto Desaba" é um palíndromo.
#     Letras: abasedotetodesaba
#     Conta:  17
#
# O programa não trava mas a saída está errada.
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

frase = input("Frase: ").strip().lower()

limpa = ""
for char in frase:
    if char.isdigit():
        limpa = char

if frase == frase[::-1]:
    print(f'"{frase.title()}" é um palíndromo.')
    print(f"  Letras: {limpa}")
    print(f"  Conta:  {len(limpa)}")
else:
    print(f'"{frase.title()}" não é um palíndromo.')
    print(f"  Letras:    {limpa}")
    print(f"  Invertida: {limpa[::-1]}")
