# Aula 11: Dicionários

Como você viu nas aulas anteriores, listas guardam dados por **posição**: o primeiro item fica no índice `0`, o segundo no `1`, e assim por diante. Isso funciona bem quando os dados são todos do mesmo tipo e a ordem importa.

Mas imagine guardar as informações de um aluno: nome, idade, nota, curso. Com uma lista ficaria `aluno[0]` para o nome, `aluno[1]` para a idade... e você precisaria lembrar o que cada índice representa. Isso quebra quando você adiciona ou remove campos.

Dicionários resolvem esse problema com **chaves nomeadas**: em vez de `aluno[0]`, você usa `aluno["nome"]`. O código se torna auto-explicativo.

---

## O que é um dicionário?

Um dicionário armazena pares de **chave → valor**. Você busca um valor pela chave, não por posição numérica, exatamente como um dicionário de verdade: você procura a palavra (chave) e encontra a definição (valor).

```python
aluno = {
    "nome":     "Ana",
    "idade":    20,
    "nota":     8.5,
    "aprovado": True
}
```

- Os pares ficam entre `{}` e são separados por vírgula
- Cada par é escrito como `chave: valor`
- As chaves devem ser **únicas**, não pode haver duas chaves iguais no mesmo dicionário
- As chaves precisam ser de um tipo **imutável**: strings (o mais comum) e números são os mais usados; listas não funcionam como chave (você vai ver mais sobre imutabilidade na [Aula 12](12_tuplas_sets.md))
- Os valores podem ser de qualquer tipo: número, string, lista, outro dicionário, qualquer coisa

---

## Acessando valores

O dicionário dos exemplos abaixo:

```python
aluno = {
    "nome":  "Ana",
    "idade": 20,
    "nota":  8.5,
}
```

### Com colchetes `[]`

Você busca um valor informando a chave entre colchetes, igual a uma lista, mas com um nome no lugar do número:

```python
print(aluno["nome"])    # "Ana"
print(aluno["nota"])    # 8.5
```

Se a chave não existir, o Python para o programa com `KeyError`:

```python
print(aluno["telefone"])   # KeyError: 'telefone'
```

O erro informa o nome da chave que faltou, exatamente como `IndexError` em listas quando o índice está fora do intervalo.

### Com `get()`: acesso sem risco de KeyError

`get(chave)` faz a mesma busca que `[]`, mas sem parar o programa quando a chave não existe: nesse caso, devolve `None`.

```python
print(aluno.get("nome"))        # "Ana", chave existe, funciona igual a []
print(aluno.get("telefone"))    # None, chave não existe, mas sem erro
```

Você pode passar um **segundo argumento** como valor padrão, devolvido quando a chave não existir:

```python
print(aluno.get("telefone", "não informado"))   # "não informado", chave ausente
print(aluno.get("nome",     "desconhecido"))    # "Ana", chave existe, ignora o padrão
```

O segundo argumento só entra em ação quando a chave está ausente. Se a chave existe, `get()` devolve o valor real.

### Quando usar cada um?

| Situação | Use |
|----------|-----|
| Chave sempre existe | `aluno["nome"]`|
| Chave pode não existir | `aluno.get("telefone", "padrão")`|

Use `[]` quando a chave *deveria* estar lá: se ela não estiver, você quer saber imediatamente, o `KeyError` é o aviso de que algo está errado.

Use `get()` quando a ausência da chave é um caso esperado e você já sabe o que fazer nessa situação.

Se você está usando `get()` em tudo por medo de `KeyError`, está escondendo bugs. `KeyError` é informação, use `[]` e deixe explodir quando precisar.

---

## Tamanho e verificação geral

`len()` aplicado a um dicionário retorna o número de **pares chave-valor**, não o número de caracteres das chaves, nem a soma dos valores:

```python
aluno = {"nome": "Ana", "idade": 20, "nota": 8.5}

print(len(aluno))   # 3, há três pares: "nome", "idade" e "nota"
```

