# Dúvidas frequentes

Dúvidas que aparecem com frequência — na monitoria, nos fóruns de Python, e que eu mesmo tive quando estava aprendendo. Se você travou em algo, provavelmente está aqui.

---

## Entrada e saída

**Por que `input()` retorna texto mesmo quando eu digito um número?**

Porque `input()` não sabe o que você quer fazer com o dado. Talvez você queira um número para calcular, talvez queira um texto para exibir, talvez queira validar antes de converter. Deixar sempre como string transfere essa decisão para você. A conversão é obrigatória quando for operar: `int(input(...))` ou `float(input(...))`.

---

**Por que `"1" + "2"` dá `"12"` e não `3`?**

Porque as duas são strings — e `+` entre strings é concatenação, não soma. `"1" + "2"` une os dois textos em `"12"`. Para somar, você precisa de números: `int("1") + int("2")` dá `3`.

---

**Chamei `print()` dentro da minha função e o resultado não foi guardado. Por quê?**

`print()` só exibe — não devolve nada. Para guardar ou usar o resultado fora da função, a função precisa usar `return`. Um `return` entrega o valor para quem chamou; um `print()` apenas mostra na tela e some.

```python
def dobrar(n):
    print(n * 2)       # exibe, mas não retorna

resultado = dobrar(5)  # resultado é None — não tem nada para guardar
```

```python
def dobrar(n):
    return n * 2       # devolve o valor

resultado = dobrar(5)  # resultado é 10
```

---

**Minha função retorna `None` sem eu ter escrito `return None`. Por quê?**

Toda função que não tem `return` (ou que chega ao fim sem executar nenhum `return`) devolve `None` automaticamente. É o retorno implícito do Python para funções sem resultado explícito.

---

## Variáveis e tipos

**O que é `None`? É o mesmo que `0` ou string vazia?**

Não. `None` é a ausência de valor — significa "não tem nada aqui". `0` é o número zero. `""` é uma string vazia. Os três são distintos:

```python
print(0 == None)    # False
print("" == None)   # False
print(None == None) # True
```

Use `None` quando uma variável precisa existir mas ainda não tem valor, ou quando uma função não tem resultado para retornar.

---

**Quando usar `int` e quando usar `float`?**

Regra prática: `int` para contagens, idades, índices, anos — qualquer coisa que não vai ter vírgula. `float` para medidas, preços, médias, coordenadas — qualquer coisa que naturalmente pode ser decimal.

```python
quantidade = 3        # int — não existe "2.5 maçãs"
preco = 4.99          # float — preço pode ter centavos
ano = 2026            # int — ano não tem fração
media = 7.3           # float — média raramente é exata
```

Usar `float` para tudo funciona na maioria dos casos, mas floats carregam uma pequena imprecisão e algumas operações (índices de lista, `range()`) exigem `int` explicitamente.

---

**Por que `0.1 + 0.2` não é `0.3`?**

Porque computadores representam decimais em binário (base 2), e `0.1` não tem representação exata nessa base — como `1/3` não tem representação exata em decimal. O resultado é `0.30000000000000004`. Na prática isso raramente causa problema — ao formatar com `:.2f` você nunca vê a diferença. Onde importa: nunca compare floats com `==` diretamente.

```python
print(0.1 + 0.2 == 0.3)          # False
print(round(0.1 + 0.2, 10) == 0.3)  # True
```

---

**Qual a diferença entre `=` e `==`?**

`=` atribui um valor a uma variável. `==` compara dois valores e retorna `True` ou `False`. Usar `=` dentro de um `if` é um erro de sintaxe — o Python vai reclamar na hora.

```python
nota = 7       # atribuição: nota recebe o valor 7
nota == 7      # comparação: isso é 7?  → True
```

---

### Como o Python guarda variáveis na memória — e o que o `is` realmente verifica?

Todo valor que o Python cria precisa ser guardado em algum lugar. Esse lugar é a **memória RAM** do computador — um espaço imenso dividido em bilhões de células minúsculas, cada uma com um endereço único (como casas numa rua infinita).

Quando você escreve `nome = "Gabriel"`, o Python faz três coisas:

1. Encontra um espaço livre na memória e guarda o valor `"Gabriel"` lá.
2. Anota o endereço desse espaço.
3. Cria a variável `nome` como um rótulo que aponta para esse endereço.

A variável não *é* o valor — ela é uma **referência** para onde o valor está guardado. Pense como um post-it colado numa gaveta: o post-it tem o endereço da gaveta, o objeto está dentro dela.

```text
Memória RAM (simplificado):

  endereço 0x4f2a  →  "Gabriel"     ← valor guardado aqui

Variáveis:
  nome  →  0x4f2a                   ← nome aponta para esse endereço
```

**Quando duas variáveis apontam para o mesmo lugar:**

```python
a = "Gabriel"
b = a           # b recebe o mesmo endereço, não uma cópia do valor
```

```text
  0x4f2a  →  "Gabriel"

  a  →  0x4f2a
  b  →  0x4f2a   ← mesmo endereço que a
```

**Quando duas variáveis têm o mesmo conteúdo mas em lugares diferentes:**

```python
a = [1, 2, 3]
b = [1, 2, 3]   # Python cria uma NOVA lista, em outro endereço
```

```text
  0x4f2a  →  [1, 2, 3]   ← lista criada para a
  0x7c8b  →  [1, 2, 3]   ← lista criada para b (objeto separado)

  a  →  0x4f2a
  b  →  0x7c8b
```

Aqui está a distinção entre `==` e `is`:

- `==` compara os **conteúdos** (os valores em si são iguais?)
- `is` compara os **endereços** (são o mesmo objeto na memória?)

