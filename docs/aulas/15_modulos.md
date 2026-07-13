# Aula 15: Módulos e Bibliotecas

Todo programa que você escreveu até aqui usou só o que o Python entrega de fábrica: `print()`, `input()`, `len()`, `range()`. Funcionou bem para aprender, mas a partir de agora você tem acesso a outro nível: módulos prontos para gerar números aleatórios, trabalhar com datas, ler CSVs sem gambiarra. E se a biblioteca padrão não tiver o que você precisa, a comunidade provavelmente já fez e publicou. Esta aula explica como acessar tudo isso.

---

## O que é um módulo?

Um **módulo** é simplesmente um arquivo `.py` com funções, classes e variáveis que você pode usar em outros programas. Quando você escreve `import math`, por exemplo, está pedindo ao Python para carregar o arquivo `math.py` que está incluso na instalação padrão.

Isso existe por uma razão prática: ninguém consegue nem deve colocar tudo em um único arquivo. Dividir o código em módulos permite reutilizar o que você escreveu em outros projetos, manter cada arquivo com um propósito único e, no trabalho em equipe, garantir que você e seu colega não pisem no mesmo arquivo o tempo todo.

---

## Importando módulos

Existem três formas de importar um módulo. Cada uma tem um uso diferente, e saber quando usar qual evita confusão mais tarde.

### `import`: importa o módulo inteiro

```python
import math

print(math.sqrt(25))   # 5.0
print(math.pi)         # 3.141592653589793
print(math.ceil(4.2))  # 5  (arredonda para cima)
print(math.floor(4.8)) # 4  (arredonda para baixo)
```

Quando o Python executa `import math`, ele encontra o arquivo `math.py` na instalação padrão, executa ele uma vez e coloca tudo que estava definido ali dentro de um "compartimento" chamado `math`. Esse compartimento é o que chamamos de **namespace**, que é basicamente um agrupamento de nomes para evitar que coisas de lugares diferentes se misturem.

Você acessa o conteúdo desse compartimento com o prefixo `math.`. O ponto é o separador: "dentro do compartimento `math`, pegue `sqrt`".

Isso importa mais do que parece. Imagine que você usa dois módulos ao mesmo tempo, e ambos têm uma função com o mesmo nome:

```python
import math
import cmath   # versão do math para números complexos

print(math.sqrt(25))    # 5.0
print(cmath.sqrt(-1))   # 1j  (raiz de número negativo, resultado complexo)
```

Com o prefixo, nunca há dúvida sobre qual `sqrt` você está chamando. Sem o prefixo, um ia sobrescrever o outro sem aviso.

### `from ... import`: importa partes específicas

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0  (sem o prefixo "math.")
print(pi)         # 3.141592653589793
```

Essa forma pega uma função específica do módulo e coloca diretamente no seu namespace, sem o prefixo. É útil quando você vai usar a mesma função repetidas vezes num arquivo e o prefixo ficaria cansativo de escrever.

O risco: se dois módulos têm funções com o mesmo nome e você importa as duas dessa forma, a segunda sobrescreve a primeira em silêncio. Sem erro, sem aviso, o nome anterior simplesmente some:

```python
from math import sqrt       # sqrt agora é a versão do math
from cmath import sqrt      # sqrt agora é a versão do cmath, a anterior foi embora

print(sqrt(25))   # 5+0j  (resultado complexo, não o 5.0 que você talvez esperava)
```

Esse tipo de bug é difícil de encontrar porque o programa não trava, só produz resultado errado. Com `import math` e `import cmath`, os dois `sqrt` ficam em compartimentos separados e o problema não existe.

Existe ainda uma variante que você pode encontrar por aí: `from math import *`, que importa tudo do módulo sem prefixo. Evite. Ela traz para o seu namespace todos os nomes do módulo de uma vez, e você não sabe quais são nem se algum vai colidir com algo que você já definiu.

### `as`: apelido para o nome do módulo

```python
import statistics as stats