### Verificando se o dicionário está vazio

Em Python, coleções vazias são consideradas `False` em contexto booleano, ou seja, dentro de um `if` ou `while`. Isso vale para listas, strings e dicionários:

```python
print(bool({}))              # False, vazio
print(bool({"nome": "Ana"})) # True, tem dados
```

Na prática, você usa isso diretamente no `if`:

```python
aluno = {}

if aluno:
    print("Tem dados para processar")
else:
    print("Dicionário vazio")
```

As formas abaixo são todas equivalentes, as três verificam a mesma coisa:

```python
if aluno:             # prefira
if len(aluno) > 0:    # mais explícito
if len(aluno) != 0:   # também funciona
```

Para verificar se está **vazio**, use `not`:

```python
if not aluno:
    print("Dicionário vazio")
```

`not aluno` é `True` quando `aluno` está vazio, e `False` quando tem dados.

---

## Adicionando e modificando

A atribuição com `[]` faz as duas coisas: **atualiza** se a chave já existe, **cria** se não existe:

```python
aluno = {"nome": "Gabriel", "nota": 8.5}

aluno["nota"] = 9.0       # atualiza, "nota" já existe
aluno["curso"] = "BCC"     # cria, "curso" é uma chave nova

print(aluno)
# {"nome": "Gabriel", "nota": 9.0, "curso": "BCC"}
```

### `update()`: atualiza com vários pares de uma vez

```python
aluno.update({"nota": 9.5, "turma": "A", "periodo": 2})

print(aluno)
# {"nome": "Gabriel", "nota": 9.5, "curso": "BCC", "turma": "A", "periodo": 2}
```

`update()` é equivalente a fazer várias atribuições `[]` uma a uma, só que em uma única chamada.

---

## Removendo entradas

Você já viu `pop()`, `del` e `clear()` em listas na [Aula 09](09_listas.md). Em dicionários o comportamento é o mesmo, a única diferença é que você passa uma **chave** no lugar de um **índice numérico**.

| Situação | Use |
|----------|-----|
| Quer remover e usar o valor | `pop(chave)` |
| Só quer remover | `del dicionario[chave]` |
| Quer esvaziar tudo | `clear()` |

### `pop(chave)`: remove e retorna o valor

```python
aluno = {"nome": "Ana", "nota": 8.5, "rascunho": True}

removido = aluno.pop("rascunho")
print(removido)   # True
print(aluno)      # {"nome": "Ana", "nota": 8.5}
```

Uma diferença em relação a listas: em dicionários, `pop()` aceita um segundo argumento como valor padrão, devolvido silenciosamente se a chave não existir, sem `KeyError`. Pode ser qualquer valor, não só `None`:

```python
aluno.pop("telefone", None)          # chave ausente → None
aluno.pop("telefone", "não tinha")   # chave ausente → "não tinha"
aluno.pop("telefone", 0)             # chave ausente → 0
```

Funciona exatamente como o segundo argumento do `get()`. A diferença é que `pop()` **remove** a entrada se ela existir; `get()` só lê. Quando a chave existe, os dois devolvem o valor real, o padrão é ignorado:

```python
aluno = {"nome": "Ana", "nota": 8.5}

aluno.pop("nota", 0)    # remove "nota" e devolve 8.5, o 0 foi ignorado
aluno.get("nome", "?")  # lê "nome" e devolve "Ana", o "?" foi ignorado
```

Em listas, `pop()` não tem esse segundo argumento.

### `del`: remove sem retornar

```python
del aluno["nota"]
print(aluno)   # {"nome": "Ana"}
```

### `clear()`: remove tudo

```python
aluno.clear()
print(aluno)   # {}
```

---

## Verificando existência de chaves

`in` você já usa em listas para checar se um item está lá ([Aula 09](09_listas.md)). Em dicionários funciona igual, mas por padrão verifica **chaves**, não valores:

