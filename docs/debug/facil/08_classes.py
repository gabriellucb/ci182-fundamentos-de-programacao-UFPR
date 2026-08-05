# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Classes
# ────────────────────────────────────────────────────────────
#
# O programa define uma classe Produto com estoque inicial,
# métodos vender() e repor(), e __str__ formatado.
#
# Saída esperada (dados fixos no código):
#
#   Venda de 3 unidade(s) registrada.
#   Reposição de 10 unidade(s) registrada.
#   Produto: Teclado, estoque: 12
#
# Encontre e corrija o erro antes de rodar.
# ────────────────────────────────────────────────────────────

class Produto:
    def __init__(self, nome, estoque_inicial=0):
        self.nome    = nome
        self.estoque = estoque_inicial

    def vender(quantidade):
        self.estoque -= quantidade
        print(f"Venda de {quantidade} unidade(s) registrada.")

    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"Reposição de {quantidade} unidade(s) registrada.")

    def __str__(self):
        return f"Produto: {self.nome}, estoque: {self.estoque}"


produto = Produto("Teclado", 5)
produto.vender(3)
produto.repor(10)
print(produto)
