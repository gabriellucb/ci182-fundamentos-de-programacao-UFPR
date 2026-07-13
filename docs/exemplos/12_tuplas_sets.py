"""Grade de show de trap/funk — tuplas como ficha de artista, sets como grade de cada dia.

Você comprou ingresso só pro sábado achando que ia ser o dia mais maneiro.
Não pesquisou o lineup completo. Erro clássico. Esse programa faz o que
você deveria ter feito antes: cruza as grades dos três dias, descobre quem
toca em mais de uma noite e lista exatamente o que você vai perder.

Conceitos: tuplas, desempacotamento, sets, operações de conjunto (|, &, -), add, for.
"""

lineup = {
    "matue":      ("Matuê",      "trap",  90),
    "teto":       ("Teto",       "trap",  60),
    "wiu":        ("WIU",        "trap",  45),
    "brandao":    ("Brandão",    "trap",  55),
    "alee":       ("Alee",       "trap",   50),
    "ga":         ("G.A.",       "trap",   45),
    "veigh":      ("Veigh",      "trap",   50),
    "mc_livinho": ("MC Livinho", "funk",  65),
}

sexta   = {"alee", "brandao", "ga", "veigh", "wiu"}
sabado  = {"matue", "teto", "mc_livinho", "alee", "brandao"}
domingo = {"matue", "wiu", "mc_livinho", "veigh", "teto"}

print("=== GRADE DO FESTIVAL ===")
print(f"\nTotal de artistas no festival: {len(sexta | sabado | domingo)}")

for nome_dia, grade in [("Sexta", sexta), ("Sábado", sabado), ("Domingo", domingo)]:
    minutos = 0
    generos = set()
    for chave in grade:
        _, genero, duracao = lineup[chave] 
        generos.add(genero)
        minutos += duracao
    horas = minutos // 60
    resto  = minutos % 60
    print(f"\n{nome_dia} — {len(grade)} artistas, {horas}h{resto:02d} de música")
    print(f"  Gêneros: {', '.join(sorted(generos))}")
    for chave in sorted(grade):
        nome, _, duracao = lineup[chave]
        print(f"  {nome} ({duracao} min)")

repete = (sexta & sabado) | (sexta & domingo) | (sabado & domingo)
print(f"\nArtistas em mais de um dia ({len(repete)}):")
for chave in sorted(repete):
    nome, genero, _ = lineup[chave]
    dias = []
    if chave in sexta:
        dias.append("sex")
    if chave in sabado:
        dias.append("sáb")
    if chave in domingo:
        dias.append("dom")
    print(f"  {nome} ({genero}) — {' + '.join(dias)}")

perderia = (sexta | domingo) - sabado
print(f"\nSe for só no sábado, perde ({len(perderia)}):")
for chave in sorted(perderia):
    nome, genero, duracao = lineup[chave]
    print(f"  {nome} ({genero}, {duracao} min)")