```python
aluno = {"nome": "Ana", "nota": 8.5}

print("nome" in aluno)      # True, chave existe
print("telefone" in aluno)  # False, chave não existe
print("nome" not in aluno)  # False, o inverso de in

if "nota" in aluno:
    print(f"Nota: {aluno['nota']}")
```

Para verificar se um **valor** existe, use `.values()`:

```python
print("Ana" in aluno.values())    # True
print(8.5 in aluno.values())      # True
print(10.0 in aluno.values())     # False
```

---

## Percorrendo dicionários

### Só as chaves

O `for` em dicionários funciona como o `for` em listas que você já viu na [Aula 09](09_listas.md): a cada iteração, a variável recebe um item. A diferença é que em dicionários o "item" padrão é uma **chave**, não um valor:

```python
aluno = {"nome": "Ana", "idade": 20, "nota": 8.5}

for chave in aluno:
    print(chave)
# nome
# idade
# nota
```

A vantagem de ter a chave no laço é que você pode usá-la para buscar o valor no mesmo passo:

```python
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")
# nome: Ana
# idade: 20
# nota: 8.5
```

Existe também `.keys()`, que faz exatamente a mesma coisa com nome mais explícito:

```python
for chave in aluno.keys():
    print(chave)
```

Na prática, `for chave in aluno` é o mais comum, `.keys()` aparece geralmente quando você quer deixar a intenção evidente na leitura.

### Só os valores

`.values()` devolve apenas os valores, sem as chaves. Útil quando você precisa operar nos dados mas não precisa saber de qual campo veio cada um:

```python
for valor in aluno.values():
    print(valor)
# Ana
# 20
# 8.5
```

Um exemplo prático é calcular a média de notas sem se preocupar com os nomes das provas:

```python
notas = {"P1": 8.0, "P2": 7.5, "P3": 9.0}

total = 0
for nota in notas.values():
    total += nota

print(total / len(notas))   # 8.166...
```

A limitação: você perde o contexto da chave. Dentro do laço, você sabe o valor mas não sabe mais de qual campo ele veio. Quando precisar dos dois ao mesmo tempo, use o `.items() da próxima seção.

### Chaves e valores juntos

Você já iterou listas com `for elemento in lista` na Aula 09. Aqui funciona igual, só que com `.items()` cada elemento é um par `(chave, valor)` desempacotado automaticamente pelo `for`:

```python
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
# nome: Ana
# idade: 20
# nota: 8.5
```

Este é o padrão mais usado para percorrer dicionários. O desempacotamento `chave, valor` funciona da mesma forma que `i, elemento` no `enumerate()` de listas da [Aula 09](09_listas.md).

---

## Padrões comuns com dicionários

### Contador de ocorrências

Contar quantas vezes cada item aparece é um dos usos mais frequentes de dicionários:

```python
texto = "abracadabra"
contagem = {}

for letra in texto:
    if letra in contagem:
        contagem[letra] = contagem[letra] + 1   # letra já existe, soma 1
    else:
        contagem[letra] = 1                     # letra nova, começa em 1

print(contagem)
# {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
```

A versão mais compacta usa `get()` com padrão zero:

```python
for letra in texto:
    contagem[letra] = contagem.get(letra, 0) + 1
```

Os dois fazem a mesma coisa. O `get(letra, 0)` retorna o valor atual (ou `0` se a letra ainda não foi vista), e somamos `1`.

### Tabela de tradução

Dicionários são perfeitos para mapear um valor em outro sem precisar de vários `if/elif`:

```python
# Sem dicionário, repetitivo e difícil de manter
numero = int(input("Dia (1–7): "))

if numero == 1:
    dia = "Segunda"
elif numero == 2:
    dia = "Terça"
elif numero == 3:
    dia = "Quarta"
elif numero == 4:
    dia = "Quinta"
elif numero == 5:
    dia = "Sexta"
