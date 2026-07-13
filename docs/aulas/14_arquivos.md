# Aula 14: Manipulação de Arquivos

Até agora, tudo que o programa faz desaparece quando você fecha o terminal. Você calcula a média de uma turma, some. Você cria uma lista de tarefas, some. Você registra o placar de um jogo, some. O programa recomeça do zero toda vez.

Arquivos resolvem isso: eles **persistem dados entre execuções**. E isso está em tudo.

## Onde arquivos aparecem

Você usa arquivos o tempo todo sem pensar nisso:

- **Saves de jogos**: quando você salva seu mundo de qualquer RPG, basicamente o jogo escreve um arquivo com sua posição, inventário, progresso, etc. Quando você carrega, ele lê esse arquivo de volta.
- **Configurações do VS Code**: suas preferências de tema, fonte e extensões ficam em um arquivo `settings.json`. Se você trocar de computador e copiar esse arquivo, suas configurações vêm junto.
- **Histórico do navegador**: cada site que você visita é registrado em um arquivo local. O modo anônimo só desativa essa escrita.
- **Planilhas e documentos**: um `.xlsx` ou `.docx` é um arquivo que o Excel ou Word lê, exibe e salva de volta.
- **Logs de sistema**: toda vez que seu computador faz algo importante (liga, instala um programa, trava), ele registra em arquivos de log. Quando algo quebra, os técnicos leem esses logs para entender o que aconteceu.

O que você vai aprender nesta aula é exatamente o que todos esses programas fazem internamente, só que em Python.

---

## Abrindo um arquivo: `open()`

Para trabalhar com arquivos em Python, você usa a função `open()`. Ela recebe o nome do arquivo, o **modo** de abertura e, na prática, um terceiro argumento que você vai querer sempre colocar:

```python
arquivo = open("dados.txt", "w", encoding="utf-8")   # abre para escrita
arquivo.write("Olá!\n")
arquivo.close()                                       # fecha o arquivo
```

O `encoding="utf-8"` garante que acentos e cedilhas funcionem em qualquer sistema. No Windows, o padrão pode ser diferente (`cp1252` ou `latin-1`) e vai causar erros ou lixo ao ler arquivos com letras especiais, um dos bugs mais comuns e mais difíceis de entender sem saber que esse parâmetro existe.

O `close()` ao final é obrigatório, sem ele, partes do conteúdo podem não ser salvas (ficam presas em uma memória temporária chamada **buffer**) e o arquivo fica "preso" até o programa encerrar. Mas existe uma forma melhor de fazer isso.

---

## O jeito correto: `with`

Fechar o arquivo manualmente é trabalhoso e fácil de esquecer, especialmente se ocorrer um erro no meio do caminho, onde o `close()` nunca seria executado. O Python tem uma saída melhor: o bloco `with`.

```python
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá!\n")
    arquivo.write("Segunda linha.\n")
# arquivo já está fechado aqui, automaticamente, mesmo que ocorra um erro
```

A linha `with open(...) as arquivo:` abre o arquivo e dá a ele o nome `arquivo`. Tudo dentro do bloco indentado tem acesso ao arquivo. Quando a indentação volta ao nível anterior, seja fim normal ou erro no meio do caminho, o Python fecha o arquivo automaticamente e descarrega o buffer.

Tente usar sempre o `with`, é o jeito padrão em Python, e você nunca vai esquecer de fechar o arquivo nem perder dados por causa do buffer.

---

## Modos de abertura

O segundo argumento do `open()` define o que você pode fazer com o arquivo:

| Modo | Significado | O arquivo já existe? |
|------|-------------|----------------------|
| `"r"` | Leitura | Abre normalmente |
| `"w"` | Escrita | **Apaga tudo** e começa do zero |
| `"a"` | Acrescentar | Continua do final, sem apagar |
| `"x"` | Criar (exclusivo) | Falha se o arquivo já existir |
| `"r+"` | Leitura e escrita | Abre normalmente, sem apagar |

Os dois últimos (`"x"` e `"r+"`) você vai raramente precisar por enquanto, `"x"` é útil quando quer garantir que não vai sobrescrever algo que já existe, `"r+"` quando precisa editar um arquivo no lugar sem apagar o conteúdo. Por ora, os três primeiros resolvem quase tudo.