notas = [7.5, 8.0, 6.5, 9.0, 7.0]
print(stats.mean(notas))    # 7.6
print(stats.stdev(notas))   # 0.927...
```

`as` cria um apelido: o módulo ainda existe como antes, mas você o acessa por um nome mais curto. Tem dois usos principais.

**1. Nome longo.** O módulo `statistics` tem 11 caracteres. Usar `stats` é mais rápido de escrever e de ler quando aparece muitas vezes no arquivo.

**2. Evitar a repetição do próprio nome.** O módulo `datetime` tem uma classe dentro dele que também se chama `datetime`. Sem apelido, você escreve `datetime.datetime.now()`, o que parece confuso:

```python
import datetime
agora = datetime.datetime.now()   # confuso de ler
```

Com alias:

```python
import datetime as dt
agora = dt.datetime.now()         # mais limpo
```

Ou melhor ainda, importando só o que precisa:

```python
from datetime import datetime
agora = datetime.now()            # mais limpo ainda
```

**3. Convenção da comunidade.** Em ciência de dados existe uma convenção que todo mundo segue: `import numpy as np` e `import pandas as pd`. Não é obrigatório, mas você vai ver esses apelidos em qualquer tutorial ou código de análise de dados. Adotar a convenção torna seu código imediatamente reconhecível para qualquer outra pessoa da área.

---

## Criando seus próprios módulos

Qualquer arquivo `.py` que você criar é um módulo. Isso significa que você pode dividir seu programa em arquivos e importar entre eles.

Crie `calculos.py`:

```python
APROVACAO = 7.0   # constantes também podem ser exportadas por um módulo

def media(numeros):
    return sum(numeros) / len(numeros)

def maior(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)
```

Use em `main.py` (na mesma pasta):

```python
import calculos

notas = [8.5, 7.0, 9.0, 6.5]
print(calculos.media(notas))      # 7.75
print(calculos.maior(notas))      # 9.0
print(calculos.menor(notas))      # 6.5
print(calculos.APROVACAO)         # 7.0
```

Ou importando só o que precisa:

```python
from calculos import media, maior, menor

print(media([8.5, 7.0, 9.0]))   # 8.166...
```

Quando você escreve `import calculos`, o Python lê o arquivo `calculos.py` de cima para baixo, define as funções e a constante na memória, e pronto. Se você importar o mesmo módulo em dois lugares diferentes do programa, o Python não lê o arquivo duas vezes: executa uma vez, guarda o resultado em cache, e reutiliza nas chamadas seguintes.

### Como o Python encontra o módulo

Quando você escreve `import calculos`, o Python procura `calculos.py` nesta ordem:

1. Na **mesma pasta** do arquivo que está rodando
2. Nas pastas do sistema onde a biblioteca padrão está instalada
3. Em pastas extras configuradas no `PYTHONPATH` (avançado, não precisa saber agora)

O caso mais simples, e o que você vai usar, é o primeiro: os dois arquivos na mesma pasta.

**Estrutura correta:**

```text
projeto/
├── calculos.py    ← módulo com as funções
└── main.py        ← faz o import e usa as funções
```

Para rodar, você abre o terminal, entra na pasta do projeto e executa `main.py`:

```text
cd projeto/
python3 main.py
```

O Python roda `main.py`, encontra `import calculos`, procura `calculos.py` na mesma pasta (`projeto/`), encontra, carrega as funções, e continua.

**O que falha e por quê:**

Se você criar os arquivos em pastas separadas como abaixo, o import vai quebrar:

```text
projeto/
├── modulos/
│   └── calculos.py    ← aqui
└── main.py            ← import calculos falha aqui
```

O Python procura `calculos.py` na pasta onde `main.py` está (`projeto/`), não dentro de `modulos/`. O arquivo existe, mas está num lugar que o Python não vai olhar por padrão.

Para projetos pequenos como os desta disciplina, a recomendação é simples: **tudo na mesma pasta**.

Mas se você quiser organizar por pastas mesmo assim, a solução correta é transformar a pasta em um **pacote**: basta criar um arquivo vazio chamado `__init__.py` dentro dela, e então importar com `from pasta import modulo`:

```text
projeto/
├── modulos/
│   ├── __init__.py    ← arquivo vazio que diz "esta pasta é um pacote"
│   └── calculos.py
└── main.py
```

```python
# main.py
from modulos import calculos

