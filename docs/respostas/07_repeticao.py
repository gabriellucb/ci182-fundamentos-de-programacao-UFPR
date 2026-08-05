"""Resposta: Aula 07 | Repetição
Exercício: leitura de números até digitar 0, soma, quantidade, média e maior.
"""

soma       = 0
quantidade = 0
maior      = None

print("Digite números (0 para encerrar):")

while True:
    numero = float(input("  Número: "))
    if numero == 0:
        break
    soma       += numero
    quantidade += 1
    if maior is None or numero > maior:
        maior = numero

if quantidade == 0:
    print("\nNenhum número digitado.")
else:
    media = soma / quantidade
    print(f"\nQuantidade: {quantidade}")
    print(f"Soma:       {soma:.2f}")
    print(f"Média:      {media:.2f}")
    print(f"Maior:      {maior:.2f}")
