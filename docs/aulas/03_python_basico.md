# Aula 03: Python Básico

Na [Aula 02](02_introducao.md) você viu o que é um programa, agora você vai escrever o seu. Hoje você vai sair com algo funcionando de verdade: um programa que pede informações do usuário, faz uma conta e responde. Antes disso, a gente precisa cobrir o básico: variáveis, tipos e como o Python pensa sobre dados.

---

## Seu primeiro programa

Todo programador, em toda linguagem, começa com o mesmo programa. Provavelmente você já viu isso em algum lugar. É quase uma tradição. 
Crie um arquivo `main.py` e escreva:

```python
print("Olá, mundo!")
```

Execute no botão ou no terminal com `python3 main.py` e veja a mensagem aparecer na tela.

### Como o `print()` funciona

Esse `print()` é uma **função**, um comando que faz algo. Neste caso, ele exibe o que está entre os parênteses na tela. Funciona com qualquer tipo de dado:

```python
print("Olá, mundo!")   # texto
print(42)              # inteiro
print(3.14)            # decimal
print(True)            # booleano
```

#### Múltiplos valores com vírgula

Quando você passa vários valores separados por vírgula, o `print()` coloca um espaço entre eles automaticamente:

```python
nome = "Maria"
idade = 20
print("Nome:", nome, "| Idade:", idade)   # Nome: Maria | Idade: 20
```

#### Unindo textos com `+`

Você também pode juntar strings antes de exibir usando `+`:

```python
print("Olá, " + nome + "!")   # Olá, Maria!
```

A vírgula é mais prática porque não exige nenhuma conversão de tipo, você passa direto o que quiser. A concatenação com `+` só funciona quando todos os valores são strings. Quando você chegar na **[Aula 05](05_entrada_saida.md)** vai aprender f-strings, que são, na minha opinião, a melhor maneira de montar texto com variáveis.

#### `print()` como ferramenta de debug

Você vai usar `print()` o tempo todo, não só para exibir resultados finais, mas para inspecionar o que está acontecendo enquanto escreve. É a ferramenta de debug mais simples que existe: coloque um `print()` em qualquer variável e você vê o valor dela naquele ponto da execução.

```python
pontos = 0
print("antes:", pontos)    # antes: 0
pontos = pontos + 10
print("depois:", pontos)   # depois: 10
```

Na **[Aula 05](05_entrada_saida.md)** você vai ver como formatar a saída: controlar casas decimais, alinhar colunas e usar f-strings de verdade.

---

## Variáveis

Quando um programa precisa guardar uma informação para usar depois, ele usa uma **variável**. Pense nela como uma caixa com etiqueta: você coloca um valor dentro e usa o nome da etiqueta para acessar quando precisar.

```python
nome = "Maria"
idade = 20
altura = 1.70
```

A linha `nome = "Maria"` faz três coisas: cria a caixa, cola a etiqueta `nome` nela e coloca o valor `"Maria"` dentro.

```text
 nome = "Maria"
  │         │
  │         └── valor guardado dentro da caixa
  └── etiqueta colada na caixa (o nome que você usa para acessar)
```

Em Python, você não precisa declarar o tipo da variável antes de usá-la, o Python descobre sozinho. Isso é diferente de linguagens como C ou Java, onde você precisa escrever algo como `int idade = 20`.

Eu comecei a programar em Algoritmos e Estruturas de Dados I, materia do primeiro período de Ciência da Computação onde ensinam em Pascal. Depois C. As duas obrigam a declarar o tipo antes de usar a variável `int`, `float`, `char`. Quando comecei a usar Python, ficou até estranho não ter isso. Parecia que faltava algo. Com o tempo você percebe que é uma confortabilidade, não uma falta.

Você pode mudar o valor de uma variável a qualquer momento, simplesmente atribuindo um novo valor:

```python
pontos = 0
print(pontos)       # 0

pontos = pontos + 10
print(pontos)       # 10

pontos = pontos + 5
print(pontos)       # 15
```

A linha `pontos = pontos + 10` pode parecer estranha matematicamente, mas em programação significa: "pegue o valor atual de `pontos`, some 10, e guarde o resultado de volta em `pontos`".

### Regras para nomear variáveis

Python tem algumas regras que você precisa seguir, senão o programa nem roda:

- **Comece com letra ou `_`**, nunca com número. `nota1` é válido, `1nota` não.
- **Sem espaços**, use `_` para separar palavras: `nota_final`, `nome_completo`, `preco_com_desconto`.
- **Não use palavras reservadas** como `if`, `while`, `for`, `def`, `class`, `True`, `False`. Essas palavras têm significado especial para o Python.

