"""Resposta: Aula 04 | Operadores
Exercício: soma, média, divisão, paridade e comparação de três números.
"""

a = int(input("Primeiro número:  "))
b = int(input("Segundo número:   "))
c = int(input("Terceiro número:  "))

soma      = a + b + c
media     = soma / 3
quociente = a // b
resto     = a % b

print("Soma:", soma)
print("Média:", media)
print("Quociente de", a, "por", b, ":", quociente)
print("Resto de", a, "por", b, ":", resto)
print(c, "é par?", c % 2 == 0)
print("Média maior que", c, "?", media > c)