print(calculos.soma(3, 4))
```

Ou, se quiser importar só a função:

```python
from modulos.calculos import soma

print(soma(3, 4))
```

O `__init__.py` é o que avisa o Python que a pasta `modulos/` não é uma pasta qualquer: é um pacote que pode ser importado. Sem ele, o `from modulos import calculos` falha com `ModuleNotFoundError` mesmo o arquivo existindo.

### Como dividir um programa

Não existe regra obrigatória, mas tem um padrão que funciona bem para projetos do tamanho que você vai fazer agora:

- **`uteis.py`** (ou o nome do tema: `calculos.py`, `notas.py`, `jogador.py`) com as funções que fazem o trabalho pesado: calcular, transformar, validar, ler e salvar dados.
- **`main.py`** com o fluxo do programa: pedir entrada do usuário, chamar as funções, exibir os resultados.

A ideia é separar "o que o programa faz" de "como o usuário interage com ele". As funções em `uteis.py` não sabem que existe um terminal: elas só recebem dados e devolvem resultados. Isso tem uma vantagem prática: se amanhã você quiser reusar `media()` em outro projeto, é só copiar o arquivo, sem arrastar junto todo o `input()` e `print()`.

Dois sinais de que vale a pena criar um módulo separado:

1. O arquivo principal ficou grande e você está se perdendo. Funções que fazem a mesma coisa merecem um arquivo próprio.
2. Você percebeu que está copiando as mesmas funções de um projeto para outro. Coloque elas num módulo e importe de lá.

Para o tamanho dos programas desta disciplina, dois arquivos já resolvem: um módulo com as funções, um `main.py` que usa tudo. Não precisa ir além disso agora.

### Testando um módulo sozinho: `if __name__ == "__main__":`

Enquanto escreve `calculos.py`, é comum querer testar as funções ali mesmo, sem precisar abrir `main.py` toda vez:

```python
def media(numeros):
    return sum(numeros) / len(numeros)

def maior(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)

print(media([8, 9, 10]))   # só um teste rápido, pra conferir se a função funciona
```

Isso funciona bem enquanto você roda `python3 calculos.py` direto. O problema aparece na hora de importar: `import calculos` executa o arquivo inteiro de cima a baixo (você viu isso agora mesmo), incluindo aquele `print` de teste. Resultado: toda vez que `main.py` faz `import calculos`, o `9.0` aparece sozinho na tela, sem que você tenha pedido nada.

A solução é uma variável que o Python já cria automaticamente em todo arquivo, chamada `__name__`, e que diz como aquele arquivo está sendo usado:

- Se o arquivo foi executado diretamente (`python3 calculos.py`), `__name__` vale `"__main__"`.
- Se o arquivo foi importado por outro (`import calculos`), `__name__` vale `"calculos"`, o nome do próprio módulo.

Com isso, você protege o teste dentro de um `if`:

```python
def media(numeros):
    return sum(numeros) / len(numeros)

def maior(numeros):
    return max(numeros)

def menor(numeros):
    return min(numeros)

if __name__ == "__main__":
    print(media([8, 9, 10]))   # só roda quando calculos.py é executado direto
```

Agora `python3 calculos.py` ainda mostra o teste, mas `import calculos` a partir de `main.py` fica em silêncio, só disponibiliza as funções. Você vai ver esse `if __name__ == "__main__":` com frequência em código de terceiros, inclusive dentro do próprio `main.py`, como forma de dizer "isto aqui é o ponto de entrada do programa, não um módulo pra ser importado por outra coisa".

---

## A biblioteca padrão do Python

Python vem com uma biblioteca padrão enorme, com centenas de módulos prontos para usar sem instalar nada. Aqui estão os mais úteis para o dia a dia.

### `math`: matemática

```python
import math

