# Aula 09: Listas

Até agora cada variável guardava um único valor: `nota = 8.5`, `nome = "Ana"`. Isso funciona quando você sabe exatamente quantos valores vai ter. Mas e quando não sabe? E quando precisa guardar todas as notas de uma turma, ou todos os itens de um carrinho de compras, ou os resultados que o usuário foi digitando um por um?

É para isso que existem as listas, a estrutura de dados mais usada em Python. Com listas, você pode guardar qualquer quantidade de valores numa única variável e processá-los com laços. Combinando listas com o `for` e o `while` que você já sabe, é possível escrever programas que trabalham com qualquer volume de dados, cinco itens ou cinco mil, o código é o mesmo.

---

## O que é uma lista?

Uma lista é uma **sequência ordenada e mutável** de valores.

**Ordenada** significa que os itens têm uma posição fixa e essa posição importa: o primeiro item é sempre o primeiro, o segundo é sempre o segundo. Se você coloca `"Ana"` antes de `"Bruno"`, eles vão continuar nessa ordem até você mudar explicitamente. Diferente de um conjunto matemático, onde a ordem não existe. Veremos mais sobre conjuntos em python na aula [Aula 12](12_tuplas_sets.md) com os Sets.

**Mutável** significa que você pode alterar o conteúdo depois de criar a lista: adicionar itens, remover, trocar um pelo outro. Isso é diferente das strings que você viu na [Aula 08](08_strings.md): strings são imutáveis, qualquer "mudança" cria uma nova string do zero. Listas modificam no lugar.

```python
notas = [7.5, 8.0, 6.5, 9.0]
nomes = ["Ana", "Bruno", "Carlos"]
vazia = []                             # lista vazia
misturada = [1, "texto", True, 3.14]  # tipos diferentes são permitidos
```

As listas usam colchetes `[]` e separam os itens por vírgula.

A lista `misturada` acima é válida em Python, mas na prática você quase sempre vai guardar valores do mesmo tipo: uma lista de notas, uma lista de nomes, uma lista de idades. Misturar tipos as vezes dificulta o processamento, se você quiser somar os itens, o Python não vai saber o que fazer com `"texto"` no meio de números.

---

## Indexação e fatiamento

Listas funcionam exatamente como strings para acesso por índice, e você já sabe fazer isso desde a [Aula 08](08_strings.md). Cada item ocupa uma posição numerada, começando sempre do zero:

```text
┌──────────┬──────────┬───────────┬───────┬─────────┐
│  'maçã'  │ 'banana' │ 'laranja' │ 'uva' │ 'melão' │
└──────────┴──────────┴───────────┴───────┴─────────┘
     0          1           2         3        4      ← positivos
    -5         -4          -3        -2       -1      ← negativos
```

Os índices negativos contam do final: `-1` é sempre o último item, `-2` o penúltimo, independente do tamanho da lista.

```python
frutas = ["maçã", "banana", "laranja", "uva", "melão"]

print(frutas[0])    # "maçã", primeiro
print(frutas[-1])   # "melão", último
print(frutas[1:3])  # ["banana", "laranja"], fatia (fim excluído)
print(frutas[:2])   # ["maçã", "banana"]
print(frutas[2:])   # ["laranja", "uva", "melão"]
print(frutas[::-1]) # ["melão", "uva", "laranja", "banana", "maçã"], invertida
```

O fatiamento `[início:fim]` segue a mesma lógica do `range()` da [Aula 07](07_repeticao.md) e das strings da [Aula 08](08_strings.md): o `início` entra, o `fim` fica de fora. `frutas[1:3]` pega os índices 1 e 2, não o 3.

Um fatiamento **sempre retorna uma lista nova**. Modificar a fatia não afeta a lista de onde ela veio:

```python
frutas = ["maçã", "banana", "laranja", "uva", "melão"]
fatia = frutas[1:3]       # ["banana", "laranja"], lista nova, independente

fatia[0] = "MODIFICADO"
print(fatia)    # ["MODIFICADO", "laranja"], fatia mudou
print(frutas)   # ["maçã", "banana", "laranja", "uva", "melão"], original intacta
```

