# Aula 08: Strings

Strings são textos, e texto está em todo lugar: nomes, mensagens, arquivos, URLs, CPFs, CEPs. Você já usou strings desde a primeira aula, mas até agora tratou elas como caixas opacas. Nesta aula vamos abrir essa caixa e ver tudo que dá para fazer com texto em Python.

---

## Criando strings

Você já sabe que strings ficam entre aspas. O Python aceita aspas simples ou duplas, o resultado é idêntico:

```python
texto1 = "Olá, mundo!"
texto2 = 'Python é legal'
```

A escolha importa quando o próprio texto contém aspas:

```python
frase1 = "Ela disse 'oi'."    # aspas simples dentro de duplas
frase2 = 'Ele disse "tchau".' # aspas duplas dentro de simples

# Se precisar misturar, use \:
frase3 = "Ela disse \"olá\"."
```

### Strings de múltiplas linhas

Use três aspas (`"""` ou `'''`) para criar strings que ocupam mais de uma linha:

```python
mensagem = """Olá!

Este é um texto
com várias linhas.
"""

print(mensagem)
```

O Python preserva todas as quebras de linha exatamente como você escreveu. Eu usava isso pra montar o cabeçalho de trabalhos, aquele bloco com nome, GRR e enunciado, sem ter que escrever um `print` por linha.

