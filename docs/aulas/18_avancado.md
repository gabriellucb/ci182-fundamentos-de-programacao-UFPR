# Aula 18: Avançando em Python

Parabéns por chegar até aqui! Esta é a última aula com conteúdo novo do material base. Você já sabe programar, já resolve problema com condicional, laço, lista, dicionário, função, arquivo, classe. O que falta agora são ferramentas que fazem o código que você já sabe escrever ficar mais compacto, mais seguro e mais fácil de ler. Aqui você verá `zip` e `enumerate` (que já apareceram antes e agora ganham o resto da história), compreensões, type hints, tratamento de erros com `try/except`, e por fim boas práticas de estilo com PEP 8.

---

## `zip` e `enumerate`

Dois recursos de iteração que aparecem muito na prática, principalmente quando você tem duas listas que "andam juntas".

### `zip`: percorrer dois iteráveis juntos

Imagina que você tem uma lista de nomes e uma lista de notas, na mesma ordem, e quer imprimir os dois lado a lado:

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 9.2]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
```

`zip` emparelha os elementos na mesma posição. Na primeira iteração você tem `("Ana", 8.5)`, na segunda `("Bruno", 6.0)` e assim por diante.

Sem `zip`, o jeito mais comum de fazer isso é manter um índice manual:

```python
for i in range(len(nomes)):
    print(f"{nomes[i]}: {notas[i]}")
```

Funciona, mas é mais frágil do que parece: toda vez que você mexe numa das duas listas sem mexer na outra (ordena uma, filtra uma, adiciona item só numa delas), o alinhamento quebra, e ele quebra **silenciosamente**: o nome de uma pessoa aparece colado na nota de outra, sem nenhum erro te avisando. `zip` não resolve esse problema de fundo (se as listas já chegarem desalinhadas, ele emparelha errado do mesmo jeito), mas tira o índice manual do meio, que é a forma mais comum de erro: usar `nomes[i]` num lugar e esquecer de trocar pra `notas[i]` logo abaixo.

Se os iteráveis tiverem tamanhos diferentes, `zip` para no menor, sem lançar erro nenhum, mas os elementos extras do maior são silenciosamente ignorados. Veja o "Diego" sumir sem nenhum aviso:

```python
nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [8.5, 6.0, 9.2]

for nome, nota in zip(nomes, notas):
    print(f"{nome}: {nota}")
# Ana: 8.5
# Bruno: 6.0
# Carla: 9.2
```

`notas` só tem 3 itens, então `zip` para aí. Diego nunca aparece, e o Python não reclama de nada: se você não conferir se `len(nomes) == len(notas)` antes, esse tipo de bug passa despercebido.

`zip` também não se limita a dois iteráveis, dá pra emparelhar três ou mais de uma vez:

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 9.2]
turmas = ["A", "B", "A"]

for nome, nota, turma in zip(nomes, notas, turmas):
    print(f"{nome} ({turma}): {nota}")
# Ana (A): 8.5
# Bruno (B): 6.0
# Carla (A): 9.2
```

### `enumerate`: revisão rápida

Você já viu `enumerate()` na [Aula 09](09_listas.md): índice e valor juntos, sem contador manual, com `start` pra ajustar onde a contagem começa. Não vou reensinar aqui, só um lembrete rápido:

```python
ranking = ["Ana", "Carlos", "Beto"]

for pos, nome in enumerate(ranking, start=1):
    print(f"{pos}º lugar: {nome}")
# 1º lugar: Ana
# 2º lugar: Carlos
# 3º lugar: Beto
```

Ele reaparece aqui porque combina muito bem com `zip`, os dois costumam andar juntos na prática. Dá pra colocar um dentro do outro:

```python
for pos, (nome, nota) in enumerate(zip(nomes, notas), start=1):
    print(f"{pos}. {nome}: {nota}")
# 1. Ana: 8.5
# 2. Bruno: 6.0
# 3. Carla: 9.2
```

Repare no parêntese extra em `(nome, nota)`: o `zip` entrega pares, e o `enumerate` embrulha cada par num outro par `(posição, par)`. O `for` desempacota os dois níveis de uma vez: a posição vai pra `pos`, e o par interno já sai desmontado direto em `nome` e `nota`.

---

## Compreensões

