"""Resposta: Aula 18 | Avançado
Exercício: ler notas de CSV, montar ranking com zip/enumerate, calcular
a média com statistics e salvar um relatório com aprovados e reprovados.
Gera um CSV de exemplo automaticamente se o arquivo de entrada não existir.
"""

import csv
import os
import statistics

ARQUIVO_ENTRADA = "notas_turma.csv"
ARQUIVO_SAIDA = "relatorio_final.txt"


def criar_exemplo():
    """Gera um CSV de exemplo quando o arquivo de entrada ainda não existe."""
    with open(ARQUIVO_ENTRADA, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Nota"])
        escritor.writerows([
            ["Ana Silva", 8.5],
            ["Beto Souza", 6.0],
            ["Carla Lima", 9.2],
            ["Diego Melo", 4.5],
            ["Eva Rocha", 7.0],
        ])
    print(f"Arquivo de exemplo criado: {ARQUIVO_ENTRADA}\n")


def carregar_turma(caminho):
    """Lê nomes e notas válidas do CSV e os empareha com zip."""
    nomes = []
    notas = []
    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                nota = float(linha["Nota"])
            except ValueError:
                print(f"  Linha inválida ignorada: {linha}")
                continue
            nomes.append(linha["Nome"])
            notas.append(nota)

    return list(zip(nomes, notas))


def salvar_relatorio(turma, media):
    """Escreve o relatório final com ranking, aprovados e reprovados."""
    ranking = sorted(turma, key=lambda item: item[1], reverse=True)

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO FINAL\n")
        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"{'#':<4}{'Nome':<20}{'Nota':>6}  Situação\n")
        arquivo.write("-" * 40 + "\n")

        aprovados = 0
        reprovados = 0
        for posicao, (nome, nota) in enumerate(ranking, start=1):
            if nota >= 7:
                situacao = "Aprovado"
                aprovados += 1
            else:
                situacao = "Reprovado"
                reprovados += 1
            arquivo.write(f"{posicao:<4}{nome:<20}{nota:>6.1f}  {situacao}\n")

        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"Média geral:  {media:.2f}\n")
        arquivo.write(f"Aprovados:    {aprovados}\n")
        arquivo.write(f"Reprovados:   {reprovados}\n")


def main():
    """Orquestra leitura, cálculo da média e geração do relatório."""
    try:
        if not os.path.exists(ARQUIVO_ENTRADA):
            criar_exemplo()

        turma = carregar_turma(ARQUIVO_ENTRADA)

        if not turma:
            print("Nenhuma nota válida encontrada no arquivo.")
            return

        notas = [nota for _, nota in turma]
        media = statistics.mean(notas)

        print(f"Alunos carregados: {len(turma)}")
        print(f"Média geral:       {media:.2f}")

        salvar_relatorio(turma, media)
        print(f"Relatório salvo em: {ARQUIVO_SAIDA}")

    except FileNotFoundError as erro:
        print(f"Arquivo não encontrado: {erro}")
    except ValueError as erro:
        print(f"Erro ao processar dados: {erro}")


if __name__ == "__main__":
    main()
