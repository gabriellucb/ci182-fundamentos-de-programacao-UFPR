# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Arquivos
# ────────────────────────────────────────────────────────────
#
# Um diário de horas de estudo registra sessões e exibe
# estatísticas ao final.
#
# Para testar: apague 'docs/debug/medio/estudo.csv' se ele existir, depois
# execute o programa três vezes seguidas registrando uma
# sessão por vez:
#   1ª execução: "Algoritmos", 2.5 horas
#   2ª execução: "Cálculo",    1.0 hora
#   3ª execução: "Programação", 3.0 horas
#
# Saída esperada na 3ª execução (acumulado das 3 sessões):
#
#   Sessões registradas: 3
#   Total de horas: 6.5h
#   Média por sessão: 2.2h
#
# Encontre os bugs. O programa roda sem erros,
# mas os resultados estão incorretos.
# ────────────────────────────────────────────────────────────

ARQUIVO = "docs/debug/medio/estudo.csv"


def registrar_sessao(disciplina, horas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        f.write(f"{disciplina},{horas:.1f}\n")


def relatorio():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print("Nenhuma sessão registrada ainda.")
        return

    if len(linhas) == 0:
        print("Nenhuma sessão registrada ainda.")
        return

    num_sessoes = len(linhas)

    for linha in linhas:
        total_horas = 0.0
        partes = linha.strip().split(",")
        total_horas += float(partes[1])

    media = total_horas / len(partes)

    print(f"Sessões registradas: {num_sessoes}")
    print(f"Total de horas: {media:.1f}h")
    print(f"Média por sessão: {total_horas:.1f}h")


print("=== DIÁRIO DE ESTUDO ===")
while True:
    print("\n1. Registrar sessão")
    print("2. Ver relatório")
    print("3. Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        disciplina = input("Disciplina: ").strip()
        try:
            horas = float(input("Horas estudadas: "))
        except ValueError:
            print("Digite um número.")
            continue
        registrar_sessao(disciplina, horas)
        print(f"Sessão registrada: {disciplina}, {horas:.1f}h")
    elif opcao == "2":
        relatorio()
    elif opcao == "3":
        break
