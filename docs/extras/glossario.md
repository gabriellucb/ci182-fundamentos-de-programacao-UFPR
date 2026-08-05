# Glossário

Termos técnicos explicados do jeito que explico na monitoria: sem definição de livro, com exemplo direto.

Os termos estão em ordem de quando aparecem no curso, não em ordem alfabética.

---

## Algoritmo

Uma sequência de passos finita e ordenada que resolve um problema. Não é código, é a ideia antes do código. Uma receita de bolo é um algoritmo: tem começo, meio e fim, e cada passo depende do anterior.

---

## Programa

Um algoritmo escrito em uma linguagem que o computador consegue executar. O mesmo algoritmo pode virar programas em Python, Java ou qualquer outra linguagem.

---

## Interpretador / Compilador

Dois jeitos de transformar código em algo que o computador executa. Um compilador traduz o programa inteiro para código de máquina antes de rodar, gerando um arquivo executável separado. Um interpretador lê e executa o código linha a linha, sem esse passo intermediário. Python é interpretado: quando você roda `python programa.py`, o Python vai lendo e executando cada linha na hora.

---

## Pseudocódigo

Uma forma de escrever um algoritmo em português (ou qualquer língua natural) estruturado como código, mas sem se prender à sintaxe de nenhuma linguagem específica. Serve para planejar a lógica antes de escrever Python de verdade.

```text
SE idade >= 18 ENTÃO
    escreva "Maior de idade"
SENÃO
    escreva "Menor de idade"
```

---

## Sintaxe

O conjunto de regras que define como o código precisa ser escrito para o Python entender. É "gramática" da linguagem: onde vai `:`, onde vai parêntese, quais palavras são reservadas. Errar a sintaxe não é um erro de lógica, é o Python nem conseguir ler o que você escreveu.

```python
print("Olá"   # SyntaxError: '(' was never closed
```

Um erro de sintaxe impede o programa de rodar, ele nem chega a começar. É diferente de uma exceção, que acontece com o programa já em execução.

---

## Variável

Um nome que aponta para um valor guardado na memória. Quando você escreve `idade = 20`, está dizendo: "guarda o número 20 e chama esse espaço de `idade`".

```python
nome  = "Gabriel"
idade = 20
```

O valor pode mudar ao longo do programa: é por isso que se chama *variável*.

---

## Tipo

A categoria do valor que uma variável guarda. O tipo determina o que você pode fazer com o valor.

| Tipo | Nome em Python | Exemplo |
| --- | --- | --- |
| Número inteiro | `int` | `42`, `-7`, `0` |
| Número decimal | `float` | `3.14`, `-0.5` |
| Texto | `str` | `"olá"`, `"Python"` |
| Verdadeiro/falso | `bool` | `True`, `False` |

```python
type(42)       # <class 'int'>
type(3.14)     # <class 'float'>
type("olá")    # <class 'str'>
type(True)     # <class 'bool'>
```

---

## String

Qualquer sequência de caracteres entre aspas. `"Python"`, `"123"`, `"oi!"` são todas strings. O número `"123"` como string é diferente do número `123` como inteiro; você não consegue fazer conta com ele diretamente.

```python
texto  = "Python"
numero = "42"      # isso é texto, não número
print(numero + 1)  # TypeError: não dá para somar texto com número
```

---

## Conversão de tipo

Transformar um valor de um tipo em outro. Necessária porque `input()` sempre retorna string, mesmo que o usuário digite um número.

```python
entrada = input("Idade: ")   # "20" : string
idade   = int(entrada)       # 20   : inteiro

preco   = float("9.90")      # 9.9  : float
texto   = str(42)            # "42" : string
```

---

## `input()`

Função que pausa o programa, mostra uma mensagem ao usuário, espera ele digitar algo e aperta Enter, e **sempre devolve o que foi digitado como string**.

```python
nome = input("Seu nome: ")   # nome é sempre str
```

---

## `print()`

Função que exibe um valor na tela. Não guarda nada, não calcula nada, só mostra.