Se você pedir um índice que não existe, o Python para o programa com `IndexError`:

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[10])   # IndexError: list index out of range
```

Esse erro é o mesmo que `IndexError` em strings. A causa mais comum é usar um índice calculado que ficou um passo além do fim da lista, se aparecer, cheque se seu índice está dentro do intervalo `0` a `len(lista) - 1`.

E comentando mais uma vez a diferença em relação às strings: listas são **mutáveis**, então você pode alterar um item pelo índice:

```python
frutas[0] = "abacaxi"
print(frutas)   # ["abacaxi", "banana", "laranja", "uva", "melão"]
```

Em strings isso daria `TypeError`. Em listas é permitido.

---

## Adicionando itens

### `append()`: adiciona no final

O método mais usado para construir listas dinamicamente. Sempre adiciona um único item ao final:

```python
compras = []
compras.append("arroz")
compras.append("feijão")
compras.append("óleo")
print(compras)   # ["arroz", "feijão", "óleo"]
```

O padrão geralmente é começar com a lista vazia e ir preenchendo com `append()`. É assim que você coleta entradas do usuário, lê linhas de um arquivo, ou filtra resultados, você não sabe quantos itens vai ter no final, então não dá para criar a lista com o tamanho certo logo de cara.

`append()` sempre coloca no final. Se você quiser em outro lugar, use `insert()`.

### `insert(índice, valor)`: insere em posição específica

```python
compras = ["arroz", "feijão", "óleo"]
compras.insert(1, "sal")   # insere "sal" na posição 1
print(compras)             # ["arroz", "sal", "feijão", "óleo"]
```

Os itens a partir da posição escolhida são empurrados para a direita, nenhum é sobrescrito, a lista cresce de tamanho. `insert(0, valor)` insere no início; `insert(len(lista), valor)` é equivalente a `append()`.

Se o índice for maior do que o tamanho da lista, o Python não dá erro, simplesmente insere no final:

```python
lista = ["a", "b", "c"]   # 3 itens, índices válidos: 0, 1, 2
lista.insert(1000, "z")   # índice absurdo, mas não quebra
print(lista)              # ["a", "b", "c", "z"], foi para o final
```

O mesmo vale para índices negativos muito grandes: se o índice negativo ultrapassar o início da lista, o item vai para o começo sem erro. `insert()` nunca lança `IndexError`.

Na prática, `insert()` aparece menos do que `append()`. Você usa tipo quando precisa manter uma lista em uma ordem específica e quer encaixar um novo item na posição certa, em vez de adicionar no final e reordenar depois.

Um ponto que acho legal de comentar sobre o que disse antes: grande parte das vezes, adicionar no final e reordenar é mais eficiente do que inserir na posição certa. O motivo tem a ver com o custo de cada operação. Se quiser entender por quê, veja o [Apêndice: Custo de operações em listas](../apendices/custo_de_operacoes.md), é um assunto que vai além da matéria, mas vale a leitura.

### `extend()`: adiciona vários itens de outra lista

```python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_a.extend(lista_b)
print(lista_a)   # [1, 2, 3, 4, 5, 6]
```

A diferença entre `extend()` e `append()` é uma das mais confusas no começo:

```python
lista = [1, 2, 3]
lista.append([4, 5, 6])    # adiciona a lista inteira como UM item
print(lista)               # [1, 2, 3, [4, 5, 6]]  ← lista dentro de lista!

lista = [1, 2, 3]
lista.extend([4, 5, 6])    # adiciona cada item individualmente
print(lista)               # [1, 2, 3, 4, 5, 6]   ← flat, como esperado
```

Use `extend()` quando quiser combinar duas listas numa só. Use `append()` quando quiser adicionar um único item (que pode ser qualquer tipo, inclusive outra lista).

Você também pode concatenar listas com `+`, que cria uma lista nova sem modificar as originais:

```python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

