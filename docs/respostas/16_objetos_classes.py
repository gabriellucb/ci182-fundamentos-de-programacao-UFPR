"""Resposta: Aula 16 | Objetos e Classes
Exercício: classe Produto com disponivel(), vender() e reabastecer().
"""


class Produto:
    def __init__(self, nome, preco, estoque):
        """Cria um produto novo com nome, preço e estoque inicial."""
        self.nome    = nome
        self.preco   = preco
        self.estoque = estoque

    def disponivel(self):
        """Retorna True se ainda houver estoque do produto."""
        return self.estoque > 0

    def vender(self, qtd):
        """Diminui o estoque em qtd unidades, se houver saldo suficiente."""
        if not self.disponivel():
            return f"'{self.nome}' sem estoque."
        if qtd > self.estoque:
            return f"Estoque insuficiente, só há {self.estoque} unidade(s) de '{self.nome}'."
        self.estoque -= qtd
        return f"Venda de {qtd} '{self.nome}' realizada. Estoque restante: {self.estoque}."

    def reabastecer(self, qtd):
        """Aumenta o estoque em qtd unidades."""
        self.estoque += qtd
        return f"'{self.nome}' reabastecido. Novo estoque: {self.estoque}."

    def __str__(self):
        """Retorna o produto formatado em uma linha de tabela."""
        status = "disponível" if self.disponivel() else "sem estoque"
        return f"{self.nome:<15} R$ {self.preco:>8.2f}  estoque: {self.estoque:>3}  ({status})"


notebook = Produto("Notebook",   3500.00, 5)
mouse    = Produto("Mouse",        89.90, 0)
cadeira  = Produto("Cadeira",     799.00, 3)

print(notebook.vender(2))
print(notebook.vender(10))
print(mouse.vender(1))
print(mouse.reabastecer(8))
print(mouse.vender(3))
print(cadeira.vender(1))

print("\n=== ESTADO FINAL ===")
for p in [notebook, mouse, cadeira]:
    print(f"  {p}")
