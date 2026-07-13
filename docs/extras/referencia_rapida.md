# Referência Rápida: Python Fundamentos

Consulta rápida de sintaxe, métodos e padrões. Não substitui as aulas, serve para quando você já entende o conceito e só precisa lembrar como escreve.

---

## Tipos básicos

| Tipo | O que guarda | Exemplo |
|------|-------------|---------|
| `int` | Inteiro | `42`, `-7`, `0` |
| `float` | Decimal | `3.14`, `-0.5` |
| `str` | Texto | `"olá"`, `'Python'` |
| `bool` | Verdadeiro/Falso | `True`, `False` |
| `None` | Ausência de valor | `None` |

```python
type(42)       # <class 'int'>
int("10")      # 10
float("3.14")  # 3.14
str(42)        # "42"
bool(0)        # False  (0, "", [], {}, None → False; tudo mais → True)
```

---

## Operadores

### Aritméticos

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | Soma | `10 + 3` | `13` |
| `-` | Subtração | `10 - 3` | `7` |
| `*` | Multiplicação | `4 * 3` | `12` |
| `/` | Divisão (float) | `10 / 4` | `2.5` |
| `//` | Divisão inteira | `10 // 4` | `2` |
| `%` | Resto | `10 % 3` | `1` |
| `**` | Potência | `2 ** 8` | `256` |

### Relacionais

| Operador | Significado |
|----------|-------------|
| `==` | Igual |
| `!=` | Diferente |
| `>` / `<` | Maior / Menor |
| `>=` / `<=` | Maior ou igual / Menor ou igual |

### Lógicos

| Operador | Retorna `True` quando... |
|----------|--------------------------|
| `and` | As duas condições são verdadeiras |
| `or` | Pelo menos uma é verdadeira |
| `not` | A condição é falsa |

### Atribuição composta

```python
x += 3   # x = x + 3
x -= 2   # x = x - 2
x *= 4   # x = x * 4
x /= 2   # x = x / 2
x //= 3  # x = x // 3
x %= 2   # x = x % 2
x **= 2  # x = x ** 2
```

---

## Strings: métodos principais

```python
s = "  Olá, Mundo!  "

s.upper()          # "  OLÁ, MUNDO!  "
s.lower()          # "  olá, mundo!  "
s.strip()          # "Olá, Mundo!"       (remove espaços nas bordas)
s.lstrip()         # "Olá, Mundo!  "     (só da esquerda)
s.rstrip()         # "  Olá, Mundo!"     (só da direita)
s.strip().lower()  # "olá, mundo!"       (encadeando)

"olá mundo".split()          # ["olá", "mundo"]
"a,b,c".split(",")           # ["a", "b", "c"]
", ".join(["a", "b", "c"])   # "a, b, c"

"Python".replace("P", "p")   # "python"
"Python".startswith("Py")    # True
"Python".endswith("on")      # True
"Python".find("th")          # 2  (índice onde começa, -1 se não achar)
"Python".count("o")          # 1

"  ".isspace()      # True
"abc".isalpha()     # True
"123".isdigit()     # True
"abc123".isalnum()  # True

len("Python")     # 6
"Python"[0]       # "P"
"Python"[-1]      # "n"
"Python"[1:4]     # "yth"
"Python"[::-1]    # "nohtyP"
```

### Tarefas comuns: "quero... → como faço"

| Quero... | Como faço |
|----------|-----------|
| Inverter a string | `s[::-1]` |
| Pegar a primeira palavra | `s.split()[0]` |
| Pegar a última palavra | `s.split()[-1]` |
| Limpar espaços das bordas | `s.strip()` |
| Comparar ignorando maiúsculas | `s.lower() == outro.lower()` |
| Ver se contém um trecho | `"py" in s` |
| Contar quantas vezes algo aparece | `s.count("a")` |
| Trocar um trecho por outro | `s.replace("a", "b")` |
| Quebrar texto em lista | `s.split(",")` |
| Juntar uma lista em texto | `", ".join(lista)` |
| Conferir se é só dígitos | `s.isdecimal()` |

### f-string: formatação

```python
nome = "Ana"
nota = 8.567

f"{nome}"           # "Ana"
f"{nota:.2f}"       # "8.57"      (2 casas decimais)
f"{nota:.0f}"       # "9"         (sem decimal)
f"{1234567:,}"      # "1,234,567" (separador de milhar)
f"{nome:<10}"       # "Ana       " (alinhado à esquerda, 10 chars)
f"{nome:>10}"       # "       Ana" (alinhado à direita)
f"{nome:^10}"       # "   Ana    " (centralizado)
f"{'sim' if nota >= 7 else 'não'}"   # expressão condicional dentro
```