```python
a = [1, 2, 3]
b = [1, 2, 3]   # mesmo conteúdo, objetos diferentes
c = a           # mesmo objeto que a

print(a == b)   # True  — conteúdo igual
print(a is b)   # False — endereços diferentes
print(a is c)   # True  — c aponta para o mesmo endereço que a
```

**A consequência prática — mutações:**

Como `c = a` faz `c` apontar para o mesmo objeto, qualquer modificação vista por `a` também é vista por `c` — porque são a mesma gaveta:

```python
a = [1, 2, 3]
c = a

a.append(4)
print(a)   # [1, 2, 3, 4]
print(c)   # [1, 2, 3, 4] — mudou junto: eram o mesmo objeto
```

Para criar uma cópia independente, use `.copy()`:

```python
c = a.copy()   # mesmo conteúdo, mas em endereço diferente
a.append(5)
print(c)       # [1, 2, 3] — não foi afetado
```

**Por que números e strings se comportam diferente:**

Números, strings e tuplas são **imutáveis** — depois de criados, não têm como ser modificados. Por isso o Python às vezes reutiliza o mesmo objeto para economizar memória — isso se chama *interning*:

```python
a = 10
b = 10
print(a is b)   # True (em CPython, inteiros pequenos são compartilhados)
```

Isso é um detalhe de implementação que pode mudar dependendo do valor ou da versão do Python. **Nunca use `is` para comparar valores** — use `==`. O `is` existe para verificar identidade, não conteúdo.

**Por que `None` é especial:**

Existe exatamente **um único** objeto `None` em todo programa Python. Quando você escreve `x = None`, `x` aponta para esse objeto singleton. Isso torna `is None` sempre confiável:

```python
resultado = None
print(resultado is None)   # True  — aponta para o único None

resultado = 0
print(resultado is None)   # False — 0 não é None
print(resultado == None)   # False — mesmo resultado, mas prefira is None
```

**Resumo — quando usar cada um:**

| Situação | Use |
| --- | --- |
| Comparar valores (números, strings, etc.) | `==` |
| Verificar se algo é `None` | `is None` |
| Verificar se dois objetos são idênticos na memória | `is` (raro fora de listas/objetos) |

---

## Condicionais

**Quando usar `match` em vez de vários `elif`?**

Quando você está comparando a **mesma variável** contra uma lista de valores fixos conhecidos: um menu, um código de opção, um dia da semana. Nesses casos `match` é mais legível do que uma sequência de `elif == "valor"`.

```python
opcao = "2"

match opcao:
    case "1":
        print("Depósito")
    case "2":
        print("Saque")
    case _:                # caso padrão, igual o else
        print("Opção inválida")
```

Se a lógica envolve comparar coisas diferentes a cada bloco (`if idade >= 18`, `elif nota > 7`), `match` não ajuda; `if/elif` continua sendo a ferramenta certa. E se você estiver numa versão do Python anterior à 3.10, `match` nem existe: use `elif`.

---

## Listas e estruturas

**Por que quando copio uma lista com `=` e altero a cópia, a original muda também?**

Porque `=` não copia a lista — cria uma segunda variável apontando para a mesma lista na memória. As duas são o mesmo objeto.

```python
a = [1, 2, 3]
b = a           # b e a apontam para a mesma lista
b.append(4)
print(a)        # [1, 2, 3, 4] — mudou junto!
```

Para criar uma cópia independente, use `.copy()` ou fatiamento:

```python
b = a.copy()    # agora são listas separadas
b = a[:]        # faz a mesma coisa
```

---

**Qual a diferença entre `lista.clear()` e `lista = []`?**

Na maioria dos casos não faz diferença: os dois deixam você com uma lista vazia para continuar usando. A diferença aparece quando você tem **duas variáveis conectadas à mesma lista**.

Isso acontece ao fazer `b = a`: `b` não é uma cópia — é o mesmo conteúdo, com outro nome. Qualquer mudança feita por `a` também aparece em `b`, e vice-versa.

Veja o que acontece quando você usa `a = []` nessa situação:

```python
a = [1, 2, 3]
b = a   # b é a mesma lista com outro nome

a = []          # a agora tem uma lista nova e vazia
print(a)        # []
print(b)        # [1, 2, 3]  — b não mudou, continua com a lista antiga
```

E quando você usa `a.clear()` na mesma situação:

```python
a = [1, 2, 3]
b = a   # b é a mesma lista com outro nome

a.clear()       # esvazia o conteúdo da lista que os dois compartilham
print(a)        # []
print(b)        # []  — b também ficou vazio!
```

O resultado é diferente porque `a = []` troca `a` por uma lista nova (deixando `b` com a lista velha), enquanto `a.clear()` esvazia a lista que `a` e `b` compartilham.

Se você está começando agora e ainda não chegou na seção de Cópias da [Aula 09](../aulas/09_listas.md), não precisa se preocupar com isso: enquanto você usar uma única variável por lista, tanto faz qual dos dois usar.

---

**Por que `[[0] * 4] * 3` não funciona como eu esperava?**

Porque `* 3` na lista externa não cria três listas novas — cria **três nomes para a mesma lista**. É a mesma armadilha de `b = a` aplicada a listas aninhadas.

```python
matriz = [[0] * 4] * 3

matriz[0][0] = 9
print(matriz)
# [[9, 0, 0, 0],
#  [9, 0, 0, 0],   ← todas as linhas mudaram!
#  [9, 0, 0, 0]]
```

O que aconteceu: `[0] * 4` criou uma lista `[0, 0, 0, 0]`. O `* 3` criou três entradas na lista externa, mas todas apontam para essa mesma lista interna. Modificar `matriz[0][0]` é modificar o único objeto que existe — e as três entradas o enxergam.

A solução é criar cada linha dentro de um laço, assim cada iteração gera um objeto novo:

```python
matriz = []
for i in range(3):
    matriz.append([0] * 4)   # cada iteração cria uma lista nova e independente

matriz[0][0] = 9
print(matriz)
# [[9, 0, 0, 0],
#  [0, 0, 0, 0],   ← só a linha 0 foi afetada
#  [0, 0, 0, 0]]
```

O `[0] * 4` dentro do laço é seguro porque repete um número (imutável), não uma lista. O problema só ocorre quando você aplica `*` a uma lista na posição externa. Esse comportamento é explicado com mais detalhe na seção de memória [desta entrada do FAQ](#como-o-python-guarda-variáveis-na-memória--e-o-que-o-is-realmente-verifica).

---

**Por que `lista.sort()` não retorna nada?**

Porque `.sort()` ordena a lista no lugar (modifica a própria lista) e retorna `None`. Se você fizer `resultado = lista.sort()`, o `resultado` será `None`. Use `lista.sort()` sozinho. Se quiser uma nova lista ordenada sem modificar a original, use `sorted(lista)` — essa sim retorna.

```python
notas = [8, 3, 9, 5]
notas.sort()            # ordena notas no lugar
print(notas)            # [3, 5, 8, 9]

nova = sorted(notas)    # retorna nova lista, não modifica notas
```

---

**Como verificar se um valor está numa lista sem usar `for`?**

Use `in`:

```python
frutas = ["maçã", "banana", "laranja"]
print("banana" in frutas)   # True
print("melão" in frutas)    # False
```

Funciona também em strings: `"py" in "python"` retorna `True`.

---

**Qual a diferença entre `sorted()` e `.sort()`?**

| | `sorted()` | `.sort()` |
| --- | --- | --- |
| Tipo | Função | Método de lista |
| Modifica a original? | Não | Sim |
| Retorna | Nova lista ordenada | `None` |
| Funciona com | Qualquer iterável | Só listas |

---

**Por que Python tem funções prontas como `sum()` e `sort()`?**

Python segue a filosofia de *batteries included* — muita coisa vem embutida. Em linguagens de mais baixo nível, como C, as mesmas operações exigem código manual.

Somar uma lista em C:

```c
int numeros[] = {3, 1, 4, 1, 5};
int n = 5, soma = 0;
for (int i = 0; i < n; i++) soma += numeros[i];
printf("%d\n", soma);  /* 14 */
```

Em Python:

```python
numeros = [3, 1, 4, 1, 5]
print(sum(numeros))   # 14
```

Ordenar é ainda mais dramático. Por baixo de `sort()` existe um algoritmo chamado **Timsort** — implementá-lo corretamente levaria dezenas de linhas. Uma versão simples (mas mais lenta) já tem essa cara:

```python
# bubble sort — uma versão simplificada do que sort() faz por baixo
def ordenar(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# com sort() nativo — exatamente o mesmo resultado, em uma linha
numeros = [5, 2, 9, 1, 7]
numeros.sort()
```

**Vantagens de ter isso pronto:**

- Menos código para escrever e ler.
- Menos chance de erro — um `<` trocado por `<=` num algoritmo de ordenação é um bug difícil de perceber.
- Mais rápido de desenvolver.

**Desvantagem:**

- Oculta o mecanismo por baixo. Em CI182 você vai aprender a escrever esses algoritmos justamente para entender *como* `sort()` e `sum()` funcionam — usar a função pronta sem saber o que ela faz é conforto sem compreensão.

A regra prática: em projetos reais, use as funções prontas. Em exercícios de algoritmo, escreva o laço ou o algoritmo à mão — esse é o ponto do exercício.

---

## Dicionários

**Por que `dicionario["chave"]` dá `KeyError` mas `dicionario.get("chave")` não?**

Porque os dois têm contratos diferentes: `[]` assume que a chave existe e avisa imediatamente se não existir — o `KeyError` é intencional, não um descuido do Python. `get()` assume que a chave pode não existir e devolve `None` (ou um valor padrão) sem parar o programa.

```python
aluno = {"nome": "Ana", "nota": 8.5}

print(aluno["telefone"])               # KeyError: 'telefone' — para tudo
print(aluno.get("telefone"))           # None  — continua
print(aluno.get("telefone", "—"))      # "—"   — valor padrão
```

Use `[]` quando a ausência da chave é um bug que você quer detectar logo: se a chave *deveria* estar lá e não está, faz sentido o programa parar. Use `get()` quando a ausência é um caso esperado e você tem um comportamento padrão para ele.

A armadilha de usar `get()` em tudo: você esconde bugs. Se sempre usar `get("nome")` e o valor estiver como `None` em vez de `"Ana"`, o erro vai aparecer só mais tarde — num `print`, num cálculo, num lugar sem relação aparente com o dicionário.

---

## Sets e Tuplas

**Por que `{1, 2, 3}` não preserva a ordem que eu digitei?**

Porque sets não guardam ordem — por design. Internamente, cada elemento é colocado numa posição determinada pelo seu **hash**, um número calculado a partir do próprio valor. Essa posição não tem nada a ver com a ordem de inserção.

```python
s = {5, 1, 4, 2, 3}
print(s)   # {1, 2, 3, 4, 5} — ordenado pelo hash, não pela inserção

s = {"banana", "abacaxi", "kiwi"}
print(s)   # pode sair em qualquer ordem — depende do hash de cada string
```

É a mesma razão pela qual buscar em um set é muito mais rápido do que em uma lista: em vez de percorrer tudo, Python calcula o hash e vai direto ao endereço onde aquele valor estaria. O custo dessa velocidade é a ordem — você troca uma pela outra.

Para entender como o hash vira um endereço de memória, por que listas não podem ser chaves de dicionário, o que são colisões e por que inteiros pequenos às vezes parecem vir "em ordem": [Apêndice: Como funciona uma tabela hash](../apendices/tabela_hash.md).

Se precisar percorrer em ordem, use `sorted()`:

```python
for item in sorted(s):
    print(item)   # sempre em ordem crescente
```

E se precisar de ordem de inserção com valores únicos, a solução mais simples é um `for` manual:

```python
vistos = set()
unicos_em_ordem = []
for item in colecao:
    if item not in vistos:
        unicos_em_ordem.append(item)
        vistos.add(item)
```

---

## Funções e escopo

**Por que uma variável criada dentro de uma função não existe fora dela?**

Porque ela tem escopo local — existe só durante a execução da função. Quando a função termina, a variável some. É o comportamento esperado: evita que funções alterem acidentalmente variáveis de outras partes do programa.

Se precisar do valor fora, use `return`:

```python
def calcular(n):
    resultado = n * 2   # existe só aqui dentro
    return resultado    # entrega o valor para fora

valor = calcular(5)     # valor recebe 10
```

---

**Quando devo usar recursão em vez de loop?**

Use recursão quando o problema tem estrutura naturalmente recursiva — ou seja, quando a solução de um caso depende da solução de uma versão menor do mesmo problema. Exemplos clássicos: percorrer uma árvore de pastas, calcular fatorial, busca binária em uma estrutura aninhada.

Para a maioria dos problemas do dia a dia (somar uma lista, percorrer elementos, acumular resultados), um `for` ou `while` é mais legível e mais eficiente — o Python tem um limite padrão de ~1000 chamadas recursivas antes de lançar `RecursionError`.

```python
# Com loop — direto, sem limite de profundidade
def soma_loop(nums):
    total = 0
    for n in nums:
        total += n
    return total

# Com recursão — elegante, mas desnecessário aqui
def soma_recursiva(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + soma_recursiva(nums[1:])
```

Ambos dão o mesmo resultado. Para listas grandes, o loop é a escolha certa. Use recursão quando o código recursivo for *mais claro* do que o iterativo — não quando for impressionante.

---

**Por que modificar uma lista dentro de uma função modifica ela fora também?**

Porque listas são passadas por referência — a função recebe o mesmo objeto, não uma cópia. Qualquer modificação feita dentro da função afeta a lista original. Isso é diferente de números e strings, que são imutáveis.

```python
def adicionar(lista, item):
    lista.append(item)   # modifica a lista original

notas = [7, 8]
adicionar(notas, 9)
print(notas)   # [7, 8, 9] — foi modificada
```

Se não quiser isso, passe uma cópia: `adicionar(notas.copy(), 9)`.

---

**Se eu anotar `notas: list[float]`, o Python me impede de passar o tipo errado?**

Não. Type hints são documentação, não uma trava de segurança. O Python não verifica isso em tempo de execução:

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

calcular_media(["a", "b"])
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

O erro não é "você passou o tipo errado": o Python deixa a chamada passar de boas e só quebra depois, dentro do `sum()`, quando de fato tenta somar `0` com `"a"`. A anotação existe para te lembrar (e para o editor te avisar enquanto você digita), não para impedir a execução. Quem garante que os tipos batem continua sendo você.

---

## Arquivos

**Por que meu arquivo com acentos abre com caracteres estranhos ou dá erro?**

Provavelmente um problema de **encoding**. Quando você cria um arquivo em UTF-8 (padrão no Linux/Mac e em qualquer editor moderno) e tenta abrir sem especificar o encoding, o Windows pode tentar decodificar usando o padrão do sistema — geralmente `cp1252` ou `latin-1`. O resultado é lixo (`Ã©` em vez de `é`) ou um `UnicodeDecodeError`.

A solução é sempre especificar `encoding="utf-8"` tanto ao escrever quanto ao ler:

```python
# Errado — comportamento depende do sistema operacional
with open("notas.txt", "w") as f:
    f.write("Leônidas, 8.5\n")

# Certo — funciona igual em qualquer sistema
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Leônidas, 8.5\n")

with open("notas.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Se você já tem um arquivo com encoding errado e precisa convertê-lo, abra no VS Code e clique no indicador de encoding no canto inferior direito — lá dá para mudar e salvar no formato certo.

---

**Qual a diferença entre `read()`, `readline()` e `readlines()`?**

Três formas de ler um arquivo, cada uma com um caso de uso diferente:

| Método | O que retorna | Quando usar |
| --- | --- | --- |
| `f.read()` | Conteúdo inteiro como uma string | Arquivos pequenos, quer tudo de uma vez |
| `f.readline()` | Uma linha (avança o cursor) | Pular cabeçalho, ler linha específica |
| `f.readlines()` | Lista com todas as linhas | Precisa de índice ou número de linhas |

```python
with open("turma.csv", "r", encoding="utf-8") as f:
    cabecalho = f.readline()   # lê "nome,nota\n" e avança
    for linha in f:            # continua do ponto onde readline() parou
        print(linha.strip())
```

Na maioria dos casos, a forma mais eficiente é usar o arquivo diretamente no `for` (`for linha in f:`) — o Python lê uma linha por vez sem carregar tudo na memória. `readlines()` só vale quando você precisa acessar linhas por índice ou saber o total.

---

**Posso misturar `readline()` com `for linha in f` na mesma abertura?**

Sim — e é exatamente o que o padrão de pular cabeçalho faz. `readline()` e `for linha in f` compartilham o mesmo cursor interno. Quando você chama `readline()` uma vez, o cursor avança para a segunda linha. O `for` subsequente continua de onde o cursor está:

```python
with open("turma.csv", "r", encoding="utf-8") as f:
    cabecalho = f.readline()   # lê linha 1, cursor vai para linha 2
    for linha in f:            # começa da linha 2 — o cabeçalho foi pulado
        print(linha.strip())
```

O cuidado: se você chamar `readline()` demais antes do `for`, vai pular linhas de dados sem perceber. E se chamar `readlines()` antes do `for`, o `for` não vai produzir nada — o cursor já chegou ao fim do arquivo.

---

**Posso usar `try/except` em vez de `os.path.exists()` para verificar se um arquivo existe?**

Sim — e é a forma preferida em Python. Checar se o arquivo existe antes de abrir e depois abrir são duas operações separadas, e entre as duas o arquivo pode ter sumido (outro processo deletou, o disco falhou). O `try/except` trata isso de uma vez:

```python
# Com os.path.exists — dois passos, pode falhar entre eles
import os
if os.path.exists("dados.txt"):
    with open("dados.txt", "r", encoding="utf-8") as f:
        ...

# Com try/except — uma operação, mais seguro e idiomático
try:
    with open("dados.txt", "r", encoding="utf-8") as f:
        ...
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

O estilo Python chama isso de EAFP (*Easier to Ask Forgiveness than Permission*): tente fazer, trate o erro se acontecer. O `import os` também introduz um módulo que só vai aparecer na Aula 15 — então em exercícios de Aula 14, use sempre `try/except`.

---

**`float(partes[1])` dá `ValueError` mesmo o arquivo existindo. Por quê?**

Provavelmente uma linha vazia no final do arquivo. Quando você usa `f.write("Ana,8.5\n")`, o `\n` cria uma nova linha — então o arquivo termina com uma linha em branco. `readlines()` inclui essa linha como `"\n"` na lista, e `"\n".strip().split(",")` vira `[""]`, onde `partes[1]` não existe ou é uma string vazia que `float()` não consegue converter.

Duas soluções:

```python
# Solução 1: pular linhas vazias antes de processar
for linha in f:
    linha = linha.strip()
    if linha == "":
        continue          # ignora linha vazia e vai para a próxima
    partes = linha.split(",")
    nota = float(partes[1])

# Solução 2: capturar o erro (útil quando o arquivo pode ter dados malformados)
for linha in f:
    try:
        partes = linha.strip().split(",")
        nota = float(partes[1])
    except (ValueError, IndexError):
        continue          # linha com problema — pula e continua
```

A solução 1 é mais clara quando o único problema esperado é linha vazia. A solução 2 é mais robusta quando o arquivo pode ter outros tipos de dado inválido.

---

## Laços

**Quando usar `while` e quando usar `for`?**

Se você sabe o que vai percorrer (uma lista, um range, uma sequência), use `for`. Se você não sabe quantas vezes vai repetir, use `while`.

Na dúvida: se a frase natural é "repita enquanto..." → `while`. Se for "para cada item em..." → `for`.

---

**Qual a diferença entre `break` e `continue`?**

`break` encerra o laço completamente. `continue` pula o restante da iteração atual e vai para a próxima.

```python
for i in range(5):
    if i == 3:
        break        # para tudo: imprime 0, 1, 2
    print(i)

for i in range(5):
    if i == 3:
        continue     # pula o 3: imprime 0, 1, 2, 4
    print(i)
```

---

**O que é um laço infinito e como sair?**

Um laço que nunca termina porque a condição de parada nunca vira `False`. Acontece mais com `while` quando você esquece de atualizar a variável que a condição verifica. Para forçar o encerramento: **Ctrl+C** no terminal.

---

**Por que usar `while True` com `break` em vez de colocar a condição direto no `while`?**

Porque às vezes você só descobre se deve parar *depois* de executar o corpo do laço — não antes.

Com a condição no `while`, o Python verifica *antes* de cada rodada. Isso exige que a variável que controla a saída já exista e já tenha um valor relevante antes do laço começar. Quando o valor vem do usuário ou é calculado dentro do laço, você precisa duplicar código: uma vez antes do laço (para ter algo a checar) e de novo dentro (para atualizar). Isso fica feio e propenso a erro.

```python
# jeito duplicado — lê a entrada duas vezes
linha = input("Texto (ou 'fim'): ")
while linha != "fim":
    print("Processando:", linha)
    linha = input("Texto (ou 'fim'): ")   # repetição do mesmo input
```

Com `while True` + `break`, você lê uma vez, processa, decide se para — tudo no mesmo lugar:

```python
# jeito limpo
while True:
    linha = input("Texto (ou 'fim'): ")
    if linha == "fim":
        break
    print("Processando:", linha)
```

Outra vantagem: o `break` pode estar no meio ou no final do corpo, não só no começo. Quando a condição de saída depende de vários passos que acontecem durante a iteração, `while True` + `break` deixa o fluxo muito mais claro do que uma condição complexa no cabeçalho do `while`.

O padrão é tão comum que vale decorar a estrutura — você vai ver em praticamente qualquer código que lê entradas do usuário.

---

**Qual a diferença entre `enumerate()` e `zip()`?**

Os dois evitam índice manual, mas resolvem problemas diferentes. `enumerate()` percorre **uma** sequência e entrega o índice junto com o valor:

```python
frutas = ["maçã", "banana"]

for i, fruta in enumerate(frutas):
    print(i, fruta)
# 0 maçã
# 1 banana
```

`zip()` percorre **duas ou mais** sequências ao mesmo tempo, emparelhando os elementos que estão na mesma posição:

```python
nomes = ["Ana", "Bruno"]
notas = [8.5, 6.0]

for nome, nota in zip(nomes, notas):
    print(nome, nota)
# Ana 8.5
# Bruno 6.0
```

Resumindo: precisa só do índice de uma lista → `enumerate()`. Precisa andar por duas listas ao mesmo tempo → `zip()`. Se as listas do `zip()` tiverem tamanhos diferentes, ele para no menor, sem avisar: confira `len()` das duas antes se isso for um problema.

---

### Por que a contagem começa em 0 e não em 1?

Parece arbitrário, mas tem razão técnica de verdade — não é capricho do Python nem convenção inventada do nada.

#### A origem: como a memória funciona

Quando um programa guarda uma sequência de valores (um array, uma lista), eles ficam em posições consecutivas na memória RAM. Para acessar o elemento de índice `i`, o computador calcula:

```text
endereço do elemento = endereço do início + (i × tamanho_de_cada_elemento)
```

O primeiro elemento está a **zero posições** de distância do início — ou seja, seu deslocamento (*offset*) é 0. Com indexação 1, a fórmula viraria `base + (i−1) × tamanho`, exigindo uma subtração extra a cada acesso. Em C (1972), onde arrays são ponteiros para blocos de memória, `arr[0]` mapeia diretamente para `*arr` sem nenhuma conta. Zero-indexing não é gosto — é o jeito que o hardware funciona.

BCPL (1967), predecessor direto de C, já fazia isso. C herdou e consolidou. Nenhuma pessoa "decidiu" começar em zero: foi consequência do modelo de memória.

#### O argumento matemático de Dijkstra (1982)

Alguns anos depois, o cientista da computação Edsger Dijkstra escreveu um texto famoso (EWD831, "Why Numbering Should Start at Zero") formalizando matematicamente por que a escolha faz sentido.

O argumento: para representar uma sequência de inteiros, o intervalo **semi-aberto** `[a, b)` — onde `a` entra e `b` não entra — é o único que não tem problemas nos casos limite:

- O comprimento da sequência é sempre `b − a`, sem ajuste de ±1.
- Uma sequência vazia é representada por `a == b`, sem precisar de valor negativo.
- Para uma sequência de `n` elementos começando em 0: `[0, n)`. O índice de cada elemento é exatamente o número de elementos que o precedem.

Dijkstra chamou qualquer outra escolha de "intelectualmente feia". O argumento dele é o mais elegante, mas é posterior à adoção em C — é a justificativa teórica de algo que já existia por razão de hardware.

#### Por que Python especificamente

Python é de alto nível — não tem aritmética de ponteiros exposta. Guido van Rossum poderia ter escolhido 1-indexing. Não o fez por duas razões:

1. **Influência de C**: Guido trabalhou extensivamente com C antes de criar Python. A escolha veio naturalmente.
2. **Slices funcionam melhor**: com zero-indexing e intervalos semi-abertos, `a[:i]` e `a[i:]` dividem qualquer sequência em dois pedaços que somam o original, inclusive quando um dos lados está vazio. Com indexação 1 e intervalos fechados, isso quebra nos casos limite.

O `range()` segue a mesma lógica: `range(n)` gera `n` elementos, e dividir em dois pedaços em qualquer ponto `k` produz `range(k)` e `range(k, n)` — sem sobreposição e sem lacuna.

#### Linguagens que usam 1-indexing — e por quê

Nem todas as linguagens fazem isso. Fortran (1957), MATLAB, R e Lua começam em 1. O argumento delas não é técnico: são voltadas para matemáticos e cientistas, e na matemática você escreve `x₁, x₂, ..., xₙ` — então `x[1]` é mais natural que `x[0]`.

Não estão erradas. São otimizadas para corresponder ao domínio de quem usa. A diferença é de público-alvo, não de correção.

#### Resumo

| O que | Por que começa em 0 |
| --- | --- |
| Hardware / C | Offset de memória: primeiro elemento está a 0 posições do início |
| Dijkstra (matemática) | Intervalo `[a, b)` é o único que não degenera para sequências vazias |
| Python (slices) | `a[:i]` + `a[i:]` = `a` inteiro, sem ajuste, inclusive para `i=0` |
| Linguagens em 1 (Fortran, R) | Público científico; `x1` é a notação matemática padrão |

---

## Erros e mensagens

**O Python apontou o erro numa linha que parece correta. Por quê?**

O Python percebe o problema quando chega num ponto que não faz sentido dado o que veio antes. Um parêntese aberto na linha 5 pode causar um `SyntaxError` só na linha 8, quando o Python tenta continuar a expressão e não encontra o fechamento esperado. Sempre olhe a linha indicada **e** as linhas anteriores.

---

**O que é `IndentationError`?**

O código tem recuo errado. O Python usa a indentação para saber o que pertence a qual bloco (`if`, `for`, `def`...). Se você misturou espaços e tabs, ou usou recuo inconsistente, ele não consegue interpretar a estrutura.

Configure o editor para usar sempre 4 espaços — nunca tabs. No VS Code isso está em `Configurações > Editor: Tab Size` e `Insert Spaces`.

---

**O que é `UnboundLocalError`?**

Aparece quando você tenta ler uma variável dentro de uma função que existe fora dela, mas também é atribuída dentro da função em algum ponto. O Python decide que ela é local (por causa da atribuição) e tenta lê-la antes de ter sido definida.

```python
total = 0

def adicionar(n):
    total = total + n   # UnboundLocalError: Python vê a atribuição e decide que total é local
```

A solução mais limpa é passar como parâmetro e retornar:

```python
def adicionar(total, n):
    return total + n

total = adicionar(total, 5)
```

---

## Strings

**Chamei `.upper()` (ou `.strip()`, `.replace()`...) e a string não mudou. Por quê?**

Porque strings são **imutáveis** — nenhum método altera a string original. Eles devolvem uma **string nova** com o resultado, e a antiga fica intacta. Se você não guarda esse retorno, ele simplesmente se perde e parece que "não funcionou".

```python
nome = "ana"
nome.upper()        # cria "ANA"... e joga fora, porque ninguém guardou
print(nome)         # "ana" — nada mudou

nome = nome.upper() # captura o retorno de volta na variável
print(nome)         # "ANA"
```

A regra: se quer manter o resultado, **reatribua** (`nome = nome.metodo()`). Vale para `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.title()` — todos.

---

**Por que `"gabriel" != "Gabriel"`?**

Python diferencia maiúsculas de minúsculas em strings. `"gabriel"` e `"Gabriel"` são caracteres diferentes para ele. Quando comparar entrada do usuário, normalize primeiro:

```python
resposta = input("Continuar? (s/n): ").strip().lower()
if resposta == "s":
    ...
```

---

**Por que `int("3.5")` dá erro?**

Porque `"3.5"` não é um inteiro válido — tem parte decimal. `int()` não aceita isso. Se o valor pode ser decimal, converta em dois passos: `int(float("3.5"))` → `3`.

---

**Por que `join()` é chamado no separador e não na lista?**

Parece invertido, mas faz sentido quando você pensa no papel de cada um: o separador é quem "cola" — então é ele que tem a responsabilidade de juntar. A lista é só o material.

O jeito de ler que funciona pra mim: `", ".join(palavras)` = *"use vírgula-e-espaço para juntar `palavras`"*.

```python
palavras = ["maçã", "banana", "laranja"]
", ".join(palavras)    # "maçã, banana, laranja"
" | ".join(palavras)   # "maçã | banana | laranja"
"".join(palavras)      # "maçãbananalaranja"
```

O inverso seria `palavras.join(", ")` — mas `", "` é uma string, não uma lista, e a lista não sabe qual separador você quer usar. Colocar o método no separador resolve: o separador decide o formato, a lista fornece o conteúdo.

---

### isdecimal() vs isdigit() vs isnumeric()

Python tem três métodos para perguntar "isso é um número?", e eles diferem em quais caracteres Unicode aceitam:

| Método | Aceita | Exemplo que distingue |
| --- | --- | --- |
| `isdecimal()` | Só `0`–`9` | `"²".isdecimal()` → `False` |
| `isdigit()` | `0`–`9` + superescritos (`²`, `³`) | `"²".isdigit()` → `True` |
| `isnumeric()` | Tudo acima + frações (`½`) e romanos (`Ⅷ`) | `"½".isnumeric()` → `True` |

Na prática, para validar o que um usuário digitou no teclado, os três se comportam igual — nenhum aceita ponto, vírgula, sinal de menos ou espaço:

```python
print("12345".isdecimal())  # True
print("3.14".isdecimal())   # False — ponto decimal não é aceito
print("-5".isdecimal())     # False — sinal de menos não é aceito
```

**Regra prática:** use `isdecimal()` por padrão. É o mais restrito e evita surpresas com caracteres incomuns que `isdigit()` e `isnumeric()` aceitariam.

---

## Módulos

**Os números do `random` são realmente aleatórios?**

Não. Computadores são máquinas determinísticas: dada a mesma entrada, sempre produzem a mesma saída. O que o Python faz é usar um algoritmo chamado **Mersenne Twister** que gera sequências de números que *parecem* aleatórias, mas se você souber o ponto de partida, dá para prever todos os resultados.

Esse ponto de partida é a **seed** (semente):

```python
import random

random.seed(42)
print(random.randint(1, 100))   # sempre o mesmo número
print(random.randint(1, 100))   # sempre o mesmo número
print(random.randint(1, 100))   # sempre o mesmo número
```

Execute isso quantas vezes quiser, em qualquer computador: os resultados vão ser idênticos. Se você não definir uma seed, o Python usa o horário do sistema como ponto de partida, então cada execução começa diferente e parece aleatória.

Isso tem uma aplicação prática em machine learning: é convencional usar `random.seed(42)` no início dos experimentos para que os resultados sejam reproduzíveis. Outra pessoa pode rodar o mesmo código e chegar nos mesmos números. O 42 não tem nada de especial; é referência ao *O Guia do Mochileiro das Galáxias*, mas virou padrão de tanto uso.

Para casos onde a aleatoriedade precisa ser imprevisível de verdade (senhas, tokens de autenticação), existe o módulo `secrets`, que usa fontes de entropia do sistema operacional:

```python
import secrets
print(secrets.randbelow(100))    # número aleatório real
print(secrets.token_hex(16))     # string hexadecimal para tokens e senhas
```

Regra simples: para jogos e simulações, use `random`. Para segurança, use `secrets`.

**Por que `venv\Scripts\activate` dá erro de "scripts is disabled" no Windows?**

Porque o terminal padrão do VS Code no Windows é o PowerShell, e por padrão ele bloqueia a execução de scripts por segurança. A mensagem completa costuma ser algo como:

```text
... cannot be loaded because running scripts is disabled on this system.
```

Não é um erro no seu código nem no ambiente virtual em si, é uma política de segurança do próprio PowerShell. Resolve rodando, uma única vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois disso, `venv\Scripts\activate` funciona normalmente em qualquer projeto (mais detalhes no [Apêndice: Ambiente Avançado](../apendices/ambiente_avancado.md)).

---

## Classes e objetos

**Para que serve o `self`?**

`self` é a referência ao próprio objeto dentro dos métodos. Quando você chama `conta.depositar(100)`, o Python passa `conta` como primeiro argumento automaticamente — e esse argumento chega ao método com o nome `self`. É obrigatório declarar, mas o Python preenche na chamada.

```python
class Conta:
    def depositar(self, valor):   # self = a conta específica que chamou
        self.saldo += valor
```

---

**Qual a diferença entre atributo e método?**

Atributo é dado (o que o objeto tem ou é). Método é ação (o que o objeto sabe fazer). Em `conta.saldo`, `saldo` é atributo. Em `conta.depositar(100)`, `depositar` é método — note os parênteses.

---

**Por que meu método dá `TypeError: takes 1 positional argument but 2 were given`?**

Você esqueceu o `self` no método. Compare:

```python
class Conta:
    def depositar(valor):        # faltou o self
        self.saldo += valor
```

```python
class Conta:
    def depositar(self, valor):  # correto
        self.saldo += valor
```

Quando você chama `conta.depositar(100)`, o Python sempre passa o próprio objeto como primeiro argumento, além de qualquer outro que você escreva na chamada. Se o método só tem um parâmetro (`valor`), o Python tenta encaixar dois argumentos (`conta` e `100`) num espaço que só tem lugar pra um, e o erro conta exatamente isso: "esperava 1 argumento, recebi 2".

A correção é sempre a mesma: todo método de uma classe precisa de `self` como primeiro parâmetro, mesmo que você nunca o use dentro do corpo da função.

---

**Por que `print` de uma lista de objetos mostra o endereço feio mesmo com `__str__` definido?**

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Aluno({self.nome})"

a1 = Aluno("Ana")
a2 = Aluno("Bruno")

print(a1)          # Aluno(Ana), usa o __str__ normalmente
print([a1, a2])     # [<__main__.Aluno object at 0x...>, <__main__.Aluno object at 0x...>]
```

`__str__` controla a exibição direta de um objeto: `print(objeto)`, `str(objeto)`, dentro de f-strings. Mas quando o objeto aparece dentro de uma estrutura (lista, tupla, dicionário), o Python usa outro método parecido chamado `__repr__` pra decidir como mostrar cada item, não o `__str__`. Se você não definir `__repr__`, ele continua sendo o padrão herdado, o mesmo endereço feio de sempre, mesmo com `__str__` já definido.

Regra prática: `__str__` é a versão "pra mostrar pro usuário"; `__repr__` é a versão "técnica", usada dentro de coleções e no console interativo. Definir os dois é comum em código real, mas foge do escopo de CI182.

Sem aprender `__repr__`, o jeito mais simples de exibir uma lista de objetos é percorrer com `for` e chamar o método de exibição de cada um, em vez de dar `print()` na lista inteira:

```python
for aluno in turma:
    aluno.apresentar()
```

---

**O que é polimorfismo, na prática?**

Objetos de classes diferentes respondendo ao mesmo método, cada um do seu jeito, sem quem chama precisar saber qual tipo específico está lidando.

```python
class Cachorro:
    def fazer_som(self):
        print("Au au!")

class Gato:
    def fazer_som(self):
        print("Miau!")

for animal in [Cachorro(), Gato()]:
    animal.fazer_som()   # cada um responde do seu jeito
# Au au!
# Miau!
```

O `for` chama `animal.fazer_som()` sem saber se é `Cachorro` ou `Gato`, cada objeto sabe responder pelo próprio tipo. Isso é diferente de um `if isinstance(animal, Cachorro): ...` espalhado pelo código: com polimorfismo, quem decide "como fazer" é o próprio objeto, não quem está chamando.

---

**O que significa encapsulamento na prática, se Python não trava nada de verdade?**

Encapsulamento é controlar o acesso aos dados internos de um objeto, para que ele só mude de jeitos previsíveis, em vez de qualquer parte do código alterar qualquer atributo diretamente. Em Python isso é **convenção**, não uma trava real da linguagem: um `_` no início do nome (`self._vida`) avisa "isto é interno, use os métodos", mas nada impede tecnicamente de acessar `objeto._vida` direto.

```python
class Personagem:
    def __init__(self, vida_maxima):
        self._vida = vida_maxima   # _ avisa: acesse pelos métodos, não direto

    def receber_dano(self, dano):
        if dano <= self._vida:
            self._vida -= dano
        else:
            self._vida = 0
```

A vantagem: se toda alteração passa por `receber_dano()`, você garante que a vida nunca fica negativa. Se qualquer código pudesse fazer `personagem._vida = -50` direto, essa garantia desaparece.

---

**O que é abstração, e como isso é diferente de encapsulamento?**

Abstração é esconder **como** uma classe faz por dentro, deixando visível só **o que** ela oferece. Quem usa a classe chama os métodos sem precisar saber a implementação, e essa implementação pode mudar depois sem quebrar quem usa.

É fácil confundir com encapsulamento porque os dois lidam com "esconder coisas", mas a diferença é o alvo: encapsulamento protege **dados** (você não mexe em `self._vida` direto). Abstração simplifica **comportamento** (você chama `personagem.receber_dano(50)` sem saber se por dentro ela só subtrai um número ou também dispara uma animação e um som).

```python
personagem.receber_dano(50)   # você só precisa saber que isso existe e o que faz
# não importa se por dentro é uma soma simples ou algo bem mais complexo
```

Veja os quatro pilares juntos na [Aula 17](../aulas/17_poo.md).

---

**Qual a diferença entre herança e composição, na prática?**

Herança é "é um": `Guerreiro` *é um* `Personagem`, então ele herda tudo (`receber_dano()`, `curar()`, `vida()`) automaticamente com `class Guerreiro(Personagem):`.

Composição é "tem um": quando a relação não é de tipo, e sim de posse, um objeto guarda outro como atributo em vez de herdar dele.

```python
class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

class Guerreiro(Personagem):
    def __init__(self, nome, vida_maxima=120):
        super().__init__(nome, vida_maxima)
        self.arma = Arma("Espada longa", 30)   # tem uma Arma, não é uma Arma
```

Faz sentido dizer "Guerreiro é um Personagem" (herança), mas não faz sentido dizer "Guerreiro é uma Arma" — ele *tem* uma. Se você tentar forçar herança numa relação de posse (`class Guerreiro(Arma)`), o `Guerreiro` herdaria atributos e métodos de `Arma` que não fazem sentido nenhum para ele (`dano` de uma arma não é o mesmo que a força de um guerreiro). Veja [Aula 17](../aulas/17_poo.md#herança).
