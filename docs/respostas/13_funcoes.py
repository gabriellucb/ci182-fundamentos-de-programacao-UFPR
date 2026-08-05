"""Resposta: Aula 13 | Funções
Exercício: media(), eh_par() e saudar(); toda lógica dentro das funções,
hora recebida como parâmetro inteiro (0–23).
"""


def media(numeros):
    """Retorna a média aritmética de uma lista de números."""
    return sum(numeros) / len(numeros)


def eh_par(numero):
    """Retorna True se o número é par, False caso contrário."""
    return numero % 2 == 0


def saudar(nome, hora):
    """Retorna uma saudação adequada ao período do dia."""
    if hora < 12:
        periodo = "Bom dia"
    elif hora < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"
    return f"{periodo}, {nome}!"


def main():
    """Programa principal que usa as três funções juntas."""
    nome = input("Seu nome: ")
    hora = int(input("Que horas são? (0-23): "))
    print(saudar(nome, hora))

    numeros_str = input("Digite números separados por espaço: ").split()
    numeros = []
    for n in numeros_str:
        numeros.append(float(n))
    print(f"Média: {media(numeros):.2f}")

    numero = int(input("Digite um número para verificar paridade: "))
    if eh_par(numero):
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")


main()
