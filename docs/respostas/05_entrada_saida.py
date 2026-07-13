"""Resposta — Aula 05: Entrada e Saída
Exercício: contracheque com cálculo de desconto INSS.
"""

nome        = input("Nome do funcionário: ")
salario     = float(input("Salário bruto (R$): "))
percentual  = float(input("Percentual INSS (%): "))

desconto = salario * (percentual / 100)
liquido  = salario - desconto

print(f"\n{'='*32}")
print(f"{'CONTRACHEQUE':^32}")
print(f"{'='*32}")
print(f"{'Funcionário':<16}: {nome}")
print(f"{'Salário bruto':<16}: R$ {salario:>9,.2f}")
print(f"{'Desconto INSS':<16}: R$ {desconto:>9,.2f}")
print(f"{'Salário líquido':<16}: R$ {liquido:>9,.2f}")
print(f"{'='*32}")
