"""Log de partida — filtros, estatísticas e fatiamento de listas.

Aquele momento no fim da partida onde você abre as estatísticas e descobre
que fez 9% do dano total da equipe enquanto ficava "dando suporte". Esse
programa processa o log de uma rodada e entrega os números sem piedade:
quem matou, quem curou, quem morreu três vezes e ainda assim conseguiu
o abate final.

Conceitos: criação de lista, append, extend, in, len, sum, max, min,
           index, count, enumerate, copy, sort, fatiamento.
"""

tipos     = ["DANO",       "DANO",         "CURA",         "DANO",        "ABATE",
             "MORTE",      "DANO",         "CURA",         "DANO",        "DANO",
             "ABATE",      "MORTE",        "CURA",         "DANO",        "DANO",
             "ABATE",      "MORTE",        "DANO",         "CURA",        "MORTE",
             "DANO",       "ABATE"]

jogadores = ["Sandero",     "SujiroKifuja", "SirBagre",     "Sandero",     "SujiroKifuja",
             "PhessoMort0", "PhessoMort0",  "SirBagre",     "SujiroKifuja","Sandero",
             "Sandero",     "PhessoMort0",  "SirBagre",     "PhessoMort0", "Sandero",
             "SujiroKifuja","PhessoMort0",  "PhessoMort0",  "SirBagre",    "Sandero",
             "SujiroKifuja","PhessoMort0"]

valores   = [85,  120,   60,  70,   0,
              0,   40,   45,  95,  55,
              0,    0,   75,  88, 110,
              0,    0,   35,  50,   0,
            130,    0]

print("=== LOG DA PARTIDA ===")
print(f"{len(tipos)} eventos registrados.\n")

for i, tipo in enumerate(tipos):
    if tipo in ("ABATE", "MORTE"):
        print(f"  [{i + 1:02d}] {tipo:<5} — {jogadores[i]}")
    else:
        print(f"  [{i + 1:02d}] {tipo:<5} — {jogadores[i]}: {valores[i]} pts")

# danos
hits    = []
autores = []
for i, tipo in enumerate(tipos):
    if tipo == "DANO":
        hits.append(valores[i])
        autores.append(jogadores[i])

maior = max(hits)
idx   = hits.index(maior)

print("\n--- DANO ---")
print(f"  Acertos:     {len(hits)}")
print(f"  Total:       {sum(hits)} pts")
print(f"  Maior hit:   {maior} pts — {autores[idx]}")
print(f"  Menor hit:   {min(hits)} pts")
print(f"  Média:       {sum(hits) / len(hits):.1f} pts")

ranking = hits.copy()
ranking.sort(reverse=True)
print(f"  Top 3 hits:  {ranking[:3]}")

# curas
curas     = []
curadores = []
for i, tipo in enumerate(tipos):
    if tipo == "CURA":
        curas.append(valores[i])
        curadores.append(jogadores[i])

maior_cura = max(curas)
idx_cura   = curas.index(maior_cura)

print("\n--- CURA ---")
print(f"  Total curado: {sum(curas)} pts")
print(f"  Maior cura:   {maior_cura} pts — {curadores[idx_cura]}")

# abates
killers = []
for i, tipo in enumerate(tipos):
    if tipo == "ABATE":
        killers.append(jogadores[i])

print(f"\n--- ABATES ({len(killers)} no total) ---")
for i, nick in enumerate(killers, start=1):
    print(f"  {i}. {nick}")

# mortes
mortos = []
for i, tipo in enumerate(tipos):
    if tipo == "MORTE":
        mortos.append(jogadores[i])

print(f"\n--- MORTES ({len(mortos)} no total) ---")
for i, nick in enumerate(mortos, start=1):
    print(f"  {i}. {nick}")

mortos_unicos = []
for nick in mortos:
    if nick not in mortos_unicos:
        mortos_unicos.append(nick)
for nick in mortos_unicos:
    print(f"  {nick}: {mortos.count(nick)}x")

# participação em combate (dano + abate)
combatentes = autores.copy()
combatentes.extend(killers)

nicks_unicos = []
for nick in combatentes:
    if nick not in nicks_unicos:
        nicks_unicos.append(nick)
nicks_unicos.sort()

print("\n--- PARTICIPAÇÃO EM COMBATE ---")
for nick in nicks_unicos:
    print(f"  {nick:<14}: {combatentes.count(nick)} ação(ões)")

# recorte do log
print(f"\nInício da rodada (primeiros 5): {jogadores[:5]}")
print(f"Fim da rodada (últimos 3):      {jogadores[-3:]}")

# ficha individual
foco  = "PhessoMort0"
acoes = jogadores.count(foco)

if foco in killers:
    status = "sim"
else:
    status = "não"

dano_foco = []
for i, autor in enumerate(autores):
    if autor == foco:
        dano_foco.append(hits[i])

print(f"\n--- FICHA: {foco} ---")
print(f"  Ações no log: {acoes}")
print(f"  Mortes:       {mortos.count(foco)}x")
print(f"  Fez abate:    {status}")
print(f"  Dano total:   {sum(dano_foco)} pts")
print(f"  Maior hit:    {max(dano_foco)} pts")
print(f"  Share do time:{sum(dano_foco) / sum(hits) * 100:.1f}%")
