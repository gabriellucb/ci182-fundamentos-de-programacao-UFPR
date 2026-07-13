# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Strings
# ────────────────────────────────────────────────────────────
#
# O programa deve ler uma frase e exibir:
#   - a frase em maiúsculas
#   - a quantidade de palavras
#   - a última palavra
#   - a frase com a primeira letra de cada palavra em maiúscula
#
# Saída esperada (frase: "hello world python"):
#
#   Maiúsculas:    HELLO WORLD PYTHON
#   Palavras:      3
#   Última:        python
#   Capitalizada:  Hello World Python
#
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

frase = input("Digite uma frase: ")

palavras = frase.Split()

print(f"Maiúsculas:    {frase.upper()}")
print(f"Palavras:      {len(frase)}")
print(f"Última:        {palavras[-1]}")
print(f"Capitalizada:  {frase.capitalize()}")
