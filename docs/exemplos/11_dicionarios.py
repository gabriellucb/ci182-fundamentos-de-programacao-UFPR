"""Artilharia da Copa do Mundo — dicionários, dicionários aninhados, lista de dicionários.

Copa do mundo é a única época do ano em que seu amigo que não liga para esporte
de repente vira o maior comentarista esportivo do país. Esse programa mantém a
artilharia atualizada: fichas de jogadores, histórico de gols e um menu para
registrar o próximo gol ao vivo sem sair do terminal.

Conceitos: dicionários, .get(), .items(), .values(), in,
           dicionários aninhados, lista de dicionários, contador de ocorrências.
"""

tipos_de_gol = {
    "normal":  "gol de campo",
    "cabeca":  "gol de cabeça",
    "falta":   "cobrança de falta",
    "penalti": "pênalti",
    "contra":  "gol contra",
}

artilheiros = {
    "Mbappé":    {"selecao": "França",          "gols": 5, "assist": 2, "jogos": 6},
    "Vini Jr":   {"selecao": "Brasil",          "gols": 4, "assist": 3, "jogos": 6},
    "Kane":      {"selecao": "Inglaterra",      "gols": 4, "assist": 1, "jogos": 5},
    "Messi":     {"selecao": "Argentina",       "gols": 6, "assist": 3, "jogos": 7},
    "Cristiano": {"selecao": "Portugal",        "gols": 3, "assist": 0, "jogos": 5},
    "Havertz":   {"selecao": "Alemanha",        "gols": 3, "assist": 2, "jogos": 5},
    "Haaland":   {"selecao": "Noruega",         "gols": 4, "assist": 1, "jogos": 5},
    "Diomandé":  {"selecao": "Costa do Marfim", "gols": 2, "assist": 1, "jogos": 4},
}

gols = [
    {"artilheiro": "Messi",     "minuto": 10, "adversario": "Arábia Saudita", "tipo": "normal"},
    {"artilheiro": "Mbappé",    "minuto": 23, "adversario": "Austrália",      "tipo": "normal"},
    {"artilheiro": "Vini Jr",   "minuto": 37, "adversario": "Sérvia",         "tipo": "cabeca"},
    {"artilheiro": "Kane",      "minuto": 45, "adversario": "Irã",            "tipo": "penalti"},
    {"artilheiro": "Haaland",   "minuto": 54, "adversario": "Inglaterra",     "tipo": "normal"},
    {"artilheiro": "Cristiano", "minuto": 62, "adversario": "Gana",           "tipo": "penalti"},
    {"artilheiro": "Havertz",   "minuto": 71, "adversario": "Japão",          "tipo": "falta"},
    {"artilheiro": "Diomandé",  "minuto": 80, "adversario": "Marrocos",       "tipo": "cabeca"},
    {"artilheiro": "Mbappé",    "minuto": 88, "adversario": "Dinamarca",      "tipo": "normal"},
    {"artilheiro": "Messi",     "minuto": 93, "adversario": "França",         "tipo": "penalti"},
]

LINHA = "─" * 48

print(f"\n  {'ARTILHARIA DA COPA DO MUNDO':^44}")
print(f"  {LINHA}")
print(f"  {'Jogador':<12} {'Seleção':<18} {'G':>3} {'A':>3} {'J':>3}")
print(f"  {LINHA}")
for nome, ficha in artilheiros.items():
    print(f"  {nome:<12} {ficha['selecao']:<18} "
          f"{ficha['gols']:>3} {ficha['assist']:>3} {ficha['jogos']:>3}")

gols_por_selecao = {}
for ficha in artilheiros.values():
    s = ficha["selecao"]
    gols_por_selecao[s] = gols_por_selecao.get(s, 0) + ficha["gols"]

print("\n  Gols por seleção")
print(f"  {'─' * 28}")
for selecao, total in gols_por_selecao.items():
    barra = "█" * total
    print(f"  {selecao:<18} {total:>2}  {barra}")

print("\n  Últimos gols")
print(f"  {'─' * 28}")
for registro in gols[-3:]:
    descricao = tipos_de_gol.get(registro["tipo"], "gol")
    print(f"  {registro['artilheiro']:<10} {registro['minuto']:>2}'  "
          f"vs {registro['adversario']:<16} {descricao}")

while True:
    print(f"\n  {LINHA}")
    print(f"  {'[1]'} Registrar gol   {'[2]'} Ver ficha   {'[3]'} Sair")
    print(f"  {LINHA}")
    opcao = input("  Opção: ").strip()

    if opcao == "1":
        jogador_input = input("  Jogador: ").strip()
        adversario    = input("  Adversário: ").strip()
        minuto        = int(input("  Minuto: "))
        tipo_input    = input("  Tipo (normal/cabeca/falta/penalti/contra): ").strip().lower()

        tipo_valido = tipo_input if tipo_input in tipos_de_gol else "normal"
        descricao   = tipos_de_gol[tipo_valido]

        jogador = jogador_input
        for nome in artilheiros:
            if nome.lower() == jogador_input.lower():
                jogador = nome
                break

        gols.append({
            "artilheiro": jogador,
            "minuto":     minuto,
            "adversario": adversario,
            "tipo":       tipo_valido,
        })

        if jogador in artilheiros:
            artilheiros[jogador]["gols"] += 1
            print(f"\n  ✓ {jogador} ({descricao}) {minuto}' vs {adversario}")
            print(f"    Total no torneio: {artilheiros[jogador]['gols']} gols")
        else:
            artilheiros[jogador] = {"selecao": "?", "gols": 1, "assist": 0, "jogos": 1}
            print(f"\n  ✓ Novo artilheiro: {jogador} — 1 gol vs {adversario}")

    elif opcao == "2":
        jogador_input = input("  Jogador: ").strip()

        jogador = None
        for nome in artilheiros:
            if nome.lower() == jogador_input.lower():
                jogador = nome
                break

        if jogador:
            ficha = artilheiros[jogador]
            print(f"\n  {jogador} — {ficha['selecao']}")
            print(f"  {'─' * 28}")
            print(f"  Gols: {ficha['gols']}   Assist: {ficha.get('assist', 0)}   Jogos: {ficha['jogos']}")
            print(f"  {'─' * 28}")
            encontrou = False
            for registro in gols:
                if registro["artilheiro"] == jogador:
                    descricao = tipos_de_gol.get(registro["tipo"], "gol")
                    print(f"  {registro['minuto']:>2}'  vs {registro['adversario']:<18} {descricao}")
                    encontrou = True
            if not encontrou:
                print("  Nenhum gol registrado ainda.")
        else:
            print(f"  Jogador '{jogador_input}' não encontrado.")

    elif opcao == "3":
        lider = ""
        mais_gols = -1
        for nome, ficha in artilheiros.items():
            if ficha["gols"] > mais_gols:
                mais_gols = ficha["gols"]
                lider = nome

        ficha_lider = artilheiros[lider]
        print(f"\n  {LINHA}")
        print(f"  Artilheiro do torneio: {lider} ({ficha_lider['selecao']})")
        print(f"  {mais_gols} gols  ·  {ficha_lider.get('assist', 0)} assistência(s)")
        print(f"  {LINHA}\n")
        break

    else:
        print("  Opção inválida.")
