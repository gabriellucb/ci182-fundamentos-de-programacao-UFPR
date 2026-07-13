"""Username check para jogos — métodos de string, fatiamento, for.

Nome de jogo é um tipo de identidade. Esse programa verifica se o nick passa nas
regras básicas da maioria das plataformas (tamanho, caracteres, posição de símbolos),
conta vogais, gera versão "leet" (letras trocadas por números parecidos: a→4,
e→3, i→1, o→0), detecta palíndromo e mais.

Conceitos: len, isalnum, isdigit, isalpha, startswith, endswith, find, count,
           replace, split, join, upper/lower/strip, fatiamento, indexação, for, in.
"""

MINIMO = 3
MAXIMO = 20

print("=== USERNAME CHECK ===\n")

nick = input("Qual nickname você quer testar? ").strip()

if len(nick) == 0:
    print("Username vazio não rola.")
else:
    nick_lower = nick.lower()
    tamanho = len(nick)

    print(f"\nNick:    {nick}")
    print(f"Tamanho: {tamanho}/{MAXIMO} caracteres\n")

    # --- validações ---
    valido = True

    if tamanho < MINIMO:
        print(f"  Muito curto — mínimo {MINIMO} caracteres.")
        valido = False
    if tamanho > MAXIMO:
        print(f"  Muito longo — máximo {MAXIMO} caracteres.")
        valido = False
    if not nick.replace("_", "").replace("-", "").isalnum():
        print("  Só letras, números, _ e - são permitidos.")
        valido = False
    if nick[0].isdigit():
        print("  Não pode começar com número.")
        valido = False
    if nick.startswith("-") or nick.startswith("_"):
        print("  Não pode começar com traço ou underscore.")
        valido = False
    if nick.endswith("-") or nick.endswith("_"):
        print("  Não pode terminar com traço ou underscore.")
        valido = False

    if valido:
        print("Nick válido! Passa nas regras básicas.\n")

        vogais = "aeiouáéíóúàâãèêìîõòôùû"
        qtd_letras = 0
        qtd_vogais = 0
        for letra in nick_lower:
            if letra.isalpha():
                qtd_letras += 1
                if letra in vogais:
                    qtd_vogais += 1

        print(f"Letras:         {qtd_letras} ({qtd_vogais} vogais)")
        print(f"Invertido:      {nick[::-1]}")

        if "_" in nick:
            pos = nick.find("_")
            qtd = nick.count("_")
            partes = nick.split("_")
            print(f"\nUnderscores: {qtd} (primeiro na posição {pos})")
            print(f"Blocos:      {' | '.join(partes)}")

        leet = (nick_lower
            .replace("a", "4")
            .replace("e", "3")
            .replace("i", "1")
            .replace("o", "0")
            .replace("s", "5")
            .replace("t", "7")
        )
        print(f"\nVersão leet:  {leet}")

        if nick_lower == nick_lower[::-1]:
            print("\nSeu nick é palíndromo!!")
