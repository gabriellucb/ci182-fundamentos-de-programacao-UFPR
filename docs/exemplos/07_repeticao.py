"""Ficha de Treino — while, for, range, break, continue, acumuladores, laços aninhados.

Toda semana eu planejo ir na academia. Essa já passou. A próxima com certeza vai. 
Enquanto eu procrastino, esse programa pelo menos gera uma ficha para auxiliar onde 
cada □ é uma repetição pra riscar.

Conceitos: while, for, range, break, continue, acumuladores, laços aninhados.

Os símbolos □ ─ │ ┌ ┐ └ ┘ são caracteres Unicode, strings normais. Copie daqui
ou pesquise "unicode box drawing" e "unicode misc symbols" numa tabela online.
No VS Code: Ctrl+Shift+P -> "Insert Unicode character".
"""

LIMITE_REPS = 15

print("=== FICHA DE TREINO ===\n")
print("Cadastre os exercícios do dia. Digite 'fim' para encerrar.\n")

total_exercicios = 0
total_series     = 0
total_reps       = 0

while True:
    exercicio = input("Exercício (ou 'fim'): ").strip()

    if exercicio.lower() == "fim":
        break

    if exercicio == "":
        print("Nome em branco. Tenta de novo.\n")
        continue

    series = int(input("  Séries: "))
    reps   = int(input("  Repetições por série: "))

    exibir  = reps
    if exibir > LIMITE_REPS:
        exibir = LIMITE_REPS

    borda_h = "─" * (exibir * 2 + 1)

    print(f"\n  {exercicio.upper()}  ·  {series} séries  ×  {reps} reps")
    print("  ┌" + borda_h + "┐")
    for serie in range(series):
        print("  │ ", end="")
        for rep in range(exibir):
            print("□", end=" ")
        if reps > LIMITE_REPS:
            print(f"│  série {serie + 1}  (+{reps - LIMITE_REPS} reps)")
        else:
            print(f"│  série {serie + 1}")
    print("  └" + borda_h + "┘")
    print()

    total_exercicios += 1
    total_series     += series
    total_reps       += series * reps


if total_exercicios == 0:
    print("Nenhum exercício cadastrado. Dia de descanso (mais uma vez).")
else:
    print("=" * 40)
    print("  RESUMO")
    print("=" * 40)
    print(f"  Exercícios : {total_exercicios}")
    print(f"  Séries     : {total_series}")
    print(f"  Total reps : {total_reps}")
    print()
    if total_reps >= 400:
        print("  Treino pesado. Você é uma máquina.")
    elif total_reps >= 150:
        print("  Ficha bem consistente.")
    elif total_reps >= 60:
        print("  Bom começo. Melhor que zero.")
    else:
        print("  Tá lesionado é?")
