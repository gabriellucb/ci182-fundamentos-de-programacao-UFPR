# Debug: encontre o erro

Cada arquivo tem um programa com bug intencional.

O programa está escrito, roda (ou tenta rodar), mas produz um resultado errado ou lança um erro. Seu trabalho é encontrar o problema e corrigir.

**Como usar:**

1. Leia o comentário no topo: ele descreve o que o programa deveria fazer e mostra um exemplo da saída esperada.
2. Tente rodar.
3. Leia a mensagem de erro com calma, ela diz o tipo, a linha e às vezes aponta exatamente o problema. Se não houver erro, compare a saída com o exemplo esperado.
4. Corrija e rode de novo até funcionar.

Não existe gabarito aqui. Se travar, releia a seção correspondente no `docs/guia_de_estudo.md`.

---

## Fácil (`facil/`)

Um bug por arquivo. Produz um erro com traceback claro ou um resultado visivelmente errado.

| Arquivo | Tema |
| --- | --- |
| `01_tipos.py` | Tipos e conversão |
| `02_condicionais.py` | Condicionais |
| `03_repeticao.py` | Repetição |
| `04_strings.py` | Strings |
| `05_listas.py` | Listas |
| `06_dicionarios.py` | Dicionários |
| `07_funcoes.py` | Funções |
| `08_classes.py` | Classes |

---

## Médio (`medio/`)

Um ou dois bugs por arquivo. Pode não dar traceback, o programa roda, mas o resultado está errado.

| Arquivo | Tema |
| --- | --- |
| `01_condicionais.py` | Multa por excesso de velocidade |
| `02_repeticao.py` | Sequência de Fibonacci |
| `03_strings.py` | Verificador de palíndromo |
| `04_listas.py` | Torneio de games (ranking de pontuações) |
| `05_matrizes.py` | Placar de eSports (laços aninhados e médias) |
| `06_funcoes.py` | Conversor de temperatura |
| `07_arquivos.py` | Diário de estudo (leitura/escrita e acumulação) |
| `08_classes.py` | Sistema de RPG (atributos e inventário) |

---

## Difícil (`dificil/`)

Mais de um bug por arquivo. Mistura de temas: listas, funções, classes, lógica. Alguns bugs dão traceback, outros produzem resultado silenciosamente errado.

| Arquivo | Tema |
| --- | --- |
| `01_ranking.py` | Ranking com ordenação e cálculo de médias (Aula 11) |
| `02_caixa_registradora.py` | Caixa com quantidade por produto, cupom de desconto, faixas por valor e imposto (Aula 16) |
| `03_jogo_forca.py` | Desafio final: categorias, dificuldade, placar persistente em arquivo e ranking (Aula 18) |