```python
print("Olá!")
print(42)
print(f"Você tem {idade} anos.")   # f-string: coloca variáveis dentro do texto
```

---

## Função embutida

Uma função que já vem pronta no Python: você chama a qualquer momento, sem instalar nem definir nada. `print()`, `input()`, `len()`, `int()`, `float()`, `str()` e `type()` são todas embutidas. Quando precisar de algo que não é embutido, você importa de um módulo (Aula 15) ou cria a sua própria função (Aula 13).

```python
len("Python")   # 6    : conta os caracteres
str(42)         # "42" : converte número em texto
```

---

## Expressão

Qualquer pedaço de código que produz um valor. `2 + 2` é uma expressão (produz `4`). `"oi"` é uma expressão. `idade >= 18` é uma expressão (produz `True` ou `False`).

---

## Condição

Uma expressão que resulta em `True` ou `False`. Usada para tomar decisões com `if`.

```python
idade >= 18    # True se a idade for 18 ou mais
nota == 10     # True só se a nota for exatamente 10
nome != ""     # True se o nome não for vazio
```

---

## Operadores de identidade e pertencimento (`is` / `in`)

`is` compara se duas variáveis são exatamente o mesmo objeto na memória (diferente de `==`, que compara se os valores são iguais). `in` verifica se um valor existe dentro de uma coleção (string, lista, tupla, dicionário, set).

```python
nota = None
if nota is None:        # is, não ==, para comparar com None
    print("Nota não informada")

vogais = "aeiou"
if "a" in vogais:        # in verifica pertencimento
    print("é vogal")
```

Veja [Aula 04](../aulas/04_operadores.md).

---

## `match`

Uma estrutura que compara uma variável com vários valores fixos possíveis, um `case` por valor. É mais limpo do que uma sequência longa de `elif == "valor"` quando as opções são conhecidas de antemão, como um menu.

```python
match opcao:
    case "1":
        print("Depósito")
    case "2" | "3":     # combina valores com |
        print("Saque ou saldo")
    case _:              # caso padrão, igual o else
        print("Opção inválida")
```

Existe desde o Python 3.10. Se sua versão for mais antiga, use `elif`.

---

## Bloco

Um conjunto de linhas que pertencem à mesma estrutura (`if`, `for`, `while`, `def`). Em Python, o bloco é definido pela **indentação**: todas as linhas do bloco têm o mesmo recuo.

```python
if nota >= 7:
    print("Aprovado")    # bloco do if
    print("Parabéns!")   # ainda no bloco do if
print("Fim")             # fora do bloco : sempre executa
```

---

## Indentação

O recuo (espaços no início da linha) que define a quais estruturas cada linha pertence. Em Python é obrigatório e significativo: código com indentação errada não funciona.

O padrão é **4 espaços** por nível.

---

## Laço (loop)

Uma estrutura que repete um bloco de código. Há dois tipos principais:

- `while`: repete enquanto uma condição for verdadeira
- `for`: percorre uma sequência de valores

---

## Iteração

Cada execução individual do bloco dentro de um laço. Se um `for` roda 5 vezes, houve 5 iterações.

---

## Acumulador

Uma variável que vai sendo atualizada a cada iteração do laço para "acumular" um resultado: soma, produto, contagem.

```python
soma = 0              # inicializa o acumulador
for n in [3, 5, 2]:
    soma = soma + n   # acumula
print(soma)           # 10
```

---

## Contador

Uma variável numérica usada para contar quantas vezes algo aconteceu, ou para controlar quantas vezes um laço deve rodar. Segue sempre o mesmo padrão: inicializa antes do laço, incrementa (ou decrementa) dentro dele, e é usada na condição que decide quando parar.

```python
contador = 0          # inicializa
while contador < 3:
    print(contador)
    contador += 1     # incrementa a cada rodada
```

---

## Bandeira (flag)

