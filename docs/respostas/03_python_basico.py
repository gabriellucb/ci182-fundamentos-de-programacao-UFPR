"""Resposta — Aula 03: Python Básico
Exercício: nome, idade e ano em que o usuário vai fazer 30 anos.
"""

nome  = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

anos_para_30 = 30 - idade
ano_atual    = 2026
ano_30       = ano_atual + anos_para_30

print("Olá,", nome + "! Em", ano_30, "você vai fazer 30 anos.")