O mais perigoso é `"w"`: se o arquivo já tiver conteúdo, ele **some sem aviso**, sem confirmação, sem lixeira, sem desfazer. Use com cuidado.

```python
# Salva as preferências...
with open("config.txt", "w", encoding="utf-8") as f:
    f.write("tema=escuro\n")

# Mais tarde, abre de novo com "w" para salvar outra coisa
with open("config.txt", "w", encoding="utf-8") as f:
    f.write("resolucao=1080\n")

# O arquivo tem só a segunda linha, tema perdido para sempre
```

### `write()`: escreve uma string

```python
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Ana: 8.5\n")
    f.write("Bruno: 7.0\n")
    f.write("Carlos: 9.0\n")
```

O `\n` é a quebra de linha, sem ele, tudo ficaria numa única linha enorme. O `write()` escreve exatamente o que você passa, nenhum caractere a mais.

Se você já tem uma lista de strings e quer escrever todas de uma vez, use `writelines()`:

```python
linhas = ["Ana: 8.5\n", "Bruno: 7.0\n", "Carlos: 9.0\n"]
with open("notas.txt", "w", encoding="utf-8") as f:
    f.writelines(linhas)   # equivale a write() para cada item da lista
```

`writelines()` não adiciona `\n` automaticamente, cada string da lista já precisa terminar com `\n`. É útil quando você construiu a lista em outro lugar e quer descarregar de uma vez.

### Acrescentando sem apagar: modo `"a"`

```python
# Primeiro dia de aula
with open("frequencia.txt", "w", encoding="utf-8") as f:
    f.write("2026-03-10: Ana, Bruno, Carlos\n")

# Segundo dia, não apaga o primeiro
with open("frequencia.txt", "a", encoding="utf-8") as f:
    f.write("2026-03-11: Ana, Carlos\n")

# O arquivo agora tem as duas linhas
```

Esse é o padrão de qualquer sistema de log: você abre no modo `"a"` e vai acrescentando registros. O histórico cresce, nada é perdido.

---

## Lendo arquivos

Arquivo que você só escreve tem pouca utilidade. A leitura é onde a coisa fica interessante e tudo que você aprendeu sobre `split()`, `strip()` e métodos de string na [Aula 08](08_strings.md) tem uso direto aqui, porque arquivo de texto é, no fundo, uma string enorme com `\n` separando as linhas.

Um detalhe antes de começar: quando você abre um arquivo para leitura, o Python mantém um **cursor** interno, pense nele como um marcador de livro que começa no início do arquivo e avança conforme você lê. Os quatro jeitos de ler abaixo fazem coisas diferentes, mas todos movem esse cursor para frente. Você vai entender por que isso importa quando chegar em `readline()`.

### Ler tudo de uma vez: `read()`

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
```

`read()` retorna o conteúdo inteiro como uma única string, incluindo todos os `\n` que separam as linhas. Se o arquivo contiver:

```text
Ana: 8.5
Bruno: 7.0
Carlos: 9.0
```

Então `conteudo` será `"Ana: 8.5\nBruno: 7.0\nCarlos: 9.0\n"`, tudo junto, com `\n` no lugar das quebras de linha visíveis.

Para separar as linhas depois de ter lido tudo, use `.splitlines()`, ele já remove os `\n` e lida corretamente com os diferentes formatos de quebra de linha do Windows (`\r\n`) e Unix (`\n`):

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

linhas = conteudo.splitlines()
print(linhas)
# ['Ana: 8.5', 'Bruno: 7.0', 'Carlos: 9.0'], sem \n, já limpo

print(len(linhas))   # 3, número de linhas
```

Use `read()` quando quiser o conteúdo inteiro de uma vez, para buscar uma palavra, contar caracteres, substituir trechos. Para arquivos grandes (logs com gigabytes), carregar tudo na memória de uma vez é um problema, prefira a leitura linha por linha.

### Ler linha por linha: a forma mais comum

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())
```

Usar o arquivo diretamente em um `for` é a forma mais eficiente: o Python lê uma linha, você processa, ele descarta da memória e lê a próxima. A memória usada é mínima, independente do tamanho do arquivo.

O `.strip()` remove o `\n` do final de cada linha, sem ele, você teria uma linha em branco extra depois de cada `print`, porque o `\n` já está na string e o `print` adiciona outro.

Na prática, raramente você só imprime, você processa os dados. Veja o padrão completo lendo o arquivo de notas e decidindo aprovação:

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    for linha in f:
        partes = linha.strip().split(": ")   # "Ana: 8.5" → ["Ana", "8.5"]
        nome = partes[0]
        nota = float(partes[1])              # string → número para calcular
        if nota >= 7:
            print(f"{nome}: Aprovado")
        else:
            print(f"{nome}: Reprovado")
```