Uma variável booleana usada para registrar se algo aconteceu durante um laço. Começa `False`, vira `True` quando a condição de interesse ocorre, e é checada depois (ou dentro) do laço para decidir o que fazer.

```python
encontrado = False        # bandeira apagada

for numero in [3, 7, 2, 9, 1]:
    if numero == 9:
        encontrado = True  # acende a bandeira
        break

if encontrado:
    print("Achou o 9!")
else:
    print("Não encontrou.")
```

---

## Índice

A posição de um elemento dentro de uma lista ou string. Em Python, **sempre começa em 0**.

```python
frutas = ["maçã", "banana", "laranja"]
#           0         1         2

print(frutas[0])   # "maçã"
print(frutas[-1])  # "laranja" : índice negativo conta do fim
```

---

## `enumerate()`

Uma função que entrega o índice e o valor de cada item ao mesmo tempo, num laço `for`, sem você precisar criar e incrementar um contador manual.

```python
frutas = ["maçã", "banana", "laranja"]

for i, fruta in enumerate(frutas):
    print(i, fruta)
# 0 maçã
# 1 banana
# 2 laranja
```

`enumerate()` entrega pares `(índice, valor)`; o `for i, fruta in ...` desempacota cada par nas duas variáveis.

---

## Fatiamento (slicing)

Pegar um pedaço de uma string ou lista de uma vez, com `[início:fim]`. O início entra, o fim **fica de fora** (igual ao `range()`). Um terceiro número define o passo, e `-1` no passo inverte.

```python
palavra = "COMPUTADOR"
palavra[0:4]    # "COMP"        : índices 0, 1, 2, 3
palavra[4:]     # "UTADOR"      : do índice 4 até o fim
palavra[::-1]   # "RODATUPMOC"  : invertida
```

---

## Mutável

Que pode ser alterado depois de criado. Listas e dicionários são mutáveis: você edita, adiciona ou remove itens no lugar, sem criar um novo objeto. O oposto é *imutável*.

```python
notas = [7.5, 8.0]
notas.append(9.0)   # a mesma lista, agora com mais um item
notas[0] = 8.5      # altera no lugar
```

---

## Imutável

Que não pode ser alterado depois de criado. Strings e tuplas são imutáveis: para "mudar", você cria uma **nova**. O oposto é *mutável* (listas e dicionários, que dá pra editar no lugar).

```python
palavra = "Python"
palavra[0] = "J"          # TypeError : string é imutável
nova = "J" + palavra[1:]  # cria uma nova: "Jython"
```

---

## Case-sensitive

Sensível a maiúsculas e minúsculas: para o Python, `"a"` e `"A"` são caracteres diferentes. Por isso `"Python" == "python"` dá `False`. Para comparar ignorando a diferença, normalize os dois lados com `.lower()`.

```python
"SIM" == "sim"            # False
"SIM".lower() == "sim"    # True
```

---

## Lista

Uma coleção ordenada e mutável de valores. Usa colchetes `[]`. Pode misturar tipos, mas na prática é mais útil guardar coisas do mesmo tipo.

```python
notas = [7.5, 8.0, 6.5, 9.0]
notas.append(10.0)    # adiciona no final
notas[0] = 8.0        # altera o primeiro
```

---

## Big O (complexidade de tempo)

Uma notação para descrever quanto o tempo de uma operação cresce conforme o tamanho da entrada cresce, não em segundos, em proporção. `O(1)` é constante (sempre o mesmo tempo), `O(n)` é linear (dobrou a lista, dobrou o tempo), `O(n²)` é quadrática (dobrou a lista, quadruplicou o tempo).

```python
lista.append(x)   # O(1): sempre rápido, não importa o tamanho da lista
lista.insert(0, x)  # O(n): quanto maior a lista, mais lento
```

Explicação completa, com números reais comparando `insert()` e `append() + sort()`, no [Apêndice: Custo de operações em listas](../apendices/custo_de_operacoes.md).

---

## Matriz