resultado = lista_a + lista_b
print(resultado)   # [1, 2, 3, 4, 5, 6]
print(lista_a)     # [1, 2, 3], não foi modificada
print(lista_b)     # [4, 5, 6], não foi modificada
```

---

## Removendo itens

Existem quatro formas de remover itens de uma lista, e a diferença entre elas importa. Veja cada uma:

### `pop()`: remove e devolve pelo índice

`pop()` retira o item da lista **e retorna** o valor removido. Útil quando você ainda precisa usar o valor depois de tirá-lo:

```python
frutas = ["maçã", "banana", "laranja"]

ultima = frutas.pop()     # sem argumento: remove o último
print(ultima)             # "laranja"
print(frutas)             # ["maçã", "banana"]

primeira = frutas.pop(0)  # com índice: remove aquela posição
print(primeira)           # "maçã"
print(frutas)             # ["banana"]
```

Sem argumento (valor dentro dos parênteses), `pop()` sempre remove o último item. Com índice, você escolhe a posição.

`pop()` é especialmente útil quando a lista funciona como uma **pilha** (*stack*): você empilha com `append()` e desempilha com `pop()`, sempre mexendo na ponta. A regra é: o último a entrar é o primeiro a sair, como uma pilha de pratos, você coloca em cima e tira de cima, nunca do meio.

O Ctrl+Z do seu editor de texto funciona com essa lógica. Todo editor mantém uma lista de ações, cada vez que você digita, apaga ou formata algo, essa ação vai pro final. Quando você aperta Ctrl+Z, o editor pega a última ação, remove, devolve o valor e faz o inverso dela. Uma lista comum em Python já é uma pilha funcional se você usar só esses dois métodos.

### `remove()`: remove pelo valor (primeira ocorrência)

Quando você sabe *o que* quer tirar, mas não sabe *onde* ele está:

```python
materias = ["Cálculo", "Física", "Cálculo", "Inglês"]
materias.remove("Cálculo")   # remove só o primeiro "Cálculo"
print(materias)              # ["Física", "Cálculo", "Inglês"]
```

Se o valor não existir, `remove()` lança `ValueError` e o programa para, sempre verifique antes com `in`.

```python
if "Programação" in materias:
    materias.remove("Programação")
```

`remove()` para na primeira ocorrência. Para remover todas, você precisaria de um laço, veja o padrão na seção de padrões comuns mais adiante.

### `del`: remove por índice ou fatia

`del` é uma instrução do Python (não um método de lista). Remove pelo índice ou por uma fatia inteira:

```python
numeros = [10, 20, 30, 40, 50]
del numeros[2]       # remove o índice 2
print(numeros)       # [10, 20, 40, 50]

del numeros[1:3]     # remove uma fatia (índices 1 e 2)
print(numeros)       # [10, 50]
```

A vantagem sobre `pop()` é que você pode remover múltiplos itens de uma vez com fatia. A vantagem sobre `remove()` é que você não precisa saber o valor, só a posição. A diferença entre `del` e `pop()` é que `pop()` devolve o valor, `del` simplesmente descarta.

### `clear()`: remove tudo

```python
lista = [1, 2, 3]
lista.clear()
print(lista)   # []
```

`clear()` esvazia a lista, mas a variável continua existindo, agora como lista vazia. Você pode continuar usando `lista` normalmente depois disso.

Existe uma diferença sutil entre `lista.clear()` e `lista = []` que só aparece em situações específicas. A seção de Cópias mais adiante explica quando e por quê isso importa, por ora, guarde só o básico: `clear()` esvazia a lista e ela continua existindo.

**Resumo: qual usar em cada situação:**

| Situação | Use |
|----------|-----|
| Sabe a posição e quer o valor removido | `pop(índice)` |
| Sabe o valor, não a posição | `remove(valor)` |
| Sabe a posição e não precisa do valor | `del lista[índice]` |
| Quer esvaziar a lista inteira | `clear()` |

---

## Consultando a lista

Você não precisa sair escrevendo `for` para tudo. Python já tem prontos:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print(len(numeros))          # 9, quantidade de itens
print(min(numeros))          # 1, menor valor
print(max(numeros))          # 9, maior valor
print(sum(numeros))          # 36, soma de todos
print(numeros.count(1))      # 2, quantas vezes 1 aparece
print(numeros.index(5))      # 4, posição da primeira ocorrência de 5
print(5 in numeros)          # True, verifica se o valor existe
print(7 in numeros)          # False
```

