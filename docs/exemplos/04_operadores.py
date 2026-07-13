"""Racha de pizza — operadores aritméticos, divisão inteira e módulo.

Sexta à noite, galera reunida e ninguém quer pagar mais do que deve.
Esse programa divide a conta com precisão de centavo e ainda diz quantas fatias sobram pra disputar.

Conceitos: +, -, *, /, //, %, int(), round(), operadores de comparação.
"""

print("=== RACHA DE PIZZA ===")
print()

pessoas  = int(input("Quantas pessoas? "))
pizzas   = int(input("Quantas pizzas? "))
preco    = float(input("Preço por pizza (R$): "))
bebidas  = float(input("Total em bebidas (R$): "))
gorjeta  = float(input("Gorjeta (%) [0 se nenhuma]: "))

subtotal      = pizzas * preco + bebidas
valor_gorjeta = subtotal * gorjeta / 100
total         = subtotal + valor_gorjeta

por_pessoa = total / pessoas
reais      = int(por_pessoa)
centavos   = round((por_pessoa - reais) * 100)

FATIAS_POR_PIZZA  = 8
total_fatias      = pizzas * FATIAS_POR_PIZZA
fatias_cada       = total_fatias // pessoas
fatias_disputadas = total_fatias % pessoas

print()
print("------------ CONTA ------------")
print("Subtotal:          R$", round(subtotal, 2))
print("Gorjeta:           R$", round(valor_gorjeta, 2))
print("Total:             R$", round(total, 2))
print()
print("Cada um deve:      R$", reais, "reais e", centavos, "centavos")
print()
print("----------- FATIAS ------------")
print("Total de fatias:  ", total_fatias)
print("Fatias por pessoa:", fatias_cada)
print("Sobram", fatias_disputadas, "fatia(s)")
print()
print("Pelo menos 2 fatias por pessoa:", fatias_cada >= 2)
