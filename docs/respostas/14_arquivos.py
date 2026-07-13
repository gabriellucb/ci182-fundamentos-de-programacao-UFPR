"""Resposta — Aula 14: Arquivos
Exercício: salvar alunos/notas em CSV, ler de volta e calcular média da turma.
Execute duas vezes para ver o modo append funcionando.

Nota: 'turma.csv' é criado na pasta de onde você rodar o script.
É gerado pelo programa, pode apagar depois de testar.
"""

ARQUIVO = "turma.csv"


def salvar_aluno(nome, nota):
    """Acrescenta um aluno ao arquivo CSV sem apagar os anteriores."""
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{nome},{nota:.1f}\n")


def carregar_turma():
    """Lê o arquivo CSV e retorna lista de tuplas (nome, nota)."""
    alunos = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha == "":
                    continue
                partes = linha.split(",")
                nome   = partes[0]
                nota   = float(partes[1])
                alunos.append((nome, nota))
    except FileNotFoundError:
        pass   # arquivo ainda não existe, ou seja, turma vazia
    return alunos


def relatorio(alunos):
    """Exibe média geral e quem ficou acima e abaixo dela."""
    if len(alunos) == 0:
        print("Nenhum aluno no arquivo.")
        return

    soma = 0
    for nome, nota in alunos:
        soma += nota
    media = soma / len(alunos)

    print(f"\nMédia geral da turma: {media:.2f}")
    print("\nAcima da média:")
    for nome, nota in alunos:
        if nota >= media:
            print(f"  {nome:<20} {nota:.1f}")
    print("\nAbaixo da média:")
    for nome, nota in alunos:
        if nota < media:
            print(f"  {nome:<20} {nota:.1f}")


def main():
    """Coleta alunos pelo teclado, salva em CSV e exibe o relatório da turma."""
    print("Digite os alunos (nome vazio ou 'fim' para encerrar):")

    while True:
        nome = input("  Nome: ").strip()
        if nome == "" or nome.lower() == "fim":
            break
        try:
            nota = float(input(f"  Nota de {nome}: "))
        except ValueError:
            print("  Nota inválida — digite um número.")
            continue
        salvar_aluno(nome, nota)
        print(f"  '{nome}' salvo.\n")

    turma = carregar_turma()
    relatorio(turma)


main()