Esse é o padrão completo: `.strip()` para limpar o `\n`, `.split()` para dividir os campos, conversão de tipo para operar sobre os dados. Vai aparecer toda vez que você ler um arquivo estruturado.

### `readline()`: uma linha de cada vez

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    primeira = f.readline()   # lê a linha 1, avança o cursor para a linha 2
    segunda  = f.readline()   # lê a linha 2, avança o cursor para a linha 3
    print(primeira.strip())   # "Ana: 8.5"
    print(segunda.strip())    # "Bruno: 7.0"
```

`readline()` lê exatamente uma linha e move o cursor para o início da próxima. É como virar uma página manualmente, enquanto o `for` vira todas de uma vez automaticamente.

Quando o arquivo acaba, `readline()` não levanta erro, retorna uma string **vazia** `""`. Isso é diferente de uma linha em branco (`"\n"`), que seria uma linha que existe no arquivo mas não tem conteúdo. Esse comportamento permite usar `readline()` num laço manual:

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    while True:
        linha = f.readline()
        if linha == "":       # chegou ao fim do arquivo
            break
        print(linha.strip())
```

Na prática, esse laço faz exatamente a mesma coisa que `for linha in f`, e o `for` é mais simples. O `readline()` brilha quando as **primeiras linhas são especiais** (cabeçalho, metadados, contador de registros) e você quer tratá-las antes de processar o restante:

```python
with open("turma.csv", "r", encoding="utf-8") as f:
    cabecalho = f.readline()     # "nome,nota\n", lê e descarta
    for linha in f:              # continua de onde o cursor parou, segunda linha em diante
        partes = linha.strip().split(",")
        nome = partes[0]
        nota = float(partes[1])
        print(f"{nome}: {nota:.1f}")
```

