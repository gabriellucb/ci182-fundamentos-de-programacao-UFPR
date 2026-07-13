# Apêndice: Custo de operações em listas

> Este apêndice vai além do conteúdo de CI182/CI240. Você não precisa saber isso para passar na matéria, mas se você ficou curioso depois de ver `insert()` vs `append() + sort()`, aqui está a explicação completa.

---

## O que é "custo" de uma operação?

Quando falamos em custo de uma operação, estamos falando de quanto **tempo ela leva em função do tamanho da entrada**. Não em milissegundos: em proporção. Uma operação que leva o dobro de tempo quando você dobra a lista tem um custo diferente de uma que leva o mesmo tempo independente do tamanho.

A notação usada para isso é chamada de **Big O** (lê-se "Big Oh"), e ela descreve o pior caso: o quanto a operação pode crescer conforme a entrada cresce.

Você não precisa saber a matemática por trás. Basta entender os casos mais comuns:

| Notação | Nome | O que significa na prática |
|---------|------|---------------------------|
| O(1) | Constante | Sempre o mesmo tempo, independente do tamanho |
| O(n) | Linear | Dobra o tamanho → dobra o tempo |
| O(n log n) | Linearítmica | Um pouco pior que linear, muito melhor que quadrático |
| O(n²) | Quadrática | Dobra o tamanho → quadruplica o tempo |

Para dar uma ideia concreta, se uma operação O(n) leva 1 segundo com 1.000 itens:

| n | O(n) | O(n log n) | O(n²) |
|---|------|------------|-------|
| 1.000 | 1s | ~10s | 1.000s |
| 10.000 | 10s | ~130s | 100.000s |
| 100.000 | 100s | ~1.700s | muito tempo |

O quadrático explode rápido.

---

## Custo das operações de lista em Python

| Operação | Custo | Por quê |
|----------|-------|---------|
| `lista[i]` (acesso por índice) | O(1) | O Python sabe o endereço de cada posição direto |
| `len(lista)` | O(1) | Python guarda o tamanho internamente |
| `lista.append(x)` | O(1) amortizado | Adiciona no final, sem mover nada |
| `lista.pop()` (sem índice) | O(1) | Remove do final, sem mover nada |
| `lista.pop(0)` (do início) | O(n) | Precisa deslocar todos os elementos |
| `lista.insert(i, x)` | O(n) | Precisa deslocar todos os elementos após a posição |
| `x in lista` | O(n) | No pior caso, verifica cada elemento um por um |
| `lista.sort()` | O(n log n) | Timsort, muito eficiente pro uso geral e ainda melhor com dados parcialmente ordenados |
| `lista.index(x)` | O(n) | Busca linear |
| `lista.remove(x)` | O(n) | Busca linear + deslocamento |

### Por que `append()` é O(1) mas `insert()` é O(n)?

Quando você faz `append()`, o Python simplesmente coloca o novo valor no espaço vazio que já existe reservado ao final da lista. Nada se move.

Quando você faz `insert(i, valor)`, o Python precisa **abrir espaço na posição i**. Para fazer isso, ele move todos os elementos de `i` até o final uma posição para a direita, e isso são até `n` movimentos no pior caso (inserir no início).

```text
lista = ["a", "b", "c", "d"]

insert(1, "X"):
antes:  ["a", "b", "c", "d"]
passo:  ["a", _,  "b", "c", "d"]  ← "b", "c", "d" se moveram
depois: ["a", "X", "b", "c", "d"]
```

Quanto maior a lista, mais elementos precisam se mover. Daí o O(n).

### Por que `pop(0)` é O(n) mas `pop()` é O(1)?

Pelo mesmo motivo. Remover do final não mexe em nada: o espaço some e pronto. Remover do início exige deslocar todos os elementos uma posição para a esquerda para preencher o buraco.

Se você precisar de uma estrutura onde remover do início seja O(1), Python tem `collections.deque`, mas isso é outro assunto.

---

## O caso `insert()` na posição certa vs `append()` + `sort()`

Voltando à questão original: qual é mais eficiente para montar uma lista ordenada?

### Opção 1: inserir na posição certa a cada vez (insertion sort)

```python
lista = []
for item in dados:
    # acha a posição certa e insere
    i = 0
    while i < len(lista) and lista[i] < item:
        i += 1
    lista.insert(i, item)
```

Cada `insert()` é O(n). Fazendo isso para n elementos: **O(n²) no total**.

### Opção 2: append no final, sort no final

```python
lista = []
for item in dados:
    lista.append(item)   # O(1)
lista.sort()             # O(n log n)
```

O `sort()` é chamado uma vez só no final. Total: **O(n log n)**.

### Comparação com números reais

Para uma lista de 10.000 elementos, considerando que cada operação básica leva 1 microssegundo:

| Abordagem | Operações aproximadas | Tempo estimado |
|-----------|----------------------|----------------|
| insert na posição certa | 10.000² / 2 = 50 milhões | ~50 segundos |
| append + sort | 10.000 × log₂(10.000) ≈ 130.000 | ~0,13 segundo |

A diferença é de centenas de vezes. Para listas grandes, `append + sort` não é só "um pouco melhor": é uma ordem de magnitude diferente. Na prática, eu quase nunca uso `insert()` dentro de um laço nos meus próprios projetos, viciei em escrever `append()` e deixar o `sort()` pro final, e essa conta é o motivo.

### Quando faz sentido inserir na posição certa?

Existem situações onde manter a lista ordenada a cada inserção faz sentido:

1. **A lista já está ordenada e você insere um item por vez**: usar `bisect.insort()` (busca binária para encontrar a posição, O(log n); veja o [Apêndice: Algoritmos Notáveis](algoritmos_notaveis.md) se quiser entender como ela funciona por dentro) ainda tem custo O(n) por causa do deslocamento, mas o fator constante é menor.

2. **Você precisa que a lista esteja ordenada após cada inserção**, não só no final: ou seja, você consulta a lista entre inserções e precisa sempre encontrar os dados em ordem.

3. **A lista é pequena**: para n < ~100, a diferença é imperceptível na prática.

```python
import bisect

# bisect.insort encontra a posição com busca binária
# e insere: ainda O(n) pelo deslocamento, mas mais rápido na prática
lista = [1, 3, 5, 7]
bisect.insort(lista, 4)
print(lista)   # [1, 3, 4, 5, 7]
```

Se você precisar de inserções e remoções ordenadas com custo O(log n) de verdade, a estrutura certa é uma **heap** (`heapq`) ou uma árvore balanceada, estruturas de dados que você vai ver em Algoritmos e Estruturas de Dados.

---

## Resumo prático

- Se você está coletando dados e só precisa que estejam ordenados no final: **`append()` + `sort()`**.
- Se você precisa da lista ordenada a cada passo e ela é pequena: **`bisect.insort()`**.
- Se ela é grande e você tem muitas inserções e consultas intercaladas: **outra estrutura de dados**.
- **Nunca** use `insert()` dentro de um laço que percorre a lista inteira se puder evitar: você está escrevendo O(n²) sem perceber.