Aspas triplas têm ainda outro uso bem comum, que você vai encontrar na [Aula 13 (Funções)](13_funcoes.md#documentando-funções-com-docstrings): a **docstring**, um texto colocado para explicar o que a função faz. É a forma padrão de documentar código em Python, então vale já guardar o nome.

---

## Concatenação e repetição

Isso aqui você já viu. Concatenação com `+` apareceu lá na **[Aula 03](03_python_basico.md)** e foi detalhada na **[Aula 05](05_entrada_saida.md)**, junto com a repetição com `*`. Então é só um lembrete rápido, sem reaprofundar:

```python
saudacao  = "Olá, " + "João" + "!"   # "Olá, João!"  (junta com +)
separador = "-" * 30                  # "------------------------------"  (repete com *)
eco       = "ha" * 3                  # "hahaha"
```

> **Só não esqueça da armadilha:** `+` só funciona entre strings. Misturar com número dá `TypeError`, e aí você converte com `str(numero)` ou, melhor ainda, usa f-string (`f"Tenho {idade} anos."`), do jeito que a Aula 05 mostrou.

---

## Acessando caracteres: indexação

Uma string é uma **sequência ordenada de caracteres**: cada letra tem um lugar fixo, e esse lugar tem um número chamado **índice**. Para pegar o caractere de uma posição, você escreve o nome da variável e, logo depois, o índice entre colchetes: `palavra[índice]`.

Assim como na maioria das coisas da programação, a contagem **começa em `0`**, não em `1`. O primeiro caractere está na posição `0`, o segundo na `1`, e assim por diante. Parece estranho no começo, mas tem um motivo de verdade, e ele está explicado no [FAQ](../extras/faq.md#por-que-a-contagem-começa-em-0-e-não-em-1).

```
 P  y  t  h  o  n
 0  1  2  3  4  5   ← índices positivos (da esquerda)
-6 -5 -4 -3 -2 -1   ← índices negativos (da direita)
```

Lendo o desenho: o `P` está na posição `0`, o `y` na `1`, e o último caractere, o `n`, está na posição `5`. Repare que, numa palavra de 6 letras, o maior índice é `5` e não `6`. Como a contagem começou em `0`, o último índice é sempre o **tamanho menos 1**.

A segunda linha do desenho são os **índices negativos**, que contam de trás para frente: `-1` é o último caractere, `-2` o penúltimo, e assim por diante. A vantagem é não precisar saber o tamanho da string para chegar no fim. `palavra[-1]` sempre devolve a última letra, tenha a palavra 6 ou 600 caracteres. Sem isso, você teria que escrever `palavra[len(palavra) - 1]`, que faz a mesma coisa de um jeito mais extenso.

```python
palavra = "Python"

print(palavra[0])    # P  (primeiro caractere)
print(palavra[1])    # y
print(palavra[5])    # n  (último, índice = tamanho - 1)
print(palavra[-1])   # n  (último, pelo índice negativo)
print(palavra[-2])   # o  (penúltimo)
```

Se você pedir um índice que não existe, maior que o último ou negativo demais, o Python para o programa com um `IndexError`:

```python
palavra = "Python"
print(palavra[10])   # IndexError: string index out of range
```

Esse erro aparece bastante quando você percorre a string num laço e o contador passa do fim sem querer. Guardar que **o último índice é `len(palavra) - 1`** já evita a maioria desses tropeços.

---

## Fatiamento: pegando pedaços

Além de acessar um caractere por vez, você pode extrair **trechos** de uma string usando a sintaxe `[início:fim]`. O `início` é incluído, o `fim` é **excluído**, o mesmo comportamento do `range()` que você viu na aula anterior.

Tem um jeito de pensar nisso que faz o "fim excluído" fazer um pouco mais de sentido: imagine que os números não ficam *sobre* as letras, e sim nas **fendas entre elas**. Um fatiamento `[início:fim]` recorta tudo que está entre a "estaca" `início` e a "estaca" `fim`:

```
   C   O   M   P   U   T   A   D   O   R
 0   1   2   3   4   5   6   7   8   9   10
```

```python
texto = "COMPUTADOR"

print(texto[0:4])   # "COMP"    (da estaca 0 até a 4: pega C, O, M, P)
print(texto[4:10])  # "UTADOR"  (da estaca 4 até a 10: pega U, T, A, D, O, R)
```

Olhando o desenho dá pra ler o `[0:4]` direto: comece na fenda 0, pare na fenda 4, leve o que estiver no meio. Por isso a letra do índice 4 (`U`) **não** entra no primeiro fatiamento, ela está depois da estaca onde você parou.

Quando você omite o início ou o fim, o Python usa o começo ou o final da string:

```python
print(texto[:4])    # "COMP"        (do começo até a estaca 4, excluída)
print(texto[4:])    # "UTADOR"      (da estaca 4 até o final)
print(texto[:])     # "COMPUTADOR"  (cópia completa)
```

### O terceiro parâmetro: passo

Assim como o `range(início, fim, passo)`, o fatiamento aceita um terceiro parâmetro que define de quantos em quantos caracteres pular:

```python
texto = "COMPUTADOR"

print(texto[::2])    # "CMUAO"       (um sim, um não, passo 2)
print(texto[::-1])   # "RODATUPMOC"  (passo -1 anda de trás pra frente e inverte)
print(texto[1::2])   # "OPTDR"       (começa no índice 1, um sim um não)
```

O truque `[::-1]` para inverter uma string é muito comum, vale guardar. (É uma boa usar em algum exercício que pede para verificar se uma palavra é palíndromo: `palavra == palavra[::-1]`.)

---

## Comprimento com `len()`

`len()` é a primeira função embutida nova desta aula. *Embutida* quer dizer que já vem pronta no Python, igual ao `print()` e ao `input()` que você já usa: não precisa instalar nem definir nada, é só chamar. O nome vem de *length* (comprimento, em inglês). Você coloca algo dentro dos parênteses e ela devolve o **tamanho** desse algo. Numa string, esse tamanho é o número de caracteres, contando espaços e pontuação:

```python
print(len("Python"))       # 6
print(len("Olá, mundo!"))  # 11  (conta a vírgula, o espaço e o !)
print(len(""))             # 0   (string vazia)
print(len("  "))           # 2   (dois espaços contam!)
```

E o `len()` não para nas strings: ele é um dos comandos que você mais vai usar com **listas**, lá na [Aula 09](09_listas.md), para descobrir quantos itens uma lista tem. A ideia é a mesma, muda só o que está sendo medido.

`len()` é muito usado junto com `range()` para percorrer uma string por índice. Use quando precisar saber **onde** cada caractere está:

```python
palavra = "Python"
for i in range(len(palavra)):
    print(f"[{i}] = {palavra[i]}")
# [0] = P
# [1] = y
# ...
```

Quando não precisar da posição, só do caractere em si, dá para iterar direto, sem passar pelo índice:

```python
for letra in palavra:
    print(letra)
# P
# y
# t
# ...
```

A regra prática: use `range(len())` quando o **número da posição** importa. Use `for letra in palavra` quando quiser simplesmente percorrer os caracteres um a um, é mais legível e é o padrão que você vai ver com muito mais frequência quando chegar em listas (Aula 09).

---

## Verificando se algo está dentro: `in` e `not in`

> Você já viu `in` e `not in` na **[Aula 04](04_operadores.md)**, onde eles foram apresentados com strings. Rapidão pra refrescar:

```python
frase = "Python é Top"

print("Python" in frase)      # True
print("Java" in frase)        # False
print("Top" in frase)         # True
print("PYTHON" in frase)      # False (maiúsculas importam!)
```

Para ignorar maiúsculas/minúsculas na verificação, converta ambos para o mesmo case:

```python
if "python" in frase.lower():
    print("Menciona Python!")
```

Se esse `.lower()` pareceu familiar, é porque ele já apareceu na **[Aula 06](06_condicionais.md)** num exemplo de comparação de entrada, mas sem explicação de como funciona. Agora que chegamos em strings de verdade, dá pra ver o quadro completo: `.lower()` e `.upper()` são **métodos de string**, e esse é exatamente o próximo assunto.

---

## Métodos de string

Métodos existem em todos os tipos de dado do Python, não só em strings. Um **método** é uma função que pertence a um objeto específico. Você chama com um ponto depois da variável:

```python
texto = "python"
texto.upper()   # chama o método upper() que pertence à string texto
```

A diferença do `len()` é que ele é uma função independente, você passa a string para dentro dos parênteses. Já `texto.upper()` é um método: a própria string sabe como se transformar em maiúsculo, e você só pede pra ela fazer isso.

Mais pra frente você vai ver métodos de listas, dicionários e outros tipos. A **[Aula 16: Objetos e Classes](16_objetos_classes.md)** explica em profundidade de onde vêm os métodos, o que exatamente é um "objeto" e como criar os seus próprios. Por enquanto, a sintaxe é sempre `objeto.metodo()`. Vamos ver os métodos das strings:

### Mudando capitalização

Você já encontrou `.lower()` na **[Aula 06](06_condicionais.md)** e logo antes aqui na seção do `in`, mas nunca com explicação de onde veio. São quatro métodos nessa família: `.upper()` e `.lower()` (tudo maiúsculo / tudo minúsculo) você vai usar o tempo todo; `.capitalize()` e `.title()` aparecem menos, mas são úteis para formatar nomes e títulos:

```python
frase = "python É incrível"

print(frase.upper())       # "PYTHON É INCRÍVEL"     (tudo maiúsculo)
print(frase.lower())       # "python é incrível"     (tudo minúsculo)
print(frase.capitalize())  # "Python é incrível"     (só primeira letra maiúscula)
print(frase.title())       # "Python É Incrível"     (primeira letra de cada palavra)
```

O uso mais comum de `.lower()` é na comparação de entradas do usuário, você não sabe se ele vai digitar "Sim", "SIM" ou "sim":

```python
resposta = input("Continuar? (s/n): ").lower()   # normaliza antes de comparar

if resposta == "s":
    print("Continuando...")
```

### Removendo espaços: `strip()`

`strip()` remove espaços (e quebras de linha) das **bordas** da string. Muito útil para limpar entradas do usuário, que muitas vezes digitam espaços sem querer:

```python
entrada = "  João Silva  "

print(entrada.strip())    # "João Silva"   (remove dos dois lados)
print(entrada.lstrip())   # "João Silva  " (só da esquerda)
print(entrada.rstrip())   # "  João Silva" (só da direita)
```

```python
nome = input("Seu nome: ").strip()   # boa prática: limpar logo na leitura
```

### Substituindo partes: `replace()`

`replace(antigo, novo)` retorna uma nova string com todas as ocorrências de `antigo` trocadas por `novo`:

```python
frase = "Eu gosto de gato. Gato é legal."
print(frase.replace("gato", "cachorro"))
# "Eu gosto de cachorro. Gato é legal."  (só substituiu minúsculo!)
```

Repare que `replace()` é case-sensitive: "gato" foi substituído, mas "Gato" não. Se quiser substituir todos independentemente do case, converta primeiro ou faça dois `replace()`.

Você pode encadear vários `replace()` na mesma linha, cada um recebe o resultado do anterior:

```python
texto = "a,b;c|d"
texto = texto.replace(";", ",").replace("|", ",")
print(texto)   # "a,b,c,d"
```

Um bom exemplo de encadeamento é a conversão para o formato numérico brasileiro, prometida na Aula 05.

O problema: temos `"12,500.50"` e queremos `"12.500,50"`, trocar vírgula por ponto e ponto por vírgula. A tentativa direta seria fazer dois `replace()`:

```python
# ERRADO
"12,500.50".replace(",", ".").replace(".", ",")
# Passo 1: troca vírgula por ponto → "12.500.50"  (ok até aqui)
# Passo 2: troca ponto por vírgula → "12,500,50"  (ERRADO, trocou tudo!)
```

No passo 2, o Python não sabe distinguir o ponto que era vírgula do ponto que era decimal, todos viram vírgula. O resultado tem vírgula no lugar errado.

A solução é usar um caractere temporário que **não existe na string original** como ponte:

```python
salario = 12500.50
americano = f"{salario:,.2f}"   # "12,500.50"

brasileiro = (americano
    .replace(",", "X")   # "12X500.50"  (salva as vírgulas como X)
    .replace(".", ",")   # "12X500,50"  (converte os pontos em vírgula)
    .replace("X", ".")   # "12.500,50"  (restaura os X como ponto)
)

print(f"R$ {brasileiro}")   # R$ 12.500,50
```

O `X` age como um auxiliar: ao fazer a segunda substituição, o Python não confunde vírgulas originais com pontos porque elas já foram substituídas por `X`. Na terceira etapa, o `X` vira ponto. Qualquer caractere que não apareça no número funciona: `X`, `#`, `@`.

### Dividindo e juntando: `split()` e `join()`

`split()` divide uma string em uma **lista de partes**, quebrando onde encontrar o separador:

```python
data = "2026-05-22"
partes = data.split("-")
print(partes)        # ['2026', '05', '22']
print(partes[0])     # '2026'  (ano)
print(partes[1])     # '05'    (mês)
print(partes[2])     # '22'    (dia)
```

Lista é assunto da [Aula 09](09_listas.md); por ora, pense numa fila de pedaços que você acessa por índice, igual fez com os caracteres da string, `partes[0]` é o primeiro, `partes[2]` é o terceiro.

Sem argumento, `split()` quebra nos espaços (e ignora espaços extras):

```python
frase = "  olá   mundo  "
print(frase.split())   # ['olá', 'mundo']  (limpa espaços automaticamente)
```

`join()` faz o inverso: recebe uma lista e junta tudo em uma string, colocando o separador entre cada item:

```python
palavras = ["maçã", "banana", "laranja"]

print(", ".join(palavras))    # "maçã, banana, laranja"
print(" | ".join(palavras))   # "maçã | banana | laranja"
print("".join(palavras))      # "maçãbananalaranja"  (sem separador)
```

`split()` e `join()` são caminhos opostos da mesma estrada, um desmonta, o outro remonta:

```
            split("-")
"2026-05-22"  ───────────▶  ['2026', '05', '22']
              ◀───────────
            "-".join(...)
```

`join()` tem uma sintaxe invertida em relação ao que parece intuitivo, você chama o método no **separador**, não na lista. Vai estranhar no começo, mas logo acostuma.

### Encontrando texto: `find()` e `count()`

`find(trecho)` retorna o índice onde o trecho começa pela primeira vez. Se não encontrar, retorna `-1`:

```python
email = "joao@gmail.com"

print(email.find("@"))     # 4  (@ está na posição 4)
print(email.find("gmail")) # 5  ("gmail" começa na posição 5)
print(email.find("yahoo")) # -1 (não encontrou)
```

O retorno de `-1` é conveniente para verificar existência:

```python
if email.find("@") == -1:
    print("E-mail inválido, falta o @")
```

`count(trecho)` conta quantas vezes o trecho aparece:

```python
frase = "banana"
print(frase.count("a"))    # 3
print(frase.count("na"))   # 2
```

### Verificando o início e o fim: `startswith()` e `endswith()`

`startswith(prefixo)` e `endswith(sufixo)` verificam se a string começa ou termina com determinado texto, retornando `True` ou `False`. São essencialmente um `in` mais específico: em vez de procurar em qualquer posição, você ancora a busca no começo ou no fim.

```python
arquivo = "relatorio_2026.pdf"

print(arquivo.startswith("relatorio"))   # True
print(arquivo.endswith(".pdf"))          # True
print(arquivo.endswith(".xlsx"))         # False
```

O uso mais comum de `endswith()` é checar a extensão de um arquivo, quando você trabalhar com leitura de arquivos na **[Aula 14](14_arquivos.md)**, vai querer confirmar que está abrindo um `.txt` e não um `.pdf` antes de tentar processar. Já `startswith()` aparece bastante para filtrar linhas de texto: imagine ler um arquivo de configuração e ignorar tudo que começa com `#` (comentário):

```python
linha = "# isso é um comentário"

if not linha.startswith("#"):
    print("Processar:", linha)
```

Dá pra fazer o mesmo com `find()` ou `in`, mas `startswith()` e `endswith()` deixam a intenção mais clara, quem lê o código entende na hora o que está sendo verificado.

### Verificando o conteúdo: `isalpha()`, `isalnum()` e `isdigit()`

Esses métodos fazem perguntas sobre o conteúdo da string e respondem com `True` ou `False`, muito úteis pra validar o que o usuário digitou antes de processar. Detalhe: string vazia sempre retorna `False` em todos eles.

**`isalpha()`**: a string contém só letras?

```python
print("Python".isalpha())    # True
print("Python3".isalpha())   # False (tem número)
print("Olá".isalpha())       # True  (letras acentuadas contam)
print("Olá!".isalpha())      # False (! não é letra)
```

Dá pra usar quando você pede o nome de alguém e quer barrar um `João123`.

**`isalnum()`**: a string contém só letras e/ou números (sem espaço ou pontuação)?

```python
print("Python3".isalnum())   # True
print("Olá!".isalnum())      # False (! não é letra nem número)
print("abc 123".isalnum())   # False (espaço não é letra nem número)
```

Serve pra checar um login ou um código de matrícula, onde letra e número valem mas espaço e `@` não.

**Verificando dígitos: `isdecimal()`, `isdigit()` e `isnumeric()`**

> **Você já usou `isdigit()` na Aula 07** na validação de entrada, é o mais comum. Use **`isdecimal()`** quando quiser ter certeza que é só inteiro positivo: ela é a mais restrita das três. Nenhuma aceita ponto, vírgula, sinal de menos ou espaço:

```python
print("12345".isdecimal())  # True
print("3.14".isdecimal())   # False (ponto decimal não é dígito)
print("-5".isdecimal())     # False (sinal de menos não é dígito)
print("".isdecimal())       # False (string vazia)
```

Python tem métodos nessa família (`isdigit()` e `isnumeric()`) que diferem em quais caracteres Unicode aceitam, mas pra disciplina você nunca vai precisar dessa distinção (pelo menos nunca vi exercícios que pedem verificação de Unicode). Se a curiosidade bater, tem o detalhe completo no [FAQ](../extras/faq.md#isdecimal-vs-isdigit-vs-isnumeric).

Nenhum dos três funciona para floats ou negativos. Para validar esses casos, a abordagem mais limpa é `try/except`, que você vai ver na **[Aula 18](18_avancado.md)**.

> **Se ainda não chegou lá (ou o professor não quer que use):** dá pra validar só com o que você já sabe. A ideia é desmontar o número manualmente antes de perguntar se é dígito:
>
> ```python
> # inteiro negativo: tira o sinal e confere o resto
> numero = "-42"
> if numero.startswith("-") and numero[1:].isdecimal():
>     print("inteiro negativo válido")
>
> # float positivo: parte antes e depois do ponto precisam ser dígitos
> numero = "3.14"
> partes = numero.split(".")
> if len(partes) == 2 and partes[0].isdecimal() and partes[1].isdecimal():
>     print("float positivo válido")
>
> # float negativo: tira o sinal, depois aplica a mesma lógica do float
> numero = "-3.14"
> sem_sinal = numero[1:] if numero.startswith("-") else numero
> partes = sem_sinal.split(".")
> if len(partes) == 2 and partes[0].isdecimal() and partes[1].isdecimal():
>     print("float negativo válido")
> ```
>
> Juntando tudo num único "é número?" que cobre todos os casos:
>
> ```python
> numero = input("Digite um número: ").strip()
> sem_sinal = numero[1:] if numero.startswith("-") else numero
> partes    = sem_sinal.split(".")
>
> eh_inteiro = sem_sinal.isdecimal()
> eh_float   = len(partes) == 2 and partes[0].isdecimal() and partes[1].isdecimal()
>
> if eh_inteiro or eh_float:
>     print("número válido!")
> else:
>     print("isso não parece um número")
> ```
>
> Funciona para inteiro positivo (`"42"`), inteiro negativo (`"-42"`), float positivo (`"3.14"`) e float negativo (`"-3.14"`). Só não aceita notação científica (`"1e5"`) ou vírgula como separador decimal, mas esses casos são raros em exercícios da disciplina.

---

## Strings são imutáveis

Em Python, uma vez criada, a string **não pode ser alterada**. Qualquer tentativa de modificar um caractere diretamente dá erro:

```python
palavra = "Python"
palavra[0] = "J"   # TypeError: 'str' object does not support item assignment
```

Comparando com listas, que você vai ver na [Aula 09](09_listas.md), onde `lista[0] = "novo"` funciona sem problema porque listas são **mutáveis**: você edita no lugar. Strings não. É uma decisão de design do Python: strings imutáveis são mais seguras e eficientes internamente. Na prática, isso quase nunca atrapalha, só lembra que, pra "mexer" numa string, você cria uma nova a partir dela:

```python
palavra = "Python"
nova = "J" + palavra[1:]   # "J" + "ython"
print(nova)                # "Jython"
print(palavra)             # "Python"  (original intacta)
```

### Métodos não modificam: eles retornam

Esse comportamento imutável vale para todos os métodos. `.upper()`, `.replace()`, `.strip()`, nenhum deles altera a string original. Eles devolvem uma **nova string** com as modificações:

```python
texto = "python"

texto.upper()      # o resultado existe por uma fração de segundo e é descartado
print(texto)       # "python"  (nada mudou)

texto = texto.upper()   # agora o resultado é capturado de volta na variável
print(texto)            # "PYTHON"
```

Se chamou um método e "não funcionou", provavelmente esqueceu de reatribuir.

---

## Antes de continuar: cuidado com texto que quebra

A partir daqui vamos tratar as coisas mais como "no mundo real", e o mundo real manda entrada bagunçada. O usuário aperta Enter sem digitar nada, cola um espaço no fim, escreve "abc" onde você esperava um número. Até agora a gente quase não se preocupou com isso; daqui pra frente vale começar a tomar esse cuidado.

A boa notícia é que vários métodos desta aula servem justamente para **se defender antes de o programa quebrar** Em vez de deixar o erro acontecer, você confere primeiro e decide o que fazer. Três armadilhas clássicas e como blindar cada uma:

| O que pode dar ruim | Por que quebra | Como blindar antes |
|---------------------|----------------|--------------------|
| `int(texto)` com texto não-numérico | `"abc"` ou `""` viram `ValueError` e o programa morre | Cheque `texto.isdecimal()` antes de converter |
| `texto[i]` com `i` grande demais | índice fora da faixa da `IndexError` | Cheque `i < len(texto)` antes de indexar |
| Comparar entrada "crua" do usuário | um espaço ou maiúscula invisível faz `== "s"` falhar | Limpe com `.strip().lower()` na leitura |

Repare que o jeito de defender é sempre o mesmo: **perguntar antes de agir**. Em vez de mandar converter e torcer, você primeiro confirma que dá certo.

```python
idade = input("Sua idade: ").strip()   # tira espaço sobrando

if idade.isdecimal():                   # só converte se for mesmo número
    print(f"Ano que vem você faz {int(idade) + 1}.")
else:
    print("Isso não parece um número válido. Tenta de novo!")
```

Sem o `if`, digitar "vinte" (ou só dar Enter) derrubaria o programa com um `ValueError` feio. Com ele, você assume o controle e responde com uma mensagem amigável.

> **Atenção ao limite do `isdecimal()`:** ele só aprova **inteiros positivos**. Para aceitar negativos (`-5`) ou casas decimais (`3.14`), faça como foi mostrado anteriormente ou tente capturar o erro com `try/except`, que você vai ver na [Aula 18](18_avancado.md).

---

Exemplo rodável desta aula: [`exemplos/08_strings.py`](../exemplos/08_strings.py)

## Exercício sugerido

Peça uma frase ao usuário e exiba:
- a frase toda em maiúsculas;
- a frase toda em minúsculas;
- o número total de **letras** (sem contar os espaços e pontuação);
- a primeira palavra;
- quantas vezes a letra "a" aparece (maiúscula ou minúscula);
- a frase em ordem invertida.

---

## Exercícios de debug relacionados

| Nível | Arquivo |
|-------|---------|
| Fácil | [`../debug/facil/04_strings.py`](../debug/facil/04_strings.py) |
| Médio | [`../debug/medio/03_strings.py`](../debug/medio/03_strings.py) |

Tente corrigir. Rode e compare com a saída esperada descrita no cabeçalho de cada arquivo.

> **Resposta do exercício:** [`respostas/08_strings.py`](../respostas/08_strings.py)