Você vai ver isso em uso na [seção de CSV](#trabalhando-com-csv) mais abaixo.

### `readlines()`: todas as linhas em uma lista

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

print(linhas)
# ['Ana: 8.5\n', 'Bruno: 7.0\n', 'Carlos: 9.0\n'], note o \n em cada item

print(len(linhas))          # 3, total de linhas
print(linhas[0].strip())    # 'Ana: 8.5', primeira linha
print(linhas[-1].strip())   # 'Carlos: 9.0', última linha
```

`readlines()` carrega tudo na memória e entrega uma lista, o que abre acesso a índices, fatiamento e operações da [Aula 09](09_listas.md) que o `for` não permite:

```python
with open("turma.csv", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Pular o cabeçalho com fatiamento, sem precisar de readline()
for linha in linhas[1:]:
    partes = linha.strip().split(",")
    print(partes[0], float(partes[1]))

# Saber quantas linhas tem o arquivo
print(f"O arquivo tem {len(linhas)} registros.")

# Processar em ordem inversa
# reversed() percorre de trás para frente sem criar uma cópia, equivale a linhas[::-1] da Aula 09
for linha in reversed(linhas):
    print(linha.strip())
```

O custo é memória: para arquivos grandes, `readlines()` pode ser lento ou inviável. Para arquivos pequenos, que é o caso de quase tudo que você vai criar nesta disciplina, não faz diferença na prática.

**Resumo prático:**

| Situação | Use | Detalhe |
| --- | --- | --- |
| Arquivo pequeno, quer tudo como string | `read()` | Use `.splitlines()` para separar depois |
| Processar linha por linha, arquivo pode ser grande | `for linha in f` | Mais eficiente em memória |
| Tratar as primeiras linhas de forma especial | `readline()` | Retorna `""` no fim, não `None` |
| Precisar de índice, `len` ou ordem diferente | `readlines()` | Carrega tudo na memória de uma vez |

---

## Caminhos de arquivo

Quando você usa só o nome (`"dados.txt"`), o Python procura o arquivo **na pasta de onde o script está sendo executado**, normalmente a pasta do seu projeto.

```python
# Busca "dados.txt" na pasta atual
with open("dados.txt", "r", encoding="utf-8") as f:
    ...
```

Se o arquivo estiver em outra pasta, use o caminho:

```python
# Caminho relativo, sobe uma pasta, entra em "dados"
with open("dados/notas.txt", "r", encoding="utf-8") as f:
    ...

# Caminho absoluto, começa da raiz do sistema
with open("/home/usuario/projetos/notas.txt", "r", encoding="utf-8") as f:
    ...
```

No **Linux e macOS**, a barra `/` é o separador nativo, não há nenhuma pegadinha, use normalmente.

No **Windows**, o separador nativo é a barra invertida `\`, mas ela causa problemas em Python porque `\n` significa quebra de linha, `\t` significa tabulação, e assim por diante. A solução é usar barra normal `/` (Python aceita em todos os sistemas), dobrar a barra `\\`, ou usar uma **raw string** com `r` antes das aspas, você viu esse recurso na [Aula 08](08_strings.md):

```python
# Funciona em qualquer sistema operacional
with open("dados/notas.txt", "r", encoding="utf-8") as f: ...

# Windows com barra dobrada, também funciona
with open("dados\\notas.txt", "r", encoding="utf-8") as f: ...

# Raw string: r antes das aspas desativa \n, \t e companhia
with open(r"dados\notas.txt", "r", encoding="utf-8") as f: ...

# ERRADO no Windows: \n vira quebra de linha, o caminho some
with open("dados\notas.txt", "r", encoding="utf-8") as f: ...
```

Se quiser algo que simplesmente funciona no Windows, Mac e Linux sem precisar pensar nisso, tem o módulo `pathlib` na [Aula 15](15_modulos.md), ele constrói o caminho certo automaticamente.

---

## Tratando erros

O que acontece se você tentar ler um arquivo que não existe?

```python
with open("fantasma.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'fantasma.txt'
```

O programa trava. Para lidar com isso de forma elegante, você vai aprender `try/except` em detalhes na [Aula 18](18_avancado.md), mas a estrutura básica já aparece aqui, você precisa dela para trabalhar com arquivos:

```python
try:
    with open("dados.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e o caminho.")
```

Se ocorrer um `FileNotFoundError`, o `except` captura e você decide o que fazer, em vez de o programa travar na cara do usuário.

Você pode capturar vários tipos de erro no mesmo bloco `try`, adicionando mais `except's`:

```python
try:
    with open("dados.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado. Verifique o nome e o caminho.")
except PermissionError:
    print("Sem permissão para acessar esse arquivo.")
except IsADirectoryError:
    print("Esse caminho é uma pasta, não um arquivo.")
except UnicodeDecodeError:
    print("Erro de encoding, o arquivo pode não estar em UTF-8.")
```

O Python testa cada `except` de cima para baixo e para no primeiro que encaixar. Se nenhum encaixar, o erro segue em frente como se o `try` não existisse.

---

## Trabalhando com CSV

**CSV** (*Comma-Separated Values*) é o formato mais comum para trocar dados entre programas: Excel, Google Planilhas, bancos de dados, todos exportam CSV. É simplesmente um arquivo de texto onde cada linha é um registro e os campos são separados por vírgula:

```text
Ana,8.5,Aprovado
Bruno,6.0,Reprovado
Carlos,9.0,Aprovado
```

Você pode ler e escrever CSV com o que já sabe. As tuplas da [Aula 12](12_tuplas_sets.md) aparecem naturalmente aqui, cada linha do CSV vira um par de valores que desempacotamos no `for`:

```python
# Escrevendo
alunos = [
    ("Ana", 8.5),
    ("Bruno", 6.0),
    ("Carlos", 9.0),
]

with open("turma.csv", "w", encoding="utf-8") as f:
    f.write("nome,nota\n")   # cabeçalho
    for nome, nota in alunos:   # desempacotamento da tupla, Aula 12
        f.write(f"{nome},{nota}\n")
```

```python
# Lendo e processando
with open("turma.csv", "r", encoding="utf-8") as f:
    f.readline()   # pula o cabeçalho, lê uma linha e descarta
    for linha in f:
        partes = linha.strip().split(",")
        nome = partes[0]
        nota = float(partes[1])
        if nota >= 7:
            print(f"{nome}: Aprovado")
        else:
            print(f"{nome}: Reprovado")
```

O padrão: `.strip()` tira o `\n` do final, `.split(",")` parte na vírgula e entrega uma lista, `"Ana,8.5"` vira `["Ana", "8.5"]`, `float()` converte a nota de string para número. Essa sequência vai aparecer toda vez que você ler um arquivo estruturado.

Se o arquivo puder ter dados inválidos, um campo vazio, ou uma nota que não seja número, `float(partes[1])` vai levantar `ValueError`. Adicione um `except ValueError` ao bloco `try`, usando o mesmo padrão de `float(input(...))` que você já viu na [Aula 05](05_entrada_saida.md).

CSV simples assim funciona bem desde que nenhum campo contenha vírgula. Se o nome de um aluno for `"Silva, João"` ou uma observação tiver vírgula, o `split(",")` vai quebrar o dado no lugar errado. Para esses casos, Python tem o módulo `csv` da biblioteca padrão, você verá na [Aula 15](15_modulos.md), e ele resolve isso automaticamente.

---

## Exemplo completo: diário de treinos

Aqui é onde as funções da [Aula 13](13_funcoes.md) e os arquivos desta aula se juntam de verdade: cada função tem uma responsabilidade (`registrar_treino` só escreve, `exibir_resumo` só lê), e o histórico sobrevive entre sessões. Esse é o padrão de qualquer app de tracking: Strava, Notion, até uma planilha de academia usam exatamente isso por baixo.

Um programa que salva cada treino em arquivo e calcula estatísticas ao final:

```python
def registrar_treino(atividade, duracao, arquivo="treinos.csv"):
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(f"{atividade},{duracao}\n")
    print(f"Treino registrado: {atividade} por {duracao} minutos.")

def exibir_resumo(arquivo="treinos.csv"):
    try:
        total_minutos = 0
        num_treinos = 0

        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(",")
                atividade = partes[0]
                duracao = int(partes[1])
                total_minutos += duracao
                num_treinos += 1
                print(f"  {atividade}: {duracao} min")

        if num_treinos > 0:
            media = total_minutos / num_treinos
            print(f"\nTotal: {total_minutos} minutos em {num_treinos} treinos")
            print(f"Média por treino: {media:.1f} minutos")

    except FileNotFoundError:
        print("Nenhum treino registrado ainda.")

# Programa principal
while True:
    print("\n1. Registrar treino")
    print("2. Ver resumo")
    print("3. Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        atividade = input("Atividade: ").strip()
        try:
            duracao = int(input("Duração (minutos): "))
        except ValueError:
            print("Digite um número inteiro de minutos.")
            continue
        registrar_treino(atividade, duracao)
    elif opcao == "2":
        exibir_resumo()
    elif opcao == "3":
        break
```

Cada treino é salvo permanentemente. Você pode fechar o programa, abrir de novo amanhã, e o histórico continua lá, é exatamente o que qualquer app de registro faz por baixo.

---

Exemplo rodável desta aula: [`exemplos/14_arquivos.py`](../exemplos/14_arquivos.py)

---

## Exercício sugerido

1. Crie um programa que leia nomes de alunos e suas notas até o usuário digitar `"fim"`.
2. Salve cada entrada em um arquivo `turma.csv`, uma por linha, no formato `Nome,Nota`.
3. Ao encerrar, leia o arquivo de volta, calcule a média geral da turma e exiba quem ficou acima e abaixo da média.
4. Execute o programa duas vezes, adicionando alunos diferentes em cada execução. Se os da primeira execução sumiram na segunda, releia a seção de modos de abertura e corrija.

---

## Lista da disciplina

> Você terminou a aula de manipulação de arquivos. Este é o momento certo para resolver a **Lista 07: Manipulação de Arquivos**, disponível em `docs/listas/`.
>
> Os exercícios envolvem leitura e escrita de arquivos e organização do código em funções. Use tudo que aprendeu até aqui.

---

## Exercícios de debug relacionados

| Nível | Arquivo |
| --- | --- |
| Médio | [`../debug/medio/07_arquivos.py`](../debug/medio/07_arquivos.py) |

> **Resposta do exercício:** [`respostas/14_arquivos.py`](../respostas/14_arquivos.py)

---

> Na [Aula 15](15_modulos.md) você vai importar o módulo `csv` (que resolve o problema da vírgula dentro de campos) e o `pathlib` (que constrói caminhos de arquivo que funcionam em qualquer sistema sem precisar pensar em `\\` ou `/`). Os dois usam exatamente o que você viu aqui.