Compreensões são uma forma mais compacta de criar listas (e dicionários) a partir de sequências. A ideia já é familiar: você percorre algo e transforma ou filtra cada elemento. A diferença é que o resultado fica em uma linha.

Comparando as duas formas:

```python
# Forma tradicional
quadrados = []
for n in range(1, 6):
    quadrados.append(n ** 2)

# Compreensão de lista, mesmo resultado
quadrados = [n ** 2 for n in range(1, 6)]
print(quadrados)   # [1, 4, 9, 16, 25]
```

A leitura é: "uma lista de `n ** 2` para cada `n` em `range(1, 6)`". A estrutura é sempre `[expressão for variável in iterável]`. O que vem antes do `for` é o que você quer que sobre em cada posição da lista nova; o que vem depois é de onde você está tirando cada `n`.

Você pode adicionar um filtro com `if`, no final:

```python
notas = [7.5, 4.0, 8.5, 3.0, 9.0, 5.5]

aprovados = [nota for nota in notas if nota >= 7]
print(aprovados)   # [7.5, 8.5, 9.0]
```

Isso substitui um loop com `append` + `if` por uma linha só. Quando usar? Quando a transformação e o filtro são simples o suficiente para caber numa linha sem sacrificar a legibilidade. Para lógica mais complexa, um `for` explícito ainda é mais claro, e "mais claro" geralmente ganha de "mais curto".

### Compreensão de dicionário

O mesmo conceito funciona para dicionários, com chaves e valores. Você já viu `zip` lá em cima, então este `zip(nomes, notas)` não é novidade:

```python
nomes = ["Ana", "Bruno", "Carla"]
notas = [8.5, 6.0, 9.2]

turma = {nome: nota for nome, nota in zip(nomes, notas)}
print(turma)   # {'Ana': 8.5, 'Bruno': 6.0, 'Carla': 9.2}
```

A estrutura é parecida com a de lista, só que agora tem dois valores separados por `:` antes do `for`: o primeiro vira chave, o segundo vira valor.

---

## Type hints: indicar tipos sem forçá-los

Type hints são anotações que indicam qual tipo cada variável ou parâmetro espera receber, e qual tipo uma função retorna. Confesso que no começo achava frescura, só decoração no código. Mudei de ideia quando comecei a mexer em projetos com muitos arquivos. Sem anotação, eu tinha que abrir a função e ler o corpo inteiro só pra lembrar o que ela esperava receber; com a anotação, essa informação está bem na cara.

```python
nome:  str   = "Ana"
idade: int   = 20
nota:  float = 8.5
ativo: bool  = True
```

Para funções, você anota os parâmetros e o retorno com `->`:

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)

def saudar(nome: str, formal: bool = False) -> str:
    if formal:
        return f"Bom dia, {nome}."
    return f"Oi, {nome}!"

def imprimir_relatorio(dados: list[str]) -> None:
    for linha in dados:
        print(linha)
```

`-> None` é usada para funções que não retornam nada, só fazem efeitos colaterais como imprimir ou escrever em arquivo.

Agora, o ponto mais importante, que vale repetir: o Python **não verifica isso em tempo de execução**. A anotação é só documentação pra você e pra ferramentas como o VS Code, não é uma trava de segurança. Prova em código, usando a mesma função de cima:

```python
def calcular_media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

`notas: list[float]` promete que essa lista vem cheia de números (`float` ou `int`, que o Python trata como compatível aqui). Chamando do jeito certo, é exatamente isso que ela espera:

```python
print(calcular_media([7.5, 8.0, 9.0]))   # 8.166666666666666
```

Mas nada te impede de quebrar a promessa. Chame a mesma função passando uma lista de textos, o tipo errado segundo a própria anotação:

```python
print(calcular_media(["a", "b"]))   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Repare: o Python não te barrou na entrada da função por causa do `list[float]`, ele deixou a chamada passar de boas. O erro só estourou dois passos depois, dentro do `sum()`, quando ele tentou somar o número `0` (o ponto de partida da soma) com a string `"a"`. E olha que confuso: a mensagem fala de `int` e `str`, não menciona `list[float]` em lugar nenhum, então se você não soubesse que a anotação existia, ia ficar perdido tentando entender de onde veio esse erro. Ou seja: quem garante que os tipos batem de verdade ainda é você, a assinatura só te lembra o que é esperado, ela não impede nada.

O VS Code usa as anotações pra autocompletar com mais precisão e destacar essas inconsistências de tipo enquanto você digita, antes mesmo de rodar. Não é obrigatório usá-las, mas vale pegar o hábito cedo, principalmente quando você começar a trabalhar em projetos com mais de um arquivo, onde você não tem a função inteira na tela pra conferir.

---

## Tratamento de erros: `try / except`

Lembra do `try/except FileNotFoundError` que você já usou pra abrir arquivo lá na [Aula 14](14_arquivos.md)? A estrutura básica já apareceu ali, sem muita explicação, porque você precisava dela pra trabalhar com arquivos antes de ter visto o resto. Chegou a hora de entender de verdade o que está acontecendo.

Erros em tempo de execução são chamados de **exceções**. Em vez de deixar o programa travar, você captura a exceção e decide o que fazer. E tem uma dívida específica que dá pra pagar agora: lembra da validação manual de número que você fez na [Aula 08](08_strings.md), desmontando a string na unha com `isdecimal()` e `split()` pra aceitar float e negativo? Essa aula prometeu que `try/except` seria "a abordagem mais limpa" pra isso, e é:

```python
try:
    numero = float(input("Digite um número: "))
    print(f"Você digitou {numero}")
except ValueError:
    print("Isso não parece um número.")
```

`float()` já aceita inteiro, float, negativo, tudo junto (`"42"`, `"3.14"`, `"-7"`) sem você precisar desmontar sinal e ponto decimal na mão. Se vier algo que não é número (`"abc"`, uma string vazia), o Python levanta `ValueError`, e o `except` pega antes do programa travar. Compare isso com aquele bloco de `if`s encadeados da Aula 08: mesmo resultado, uma fração do código.

Você pode empilhar mais de um `except`, um para cada tipo de erro que quiser tratar de um jeito diferente:

```python
try:
    numero = float(input("Digite um número: "))
    print(10 / numero)