**`len()`** você já conhece: retorna quantos itens a lista tem. Muito usado para calcular médias (`sum(lista) / len(lista)`) e para checar se a lista está vazia. `if not lista` é equivalente a `if len(lista) == 0`. Funciona porque em Python uma lista vazia é tratada como `False` em condições; qualquer lista com pelo menos um item é `True`.

**`min()` e `max()`** funcionam com qualquer tipo comparável, números (pelo valor) e strings (pela ordem alfabética):

```python
nomes = ["Carlos", "Ana", "Bruno"]
print(min(nomes))   # "Ana", primeira na ordem alfabética
print(max(nomes))   # "Carlos", última na ordem alfabética
```

Passando uma lista vazia, `min()` e `max()` lançam `ValueError`. Sempre verifique se a lista tem conteúdo antes de chamar.

**`sum()`** soma todos os itens. Só funciona com listas de números, tentar somar uma lista de strings dá `TypeError`.

**`count(valor)`** conta ocorrências, e diferente do `index()`, nunca lança erro: se o valor não estiver na lista, retorna `0` e pronto. Mais seguro quando você só quer saber quantas vezes apareceu, sem precisar checar antes.

**`index(valor)`** retorna a posição da **primeira** ocorrência. Se o valor não estiver na lista, lança `ValueError`. O padrão seguro é verificar antes:

```python
if 5 in numeros:
    pos = numeros.index(5)
    print(f"5 encontrado na posição {pos}")
```

**`in`** é o mais seguro para verificar presença, use-o antes de chamar `index()` ou `remove()`. O operador funciona igual ao que você viu em strings na [Aula 08](08_strings.md): mesma sintaxe, mesma lógica, só muda o que está sendo inspecionado.

Por baixo dos panos, tanto `in` quanto `index()` percorrem a lista item a item até achar (ou desistir). Isso tem nome, é a busca linear, e existe uma alternativa bem mais rápida para listas grandes e ordenadas. Se ficou curioso, tem um apêndice sobre isso: [Algoritmos notáveis](../apendices/algoritmos_notaveis.md).

---

## Ordenando

### `sort()`: ordena a lista no lugar

`sort()` modifica a própria lista, sem criar uma nova. Sem argumentos, ordena do menor para o maior:

```python
numeros = [5, 2, 9, 1, 7]
numeros.sort()
print(numeros)   # [1, 2, 5, 7, 9]
```

Para inverter a ordem, passe `reverse=True`, do maior para o menor:

```python
numeros.sort(reverse=True)
print(numeros)   # [9, 7, 5, 2, 1]
```

O padrão (`reverse=False`) já é crescente, então você só precisa passar `reverse=True` quando quiser a ordem decrescente.

`sort()` **não retorna a lista**, retorna `None`. É assim que Python sinaliza que o método agiu na própria lista em vez de criar uma cópia. O erro clássico é escrever `resultado = numeros.sort()` achando que recebe a lista ordenada:

```python
numeros = [3, 1, 2]
resultado = numeros.sort()
print(resultado)  # None  ← sort() não devolve nada
print(numeros)    # [1, 2, 3]  ← a lista original foi modificada
```

Se precisar atribuir o resultado a uma variável nova, use o `sorted()` da próxima seção.

### `sorted()`: retorna uma nova lista ordenada

`sorted()` não toca na lista original, ela cria e retorna uma lista nova:

```python
numeros = [5, 2, 9, 1, 7]
ordenados = sorted(numeros)
print(numeros)    # [5, 2, 9, 1, 7], original intacta
print(ordenados)  # [1, 2, 5, 7, 9], lista nova
```

A regra para escolher: use `sort()` quando não precisa mais da ordem original. Use `sorted()` quando precisa manter as duas versões, a original e a ordenada, ou quando quiser atribuir o resultado direto a uma variável.