Uma estrutura de dados bidimensional organizada em linhas e colunas. Em Python, representada como lista de listas: a lista externa são as linhas, cada lista interna é uma linha com seus elementos.

```python
notas = [
    [8.0, 7.5, 9.0],   # linha 0
    [6.5, 7.0, 5.5],   # linha 1
]
print(notas[0][2])   # 9.0 : linha 0, coluna 2
```

Acesso: sempre `[linha][coluna]`, com índices a partir de zero.

---

## Diagonal principal

Em uma matriz **quadrada** (mesmo número de linhas e colunas), é a sequência de elementos onde o índice de linha é igual ao índice de coluna: `[0,0]`, `[1,1]`, `[2,2]`... Vai do canto superior esquerdo ao inferior direito.

```python
n = len(matriz)
for i in range(n):
    print(matriz[i][i])   # diagonal principal
```

---

## Diagonal secundária

Em uma matriz **quadrada**, é a sequência de elementos que vai do canto superior direito ao inferior esquerdo: `[0, n-1]`, `[1, n-2]`... A fórmula da coluna para a linha `i` é `n - 1 - i`.

```python
n = len(matriz)
for i in range(n):
    print(matriz[i][n - 1 - i])   # diagonal secundária
```

---

## Transposta

Uma operação sobre matrizes onde cada linha da original vira uma coluna no resultado (e vice-versa). Uma matriz `m × n` vira `n × m`.

```python
original = [[1, 2, 3], [4, 5, 6]]    # 2×3
# transposta: [[1, 4], [2, 5], [3, 6]]  → 3×2
```

---

## Dicionário

Uma coleção de pares **chave: valor**. Você acessa os valores pelo nome (a chave), não por posição numérica. Útil para representar um objeto com várias propriedades.

```python
aluno = {"nome": "Ana", "nota": 8.5, "aprovado": True}
print(aluno["nome"])   # "Ana"
```

---

## Tupla

Como uma lista, mas **imutável**: você não pode alterar, adicionar ou remover itens depois de criar. Útil para guardar dados que não devem mudar, como coordenadas.

```python
ponto = (-25.42, -49.27)
lat, lon = ponto        # desempacotamento
```

---

## Set (conjunto)

Uma coleção **sem duplicatas** e **sem ordem garantida**. Útil para descobrir valores únicos ou fazer operações de conjunto (união, interseção, diferença).

```python
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)   # {1, 2, 3} : duplicatas removidas
```

---

## Desempacotamento

Distribuir os valores de uma sequência (tupla, lista, string) em variáveis separadas em uma única linha. Python verifica se o número de variáveis bate com o número de valores.

```python
ponto = (10, 20)
x, y = ponto       # x = 10, y = 20

primeiro, *resto = [1, 2, 3, 4]   # * captura o excedente
# primeiro = 1, resto = [2, 3, 4]
```

Você usa desempacotamento toda vez que escreve `for i, item in enumerate(lista)` ou `for chave, valor in dicionario.items()`.

---

## Hash

Um número calculado matematicamente a partir de um valor, usado como "endereço" de onde esse valor fica na memória. É a razão pela qual buscar em um set é muito mais rápido do que em uma lista: em vez de procurar elemento por elemento, Python calcula o hash e vai direto ao endereço.

Só tipos **imutáveis** podem ter hash (strings, números, tuplas). É por isso que sets só aceitam elementos imutáveis, e chaves de dicionário também.

```python
hash("Python")   # algum número grande : o "endereço" desse valor
hash([1, 2, 3])  # TypeError : lista é mutável, não tem hash
```

---

## Subconjunto / Superconjunto

Dois conjuntos onde todos os elementos de um estão contidos no outro. Se `a` é **subconjunto** de `b`, significa que todo elemento de `a` existe em `b`. Do ponto de vista de `b`, ele é o **superconjunto**.

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