---

## Listas: métodos principais

```python
lista = [3, 1, 4, 1, 5]

lista.append(9)        # adiciona 9 no final → [3, 1, 4, 1, 5, 9]
lista.insert(2, 99)    # insere 99 no índice 2
lista.remove(1)        # remove a PRIMEIRA ocorrência de 1
lista.pop()            # remove e retorna o último item
lista.pop(0)           # remove e retorna o item no índice 0
lista.clear()          # remove tudo

lista.sort()           # ordena no lugar (modifica a original)
lista.sort(reverse=True)  # ordena em ordem decrescente
lista.reverse()        # inverte no lugar
sorted(lista)          # retorna nova lista ordenada (original intacta)

lista.index(4)         # índice da primeira ocorrência de 4
lista.count(1)         # quantas vezes 1 aparece
lista.copy()           # cópia independente (use em vez de lista2 = lista)

len(lista)             # tamanho
4 in lista             # True (pertencimento)
lista + [6, 7]         # concatenação → nova lista
lista * 2              # repetição → [3, 1, 4, 1, 5, 3, 1, 4, 1, 5]

# Fatiamento
lista[1:3]    # [1, 4]
lista[:2]     # [3, 1]
lista[2:]     # [4, 1, 5]
lista[::-1]   # invertida
```

---

## Dicionários: métodos principais

```python
d = {"nome": "Ana", "nota": 8.5, "ativo": True}

d["nome"]             # "Ana"
d.get("nome")         # "Ana"  (não lança erro se chave não existir)
d.get("idade", 0)     # 0  (valor padrão quando chave ausente)

d["cidade"] = "SP"    # adiciona ou atualiza
del d["ativo"]        # remove a chave

d.keys()              # dict_keys(['nome', 'nota', 'cidade'])
d.values()            # dict_values(['Ana', 8.5, 'SP'])
d.items()             # dict_items([('nome', 'Ana'), ...])

"nome" in d           # True (verifica se chave existe)
len(d)                # quantidade de pares

# Percorrendo
for chave, valor in d.items():
    print(f"{chave}: {valor}")
```

---

## Tuplas e Sets

```python
# Tupla (imutável, ordenada)
ponto = (3, 7)
x, y = ponto          # desempacotamento

# Set (sem duplicatas, sem ordem garantida)
nums = {1, 2, 2, 3}   # {1, 2, 3}
nums.add(4)
nums.discard(2)        # remove sem erro se não existir
4 in nums              # True

# Operações de conjunto
a = {1, 2, 3}
b = {2, 3, 4}
a | b   # união:       {1, 2, 3, 4}
a & b   # interseção:  {2, 3}
a - b   # diferença:   {1}
```

---

## Estruturas de controle

```python
# Condicional
if condicao:
    ...
elif outra:
    ...
else:
    ...

# Expressão condicional (ternário)
x = "par" if n % 2 == 0 else "ímpar"

# while
while condicao:
    ...

# for
for i in range(10):        # 0 a 9
    ...

for i in range(1, 11):     # 1 a 10
    ...

for i in range(0, 20, 2):  # 0, 2, 4...18
    ...

for item in lista:
    ...

for i, item in enumerate(lista, start=1):
    ...

for a, b in zip(lista1, lista2):
    ...

# Controle de fluxo
break      # sai do laço
continue   # pula para a próxima iteração

# match (Python 3.10+, alternativa a vários elif == "valor")
match opcao:
    case "1":
        print("Depósito")
    case "2" | "3":     # combina valores com |
        print("Saque ou saldo")
    case _:             # caso padrão, igual o else
        print("Opção inválida")
```

---

## Funções

```python
def nome(param1, param2="padrão"):
    return valor

# Chamada
resultado = nome("arg1")
resultado = nome("arg1", param2="outro")

# Lambda
dobrar = lambda x: x * 2
```

### Escopo de variáveis

```python
mensagem = "global"   # existe em todo o programa

def teste():
    resposta = "local"     # existe só dentro da função
    print(mensagem)        # a função pode LER a global
    return resposta

teste()
print(mensagem)    # "global"
print(resposta)    # NameError: resposta não existe aqui fora
```

### Docstrings

```python
def media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

help(media)         # mostra a docstring formatada
print(media.__doc__)   # "Calcula a média de uma lista de notas."
```