print(math.sqrt(144))      # 12.0  (raiz quadrada)
print(math.pow(2, 10))     # 1024.0  (potência, sempre retorna float)
print(math.log(100, 10))   # 2.0  (logaritmo base 10)
print(math.pi)             # 3.141592653589793
print(math.e)              # 2.718281828459045

print(math.ceil(4.1))      # 5  (arredonda para cima, para o inteiro maior)
print(math.floor(4.9))     # 4  (arredonda para baixo, para o inteiro menor)
print(math.fabs(-7.3))     # 7.3  (valor absoluto, sempre retorna float)
```

Algumas diferenças que valem a pena saber:

- `math.e` é o número de Euler, a base do logaritmo natural. Aparece em fórmulas de juros compostos, crescimento exponencial e em várias disciplinas de cálculo.
- `math.pow(2, 10)` sempre retorna `float` (`1024.0`), mesmo que o resultado seja inteiro. Se você precisar de `int`, use o operador `2 ** 10`, que retorna `1024`.
- `math.fabs(-7.3)` também sempre retorna `float`, diferente de `abs(-7)` que devolve o mesmo tipo do argumento (int para int, float para float). Para cálculos numéricos onde você quer garantir que vai trabalhar com float, `fabs` é mais previsível.
- `math.ceil(4.1)` retorna `5` e `math.floor(4.9)` retorna `4`: eles vão sempre para cima e para baixo respectivamente, independente de qual extremo está mais perto. Diferente de `round()`, que arredonda para o mais próximo.

### `random`: números aleatórios

```python
import random

print(random.randint(1, 6))             # número entre 1 e 6 inclusive
print(random.random())                  # float entre 0.0 e 1.0
print(random.choice(["cara", "coroa"])) # escolhe um item da lista
print(random.uniform(0, 10))           # float aleatório entre 0 e 10

notas = [8.5, 7.0, 9.0, 6.5]
random.shuffle(notas)                   # embaralha a lista no lugar
print(notas)
```

`random.randint(1, 6)` é o dado de 6 faces. `random.choice()` é o "sortear um da lista". `random.shuffle()` é o embaralhar de cartas. A diferença entre `randint` e `uniform`: `randint` retorna inteiro, `uniform` retorna float. `random.random()` é o mais básico: só retorna float entre 0.0 e 1.0, sem parâmetros.

Uma curiosidade: os números do `random` não são realmente aleatórios. Computadores são determinísticos, então o Python usa um algoritmo (Mersenne Twister) que gera sequências que *parecem* aleatórias. Dá para controlar isso com `random.seed()`, e para situações onde a imprevisibilidade realmente importa (senhas, tokens), existe o módulo `secrets`. Os detalhes estão no [FAQ](../extras/faq.md#os-números-do-random-são-realmente-aleatórios).

### `datetime`: datas e horas

```python
from datetime import datetime, date

agora = datetime.now()
print(agora)                    # 2026-05-24 02:30:00.123456
print(agora.year)               # 2026
print(agora.month)              # 5
print(agora.day)                # 24
print(agora.strftime("%d/%m/%Y"))  # 24/05/2026

hoje = date.today()
print(hoje)                     # 2026-05-24

# Diferença entre datas
nascimento = date(2005, 3, 15)
diferenca = hoje - nascimento
print(diferenca.days)           # número de dias de diferença
```

O `strftime` converte uma data para string no formato que você definir. Os códigos mais comuns:

| Código | O que representa | Exemplo |
| --- | --- | --- |
| `%d` | Dia com zero à esquerda | `07`, `24` |
| `%m` | Mês com zero à esquerda | `03`, `11` |
| `%Y` | Ano com 4 dígitos | `2026` |
| `%y` | Ano com 2 dígitos | `26` |
| `%H` | Hora no formato 24h | `09`, `14` |
| `%M` | Minuto | `05`, `30` |
| `%S` | Segundo | `00`, `59` |

Você combina os códigos como quiser:

```python
agora = datetime.now()
print(agora.strftime("%d/%m/%Y"))        # 24/05/2026
print(agora.strftime("%Y-%m-%d"))        # 2026-05-24  (formato ISO, útil para ordenar)
print(agora.strftime("%d/%m/%Y %H:%M"))  # 24/05/2026 02:30
```

Quando você subtrai duas datas (`hoje - nascimento`), o resultado não é um número simples: é um objeto `timedelta`, que representa um intervalo de tempo. O atributo `.days` extrai a contagem total de dias desse intervalo. Se você precisar trabalhar com horas ou minutos em vez de dias, use `.seconds` (dentro do dia) ou `.total_seconds()` (intervalo inteiro em segundos).

### `copy`: cópia de objetos

Lembra do problema de cópia que apareceu na [Aula 09](09_listas.md)? Quando você copia uma lista de listas com `.copy()`, a lista externa é duplicada, mas as sublistas internas continuam sendo as mesmas. Mexer em uma mexe na outra. O módulo `copy` resolve isso de vez:

```python
import copy