Além das regras obrigatórias, existe uma convenção: use nomes que descrevam o que a variável guarda. `x` e `y` funcionam em exercícios matemáticos, mas `altura` e `quantidade` são muito mais claros num programa de verdade.

---

## Tipos de dados básicos

Cada valor em Python tem um **tipo**. O tipo define o que você pode fazer com aquele valor. Os tipos principais que você vai usar desde o começo:

| Tipo | O que é | Exemplos |
|------|---------|----------|
| `int` | Número inteiro, sem decimal | `5`, `-10`, `0`, `1000` |
| `float` | Número com parte decimal | `3.14`, `-2.5`, `1.0` |
| `str` | Texto (string) | `"Python"`, `'Olá'`, `"123"` |
| `bool` | Verdadeiro ou falso | `True`, `False` |
| `None` | Ausência de valor | `None` |

Alguns detalhes que valem atenção agora:

`"123"` e `123` são coisas diferentes, o primeiro é texto, o segundo é número. Você não pode somar `"123" + 1`. Parece óbvio escrito assim, mas é um dos erros mais comuns no começo.

`bool` é a base de todo `if` e `while`, você vai usar bastante a partir da **[Aula 06 (Condicionais)](06_condicionais.md)**.

`None` aparece quando uma variável precisa existir mas ainda não tem valor atribuído. É diferente de `0` (que é o número zero) e de `""` (texto sem caracteres): `None` é literalmente a ausência de valor. Tem uma explicação mais completa com exemplos no [FAQ](../extras/faq.md#o-que-é-none-é-o-mesmo-que-0-ou-string-vazia).

### Quando usar cada um

A regra prática: use `int` para contagens, idades, índices, anos, qualquer coisa que não vai ter vírgula. Use `float` para medidas, preços, médias, qualquer coisa que naturalmente pode ser decimal.

Floats carregam uma pequena imprecisão que raramente aparece no dia a dia, mas que importa quando você começa a usar o operador `==` para comparar resultados. Isso vai fazer muito mais sentido na **[Aula 04](04_operadores.md)** e tem uma explicação detalhada no [FAQ](../extras/faq.md#por-que-01--02-não-é-03).

Para saber o tipo de qualquer valor ou variável, use `type()`:

```python
quantidade = 10
mensagem = "olá"
aprovado = True

print(type(quantidade))  # <class 'int'>
print(type(mensagem))    # <class 'str'>
print(type(aprovado))    # <class 'bool'>
print(type(3.14))        # <class 'float'>
print(type(None))        # <class 'NoneType'>
```

---

## Comentários

Comentários são linhas que o Python ignora completamente na hora de executar. Eles existem para você e para outras pessoas que lerem o seu código.

```python
# Isso é um comentário. O Python não executa esta linha.
print("Olá")  # você também pode comentar no final de uma linha de código
```

Use comentários para explicar o **porquê** de uma decisão, não o **o quê**, o código em si já diz o que está fazendo. Um comentário útil é aquele que explica algo que não é óbvio:

```python
taxa = 0.1        # taxa de desconto vigente até dezembro

# multiplica por 100 para exibir como percentual
print(taxa * 100)
```

Comentários também são úteis para desativar temporariamente uma linha enquanto você testa algo:

```python
# print("linha desativada para testar outra coisa")
print("essa linha ainda roda")
```

---

## Recebendo dados do usuário

O `input()` faz três coisas em sequência: exibe uma mensagem (o "prompt") na tela, pausa o programa esperando o usuário digitar, e quando o usuário pressiona Enter devolve tudo que foi digitado como uma string guardada numa variável.

```python
nome = input("Digite seu nome: ")
print("Olá,", nome, "!")
```

Quando você rodar isso, vai aparecer `Digite seu nome:` na tela e o programa vai ficar parado esperando. Você digita, pressiona Enter, e o programa continua com o valor em `nome`.

O texto que você passa entre os parênteses é apenas a mensagem exibida para o usuário, ele não afeta o que é retornado. Você pode chamar `input()` quantas vezes precisar:

```python
nome   = input("Nome: ")
cidade = input("Cidade: ")
print("Bem-vindo,", nome, "de", cidade + "!")
```

> **Regra fundamental:** tudo que vem do `input()` é sempre uma `str`, texto. Mesmo que o usuário digite `2`, o Python recebe isso como o texto `"2"`, não o número `2`.

Se precisar usar o valor em cálculos, é obrigatório converter:

```python
idade  = int(input("Digite sua idade: "))      # int() converte para inteiro
altura = float(input("Digite sua altura: "))   # float() converte para decimal
```

O que acontece se você esquecer a conversão e tentar fazer uma conta? O Python vai mostrar um erro parecido com 

`TypeError: can only concatenate str (not "int") to str` 

Agora que você sabe o motivo, fica mais fácil entender o que corrigir.

Uma coisa que vi na monitoria: a pessoa chega com um bug e a solução está escrita palavra por palavra na mensagem de erro. `NameError: name 'nota' is not defined`: a variável não foi definida. `TypeError: unsupported operand type(s) for +: 'int' and 'str'`: você está tentando somar número com texto.

O Python quase sempre diz exatamente o que deu errado e em qual linha. O hábito de ler o erro antes de entrar em pânico resolve a maioria dos problemas sozinho.

---

## Operações básicas com números

Com variáveis numéricas você pode fazer cálculos. As básicas você já conhece. Essas são as principais:

```python
soma        = 10 + 5     # 15
subtracao   = 10 - 3     # 7
produto     = 4 * 3      # 12
divisao     = 10 / 4     # 2.5   (divisão sempre retorna float)
divisao_int = 10 // 4    # 2     (descarta o decimal, só o inteiro)
resto       = 10 % 3     # 1     (resto da divisão, módulo)
potencia    = 2 ** 8     # 256   (2 elevado a 8)
```

As que costumam causar dúvida:

- **`/` vs `//`**: `10 / 3` resulta `3.333...`; `10 // 3` resulta `3`. Use `//` quando quiser só a parte inteira.
- **`%` (módulo)**: retorna o *resto* da divisão. `10 % 3` é `1` porque `10 = 3×3 + 1`. Muito usado para verificar se um número é par (`numero % 2 == 0`) ou para trabalhar com ciclos.

Na **[Aula 04](04_operadores.md)** vamos explorar todos os operadores com mais detalhes, incluindo os que comparam e combinam valores.

---

## Antes do exercício tente isso

Abra o terminal Python e digite exatamente isso:

```python
import this
```

Vai aparecer o **Zen of Python**: 19 princípios de design da linguagem, escritos por Tim Peters, colaborador histórico do Python. Alguns que acho interessante:

- *Beautiful is better than ugly.*: Bonito é melhor que feio. Código bem escrito é mais fácil de ler, entender e manter. Feio funciona, mas cansa.
- *Explicit is better than implicit.*: Explícito é melhor que implícito. Se o seu código precisa de uma explicação mental complexa para entender o que faz, ele provavelmente pode ser mais claro.
- *Simple is better than complex.*: Simples é melhor que complexo. Quando dá para resolver de um jeito direto, não complique. Complexidade sem necessidade é um problema, não uma virtude.
- *Errors should never pass silently.*: Erros nunca devem passar em silêncio. Se algo deu errado, o programa deve avisar, não fingir que está tudo bem.

Não precisa decorar nada. É só curioso que os criadores tenham colocado uma filosofia de vida dentro da própria linguagem, acessível com um `import`. E que essa filosofia toda esteja num módulo chamado `this`.

---

Exemplo rodável desta aula: [`exemplos/03_python_basico.py`](../exemplos/03_python_basico.py)

## Exercício prático

Coloque tudo da aula junto num único programa:

1. Pergunte o nome do usuário.
2. Pergunte a idade atual dele.
3. Calcule em que ano ele vai fazer 30 anos.
4. Exiba uma resposta simpática com essas informações.

Dica para o cálculo: se ele tem `idade` anos hoje e o ano atual é `2026`, em quantos anos ele terá 30? E 2026 mais esses anos dá qual ano?

Teste com idades diferentes, inclusive com uma idade maior que 30, e veja o que acontece. Se aparecer um erro em algum momento, leia a mensagem com calma: ela sempre diz o tipo do problema e aponta a linha onde ocorreu.

---

## Exercício de debug relacionado

**Nível fácil · Tema: tipos de dados**
[`debug/facil/01_tipos.py`](../debug/facil/01_tipos.py)

Tente encontrar e corrigir sem rodar o arquivo. Depois rode e compare com a saída esperada descrita no cabeçalho.

> **Resposta do exercício prático:** [`respostas/03_python_basico.py`](../respostas/03_python_basico.py)