`sorted()` também funciona com qualquer sequência, não só listas. Você pode passar uma string ou uma tupla, e ele sempre devolve uma lista ordenada.

### Ordenando com critério personalizado: `key`

Ambos aceitam um parâmetro `key` que define *por qual critério* ordenar. Você passa uma função, e o Python ordena pelo resultado dela, sem alterar os valores originais. (Passar função como argumento é assunto da [Aula 13](13_funcoes.md), por agora, use os exemplos abaixo como receita pronta.)

```python
nomes = ["Carlos", "ana", "Bruno"]
nomes.sort(key=str.lower)   # compara em minúsculas, mas não altera os valores
print(nomes)                # ["ana", "Bruno", "Carlos"]
```

Sem `key=str.lower`, "Carlos" viria antes de "ana" porque letras maiúsculas têm valor menor na tabela ASCII, tecnicamente, `"C"` (código 67) é "menor" que `"a"` (código 97). Com `key=str.lower`, o Python compara como se tudo fosse minúsculo, mas mantém os valores originais intactos no resultado.

```python
palavras = ["banana", "kiwi", "maçã", "laranja"]
palavras.sort(key=len)      # ordena pelo comprimento de cada palavra
print(palavras)             # ["kiwi", "maçã", "banana", "laranja"]
```

Python ter `sum()` e `sort()` prontos não é óbvio, outras linguagens como C exigiriam um laço manual para somar e um algoritmo completo para ordenar. Isso tem vantagens (menos código, menos erro) e desvantagens (esconde o mecanismo por baixo). O [FAQ](../extras/faq.md#por-que-python-tem-funções-prontas-como-sum-e-sort) tem um exemplo comparando as duas abordagens e discute os dois lados.

---

## Invertendo

`reverse()` inverte a lista no lugar, modificando a original:

```python
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)   # [5, 4, 3, 2, 1]
```

Para inverter sem modificar, use fatiamento com passo `-1`, a mesma sintaxe que você viu em strings na [Aula 08](08_strings.md):

```python
numeros = [1, 2, 3, 4, 5]
invertida = numeros[::-1]   # cria uma nova lista invertida
print(numeros)              # [1, 2, 3, 4, 5], original intacta
print(invertida)            # [5, 4, 3, 2, 1]
```

A mesma lógica de `sort()` vs `sorted()`: o método modifica no lugar, o fatiamento cria uma cópia.

Um uso prático: quando você monta uma lista na ordem que os itens chegaram (do mais antigo ao mais novo) e depois quer exibir do mais recente ao mais antigo, sem precisar redesenhar a lógica de coleta.

---

## Iterando sobre listas

O `for` percorre listas diretamente, você viu brevemente isso na [Aula 07](07_repeticao.md):

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)
# maçã
# banana
# laranja
```

A cada iteração, a variável `fruta` recebe automaticamente o próximo item da lista. Você não precisa de índice, de `range()`, nem de contador, o `for` sabe quando a lista acabou e para sozinho.

Isso é mais legível do que acessar por índice (`frutas[0]`, `frutas[1]`...). Prefira quando não precisar da posição.

**Atenção: não modifique a lista enquanto percorre ela.** Remover ou inserir itens dentro de um `for` confunde o iterador e pode pular itens ou causar comportamentos inesperados. Se precisar filtrar, crie uma lista nova:

```python
# ERRADO: pode pular itens silenciosamente
notas = [8.0, 3.5, 7.0, 4.0, 9.0]
for nota in notas:
    if nota < 5:
        notas.remove(nota)   # não faça isso dentro do for

# CERTO: filtra para uma lista nova
aprovadas = []
for nota in notas:
    if nota >= 5:
        aprovadas.append(nota)