a.issubset(b)    # True : todo elemento de a existe em b
b.issuperset(a)  # True : b contém tudo de a
```

São perspectivas opostas da mesma relação: se `a ⊆ b`, então `b ⊇ a`.

---

## Função

Um bloco de código com nome, que você pode chamar sempre que precisar. Evita repetição e organiza o código em partes menores e com responsabilidade clara.

```python
def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")     # chama a função
saudar("Bruno")   # chama de novo com outro argumento
```

---

## Parâmetro

A variável declarada na definição da função, que recebe o valor passado na chamada.

```python
def dobrar(numero):   # 'numero' é o parâmetro
    return numero * 2
```

---

## Argumento

O valor passado para a função na hora de chamá-la.

```python
dobrar(5)   # 5 é o argumento
```

Parâmetro é o nome, argumento é o valor. A confusão é comum e não é grave; na prática os dois termos são usados no mesmo sentido.

---

## `return`

A instrução que encerra a função e devolve um valor para quem a chamou. Sem `return`, a função devolve `None`.

```python
def soma(a, b):
    return a + b        # devolve o resultado

resultado = soma(3, 4)  # resultado recebe 7
```

`return` encerra a função imediatamente; nenhuma linha depois dele é executada.

---

## Escopo

A região do programa onde uma variável existe e pode ser acessada.

- **Escopo local**: variável criada dentro de uma função. Existe só ali.
- **Escopo global**: variável criada fora de qualquer função. Existe em todo o programa.

```python
x = 10          # global

def f():
    y = 5       # local : só existe dentro de f()
    print(x)    # pode LER o global
    print(y)

f()
print(x)        # OK
print(y)        # NameError : y não existe aqui
```

---

## Docstring

Uma string colocada logo após a definição de uma função (ou classe) que descreve o que ela faz. É a forma padrão de documentar funções em Python; o Python a trata como dado real, não como comentário.

```python
def calcular_media(notas):
    """Calcula e retorna a média de uma lista de notas."""
    return sum(notas) / len(notas)
```

Você pode acessá-la com `help(calcular_media)` no terminal ou pelo atributo `.__doc__`. IDEs como o VS Code exibem a docstring como dica ao digitar o nome da função.

---

## `lambda`

Uma função sem nome, definida em uma linha só, para casos rápidos e simples. Não usa `def` nem `return`, o valor depois de `:` já é o retorno.

```python
dobrar = lambda x: x * 2
print(dobrar(5))   # 10

# equivale a:
def dobrar(x):
    return x * 2
```

Use `lambda` para funções curtas e descartáveis. Para qualquer coisa com mais de uma linha de lógica, uma função normal com `def` é mais legível.

---

## Recursão

Quando uma função chama a si mesma durante a execução. Útil para problemas que se dividem em versões menores do mesmo problema. Toda função recursiva precisa de um **caso base** (condição que para a recursão) e de **progresso** em direção a ele; sem caso base, a função entra em loop infinito e o Python lança `RecursionError`.

```python
def fatorial(n):
    if n <= 1:               # caso base
        return 1
    return n * fatorial(n - 1)   # progresso: n diminui a cada chamada

print(fatorial(5))   # 120
```

Para a maioria dos problemas do dia a dia, um `for` ou `while` é mais legível. Use recursão quando o problema tem estrutura naturalmente recursiva (árvores, percurso de pastas, fractais).

---

## `None`

Um valor especial que significa "nenhum valor" ou "ausência de resultado". É o que uma função devolve quando não tem `return`.

```python
def sem_retorno():
    print("oi")

resultado = sem_retorno()
print(resultado)   # None
```

---

## Exceção (erro em tempo de execução)

Um erro que acontece enquanto o programa está rodando: diferente de um erro de sintaxe (que impede até de iniciar). Exceções têm tipo (`TypeError`, `ValueError`, `IndexError`...) e podem ser capturadas com `try/except`.

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Isso não é um número.")
```

---

## Traceback

A mensagem de erro completa que o Python exibe quando algo dá errado. Mostra o caminho de chamadas que levou ao erro e, na última linha, o tipo e a descrição do problema.

Leia **de baixo para cima**: a última linha diz o que aconteceu, as linhas acima mostram onde.

