"""Resposta: Aula 08 | Strings
Exercício: análise de frase, maiúsculas, minúsculas, total de letras
(sem espaços/pontuação), primeira palavra, contagem de 'a' e frase invertida.
"""

frase = input("Digite uma frase: ").strip()

if len(frase) == 0:
    print("Frase vazia.")
else:
    palavras = frase.split()

    total_letras = 0
    for caractere in frase:
        if caractere.isalpha():
            total_letras += 1

    contagem_a = frase.lower().count("a")

    print(f"\nMaiúsculas:        {frase.upper()}")
    print(f"Minúsculas:        {frase.lower()}")
    print(f"Total de letras:   {total_letras}")
    print(f"Primeira palavra:  {palavras[0]}")
    print(f"Letra 'a' aparece: {contagem_a} vez(es)")
    print(f"Frase invertida:   {frase[::-1]}")