except ValueError:
    print("Isso não é um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except Exception as erro:
    print(f"Algo inesperado aconteceu: {erro}")
```

O Python testa os `except` de cima para baixo e executa o primeiro que bater com o erro ocorrido. `Exception` é a classe base de quase todos os erros: funciona como um "pega tudo", mas só deve ficar por último, senão ele rouba a vez dos `except` mais específicos que viriam depois.

Já que você viu `try/except` e compreensões nesta mesma aula, vale fechar uma pegadinha que gera confusão: não dá pra enfiar um `try/except` dentro de uma compreensão, porque compreensão é uma **expressão** (ela produz um valor), não um bloco de comandos como o `try`. Se tentar converter uma lista de textos pra número assim:

```python
entradas = ["10", "20", "abc"]
numeros = [int(x) for x in entradas]   # quebra no "abc" com ValueError, e não dá pra pôr except aqui dentro
```

O programa quebra assim que chega no item inválido, e não tem como capturar o erro item a item dentro da própria compreensão. Se precisar tratar erro elemento por elemento, duas saídas: escreva uma função separada que faz a conversão com seu próprio `try/except` e chame ela dentro da compreensão, ou desista da compreensão e use um `for` normal.

### `finally`: executar sempre

O bloco `finally` roda independente de ter ocorrido erro ou não, útil para garantir que recursos sejam liberados:

```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    print("Processamento encerrado.")   # roda sempre
```

Mesmo que o arquivo não exista e o `except` seja executado, o `finally` ainda roda depois. (Vale lembrar: o `with` que você já usa pra abrir arquivo desde a Aula 14 já cuida de fechar o arquivo sozinho, então na prática você raramente precisa de um `finally` só pra isso. Ele aparece mais quando o "sempre executar" envolve outra coisa, tipo avisar que a operação terminou.)

### `raise`: lançar seus próprios erros

Você pode criar erros intencionalmente para sinalizar que algo inválido aconteceu, em vez de deixar o programa continuar com um valor que não faz sentido:

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print(e)   # O divisor não pode ser zero.
```

`raise` é útil dentro de funções para garantir que quem chama não passe valores inválidos adiante sem perceber, e para dar uma mensagem de erro clara e específica em vez de deixar o Python lançar um erro genérico lá na frente, longe de onde o problema realmente começou.

---

## Tudo isso dentro de uma classe

Vale reforçar algo que a [Aula 17](17_poo.md) prometeu lá no fechamento dela: nada do que você viu nesta aula é exclusivo de código solto. As mesmas ferramentas funcionam dentro de métodos de classe, incluindo as que você criou lá. Reaproveitando o `Guerreiro` (supondo ele já definido como na Aula 17):

```python
grupo: list[Guerreiro] = [
    Guerreiro("Alexios"),
    Guerreiro("Kassandra"),
]

vivos: list[str] = [g.nome for g in grupo if g.vida() > 0]
print(vivos)   # ['Alexios', 'Kassandra']
```

O type hint `list[Guerreiro]` documenta que é uma lista de personagens, não de números ou textos. A compreensão filtra só quem ainda está de pé, sem precisar de um `for` com `append`.

E o `try/except` que você acabou de ver funciona idêntico dentro de um método, não muda uma vírgula:

```python
class Guerreiro(Personagem):
    # ... __init__ e o resto igual à Aula 17 ...

    def equipar_arma(self, dano_extra):
        try:
            dano_extra = float(dano_extra)
        except ValueError:
            print("Dano precisa ser um número.")
            return
        self.forca += dano_extra
```

A sintaxe não muda nadinha só porque está dentro de uma classe: `try`, `except`, compreensão, type hint, tudo se comporta exatamente igual dentro ou fora de um método. O `self` não interfere em nada disso.

---

## Boas práticas: PEP 8

**PEP 8** é o guia de estilo oficial do Python. Não é uma regra, seu código roda mesmo sem seguir. Mas é a convenção adotada por todo o ecossistema Python: bibliotecas, projetos open source, empresas. Seguir torna seu código legível para qualquer programador Python, mesmo alguém que nunca viu seu projeto antes.

Os pontos principais:

### Nomes

- Variáveis e funções em `snake_case`: `nota_final`, `calcular_media`, `eh_aprovado` (esse é o nome formal que a [Aula 16](16_objetos_classes.md) prometeu te contar aqui: o padrão de minúsculas com underscore que você já vinha usando sem saber que tinha nome)
- Classes em `PascalCase`: `Personagem`, `Guerreiro`
- Constantes em `MAIUSCULO`: `PI`, `TAXA_JUROS`, `MAX_TENTATIVAS`

### Espaçamento

- Espaços ao redor de operadores: `x = a + b`, não `x=a+b`
- Sem espaço antes do parêntese em chamadas: `print("oi")`, não `print ("oi")`
- Linha em branco entre definições de funções e classes

**Exemplo aplicado:**

```python
# Ruim: viola vários pontos do PEP 8
def calcular(x,y,z):
  soma=x+y+z
  return soma/3

# Bom: segue PEP 8
def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    soma = nota1 + nota2 + nota3
    return soma / 3
```

O VS Code com a extensão Python destaca automaticamente algumas violações do PEP 8. Com o tempo, você segue sem nem pensar.

---

Exemplo rodável desta aula: [`exemplos/18_avancado.py`](../exemplos/18_avancado.py)

## Exercício sugerido

Crie um programa que:

1. Leia notas de alunos de um arquivo CSV (use o módulo `csv` da Aula 15).
2. Use uma compreensão de lista para extrair só as notas numéricas.
3. Use `zip` para emparelhar nomes e notas, e `enumerate` para gerar o ranking.
4. Calcule a média usando o módulo `statistics` (também da Aula 15).
5. Salve um relatório em outro arquivo com os aprovados e reprovados.
6. Trate com `try/except` os erros possíveis: arquivo não encontrado, valor inválido no CSV.

> **Resposta do exercício:** [`respostas/18_avancado.py`](../respostas/18_avancado.py)

---

## Exercícios de debug relacionados

| Nível | Arquivo |
| --- | --- |
| Difícil | [`../debug/dificil/03_jogo_forca.py`](../debug/dificil/03_jogo_forca.py) |

Esse é o desafio de encerramento do material base: um jogo da forca completo, com categorias, dificuldade, placar salvo em arquivo entre execuções e ranking, misturando conceitos de quase todas as aulas anteriores (sets, dicionários, classes, arquivos, `try/except`, compreensões). Não há saída fixa para comparar, a palavra é sorteada. Jogue até vencer, até perder, e rode o arquivo duas vezes seguidas: um dos bugs só aparece na segunda execução, depois que o placar já existe salvo.

---

> Terminou o exercício e o debug? Vá para a [despedida](19_despedida.md).
