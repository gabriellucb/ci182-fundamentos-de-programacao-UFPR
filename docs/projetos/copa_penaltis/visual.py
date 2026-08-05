"""Cores, barras, molduras e o placar: a parte visual do jogo.

As cores usam códigos ANSI, que a maioria dos terminais entende. Se o seu não
mostrar direito, é só zerar as constantes de cor abaixo (deixar tudo "") que o
resto continua funcionando.
"""

# Códigos ANSI de cor.
RESET = "\033[0m"
NEGRITO = "\033[1m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
CINZA = "\033[90m"


def cor(texto, codigo):
    return f"{codigo}{texto}{RESET}"


def moldura(titulo, codigo=CIANO):
    # O título precisa ser texto simples: emoji tem largura variável e
    # desalinharia a caixa.
    largura = len(titulo) + 4
    topo = "╔" + "═" * largura + "╗"
    meio = "║  " + titulo + "  ║"
    base = "╚" + "═" * largura + "╝"
    return cor(f"{topo}\n{meio}\n{base}", codigo)


def barra(valor, largura=12):
    cheias = max(0, min(largura, round(valor / 100 * largura)))
    desenho = "█" * cheias + "░" * (largura - cheias)
    if valor >= 75:
        codigo = VERDE
    elif valor >= 50:
        codigo = AMARELO
    else:
        codigo = VERMELHO
    return cor(desenho, codigo)


def linha_placar(sel, marcas, vagas):
    simbolos = []
    for i in range(vagas):
        if i < len(marcas):
            simbolos.append("⚽" if marcas[i] == "gol" else cor("✗", VERMELHO))
        else:
            simbolos.append(cor("·", CINZA))
    gols_marcados = [m for m in marcas if m == "gol"]
    gols = len(gols_marcados)
    nome = f"{sel.nome:<15}"
    return f"   {sel.bandeira}  {nome} {' '.join(simbolos)}   {cor(str(gols), NEGRITO)}"


def placar(sel_a, marcas_a, sel_b, marcas_b):
    # Cada marca é "gol" ou "erro"; o que ainda não foi cobrado vira um ponto.
    vagas = max(5, len(marcas_a), len(marcas_b))
    traco = cor("   " + "─" * 40, CINZA)
    return f"{traco}\n{linha_placar(sel_a, marcas_a, vagas)}\n{linha_placar(sel_b, marcas_b, vagas)}\n{traco}"
