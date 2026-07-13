# Apêndice: Como funciona uma tabela hash

Sets e dicionários são rápidos do jeito que são por causa de uma estrutura chamada **tabela hash**. Você não precisa saber isso para usar sets e dicts, mas entender o mecanismo responde de uma vez por que eles se comportam do jeito que se comportam: sem ordem, sem duplicatas, sem chaves mutáveis.

---

## O problema que a tabela hash resolve

Imagine uma lista com um milhão de emails. Para checar se `"ana@x.com"` está nela, Python percorre do primeiro ao último até achar, ou confirmar que não está. No pior caso, um milhão de comparações.

O problema não é velocidade do processador. É o **algoritmo**: ele depende do tamanho da coleção. Dobrou a lista, dobrou o tempo de busca.

Sets resolvem isso com uma ideia diferente: em vez de procurar, **calcular onde o elemento estaria**.

---

## O que é uma função hash

Uma função hash recebe qualquer valor e devolve um número inteiro. Sempre o mesmo número para o mesmo valor.

```python
hash("ana@x.com")   # um número grande, diferente a cada execução do Python (veja a nota abaixo)
hash(42)             # 42                    (inteiros pequenos mapeiam para si mesmos)
hash((1, 2))          # -3550055125485641917  (tuplas também têm hash, e esse número não muda entre execuções)
hash([1, 2])          # TypeError: unhashable type: 'list'  (listas não têm hash, veja abaixo)
```

A função não precisa ser sofisticada: ela precisa ser **rápida** e **determinista** (mesmo valor, mesmo hash, sempre, *dentro da mesma execução*; mais sobre isso já já).

---

## Como o hash vira um endereço

Internamente, um set é uma lista de "baldes" (*buckets*). Cada balde guarda zero ou um elemento. O número de baldes começa pequeno (8) e cresce conforme o set cresce.

Quando você **adiciona** um elemento:

1. Python calcula o hash do valor
2. Faz `hash(valor) % total_de_baldes` para saber em qual balde colocar
3. Coloca o valor lá

```text
set com 8 baldes:

balde 0: (vazio)
balde 1: (vazio)
balde 2: "carlos"    ← hash("carlos") % 8 == 2
balde 3: (vazio)
balde 4: "ana"       ← hash("ana") % 8 == 4
balde 5: (vazio)
balde 6: "bruno"     ← hash("bruno") % 8 == 6
balde 7: (vazio)
```

> **Nota:** os números de balde acima são ilustrativos, não tente reproduzi-los literalmente. O hash de strings no Python é embaralhado com uma semente aleatória a cada execução do interpretador (por segurança, desde a versão 3.3), então `hash("carlos") % 8` dá um resultado diferente cada vez que você reinicia o Python, mesmo rodando o mesmo código. Já o hash de números inteiros não muda entre execuções, é por isso que o exemplo da seção "Por que inteiros pequenos parecem vir em ordem", mais abaixo, dá pra reproduzir exatamente igual na sua máquina.

Quando você **busca** um elemento:

1. Python calcula o hash do valor procurado
2. Vai direto ao balde `hash(valor) % total_de_baldes`
3. Verifica se aquele balde tem o valor

**Um único cálculo. Zero percurso.** É por isso que `"ana" in meu_set` é instantâneo independente do tamanho do set.

---

## Por que a ordem não existe

Os elementos ficam nos baldes definidos pelo hash, não pela ordem em que foram inseridos. Quando você percorre o set, Python varre os baldes do 0 ao último: a ordem de saída é a ordem dos baldes, não a de inserção.

```python
s = {"bruno", "ana", "carlos"}
# retomando o exemplo de baldes de antes: ana foi pro balde 4, bruno pro 6, carlos pro 2
# Python varre 0→7: aparece carlos(2), ana(4), bruno(6)
print(s)   # {'carlos', 'ana', 'bruno'}: não é a ordem que você digitou (e na sua máquina os baldes provavelmente serão outros)
```

---

## Por que duplicatas são impossíveis

Antes de inserir, Python verifica o balde:

- Balde vazio → insere
- Balde ocupado com o mesmo valor → ignora (já existe)
- Balde ocupado com valor diferente → **colisão** (ver abaixo)

A verificação de "mesmo valor" é automática e acontece a cada `add()`. Por isso `set.add()` nunca duplica elementos: não é uma regra externa, é uma consequência da estrutura.

---

## Colisões

Dois valores diferentes podem ter `hash(x) % N` igual. Isso se chama **colisão** e é inevitável (infinitos valores, finitos baldes).

Python resolve com **endereçamento aberto**: quando o balde destino está ocupado, Python procura o próximo balde disponível seguindo uma sequência calculada. Na busca, o mesmo percurso é repetido até achar o valor ou um balde vazio.

Colisões são raras com uma boa função hash, e o set cresce automaticamente para manter a proporção baixa. O ponto importante: colisões fazem a busca ficar levemente mais lenta, mas na prática o tempo médio ainda é O(1).

---

## Por que listas não podem ser chaves (e tuplas podem)

O hash de um valor precisa ser **estável**: o mesmo hoje, amanhã, durante toda a execução.

Se você pudesse usar uma lista como chave e depois modificasse essa lista, o hash mudaria. O set tentaria buscar no balde novo e não encontraria o elemento, que ficou "fantasma" no balde antigo. A estrutura inteira corromperia.

Por isso Python exige que chaves de dicionário e elementos de set sejam **imutáveis**: tipos que não podem mudar depois de criados. Strings, números e tuplas são imutáveis e têm hash. Listas e dicionários são mutáveis e não têm.

```python
s = set()
s.add((1, 2))    # OK: tupla é imutável
s.add([1, 2])    # TypeError: unhashable type: 'list'
```

---

## Por que inteiros pequenos parecem vir "em ordem" nos sets

Para inteiros, `hash(n) == n`. Para um set de `{5, 1, 4, 2, 3}` com 8 baldes:

```text
hash(1) % 8 = 1  → balde 1
hash(2) % 8 = 2  → balde 2
hash(3) % 8 = 3  → balde 3
hash(4) % 8 = 4  → balde 4
hash(5) % 8 = 5  → balde 5
```

Esse aqui você pode reproduzir exatamente igual na sua máquina (diferente do exemplo de strings lá em cima). Percorrendo os baldes de 0 a 7: `{1, 2, 3, 4, 5}`, parece ordenado. Não é: é uma coincidência do hash de inteiros pequenos no CPython. Com números maiores ou strings, a ilusão desaparece.

---

## Tabela comparativa

| Operação | Lista | Set / Dict |
| --- | --- | --- |
| Busca (`x in`) | O(n), percorre tudo | O(1), calcula o hash |
| Inserção | O(1) amortizado | O(1) amortizado |
| Remoção por valor | O(n), procura primeiro | O(1), calcula o hash |
| Garante ordem | Sim (inserção) | Não |
| Permite duplicatas | Sim | Não |

---

## Onde ver mais

- [Custo de operações em listas](custo_de_operacoes.md): como listas funcionam internamente e por que `insert()` é mais caro que `append()`
- [Algoritmos Notáveis](algoritmos_notaveis.md): busca linear é O(n), assim como buscar num set sem hash seria; busca binária é O(log n), mais rápida que isso mas ainda longe do O(1) de um hash
- Python docs: [`object.__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__)