elif numero == 6:
    dia = "Sábado"
elif numero == 7:
    dia = "Domingo"
else:
    dia = "Dia inválido"

print(dia)
```

```python
# Com dicionário, o mesmo resultado
dias = {
    1: "Segunda",
    2: "Terça",
    3: "Quarta",
    4: "Quinta",
    5: "Sexta",
    6: "Sábado",
    7: "Domingo",
}

numero = int(input("Dia (1–7): "))
dia = dias.get(numero, "Dia inválido")
print(dia)
```

Esse padrão pode aparecer em tradução de códigos, mapeamento de opções de menu, configurações de programa ou qualquer coisa onde um código representa um texto.

### Agrupando itens por categoria

Agrupar uma lista de itens por alguma propriedade:

```python
alunos = [
    ["Ana",    "A"],
    ["Bruno",  "B"],
    ["Carlos", "A"],
    ["Diana",  "B"],
    ["Eva",    "A"],
]

grupos = {}

for nome, turma in alunos:
    if turma not in grupos:
        grupos[turma] = []          # cria a lista para essa turma
    grupos[turma].append(nome)      # adiciona o aluno na turma certa

print(grupos)
# {"A": ["Ana", "Carlos", "Eva"], "B": ["Bruno", "Diana"]}
```

### Lista de dicionários

Quando você tem vários registros do mesmo tipo, o padrão natural é uma lista de dicionários, cada dicionário é um registro:

```python
produtos = [
    {"nome": "Arroz",   "preco": 5.99, "estoque": 100},
    {"nome": "Feijão",  "preco": 7.50, "estoque": 0},
    {"nome": "Óleo",    "preco": 6.20, "estoque": 45},
]

# Percorrendo e filtrando
for produto in produtos:
    if produto["estoque"] > 0:
        print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

# Saída:
# Arroz: R$ 5.99
# Óleo: R$ 6.20
```

---

## Dicionários aninhados

O valor de uma chave pode ser qualquer coisa, inclusive outro dicionário. Isso permite estruturas com mais de um nível:

```python
turma = {
    "Ana":    {"nota": 8.5, "faltas": 2},
    "Bruno":  {"nota": 6.0, "faltas": 8},
    "Carlos": {"nota": 9.0, "faltas": 0},
}
```

Para acessar, você encadeia os colchetes, primeiro a chave do nível externo, depois a do interno:

```python
print(turma["Ana"]["nota"])      # 8.5
print(turma["Bruno"]["faltas"])  # 8
```

Encadear dois colchetes é exatamente o que você fez com matrizes na [Aula 10](10_matrizes.md): `matriz[linha][coluna]`. A diferença é que aqui os "índices" são nomes em vez de números, o que torna o código mais legível.

Para percorrer todos os alunos, `.items()` devolve o nome e o dicionário interno de cada aluno, a variável `dados` recebe o dicionário inteiro `{"nota": ..., "faltas": ...}`, e você acessa os campos normalmente:

```python
for nome, dados in turma.items():
    # a cada iteração: nome = "Ana",   dados = {"nota": 8.5, "faltas": 2}
    #                  nome = "Bruno", dados = {"nota": 6.0, "faltas": 8} ...
    print(f"{nome}, nota: {dados['nota']}, faltas: {dados['faltas']}")

# Ana, nota: 8.5, faltas: 2
# Bruno, nota: 6.0, faltas: 8
# Carlos, nota: 9.0, faltas: 0
```

Para acessar com segurança quando não tem certeza se o aluno existe, você encadeia dois `get()`. O truque está no valor padrão do primeiro: `{}` (dicionário vazio).

```python
# Caso 1: aluno existe
ana = turma.get("Ana", {})    # devolve {"nota": 8.5, "faltas": 2}
nota = ana.get("nota", 0)     # devolve 8.5, chave "nota" existe
print(nota)   # 8.5

