# Como contribuir

Esse repositório nasceu da minha própria monitoria de CI182/CI240 (veja o [README](README.md) pra entender o projeto todo), e cresceu mais do que eu esperava quando comecei. Contribuições são bem-vindas, desde corrigir um erro de digitação até sugerir uma aula inteira.

---

## Tipos de contribuição

**Erros de conteúdo**: algo explicado de forma errada, código que não funciona, resultado incorreto numa resposta.

**Erros de escrita**: frases confusas, formatação quebrada.

**Sugestões**: um exercício a mais, uma explicação alternativa, um exemplo que faltou, uma seção que faria diferença.

---

## Como reportar um erro

1. Abra uma [issue](../../issues/new/choose).
2. Escolha o template adequado (erro de conteúdo ou sugestão).
3. Preencha as informações pedidas, especialmente: qual arquivo, qual seção ou linha, e o que está errado.

Não precisa saber programar para reportar um problema. Se algo ficou confuso ou mal explicado para você, já é motivo suficiente para abrir uma issue.

---

## Como contribuir com código ou texto

1. Faça um fork do repositório.
2. Crie um branch com um nome descritivo: `fix/aula-07-while` ou `add/exemplo-recursao`.
3. Faça suas alterações.
4. Abra um pull request descrevendo o que mudou e por quê.

---

## Padrões do repositório

Convenções de nomes:

- Arquivos de aula seguem o padrão `NN_nome_do_tema.md` dentro de `docs/aulas/`.
- Exemplos (`docs/exemplos/`) e respostas (`docs/respostas/`) usam a mesma numeração das aulas, mantendo correspondência 1:1 (ex.: `09_listas.md`, `09_listas.py` e a resposta correspondente).
- Código em Python segue PEP 8.
- O idioma do repositório é português brasileiro.

Convenções de conteúdo (estas são as que mais pegam contribuições de boa fé de surpresa, vale ler com atenção):

- **Nunca use conceitos de aulas futuras** em exemplos, respostas ou exercícios de debug. Se o seu PR usa algo que só é ensinado numa aula posterior à que o arquivo pertence, ele vai precisar ser reescrito antes de entrar. Em caso de dúvida, procure o termo em `docs/aulas/` pra confirmar em qual aula ele é introduzido primeiro.
- **Não use travessão (—) em nenhum texto**, nem em código, nem em comentário, nem em prosa. Prefira dois pontos, vírgula, ponto e vírgula ou reformular a frase.
- Arquivos em `docs/debug/` não têm gabarito, não adicione a solução junto.
- Tom de escrita: direto, acolhedor, sem jargão desnecessário, em primeira pessoa quando fizer sentido. Este projeto é feito por um aluno pra colegas, não é material de um professor.
- Termos técnicos entram em `docs/extras/glossario.md`, dúvidas recorrentes em `docs/extras/faq.md`, e conteúdo que vai além da matéria mas é interessante em `docs/apendices/`.

---

## Dúvidas

Prefere tirar uma dúvida antes de abrir uma issue formal? Use a aba **Discussions** do repositório: é o espaço certo para perguntas abertas, ideias em rascunho e conversas sobre o conteúdo.
