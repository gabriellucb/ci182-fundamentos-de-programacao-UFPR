"""Resposta — Aula 11: Dicionários
Exercício: produto único → desconto → lista → filtragem e contagem.
"""

produto = {
    "nome":      "Notebook",
    "preco":     3500.00,
    "categoria": "Eletrônicos",
    "estoque":   5,
}

print("=== PRODUTO ===")
for chave, valor in produto.items():
    print(f"  {chave:<12}: {valor}")

produto["preco"] = produto["preco"] * 0.9
print(f"\n  Preço com 10% de desconto: R$ {produto['preco']:.2f}")

produtos = [
    produto,
    {"nome": "Mouse",   "preco":  89.90, "categoria": "Eletrônicos", "estoque": 0},
    {"nome": "Cadeira", "preco": 799.00, "categoria": "Móveis",      "estoque": 3},
]

print("\n=== PRODUTOS COM ESTOQUE ===")
for p in produtos:
    if p["estoque"] > 0:
        print(f"  {p['nome']:<12}  R$ {p['preco']:>8.2f}  estoque: {p['estoque']}")

valor_total = 0
for p in produtos:
    valor_total += p["preco"] * p["estoque"]
print(f"\nValor total em estoque: R$ {valor_total:.2f}")

print("\n=== PRODUTOS POR CATEGORIA ===")
por_categoria = {}
for p in produtos:
    cat = p["categoria"]
    if cat not in por_categoria:
        por_categoria[cat] = 0
    por_categoria[cat] += 1

for cat, qtd in por_categoria.items():
    print(f"  {cat}: {qtd} produto(s)")
