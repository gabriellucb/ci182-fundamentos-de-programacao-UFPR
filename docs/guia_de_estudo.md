# Guia de Estudo

Este documento é um complemento às aulas, não substitui nenhuma delas. Aqui você encontra orientações práticas de como usar o repositório, onde cada lista da disciplina se encaixa e uma referência rápida para os erros mais comuns que você vai encontrar.

---

## Como usar este repositório

O material principal está em [`docs/aulas/`](aulas/README.md). Cada arquivo é uma aula completa com explicação, exemplos de código e exercício sugerido no final.

Os arquivos em `docs/exemplos/` são código Python comentado, organizados por tema. Servem como referência prática para consultar sintaxe e ver padrões funcionando.

As respostas dos exercícios sugeridos ficam em `docs/respostas/`, com a mesma numeração das aulas. Se quiser praticar identificando bugs, [`docs/debug/`](debug/README.md) tem programas quebrados de propósito, separados por dificuldade (`facil/`, `medio/`, `dificil/`), sem gabarito. E [`docs/extras/`](extras/README.md) reúne glossário, FAQ e referência rápida de sintaxe, para consulta pontual quando um termo ou uma dúvida travar você no meio de uma aula.

Quem quiser ir além do que as aulas cobrem tem duas opções: `docs/apendices/` traz explicações mais fundas sobre temas que aparecem de leve nas aulas (custo de operações, algoritmos de busca, como funciona uma tabela hash, ambiente de desenvolvimento avançado), e `docs/projetos/` tem programas maiores e completos, escritos usando só o que as aulas ensinam (o `copa_penaltis`, por exemplo, é uma disputa de pênaltis interativa inteira).

Não existe jeito errado de usar o material, mas a abordagem que acredito que funciona melhor é:

1. Leia a aula com calma, sem pular nada.
2. Rode os exemplos do código.
3. Quebre algo de propósito. Mude um valor, tire uma linha, veja o que acontece.
4. Tente o exercício sugerido antes de abrir a resposta em `docs/respostas/`.
5. Resolva a lista correspondente.

---

## Listas da disciplina

As listas de exercícios estão em `docs/listas/`, em PDF e em texto. A tabela abaixo mostra qual aula corresponde a cada lista:

| Lista | Tema | Aula correspondente |
|-------|------|---------------------|
| Lista 01 | Entradas, Saídas e Operações | Aulas 03, 04 e 05 |
| Lista 02 | Condicionais e Operadores Lógicos | Aulas 04 e 06 |
| Lista 03 | Estruturas de Repetição | Aula 07 |
| Lista 04 | Estruturas de Dados: Listas | Aulas 08, 09 e 10 |
| Lista 05 | Estruturas de Dados: Matrizes | Aula 10 |
| Lista 06 | Modularização e Funções | Aula 13 |
| Lista 07 | Manipulação de Arquivos | Aula 14 |

As versões em `.txt` permitem buscar exercícios por palavra-chave.

---

## Gabaritos

Os gabaritos estão em `docs/gabaritos/` (`.ipynb`). Você pode abrir qualquer um diretamente no Google Colab, sem instalar nada, pelo navegador.

> Tente resolver a lista por conta própria antes de abrir o gabarito. Mesmo que você não consiga, anote onde travou. Ver a solução sem ter tentado antes não ajuda a aprender.

| Lista | Gabarito no Colab |
|-------|-------------------|
| Lista 01: Entradas, Saídas e Operações | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_01.ipynb) |
| Lista 02: Condicionais e Operadores Lógicos | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_02.ipynb) |
| Lista 03: Estruturas de Repetição | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_03.ipynb) |
| Lista 04: Estruturas de Dados: Listas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_04.ipynb) |
| Lista 05: Estruturas de Dados: Matrizes | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_05.ipynb) |
| Lista 06: Modularização e Funções | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_06.ipynb) |
| Lista 07: Manipulação de Arquivos | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gabriellucb/ci182-fundamentos-de-programacao-UFPR/blob/main/docs/gabaritos/Gabarito_Lista_07.ipynb) |

---

## Erros comuns e o que significam

Ler a mensagem de erro é a primeira coisa a fazer quando algo quebra. O Python é bem específico: ele diz o tipo do erro, a linha onde ocorreu, e às vezes até aponta o trecho exato com uma setinha (`^`). A maioria dos problemas já está descrita na própria mensagem, então o hábito mais importante é **ler o erro com calma antes de fazer qualquer coisa**.

O formato padrão é:

```text
Traceback (most recent call last):
  File "exercicio.py", line 7, in <module>
    total = soma + entrada
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Leia de baixo para cima: o tipo do erro vem na última linha, e o `line 7` te diz onde procurar.

---

### Erros de escrita

#### `SyntaxError`

O código tem um problema de escrita que o Python não consegue sequer começar a executar. Ele nem tenta rodar, já falha na leitura. Por isso o número de linha no `SyntaxError` às vezes aponta para a linha *seguinte* ao erro real: o Python só percebe que algo está errado quando chega em um ponto que não faz sentido.

Causas mais comuns:

- Parêntese ou colchete aberto e não fechado
- Dois pontos faltando no final de `if`, `for`, `while`, `def`
- Aspas não fechadas

```text
SyntaxError: invalid syntax
SyntaxError: expected ':'                        ← faltou o dois pontos no final de if/for/while/def
SyntaxError: unterminated string literal (detected at line N)   ← aspas abertas e não fechadas
SyntaxError: '(' was never closed                ← parêntese ou colchete não fechado
```

> Se você não acha o erro na linha indicada, procure na linha acima, especialmente por parênteses ou aspas abertas.

---

#### `IndentationError`

A indentação (o recuo do código) está errada. O Python usa o recuo para saber o que pertence a um bloco (`if`, `for`, `def` etc.), então erros aqui fazem o código não fazer sentido estruturalmente.

```text
IndentationError: expected an indented block    ← faltou o recuo depois de if/for/def
IndentationError: unexpected indent             ← tem recuo onde não deveria
IndentationError: unindent does not match any outer indentation level  ← nível de recuo inconsistente
```

A terceira variante aparece quando os recuos do arquivo não fecham de forma consistente (por exemplo, um bloco com 4 espaços e o próximo com só 3).

Um erro vizinho, e ainda mais comum na prática, é o `TabError`, com nome e mensagem próprios:

```text
TabError: inconsistent use of tabs and spaces in indentation
```

Esse aparece quando o arquivo mistura tabs e espaços entre linhas do mesmo bloco. Configure seu editor para usar só espaços (4 por nível) e nunca misturar com tabs.

---

### Erros de nome e tipo

#### `NameError`

Você usou um nome (variável, função) que o Python não reconhece naquele ponto. Pode ser porque não foi criada ainda, porque o nome está errado, ou porque foi definida dentro de uma função e você tenta usá-la fora.

```text
NameError: name 'nota' is not defined
NameError: name 'imprime' is not defined  ← função chamada antes de ser definida
```

Causas mais comuns:

- Erro de digitação no nome (`notas` vs `nota`, `Nota` vs `nota`: Python diferencia maiúsculas de minúsculas)
- Variável usada antes de receber um valor
- Função chamada antes da linha onde ela foi definida

---

#### `UnboundLocalError`

Parece com `NameError` mas acontece em um contexto específico: dentro de uma função, quando você tenta ler uma variável que existe fora dela mas também atribui a ela dentro da função em algum ponto.

```python
total = 0

def adiciona():
    total = total + 1  # erro aqui
```

```text
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
```

O Python vê que `total` recebe valor dentro da função (na linha `total = total + 1`) e decide que ela é local, mas aí tenta lê-la antes de ter sido definida. A solução mais simples é passar o valor como parâmetro e retornar o resultado, em vez de modificar variável global diretamente.

---

#### `TypeError`

Uma operação foi feita com um tipo de dado que não suporta aquela operação. É o erro mais comum para quem está começando, porque `input()` sempre retorna texto, mesmo que o usuário digite um número.

```text
TypeError: can only concatenate str (not "int") to str
TypeError: unsupported operand type(s) for +: 'int' and 'str'
TypeError: '<' not supported between instances of 'str' and 'int'
TypeError: 'int' object is not subscriptable    ← tentou usar índice num número
TypeError: object of type 'int' has no len()   ← len() em número
```

O padrão mais frequente:

```python
entrada = input("Digite um número: ")  # entrada é str, não int!
resultado = entrada * 2                # multiplica a string, não o número
```

Sempre converta o que vem do `input()`: `int(input(...))` ou `float(input(...))`.

---

#### `AttributeError`

Você chamou um método ou acessou um atributo que aquele tipo de objeto não tem. É comum a partir da Aula 16 (classes), mas também aparece com os tipos básicos quando você confunde métodos de tipos diferentes.

```text
AttributeError: 'str' object has no attribute 'append'   ← append() é de lista, não de string
AttributeError: 'int' object has no attribute 'upper'    ← upper() é de string, não de número
AttributeError: 'NoneType' object has no attribute 'strip'   ← a variável é None
```

O terceiro caso é o mais traiçoeiro: geralmente significa que uma função esqueceu o `return` e devolveu `None` sem querer, e você está tentando usar o resultado como se fosse o valor esperado. Confira se a função realmente retorna algo em todos os caminhos antes de checar o nome do método.

---

#### `ValueError`

O tipo está certo, mas o conteúdo não é válido para aquela operação. Aparece quase sempre ao tentar converter texto em número quando o texto não representa um número.

```text
ValueError: invalid literal for int() with base 10: 'abc'  ← int("abc") não existe
ValueError: invalid literal for int() with base 10: '3.5'  ← int("3.5") também falha
ValueError: math domain error                               ← raiz de número negativo
```

O segundo caso pega muita gente: `int("3.5")` falha porque `"3.5"` tem ponto decimal. Se o valor pode ser decimal, converta primeiro com `float()`: `int(float("3.5"))`.

---

### Erros de índice e coleções

#### `IndexError`

Você tentou acessar uma posição que não existe na lista ou na string. Listas começam no índice `0` e vão até `len(lista) - 1`.

```text
IndexError: list index out of range
IndexError: string index out of range
```

Causas mais comuns:

- Loop com `range(len(lista))` está correto, mas `range(len(lista) + 1)` já passa do limite
- Lista vazia e você tenta acessar o índice `0`
- Índice negativo maior que o tamanho (`lista[-10]` numa lista de 3 elementos)

Para inspecionar: coloque um `print(len(lista))` antes da linha que quebra e compare com o índice que está usando.

---

#### `KeyError`

Você tentou acessar uma chave que não existe no dicionário. Diferente de lista, onde o erro é de posição numérica, aqui é de nome.

```text
KeyError: 'nome'
KeyError: 'Nota'   ← chave existe como 'nota', mas você escreveu com N maiúsculo
```

Causas mais comuns:

- Erro de digitação ou de capitalização na chave
- Você assumiu que a chave existia, mas ela ainda não foi inserida

Quando não tem certeza se a chave existe, use `.get()` em vez de `[]`:

```python
valor = dados.get('nome')          # retorna None se não existir
valor = dados.get('nome', 'N/A')   # retorna 'N/A' se não existir
```

---

### Erros de lógica e execução

#### `ZeroDivisionError`

Divisão por zero. Simples, mas aparece em situações não óbvias, quando o divisor vem de um cálculo ou de uma entrada do usuário que pode ser zero.

```text
ZeroDivisionError: division by zero                      ← operador /
ZeroDivisionError: float division by zero                ← operador / com float
ZeroDivisionError: integer division or modulo by zero     ← operador //
ZeroDivisionError: integer modulo by zero                 ← operador %
```

O operador `%` (resto) também lança esse erro quando o divisor é zero, não só `/` e `//` (cada um com sua própria mensagem, como acima). Sempre valide antes de dividir se o divisor pode ser zero.

