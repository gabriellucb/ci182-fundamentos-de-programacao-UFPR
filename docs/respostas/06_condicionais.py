"""Resposta — Aula 06: Condicionais
Exercício: classificação de IMC.
"""

peso   = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura ** 2

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"\nIMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