original = [[1, 2], [3, 4]]

rasa = original.copy()         # cópia rasa (as sublistas são compartilhadas)
rasa[0].append(99)
print(original)                # [[1, 2, 99], [3, 4]]  (original mudou!)

profunda = copy.deepcopy(original)  # cópia profunda (tudo independente)
profunda[0].append(88)
print(original)                # [[1, 2, 99], [3, 4]]  (original intacto)
```

`copy.deepcopy()` cria uma cópia completamente independente de qualquer estrutura, por mais aninhada que seja.

Na prática, você vai precisar de `deepcopy` principalmente em duas situações: quando trabalha com **matrizes** (listas de listas da [Aula 10](10_matrizes.md)) e quando tem **dicionários dentro de dicionários** ([Aula 11](11_dicionarios.md)). Para listas simples de números ou strings, `.copy()` já resolve sem precisar importar nada.

### `os.path` e `pathlib`: caminhos de arquivo

Você viu na [Aula 14](14_arquivos.md) que caminhos de arquivo são diferentes no Windows e Linux. O módulo `os.path` e a classe `Path` do `pathlib` resolvem isso automaticamente:

```python
import os.path

# Verifica se um arquivo existe antes de tentar abrir
if os.path.exists("dados.txt"):
    with open("dados.txt", "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Arquivo não encontrado.")

# Combina partes de caminho de forma segura em qualquer sistema
caminho = os.path.join("dados", "turma", "notas.txt")
print(caminho)   # "dados/turma/notas.txt" no Linux, "dados\turma\notas.txt" no Windows
```

Com `os.path.join("dados", "notas.txt")`, o Python escolhe o separador certo para o sistema que está rodando automaticamente.

A versão mais moderna usa `pathlib`, que tem uma sintaxe mais limpa:

```python
from pathlib import Path

# O / entre Path e string funciona como separador; você vai entender o porquê na Aula 16
caminho = Path("dados") / "turma" / "notas.txt"
print(caminho)              # dados/turma/notas.txt

if caminho.exists():
    conteudo = caminho.read_text(encoding="utf-8")   # lê o arquivo diretamente
    print(conteudo)
```

`pathlib` também oferece atalhos úteis: `caminho.exists()` para checar se existe antes de abrir, `caminho.read_text()` para ler o conteúdo direto sem precisar do bloco `with`, `caminho.stem` para o nome sem extensão (`"notas"`) e `caminho.suffix` para a extensão (`".txt"`). Para projetos novos, prefira `pathlib`.

### `csv`: arquivos CSV com mais recursos

Na [Aula 14](14_arquivos.md) você aprendeu a ler CSV manualmente com `.split(",")`. O problema é que esse método quebra quando um campo tem vírgula dentro: `"Silva, João",8.5` vira três pedaços em vez de dois. O módulo `csv` lida com isso automaticamente, porque entende as aspas do formato:

```python
import csv