```text
Traceback (most recent call last):
  File "programa.py", line 5, in <module>
    resultado = 10 / divisor
ZeroDivisionError: division by zero
```

---

## Gerenciador de contexto (`with`)

Uma estrutura que garante que um recurso (como um arquivo aberto) seja liberado corretamente no final, mesmo que aconteça um erro no meio do caminho. `with open(...) as arquivo:` fecha o arquivo automaticamente ao sair do bloco, você não precisa chamar `arquivo.close()` manualmente.

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
# aqui fora, o arquivo já foi fechado, mesmo que read() tivesse dado erro
```

Veja [Aula 14](../aulas/14_arquivos.md).

---

## Buffer

Uma memória temporária onde dados ficam acumulados antes de serem gravados definitivamente. Quando você chama `arquivo.write(...)`, o Python pode não gravar imediatamente no disco: ele guarda no buffer e descarrega de uma vez quando o arquivo é fechado. É por isso que `close()` (ou o `with`) é obrigatório: sem fechar, partes do conteúdo podem não ter sido salvas.

---

## Caminho relativo / Caminho absoluto

Duas formas de especificar onde um arquivo está:

- **Caminho relativo** começa a partir de onde o programa está rodando, sem indicar a raiz do sistema. `"dados.txt"` e `"dados/notas.csv"` são caminhos relativos.
- **Caminho absoluto** especifica o caminho completo desde a raiz do sistema. `"/home/gabriel/projetos/notas.csv"` (Linux/Mac) ou `"C:/Projetos/notas.csv"` (Windows) são caminhos absolutos.

Na prática, use caminhos relativos para arquivos do projeto (portáveis entre computadores) e absolutos só quando precisar referenciar um local fixo no sistema.

```python
with open("dados.txt", "r", encoding="utf-8") as f:   # relativo : busca na pasta atual
    ...

with open("/tmp/log.txt", "r", encoding="utf-8") as f:   # absoluto
    ...
```

---

## Encoding (codificação)

O conjunto de regras que mapeia caracteres para bytes. UTF-8 é o padrão mais usado: representa todos os caracteres do Unicode (incluindo acentos, emojis, caracteres japoneses) usando 1 a 4 bytes por caractere.

No Python, sempre que abrir um arquivo de texto, especifique `encoding="utf-8"`. Sem isso, o Python usa o padrão do sistema, que no Windows pode ser `cp1252` ou `latin-1`, causando lixo ou erros ao ler arquivos com acentos criados em outro sistema.

```python
# Sem encoding: comportamento depende do sistema operacional
with open("notas.txt", "r") as f: ...

# Com encoding: funciona igual em qualquer sistema
with open("notas.txt", "r", encoding="utf-8") as f: ...
```

---

## Modo de abertura

O segundo argumento de `open()`, que define o que você pode fazer com o arquivo. Os três mais usados:

| Modo | O que faz | Cuidado |
| --- | --- | --- |
| `"r"` | Leitura | `FileNotFoundError` se o arquivo não existir |
| `"w"` | Escrita | **Apaga tudo** se o arquivo já existir |
| `"a"` | Acrescentar | Continua do final, sem apagar |

```python
with open("notas.txt", "a", encoding="utf-8") as f:
    f.write("novo registro\n")   # "a" não apaga o que já estava lá
```

O erro mais comum: usar `"w"` pensando em "write" quando deveria ser `"a"` para "append". Com `"w"`, o arquivo é zerado na hora de abrir; mesmo antes de você escrever qualquer coisa.

Os dois métodos de escrita principais:

- `f.write(texto)`: escreve uma string. Você controla cada caractere, inclusive os `\n` no final de cada linha.
- `f.writelines(lista)`: escreve uma lista de strings de uma vez, equivale a chamar `write()` para cada item. Não adiciona `\n` automaticamente; cada string da lista já precisa terminar com `\n`.

```python
linhas = ["Ana,8.5\n", "Bruno,6.0\n"]
with open("turma.csv", "w", encoding="utf-8") as f:
    f.writelines(linhas)   # equivale a dois write() seguidos
