# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Condicionais
# ────────────────────────────────────────────────────────────
#
# O programa calcula o frete de acordo com o valor da compra:
#
#   Menos de R$ 50,00        →  Frete padrão   — R$ 15,00
#   De R$ 50,00 a R$ 99,99  →  Frete reduzido  — R$  8,00
#   A partir de R$ 100,00   →  Frete grátis    — R$  0,00
#
# Exemplo (compra: R$ 100,00):
#
#   Frete: R$ 0.00  (Frete grátis)
#   Total: R$ 100.00
#
# Encontre e corrija o erro sutil.
# ────────────────────────────────────────────────────────────

valor = float(input("Valor da compra (R$): "))

if valor > 100:
    frete    = 0.0
    situacao = "Frete grátis"
elif valor >= 50:
    frete    = 8.0
    situacao = "Frete reduzido"
else:
    frete    = 15.0
    situacao = "Frete padrão"

print(f"\nFrete: R$ {frete:.2f}  ({situacao})")
print(f"Total: R$ {valor + frete:.2f}")