### Recursão

```python
def fatorial(n):
    if n <= 1:                     # caso base, encerra a recursão
        return 1
    return n * fatorial(n - 1)     # chama a si mesma com n menor

print(fatorial(5))   # 120
```

Toda função recursiva precisa de um caso base (senão vira `RecursionError`) e de progresso em direção a ele a cada chamada.

---

## Type hints

```python
nome:  str   = "Ana"
idade: int   = 20
nota:  float = 8.5

def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

def imprimir_relatorio(dados: list[str]) -> None:   # -> None: não retorna nada
    for linha in dados:
        print(linha)
```

O Python não verifica isso em tempo de execução, é só documentação para você e para o editor. `calcular_media(["a", "b"])` não é barrado na entrada, ele quebra depois, dentro do `sum()`.

---

## Compreensões

```python
quadrados   = [x**2 for x in range(10)]
pares       = [x for x in range(10) if x % 2 == 0]
mapa_notas  = {nome: nota for nome, nota in zip(nomes, notas)}
```

---

## Arquivos

```python
# Ler arquivo completo
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Ler linha por linha
with open("arquivo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

# Escrever (cria ou sobrescreve)
with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("linha 1\n")

# Adicionar ao final (não apaga o conteúdo)
with open("saida.txt", "a", encoding="utf-8") as f:
    f.write("nova linha\n")
```

### Modos de abertura

| Modo | Descrição |
|------|-----------|
| `"r"` | Leitura (padrão), erro se não existir |
| `"w"` | Escrita, cria ou sobrescreve |
| `"a"` | Append, adiciona ao final |
| `"x"` | Criação, erro se já existir |

### CSV

```python
import csv

# Escrevendo
with open("turma.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "nota"])        # cabeçalho
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Silva, João", 7.0])    # vírgula no campo, sem problema

# Lendo
with open("turma.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)   # usa o cabeçalho como chaves do dicionário
    for linha in leitor:
        print(linha["nome"], linha["nota"])
```

`newline=""` no `open()` para escrita evita linha em branco extra no Windows.

---

## Classes

```python
class MinhaClasse:
    def __init__(self, param):
        self.atributo = param

    def metodo(self):
        return self.atributo

    def __str__(self):
        return f"MinhaClasse({self.atributo})"

# Herança
class Filha(MinhaClasse):
    def __init__(self, param, extra):
        super().__init__(param)   # chama __init__ da mãe
        self.extra = extra

    def metodo(self):             # sobrescreve o da mãe
        return f"{super().metodo()} + {self.extra}"

objeto = MinhaClasse("valor")
print(objeto)     # MinhaClasse(valor)  (usa __str__)
```

---

## Tratamento de erros

```python
try:
    resultado = int(input("Número: "))
    print(10 / resultado)
except ValueError:
    print("Não é um número.")
except ZeroDivisionError:
    print("Não pode dividir por zero.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    print("Sempre executa.")

# Lançar erro intencional
raise ValueError("mensagem descritiva")
```

---

## Erros mais comuns

| Erro | Causa mais comum |
|------|-----------------|
| `SyntaxError` | `:` faltando, parêntese não fechado, aspas abertas |
| `IndentationError` | Recuo errado ou mistura de espaços e tabs |
| `NameError` | Variável ou função usada antes de ser definida |
| `TypeError` | Operação com tipo errado (ex: somar str com int) |
| `ValueError` | Tipo certo, valor inválido (ex: `int("abc")`) |
| `IndexError` | Índice fora do intervalo da lista |
| `KeyError` | Chave inexistente no dicionário |
| `ZeroDivisionError` | Divisão por zero |
| `AttributeError` | Atributo ou método não existe no objeto |
| `FileNotFoundError` | Arquivo não encontrado no caminho informado |

---

## Módulos úteis da biblioteca padrão

```python
import math
math.sqrt(25)        # 5.0
math.pi              # 3.14159...
math.ceil(3.2)       # 4
math.floor(3.9)      # 3
math.log(100, 10)    # 2.0

import random
random.randint(1, 6)               # número entre 1 e 6
random.choice(["a", "b", "c"])     # item aleatório da lista
random.shuffle(lista)              # embaralha no lugar
random.random()                    # float entre 0.0 e 1.0

import os.path
os.path.exists("arq")              # True se existir
os.path.join("dados", "notas.txt") # caminho certo pro sistema (Windows/Linux)

from datetime import datetime
datetime.now()           # data e hora atual
datetime.now().year      # só o ano
```