```

---

## CSV (Comma-Separated Values)

Um formato de arquivo de texto onde cada linha é um registro e os campos são separados por vírgula. É o formato universal para trocar dados tabulares: Excel, Google Planilhas, bancos de dados, todos exportam e importam CSV.

```text
nome,nota,situação
Ana,8.5,Aprovado
Bruno,6.0,Reprovado
```

Em Python, você pode ler e escrever CSV com `open()` e `split(",")`, ou usar o módulo `csv` da biblioteca padrão para casos com campos que contêm vírgulas, aspas ou quebras de linha.

---

## Módulo

Um arquivo Python com funções e variáveis que você pode importar e usar em outro programa. `math`, `random` e `datetime` são módulos da biblioteca padrão do Python.

```python
import math
print(math.sqrt(25))   # 5.0
```

---

## Namespace

O "compartimento" onde o Python guarda os nomes definidos dentro de um módulo, para eles não se misturarem com nomes de outros módulos. Quando você escreve `import math`, tudo que está dentro de `math.py` fica guardado no namespace `math`, e você acessa com o prefixo `math.`.

```python
import math
math.sqrt(25)     # "dentro do namespace math, pegue sqrt"

from math import sqrt
sqrt(25)          # sem prefixo, sqrt entra direto no seu namespace
```

---

## Biblioteca / Pacote

Um conjunto de módulos relacionados distribuídos juntos. `random` é um módulo. `pandas` é uma biblioteca (vários módulos que trabalham com dados tabulares).

---

## `pip`

O gerenciador de pacotes do Python: instala bibliotecas externas (que não vêm com o Python) direto no terminal, buscando no PyPI, o repositório público de pacotes da comunidade.

```bash
pip install nome-da-biblioteca
```

Depois de instalada, a biblioteca se importa como qualquer módulo: `import nome_da_biblioteca`. Sempre ative o ambiente virtual antes de instalar algo, senão vai para o Python global (veja o [Apêndice: Ambiente Avançado](../apendices/ambiente_avancado.md)).

---

## Classe

Um molde para criar objetos. Define quais atributos (dados) e métodos (ações) os objetos terão.

```python
class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        print(f"{self.nome}: au au!")
```

---

## Construtor (`__init__`)

O método especial que o Python chama sozinho toda vez que você cria um objeto novo a partir de uma classe. É onde você define os atributos iniciais desse objeto.

```python
class Cachorro:
    def __init__(self, nome):   # construtor
        self.nome = nome

rex = Cachorro("Rex")   # o __init__ roda sozinho aqui, sem você chamar
```

---

## Objeto / Instância

Um exemplar concreto criado a partir de uma classe. Cada objeto tem seus próprios valores de atributos.

```python
rex  = Cachorro("Rex")    # objeto 1
bolt = Cachorro("Bolt")   # objeto 2

rex.latir()    # Rex: au au!
bolt.latir()   # Bolt: au au!
```

---

## Atributo

Uma variável que pertence a um objeto. Cada objeto pode ter valores diferentes para o mesmo atributo.

```python
rex.nome    # "Rex"
bolt.nome   # "Bolt"
```

---

## Método

Uma função que pertence a uma classe e opera sobre os dados do objeto. O primeiro parâmetro é sempre `self`, que representa o próprio objeto.

---

## Método especial (dunder method)

Um método com nome cercado por dois underscores dos dois lados (`__init__`, `__str__`, `__len__`, `__eq__`...) que o Python chama sozinho em situações específicas: na criação do objeto, no `print()`, no `len()`, numa comparação com `==`, e por aí vai. "Dunder" vem do inglês *double underscore*.

---

## Herança

Quando uma classe (filha) aproveita tudo que outra classe (mãe) já tem, podendo adicionar ou modificar comportamentos. A relação é sempre "X é um Y".

```python
class Animal:
    def respirar(self):
        print("respirando...")