```

### Quando você precisa do índice: `enumerate()`

Se precisar do índice e do valor ao mesmo tempo, `enumerate()` entrega os dois sem criar um contador manual, é a função que a [Aula 07](07_repeticao.md) prometeu mostrar aqui:

```python
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# 0: maçã
# 1: banana
# 2: laranja
```

O `enumerate()` entrega pares `(índice, valor)` a cada iteração. O `for i, fruta in ...` **desempacota** cada par: o primeiro elemento vai para `i`, o segundo vai para `fruta`. É o atalho para não precisar escrever:

```python
# sem enumerate, mais longo e mais fácil de errar
i = 0
for fruta in frutas:
    print(f"{i}: {fruta}")
    i += 1
```

Talvez você se pergunte: e se escrever `for i, fruta in frutas` diretamente, sem `enumerate()`? O Python vai tentar desempacotar cada elemento da lista nas duas variáveis, mas cada elemento é uma string, e uma string não é um par de dois valores. O resultado é erro:

```python
frutas = ["maçã", "banana", "laranja"]

for i, fruta in frutas:   # tenta desempacotar "maçã" em dois valores
    print(i, fruta)
# ValueError: too many values to unpack (expected 2)
```

O desempacotamento com duas variáveis no `for` só funciona quando cada elemento da coleção é, ele mesmo, um par. É exatamente isso que `enumerate()` faz: por baixo, ele transforma `["maçã", "banana", "laranja"]` em pares `(0, "maçã")`, `(1, "banana")`, `(2, "laranja")`, aí sim o `for i, fruta in` funciona.

Esses pares com parênteses são **tuplas**, uma estrutura parecida com lista mas imutável. Você vai ver isso com calma na [Aula 12](12_tuplas_sets.md).

A contagem começa em `0` por padrão, igual ao índice das listas. Se quiser exibir uma lista numerada para o usuário e começar do `1`, o parâmetro `start` ajusta isso:

```python
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}: {fruta}")
# 1: maçã
# 2: banana
# 3: laranja
```

Isso é útil quando você está exibindo uma lista para o usuário e quer numerar a partir de 1, como um menu de opções.

---

## Listas aninhadas

Uma lista pode conter qualquer tipo de valor, inclusive outras listas. O caso mais comum é representar uma **matriz**:

```python
matriz = [
    [1, 2, 3],   # linha 0
    [4, 5, 6],   # linha 1
    [7, 8, 9],   # linha 2
]

print(matriz[1][2])   # 6, linha 1, coluna 2
```

O primeiro índice (`[1]`) seleciona a linha inteira, `matriz[1]` devolve `[4, 5, 6]`. O segundo índice (`[2]`) seleciona o elemento dentro dessa linha, `[4, 5, 6][2]` devolve `6`. É como fazer as duas operações em sequência.

Fora de matrizes, listas aninhadas aparecem quando você precisa agrupar itens que pertencem juntos: uma lista de pontuações por rodada, uma lista de produtos com valores. O tema completo, criar matrizes corretamente, percorrer com laços aninhados, operar por linha e coluna, e as armadilhas na cópia, é aprofundado na **[Aula 10: Matrizes](10_matrizes.md)**.

---

## Copiando listas

Esse é um dos erros mais comuns ao começar a trabalhar com listas. Quando você faz `b = a`, não está criando uma cópia, está criando um **segundo nome para a mesma lista**:

```python
a = [1, 2, 3]
b = a         # b é outro nome para a mesma lista

b.append(4)
print(a)      # [1, 2, 3, 4], a também mudou!
print(b)      # [1, 2, 3, 4]
```

Pense assim: `b = a` é como colocar uma segunda placa com o nome `b` na frente da mesma gaveta. As duas placas são nomes para a mesma gaveta, mexer pela placa `b` mexe no conteúdo que `a` também enxerga.

Esse problema aparece muito em funções: você passa uma lista para uma função, a função modifica a lista "internamente", e quando volta percebe que a lista original mudou também. Pode ser intencional (você quer modificar a original) ou um bug silencioso (você achava que a função trabalhava numa cópia). A distinção entre os dois casos é uma das primeiras armadilhas sérias de Python, a [Aula 13](13_funcoes.md) retoma isso quando você já souber criar funções.

Para criar uma cópia independente, use `.copy()` ou o fatiamento `[:]`:

```python
a = [1, 2, 3]
b = a.copy()   # cria uma lista nova com os mesmos valores
# equivalente: b = a[:]

