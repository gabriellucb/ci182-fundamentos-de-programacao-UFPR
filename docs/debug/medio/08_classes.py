# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Classes
# ────────────────────────────────────────────────────────────
#
# Um sistema de RPG registra jogadores: nível, XP e inventário.
# Ao ganhar XP suficiente, o jogador deveria subir de nível.
# Cada jogador deveria ter seu próprio inventário, independente
# dos outros.
#
# Saída esperada:
#
#   Elara | Nivel 2 | XP 50/200 | Itens: ['Espada']
#   Theron | Nivel 1 | XP 0/100 | Itens: ['Escudo']
#
# Encontre e corrija os erros. O programa roda sem crashar,
# mas os resultados estão incorretos.
# ────────────────────────────────────────────────────────────

class Jogador:
    def __init__(self, nome, nivel=1, xp=0, inventario=[]):
        self.nome = nome
        self.nivel = nivel
        self.xp = xp
        self.inventario = inventario

    def xp_para_proximo_nivel(self):
        return self.nivel * 100

    def ganhar_xp(self, quantidade):
        xp = self.xp + quantidade
        limite = self.xp_para_proximo_nivel()
        if xp >= limite:
            nivel = self.nivel + 1
            xp -= limite
        self.xp = xp

    def pegar_item(self, item):
        self.inventario.append(item)

    def __str__(self):
        return f"{self.nome} | Nivel {self.nivel} | XP {self.xp}/{self.xp_para_proximo_nivel()} | Itens: {self.inventario}"


elara = Jogador("Elara")
theron = Jogador("Theron")

elara.ganhar_xp(150)

elara.pegar_item("Espada")
theron.pegar_item("Escudo")

print(elara)
print(theron)
