# ────────────────────────────────────────────────────────────
# Nível: Difícil  │  Tema: Classes, dicionários, cupons e faixas de desconto
# ────────────────────────────────────────────────────────────
#
# produtos com quantidade, cupom de desconto por código, desconto automático
# por faixa de valor (quem gasta mais leva desconto maior) e imposto de 10% 
# aplicado depois do desconto. Quando o cupom e a faixa competem, vale sempre 
# o MAIOR desconto entre os dois, nunca os dois somados.
#
# Saída esperada (cupom "MONITOR15"):
#
#   ========================================
#     Arroz          1x R$  9.00 = R$   9.00
#     Feijão         2x R$  7.50 = R$  15.00
#     Macarrão       3x R$  4.30 = R$  12.90
#     Refrigerante   1x R$  6.00 = R$   6.00
#   ----------------------------------------
#     Subtotal       R$  42.90
#     Desconto       R$   6.43  (15%)
#     Imposto        R$   3.65  (10%)
#     Total          R$  40.11
#   ========================================
#
# Corrigir um erro pode revelar outro que só aparece depois.
# Encontre e corrija todos antes de rodar.
# ────────────────────────────────────────────────────────────

class Caixa:
    CUPONS = {
        "ALUNO10": 0.10,
        "MONITOR15": 0.15,
        "BLACKFRIDAY": 0.30,
    }

    FAIXAS_DESCONTO = [
        (30, 0.05),
        (60, 0.15),
        (100, 0.20),
    ]

    def __init__(self):
        self.produtos = []

    def adicionar(self, nome, preco, quantidade=1):
        self.produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

    def subtotal(self):
        total = 0
        for produto in self.produtos:
            total += produto["preco"]
        return total

    def desconto_por_cupom(self, codigo):
        if codigo in self.CUPONS:
            return self.CUPONS[codigo]
        return 0

    def desconto_por_faixa(self, subtotal):
        for minimo, pct in self.FAIXAS_DESCONTO:
            if subtotal >= minimo:
                return pct
        return 0

    def calcular_total(self, codigo_cupom=None):
        sub = self.subtotal()
        desconto_cupom = self.desconto_por_cupom(codigo_cupom)
        desconto_faixa = self.desconto_por_faixa(sub)
        melhor_desconto_pct = desconto_cupom + desconto_faixa
        desconto = sub * melhor_desconto_pct
        apos_desconto = sub - desconto
        imposto = sub * 0.10
        total = apos_desconto + imposto
        return total, desconto, imposto, melhor_desconto_pct

    def emitir_cupom(self, codigo_cupom=None):
        print("=" * 40)
        for produto in self.produtos:
            linha_total = produto["preco"] * produto["quantidade"]
            print(f"  {produto['nome']:<14} {produto['quantidade']}x "
                  f"R$ {produto['preco']:>5.2f} = R$ {linha_total:>6.2f}")
        print("-" * 40)
        sub = self.subtotal()
        total, desconto, imposto, pct = self.calcular_total(codigo_cupom)
        print(f"  {'Subtotal':<14} R$ {sub:>6.2f}")
        print(f"  {'Desconto':<14} R$ {desconto:>6.2f}  ({pct * 100:.0f}%)")
        print(f"  {'Imposto':<14} R$ {imposto:>6.2f}  (10%)")
        print(f"  {'Total':<14} R$ {total:>6.2f}")
        print("=" * 40)


caixa = Caixa()
caixa.adicionar("Arroz", 9.00)
caixa.adicionar("Feijão", 7.50, 2)
caixa.adicionar("Macarrão", 4.30, 3)
caixa.produtos.append({"nome": "Refrigerante", "preco": 6.00})
caixa.emitir_cupom(codigo_cupom="MONITOR15")