b.append(4)
print(a)   # [1, 2, 3], original intacta
print(b)   # [1, 2, 3, 4]
```

Agora `a` e `b` são listas independentes, modificar uma não afeta a outra.

Se você quiser entender por que `b = a` funciona assim, como o computador guarda variáveis na memória e por que atribuição não cria uma cópia, o [FAQ](../extras/faq.md#como-o-python-guarda-variáveis-na-memória--e-o-que-o-is-realmente-verifica) tem uma explicação detalhada com endereços de memória e tudo mais.

**Atenção com listas aninhadas:** `.copy()` e `[:]` fazem uma **cópia rasa**, a lista externa é copiada, mas as listas internas continuam sendo compartilhadas entre original e cópia. Se você tiver listas dentro de listas e precisar copiar tudo de verdade, existe `copy.deepcopy()`, mas isso fica para a [Aula 15](15_modulos.md), quando você entender imports. Para listas simples de números ou strings, `.copy()` resolve sem problemas.

---

## Padrões comuns com listas

**Acumular valores digitados pelo usuário:**

O padrão clássico: lista vazia + `while` + `append`. A lista cresce a cada iteração até o usuário sinalizar que terminou:

```python
notas = []
while True:
    entrada = input("Nota (ou 'fim'): ")
    if entrada.lower() == "fim":
        break
    notas.append(float(entrada))

if notas:   # evita divisão por zero se a lista estiver vazia
    print(f"Média: {sum(notas) / len(notas):.2f}")
    print(f"Maior: {max(notas)}")
    print(f"Menor: {min(notas)}") 
```

O `if notas` no final verifica se a lista tem pelo menos um item antes de calcular: se o usuário digitou "fim" sem digitar nenhuma nota, a lista ficou vazia e tentar calcular a média causaria `ZeroDivisionError`.

**Filtrar itens que atendem a uma condição:**

Crie uma ou mais listas paralelas para separar os itens que passam em um critério dos que não passam. O padrão é criar as listas vazias fora do laço e preenchê-las com `append()` dentro:

```python
notas = [8.5, 4.0, 7.0, 3.5, 9.0, 6.0]
aprovados = []
reprovados = []

for nota in notas:
    if nota >= 7:
        aprovados.append(nota)
    else:
        reprovados.append(nota)

print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
```

**Remover todas as ocorrências de um valor:**

`remove()` para na primeira ocorrência. Para tirar todas, repita enquanto o valor ainda estiver na lista:

```python
valores = [1, 3, 2, 3, 4, 3]
while 3 in valores:
    valores.remove(3)
print(valores)   # [1, 2, 4]
```

Cada iteração do `while` remove uma ocorrência do `3`. O laço para automaticamente quando não sobrar nenhum.

---

Exemplo rodável desta aula: [`exemplos/09_listas.py`](../exemplos/09_listas.py)

## Exercício sugerido

1. Crie uma lista vazia e adicione notas digitadas pelo usuário até digitar "fim" ou "f".
2. Exiba: a lista original, a lista ordenada, a maior nota, a menor nota e a média.
3. Remova a maior e a menor nota e recalcule a média.
4. Diga quantas notas ficaram acima da média original.

---

## Listas da disciplina

> Você terminou a aula de listas. Este é o momento certo para resolver a **Lista 04: Estruturas de Dados: Listas**, disponível em `docs/listas/`.
>
> Os exercícios usam índices, `append`, `sort`, `pop`, `remove` e iteração com `for`. Tente resolver sem consultar exemplos primeiro.

---

## Exercícios de debug relacionados

| Nível | Arquivo |
|-------|---------|
| Fácil | [`../debug/facil/05_listas.py`](../debug/facil/05_listas.py) |
| Médio | [`../debug/medio/04_listas.py`](../debug/medio/04_listas.py) |

Tente corrigir e compare com a saída esperada descrita no cabeçalho de cada arquivo.

> **Resposta do exercício:** [`respostas/09_listas.py`](../respostas/09_listas.py)