class Cachorro(Animal):   # Cachorro herda de Animal
    def latir(self):
        print("au au!")

rex = Cachorro()
rex.respirar()   # herdado de Animal
rex.latir()      # próprio de Cachorro
```

Veja [Aula 17](../aulas/17_poo.md).

---

## `super()`

Dentro de uma classe filha, chama a versão do método definida na classe mãe. É como usar em vez de reescrever: em vez de copiar o `__init__` da mãe na filha, você chama `super().__init__(...)` e deixa a mãe cuidar da própria parte.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)   # reaproveita o __init__ de Animal
        self.raca = raca
```

Veja [Aula 17](../aulas/17_poo.md).

---

## `self`

A referência ao próprio objeto dentro dos métodos de uma classe. Quando você chama `rex.latir()`, o Python passa `rex` como `self` automaticamente.

É confuso no começo para todo mundo. A dica: leia `self.nome` como "o nome *deste* objeto específico".

---

## Encapsulamento

Controlar o acesso aos dados internos de um objeto, em vez de deixar qualquer parte do código modificar qualquer atributo livremente. Em Python isso é uma convenção, não uma trava da linguagem: um `_` no início do nome (`self._vida`) avisa "isto é interno, use os métodos".

```python
class Cachorro:
    def __init__(self, nome):
        self._energia = 100   # _ avisa: acesse pelos métodos, não direto

    def brincar(self):
        self._energia -= 20
```

Veja [Aula 17](../aulas/17_poo.md).

---

## Polimorfismo

Objetos de classes diferentes respondendo ao mesmo método, cada um do seu jeito. Quem chama o método não precisa saber qual tipo específico está lidando.

```python
for animal in [Cachorro("Rex"), Gato("Mimi")]:
    animal.fazer_som()   # cada um late ou mia do seu jeito
```

Veja [Aula 17](../aulas/17_poo.md).

---

## Abstração

Separar o que uma classe faz (os métodos que ela oferece) de como ela faz por dentro (a implementação). Quem usa a classe só precisa conhecer os métodos disponíveis; a implementação interna pode mudar sem quebrar nada para quem usa.

Veja [Aula 17](../aulas/17_poo.md).

---

## `zip()`

Uma função que percorre dois (ou mais) iteráveis ao mesmo tempo, emparelhando os elementos que estão na mesma posição. Substitui o índice manual quando você tem duas listas que "andam juntas".

```python
nomes = ["Ana", "Bruno"]
notas = [8.5, 6.0]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
# Ana: 8.5
# Bruno: 6.0
```

Se as listas tiverem tamanhos diferentes, `zip()` para no menor, sem avisar, os elementos extras do maior são ignorados silenciosamente.

Veja [Aula 18](../aulas/18_avancado.md).

---

## Compreensão de lista (list comprehension)

Uma forma mais compacta de criar uma lista nova a partir de outra sequência, transformando ou filtrando cada elemento numa linha só, em vez de um `for` com `.append()`.

```python
# Forma tradicional
quadrados = []
for n in range(1, 6):
    quadrados.append(n ** 2)

# Compreensão, mesmo resultado
quadrados = [n ** 2 for n in range(1, 6)]
print(quadrados)   # [1, 4, 9, 16, 25]
```

O mesmo funciona para dicionários: `{chave: valor for ... in ...}`. Para lógica simples, a compreensão é mais curta; para lógica complexa, um `for` explícito continua sendo mais claro.

Veja [Aula 18](../aulas/18_avancado.md).

---

## Type hint

Uma anotação que indica qual tipo uma variável, parâmetro ou retorno de função espera, sem obrigar nada, é documentação para você e para o editor, não uma trava de segurança.

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

O Python não verifica isso em tempo de execução: chamar `calcular_media(["a", "b"])` não é barrado na entrada, o erro só aparece depois, quando o código tenta de fato somar os valores.

Veja [Aula 18](../aulas/18_avancado.md).