---

#### `RecursionError`

A função chamou a si mesma vezes demais sem chegar à condição de parada. O Python tem um limite de chamadas recursivas (em torno de 1000) para evitar travar.

```text
RecursionError: maximum recursion depth exceeded
```

Se você está usando recursão propositalmente: verifique se a condição de parada (`if` base) está correta e se ela é alcançada. Se não está usando recursão de propósito, pode ser um loop de chamadas acidental entre funções.

---

### Erros de arquivo

#### `FileNotFoundError`

O arquivo que você tentou abrir não existe no caminho informado, ou o caminho está errado.

```text
FileNotFoundError: [Errno 2] No such file or directory: 'dados.txt'
```

Causas mais comuns:

- O arquivo está em outra pasta e você não especificou o caminho completo
- Erro de digitação no nome do arquivo (incluindo extensão)
- Você está executando o script de uma pasta diferente de onde o arquivo está

Para verificar onde o Python está procurando (uma função que não é ensinada nas aulas, mas que serve exatamente para isso), use:

```python
import os
print(os.getcwd())  # mostra a pasta de onde você rodou o script
```

---

#### `PermissionError`

O arquivo existe, mas o sistema operacional não permite que o Python o abra do jeito que você pediu, geralmente porque você tentou escrever em um arquivo aberto em outro programa, ou não tem permissão de acesso.

```text
PermissionError: [Errno 13] Permission denied: 'resultado.txt'
```

No Windows, isso acontece quando o arquivo está aberto no Excel ou no Bloco de Notas ao mesmo tempo. Feche o arquivo no outro programa antes de rodar o script.

---

#### `ModuleNotFoundError`

Você tentou importar uma biblioteca que não está instalada no ambiente atual.

```text
ModuleNotFoundError: No module named 'pandas'
ModuleNotFoundError: No module named 'numpy'
```

No terminal, instale com `pip install nome_do_modulo`. Se estiver no Colab, use `!pip install nome_do_modulo` em uma célula de código. Para as bibliotecas padrão do Python (`math`, `random`, `os`), esse erro indica erro de digitação no nome do módulo.

---

## Recursos externos

Aqui ficam sugestões que acho que podem agregar bastante à sua jornada de estudos.

### Assistir

- **[Curso em Vídeo: Python](https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6)**: playlist gratuita do Gustavo Guanabara, do zero ao intermediário. Um dos melhores pontos de partida para quem prefere aprender assistindo, as aulas são muito bem apresentadas e de forma extremamente didática.

### Rodar Python sem instalar nada

- **[Google Colab](https://colab.research.google.com/)**: ambiente Python completo no navegador, com suporte a células de código e texto. Os gabaritos deste repositório rodam aqui.
- **[Replit](https://replit.com/)**: editor online para escrever e executar Python direto no navegador. Útil para testar algo rápido ou estudar num computador que não é o seu.

### Referência

- **[W3Schools Python](https://www.w3schools.com/python/)**: referência rápida com exemplos curtos. Bom para consultar sintaxe na hora, sem precisar ler explicações longas.
- **[Documentação oficial do Python](https://docs.python.org/pt-br/3/)**: referência completa da linguagem, em português. Mais técnico, mas indispensável conforme o conteúdo avança.