# Caso 2: aluno não existe
diana = turma.get("Diana", {})   # "Diana" não está em turma → devolve {}
nota = diana.get("nota", 0)      # {} não tem "nota" → devolve 0
print(nota)   # 0
```

Por que `{}` como padrão? Se `"Diana"` não existir, o primeiro `get()` devolve `{}`. O segundo `get()` roda sobre esse dicionário vazio, que não tem `"nota"`, então devolve `0`. Nenhum erro nos dois passos.

Sem `get()`, qualquer ausência travaria o programa:

```python
diana = turma["Diana"]    # KeyError, para aqui se Diana não existir
nota = diana["nota"]      # KeyError, para aqui se a chave não existir
```

---

## Copiando dicionários

O mesmo problema de cópia rasa das listas existe em dicionários. `b = a` cria um segundo nome para o **mesmo** dicionário:

```python
original = {"nome": "Ana", "nota": 8.5}
copia = original   # não é uma cópia, é o mesmo objeto

copia["nota"] = 10.0
print(original)    # {"nome": "Ana", "nota": 10.0}, original também mudou!
```

Para copiar de verdade:

```python
copia = original.copy()

copia["nota"] = 10.0
print(original)    # {"nome": "Ana", "nota": 8.5}, intacto
print(copia)       # {"nome": "Ana", "nota": 10.0}
```

Assim como em listas, `.copy()` faz uma cópia rasa, se os valores forem listas ou dicionários, eles ainda serão compartilhados. Para cópia completa, use `copy.deepcopy()`, você vai ver como isso funciona na [Aula 15](15_modulos.md), quando chegar nos módulos.

---

## Quando usar dicionário em vez de lista?

| Situação | Use |
|----------|-----|
| Dados com campos nomeados (`nome`, `nota`, `curso`) | Dicionário |
| Sequência de itens similares sem nome | Lista |
| Acessar por posição numérica | Lista |
| Mapear um valor em outro (`código → descrição`) | Dicionário |
| Contar ocorrências de itens diversos | Dicionário |
| Agrupar itens por categoria | Dicionário de listas |
| Vários registros do mesmo tipo | Lista de dicionários |

Na dúvida, comece com lista. Quando estiver escrevendo `aluno[0]` e não lembrar mais o que `0` representa, aí você usa dicionários.

Na [Aula 14](14_arquivos.md) você vai ver que arquivos JSON se convertem direto em dicionários Python, tudo que aprendeu aqui vai ser usado lá.

Na [Aula 16](16_objetos_classes.md) você vai conhecer classes, que resolvem o mesmo problema de "guardar dados nomeados" de um jeito mais organizado. Dicionários e classes se parecem bastante na superfície, o contraste vai fazer sentido quando você chegar lá.

---

Exemplo rodável desta aula: [`exemplos/11_dicionarios.py`](../exemplos/11_dicionarios.py)

## Exercício sugerido

1. Crie um dicionário representando um produto com: nome, preço, categoria e estoque.
2. Exiba todas as informações formatadas percorrendo com `.items()`.
3. Aplique um desconto de 10% no preço e atualize o dicionário.
4. Crie uma lista com 3 produtos (cada um é um dicionário).
5. Percorra a lista e exiba só os produtos com estoque maior que zero.
6. Calcule o valor total do estoque (preço × estoque de cada produto).
7. Conte quantos produtos existem por categoria usando um dicionário contador.

---

## Exercícios de debug relacionados

| Nível | Arquivo |
| --- | --- |
| Fácil | [`../debug/facil/06_dicionarios.py`](../debug/facil/06_dicionarios.py) |
| Difícil | [`../debug/dificil/01_ranking.py`](../debug/dificil/01_ranking.py) |

Tente corrigir e depois compare com a saída esperada descrita no cabeçalho de cada arquivo.

> **Resposta do exercício:** [`respostas/11_dicionarios.py`](../respostas/11_dicionarios.py)

---

