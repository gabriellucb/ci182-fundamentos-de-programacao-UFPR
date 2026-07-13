"""Resposta: Aula 15 | Módulos
Exercício: importar uteis.py, gerar notas com random, registrar data/hora e salvar CSV.
Execute a partir da pasta docs/respostas/15_modulos/ (o resultado.csv é gerado ali mesmo).
"""

import random
import datetime
import csv

from uteis import media, maior, menor


def main():
    """Gera notas aleatórias, calcula estatísticas e salva tudo em CSV."""
    notas = []
    for _ in range(10):
        nota = round(random.uniform(0, 10), 1)
        notas.append(nota)

    agora = datetime.datetime.now()
    momento = agora.strftime("%d/%m/%Y %H:%M:%S")

    print(f"Execução: {momento}")
    print(f"\nNotas geradas: {notas}")
    print(f"Média:         {media(notas):.2f}")
    print(f"Maior:         {maior(notas):.1f}")
    print(f"Menor:         {menor(notas):.1f}")

    with open("resultado.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nota", "Execucao"])
        for nota in notas:
            writer.writerow([nota, momento])

    print("\nResultados salvos em resultado.csv")


if __name__ == "__main__":
    main()
