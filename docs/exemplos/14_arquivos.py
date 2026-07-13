"""RPG com save/load — arquivos de texto, leitura, escrita, CSV manual.

Toda vez que um jogo salva o seu progresso, ele está fazendo exatamente isso:
escrevendo variáveis em arquivo. Você fecha o terminal, vai dormir, abre de novo
no dia seguinte, o personagem está lá, mesmo nível, mesmo inventário, mesma HP.
Não tem servidor, não tem nuvem. Tem um .txt de duas linhas.

Conceitos: open(), with, modos "r"/"w", readlines(), strip().split(),
           FileNotFoundError, leitura e escrita de CSV manual.
"""

ARQUIVO = "docs/exemplos/arquivos_uteis/personagem.txt"

CLASSES = ["Guerreiro", "Mago", "Arqueiro", "Ladino"]
HP_BASE = {"Guerreiro": 120, "Mago": 60, "Arqueiro": 90, "Ladino": 80}
XP_POR_NIVEL = 100


def carregar_personagem():
    """Carrega personagem do arquivo; retorna None se não existir ainda."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        partes = linhas[0].strip().split(",")
        nome   = partes[0]
        classe = partes[1]
        nivel  = int(partes[2])
        xp     = int(partes[3])
        hp     = int(partes[4])
        itens  = []
        if len(linhas) > 1 and linhas[1].strip():
            for item in linhas[1].strip().split(";"):
                itens.append(item)
        return {"nome": nome, "classe": classe, "nivel": nivel, "xp": xp, "hp": hp, "itens": itens}
    except FileNotFoundError:
        return None


def salvar_personagem(p):
    """Escreve os dados do personagem no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        f.write(f"{p['nome']},{p['classe']},{p['nivel']},{p['xp']},{p['hp']}\n")
        f.write(";".join(p["itens"]) + "\n")


def criar_personagem():
    """Pergunta nome e classe, cria personagem novo e salva."""
    print("\n=== NOVO AVENTUREIRO ===")
    nome = input("  Nome: ").strip()
    print("  Classes disponíveis:")
    for i, c in enumerate(CLASSES):
        print(f"    {i + 1}. {c}")
    while True:
        try:
            escolha = int(input("  Escolha (1-4): "))
            if 1 <= escolha <= 4:
                break
            print("  Número fora do intervalo.")
        except ValueError:
            print("  Digite um número.")
    classe = CLASSES[escolha - 1]
    p = {"nome": nome, "classe": classe, "nivel": 1, "xp": 0, "hp": HP_BASE[classe], "itens": []}
    salvar_personagem(p)
    print(f"\n  {nome} ({classe}) registrado. Boa sorte na estrada!\n")
    return p


def hp_max(p):
    """HP máximo do personagem no nível atual."""
    return HP_BASE[p["classe"]] + (p["nivel"] - 1) * 10


def exibir_ficha(p):
    """Mostra os stats e inventário do personagem."""
    xp_necessario = p["nivel"] * XP_POR_NIVEL
    fill = int(p["xp"] / xp_necessario * 20)
    barra = "█" * fill + "░" * (20 - fill)
    print(f"\n  === {p['nome']} ({p['classe']}) ===")
    print(f"  Nível {p['nivel']}    HP: {p['hp']}/{hp_max(p)}")
    print(f"  XP:   [{barra}] {p['xp']}/{xp_necessario}")
    if p["itens"]:
        print(f"  Inventário ({len(p['itens'])} item(s)):")
        for item in p["itens"]:
            print(f"    • {item}")
    else:
        print("  Inventário: vazio")
    print()


def explorar(p):
    """Escolhe destino, ganha XP e perde HP."""
    print("\n  Destinos:")
    print("  1. Floresta  (+30 XP, -5 HP)")
    print("  2. Dungeon   (+60 XP, -15 HP)")
    print("  3. Montanha  (+100 XP, -30 HP)")
    opcao = input("  > ").strip()
    destinos = {
        "1": ("Floresta",   30,  5),
        "2": ("Dungeon",    60, 15),
        "3": ("Montanha",  100, 30),
    }
    if opcao not in destinos:
        print("  Destino inválido.\n")
        return
    nome_local, xp_ganho, dano = destinos[opcao]
    p["xp"] += xp_ganho
    p["hp"]  = max(0, p["hp"] - dano)
    print(f"\n  Você explorou a {nome_local}: +{xp_ganho} XP, -{dano} HP.")
    if p["xp"] >= p["nivel"] * XP_POR_NIVEL:
        print("  Você tem XP suficiente para subir de nível! Digite 'nivel'.")
    if p["hp"] == 0:
        print("  HP zerado! Descanse antes de explorar novamente.")
    print()


def descansar(p):
    """Restaura HP ao máximo."""
    p["hp"] = hp_max(p)
    print(f"\n  Você descansou na taverna. HP restaurado para {p['hp']}.\n")


def subir_nivel(p):
    """Sobe de nível se o XP for suficiente."""
    xp_necessario = p["nivel"] * XP_POR_NIVEL
    if p["xp"] < xp_necessario:
        faltam = xp_necessario - p["xp"]
        print(f"\n  Faltam {faltam} XP para o nível {p['nivel'] + 1}.\n")
        return
    p["xp"]    -= xp_necessario
    p["nivel"]  += 1
    p["hp"]      = hp_max(p)
    print(f"\n  ★ LEVEL UP! Agora você é nível {p['nivel']}. HP: {p['hp']}.\n")


def adicionar_item(p):
    """Adiciona um item ao inventário."""
    item = input("  Item encontrado: ").strip()
    if not item:
        print("  Nome vazio — ignorado.\n")
        return
    p["itens"].append(item)
    print(f"  '{item}' adicionado ao inventário.\n")


def main():
    p = carregar_personagem()
    if p is None:
        p = criar_personagem()
    else:
        print(f"\nBem-vindo de volta, {p['nome']}! (Nível {p['nivel']})\n")

    print("Comandos: ficha | explorar | descansar | nivel | item | salvar | sair\n")

    while True:
        comando = input("> ").strip().lower()

        if comando == "sair":
            salvar_personagem(p)
            print(f"\nSalvo em '{ARQUIVO}'. Até logo, {p['nome']}!\n")
            break
        elif comando == "ficha":
            exibir_ficha(p)
        elif comando == "explorar":
            if p["hp"] == 0:
                print("\n  HP zerado! Descanse primeiro.\n")
            else:
                explorar(p)
        elif comando == "descansar":
            descansar(p)
        elif comando == "nivel":
            subir_nivel(p)
        elif comando == "item":
            adicionar_item(p)
        elif comando == "salvar":
            salvar_personagem(p)
            print("  Ficha salva!\n")
        else:
            print("  Comando não reconhecido.\n")


main()
