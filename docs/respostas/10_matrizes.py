"""Resposta — Aula 10: Matrizes
Exercício: matriz 4×4 zerada, diagonal com 1, inserção manual, soma de linhas e colunas.
"""

N = 4

matriz = []
for i in range(N):
    linha = []
    for j in range(N):
        linha.append(0)
    matriz.append(linha)

for i in range(N):
    matriz[i][i] = 1

print("Matriz inicial:")
for linha in matriz:
    print("  ", end="")
    for val in linha:
        print(f"{val:4}", end="")
    print()

linha_idx = int(input("\nLinha (0-3):  "))
col_idx   = int(input("Coluna (0-3): "))
valor     = int(input("Valor:        "))
matriz[linha_idx][col_idx] = valor

print("\nMatriz atualizada:")
for linha in matriz:
    print("  ", end="")
    for val in linha:
        print(f"{val:4}", end="")
    print()

print("\nSoma por linha:")
for i in range(N):
    total = 0
    for j in range(N):
        total += matriz[i][j]
    print(f"  Linha {i}: {total}")

print("\nSoma por coluna:")
for j in range(N):
    total = 0
    for i in range(N):
        total += matriz[i][j]
    print(f"  Coluna {j}: {total}")
