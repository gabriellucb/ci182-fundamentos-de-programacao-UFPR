# Bem-vindo ao meu repositório de Fundamentos de Programação!

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Disciplina](https://img.shields.io/badge/UFPR-CI182%20%7C%20CI240-1565C0?style=flat)
![Aulas](https://img.shields.io/badge/aulas-19-orange?style=flat)

Este repositório foi criado para acompanhar as disciplinas **CI182** e **CI240** (Fundamentos de Programação) da UFPR, mas qualquer pessoa pode usá-lo. Seja qual for o caminho que te trouxe até aqui (a disciplina, curiosidade ou o que for), seja bem-vindo!

Dando um pouco de contexto sobre o autor desse material: atualmente sou um aluno de Ciência da Computação na UFPR. Não sou um professor nem um programador experiente. Sou uma pessoa que gosta muito de computação, matemática e também de ensinar. Um amigo no colégio me mostrou a área de programação e de repente parecia que eu tinha encontrado uma coisa que fazia sentido pra mim de um jeito que eu não esperava. Não me arrependi nenhum dia de tudo que me levou a esse curso.

Fiz esse material por alguns motivos: quando entrei na monitoria, me surgiu a ideia de criar um material para ajudar o pessoal da disciplina e vi que não existe um repositório assim para a matéria. Mas também criei porque escrever sobre um assunto é uma das melhores formas de fixar o que você aprendeu.

A linguagem base do repositório e da disciplina é o Python. Ele serve para muita coisa: meu chefe no estágio usa para analisar dados de futebol, outras pessoas usam para automatizar tarefas chatas no computador, criar jogos simples, construir sites, rodar modelos de IA e muito mais. Além disso, a sintaxe é limpa, lê quase como inglês simples. Isso ajuda muito no começo. E não é só usado para coisas básicas: o Instagram, o Spotify e boa parte das ferramentas de IA que você usa no dia a dia têm partes inteiras construídas com Python.

E, se você tinha essa dúvida: o nome não vem da cobra. Vem do grupo de comédia britânico *Monty Python's Flying Circus*. O criador era fã.

---

## O que você vai aprender aqui

Ao longo das aulas deste repositório, você vai descobrir como:

- configurar seu ambiente de desenvolvimento;
- entender um pouco como os computadores "pensam" e como organizar soluções;
- escrever programas que leem dados, tomam decisões e repetem tarefas;
- trabalhar com textos, listas, dicionários e outras estruturas;
- criar funções e organizar o código de forma limpa;
- ler e escrever arquivos, e organizar código em módulos separados;
- entender como Python organiza código em classes, e os quatro pilares da POO: encapsulamento, herança, polimorfismo e abstração;
- usar ferramentas mais avançadas, como compreensões, `zip`/`enumerate` e tratamento de erros com `try/except`.

Não se preocupe se parece muito agora. Cada aula é construída em cima do que você já aprendeu antes. Você pode voltar quantas vezes quiser até o conteúdo pegar.

---

## Como aproveitar melhor este material

**Leia com calma.** Não tem pressa. Entender um conceito de verdade vale mais do que avançar rápido e ficar confuso.

**Execute os exemplos.** Ler código é diferente de rodar código. Abra o seu editor, copie o exemplo e veja funcionando. Mexe nos valores, quebra de propósito, conserta. É assim que acredito que se aprende.

**Não desanime com os erros.** Erro faz parte. Todo programador, do iniciante ao experiente, encontra erros todos os dias.

**Use os exercícios.** Cada aula tem sugestões práticas. Tente resolver antes de procurar respostas prontas. Também inseri uma seção de debug (não vi isso em outros repositórios similares): são códigos quebrados de propósito para você praticar a leitura de erros. Vale explorar depois da Aula 06, quando você já tem base para ler e entender mensagens de erro.

**Use os outros materiais do repositório.** Além das aulas, tem um [glossário](../extras/glossario.md) com definições rápidas para quando você travar num conceito, uma [referência rápida](../extras/referencia_rapida.md) com a sintaxe mais usada em Python e um [guia de estudo](../guia_de_estudo.md) para quem quer organizar melhor o aprendizado. Se tiver alguma dúvida recorrente, dá uma olhada no [FAQ](../extras/faq.md). E se quiser ver o que dá pra fazer só com o que está nas aulas, tem um projeto em [`projetos/copa_penaltis`](../projetos/copa_penaltis/README.md): uma disputa de pênaltis completa e interativa, escrita usando só conceitos que você também vai aprender aqui.

**Volte quando precisar.** Às vezes um conceito que parecia confuso encaixa sozinho depois que você avançou algumas aulas e tem mais contexto.

---

## Estrutura das aulas

| Aula | Tema |
|------|------|
| [01](01_ambiente.md) | Ambiente: instalar Python, VS Code e configurar tudo |
| [02](02_introducao.md) | Introdução: lógica, algoritmos e pensamento computacional |
| [03](03_python_basico.md) | Python Básico: variáveis, tipos e primeiros programas |
| [04](04_operadores.md) | Operadores: cálculos, comparações e lógica |
| [05](05_entrada_saida.md) | Entrada e Saída: receber dados do usuário e exibir resultados |
| [06](06_condicionais.md) | Condicionais: tomar decisões no código |
| [07](07_repeticao.md) | Repetição: automatizar tarefas com laços |
| [08](08_strings.md) | Strings: trabalhar com textos |
| [09](09_listas.md) | Listas: sequências, operações e cópias |
| [10](10_matrizes.md) | Matrizes: listas de listas e aplicações |
| [11](11_dicionarios.md) | Dicionários: pares chave-valor |
| [12](12_tuplas_sets.md) | Tuplas e Sets: imutabilidade e conjuntos |
| [13](13_funcoes.md) | Funções: organizar e reutilizar código |
| [14](14_arquivos.md) | Arquivos: leitura, escrita e persistência |
| [15](15_modulos.md) | Módulos e Bibliotecas: import e biblioteca padrão |
| [16](16_objetos_classes.md) | Objetos e Classes: criar seus próprios tipos |
| [17](17_poo.md) | POO: encapsulamento, herança, polimorfismo e abstração |
| [18](18_avancado.md) | Avançado: compreensões, `zip`/`enumerate`, type hints e tratamento de erros |
| [19](19_despedida.md) | Despedida: não é aula nova, é o fechamento (por onde continuar e uma conclusão pessoal) |

---

## Uma última coisa antes de começar

Aprender a programar não acontece de um dia para o outro. Tem momentos em que parece fácil e momentos em que parece impossível. Eu travei muito algumas vezes, fiquei olhando pra tela sem entender absolutamente nada e achei que não era pra mim. Mas passou. Sempre passa.

O que faz a diferença é continuar.

Se tiver dúvida ou encontrar algum erro, veja o [guia de contribuição](../../CONTRIBUTING.md), lá explica como abrir uma issue, o que preencher e onde tirar dúvidas mais abertas. Não precisa saber programar para isso. Se preferir contato direto, pode me chamar por e-mail em gabriellucas2 [at] ufpr.br.

Boa sorte.

---

## Por onde começar?

→ **[Aula 01: Ambiente de Desenvolvimento](01_ambiente.md)**

Configure seu computador antes de escrever qualquer código. É o primeiro passo e não deve ser pulado. Essa aula não tem código ainda, só configuração de ambiente, mas sem ela o resto não funciona.
