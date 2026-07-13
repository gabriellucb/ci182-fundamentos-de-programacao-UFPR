"""10.000 horas — variáveis, tipos e operações básicas.

A regra das 10.000 horas diz o seguinte: para dominar de vez
qualquer habilidade complexa, você precisa de cerca de 10.000 horas de prática.
Aqui a gente calcula quando você chega lá na programação.

Conceitos: str, int, float, input(), print(), aritmética básica, type().
"""

print("=== ATÉ AS 10.000 HORAS ===")
print()

nome        = input("Seu nome: ")
horas_dia   = float(input("Quantas horas por dia você estuda programação? "))
dias_semana = int(input("Quantos dias por semana? "))

horas_semana  = horas_dia * dias_semana
horas_mes     = horas_semana * 4
anos_para_10k = 10000 / horas_semana / 52

print()
print(nome + ", no seu ritmo atual:")
print("  Horas por semana: ", round(horas_semana, 1)) # round() arredonda o valor
print("  Horas por mês:    ", round(horas_mes, 1))
print("  Anos até 10.000h: ", round(anos_para_10k, 1))

print()
print("(Tipos das variáveis, por curiosidade:)")
print("  nome:        ", type(nome))
print("  horas_dia:   ", type(horas_dia))
print("  dias_semana: ", type(dias_semana))