# Escrevendo
with open("turma.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "nota"])        # cabeçalho
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Silva, João", 7.0])    # vírgula no nome: sem problema

# Lendo
with open("turma.csv", "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)   # usa o cabeçalho como chaves do dicionário
    for linha in leitor:
        print(linha["nome"], linha["nota"])
```

O `newline=""` no `open()` para escrita é necessário porque o módulo `csv` já cuida das quebras de linha internamente. Sem ele, no Windows cada linha ficaria com uma linha em branco extra (o sistema inseriria `\r\n` e o `csv` adicionaria mais um `\n`). É um detalhe chato, mas omitir causa bugs difíceis de perceber.

`csv.DictReader` lê o cabeçalho da primeira linha e usa os nomes das colunas como chaves do dicionário. Em vez de `linha[0]` e `linha[1]` (que exige lembrar a posição de cada campo), você usa `linha["nome"]` e `linha["nota"]`. Muito mais legível quando o CSV tem muitas colunas e o código precisa ser entendido por outra pessoa. (O porquê de `DictReader(f)` funcionar como funciona vai fazer mais sentido quando você ver classes na [Aula 16](16_objetos_classes.md), por ora use como receita.)

---

## Bibliotecas externas: `pip`

A biblioteca padrão é grande, mas há um universo ainda maior de ferramentas criadas pela comunidade. Essas bibliotecas ficam no **PyPI** (*Python Package Index*), um repositório público com mais de 500 mil pacotes.

Para instalar uma biblioteca do PyPI, use o `pip` no terminal (você pode ver isso no [Apêndice: Ambiente Avançado](../apendices/ambiente_avancado.md)):

```
pip install nome-da-biblioteca
```

O `pip` se conecta ao PyPI, baixa o pacote e o instala no seu ambiente Python. Depois é só importar normalmente, como qualquer módulo da biblioteca padrão:

```python
import nome_da_biblioteca
```

O processo é sempre o mesmo, independente da biblioteca: instala com `pip`, importa com `import`. Cada biblioteca tem sua própria documentação, geralmente acessível pelo site do PyPI ou pelo GitHub do projeto.

Quando precisar de algo que a biblioteca padrão não tem, pesquise `python biblioteca para X`. Para avaliar se vale a pena: número de downloads alto, data de atualização recente e projeto ativo no GitHub são bons sinais. Biblioteca sem atualização há 3 anos tem cheiro de abandono.

Antes de instalar qualquer biblioteca externa: ative o ambiente virtual primeiro. Sem isso, a instalação vai para o Python global e pode conflitar com outros projetos (detalhes no [Apêndice: Ambiente Avançado](../apendices/ambiente_avancado.md)).

### Bibliotecas externas mais usadas

| Biblioteca | Para que serve |
| --- | --- |
| `requests` | Fazer requisições HTTP para consumir APIs e baixar páginas |
| `pandas` | Análise de dados, planilhas, séries temporais |
| `numpy` | Cálculo numérico e matrizes de alta performance |
| `flask` / `fastapi` | Criar APIs e aplicações web |
| `pillow` | Abrir, editar e salvar imagens |
| `pytest` | Escrever e rodar testes automatizados |
| `beautifulsoup4` | Extrair dados de páginas HTML (web scraping) |
| `sqlalchemy` | Trabalhar com bancos de dados SQL |

---

Exemplo rodável desta aula: [`exemplos/15_modulos.py`](../exemplos/15_modulos.py)

## Exercício sugerido

1. Crie um arquivo `uteis.py` com funções: `media(lista)`, `maior(lista)`, `menor(lista)`.
2. Em um arquivo separado `main.py` (na mesma pasta que `uteis.py`), importe e use as três funções.
3. Use o módulo `random` para gerar uma lista de 10 notas aleatórias entre 0 e 10 (use `random.uniform`).
4. Use o módulo `datetime` para exibir a data e hora de quando o programa foi executado.
5. Salve os resultados em um arquivo CSV com `csv.writer`.

**Como rodar:** no terminal, navegue até a pasta onde criou os dois arquivos (`cd nome-da-pasta`) e execute `python3 main.py`. O `from uteis import ...` só funciona se os dois arquivos estiverem na mesma pasta e você rodar o script de dentro dela.

> **Resposta do exercício:** [`respostas/15_modulos/main.py`](../respostas/15_modulos/main.py) e [`respostas/15_modulos/uteis.py`](../respostas/15_modulos/uteis.py)
