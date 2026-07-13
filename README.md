# Fundamentos de Programação

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Licença: MIT + CC BY-SA 4.0](https://img.shields.io/badge/Licença-MIT%20%2B%20CC%20BY--SA%204.0-yellow?style=flat)
![Contribuições bem-vindas](https://img.shields.io/badge/contribuições-bem--vindas-brightgreen?style=flat)
![Idioma: Português](https://img.shields.io/badge/idioma-Português-009c3b?style=flat)

Material de apoio à monitoria de CI182/CI240: Fundamentos de Programação de Computadores da UFPR. Feito por um estudante e monitor, com o objetivo de ajudar quem está aprendendo e fixar melhor o próprio conteúdo.

Não sou profissional nem nenhum programador avançado, fico feliz em ouvir qualquer sugestão ou correção de erros. Veja o [CONTRIBUTING.md](CONTRIBUTING.md) se quiser ajudar.

---

## O que tem aqui

O material principal é `docs/aulas/`: 19 aulas completas em Markdown (`00` a `18`), mais uma despedida (`19`) fechando o material. Cada uma tem explicação, exemplos de código e exercício sugerido no final.

Pra praticar sem depender só da leitura:

- **`docs/exemplos/`**: arquivos Python comentados, um por aula, pra consultar sintaxe e ver padrões funcionando.
- **`docs/listas/`**: listas de exercícios oficiais da disciplina, em PDF e TXT.
- **`docs/gabaritos/`**: gabaritos das listas, abrindo direto no Google Colab. Tente resolver antes de olhar.
- **`docs/respostas/`**: minhas respostas dos exercícios sugeridos ao final de cada aula.
- **`docs/debug/`**: programas com bugs intencionais, separados por dificuldade, pra treinar leitura de erro e correção de código (sem gabarito, de propósito).

Material de referência, tudo em `docs/extras/`:

- **`glossario.md`**: termos técnicos explicados sem jargão, do jeito que eu explicaria numa monitoria de verdade.
- **`faq.md`**: dúvidas frequentes com resposta direta.
- **`referencia_rapida.md`**: consulta rápida de sintaxe e métodos, pra quando você já sabe o conceito e só precisa lembrar como se escreve.
- **`unicode_referencia.md`**: caracteres Unicode úteis pra imprimir tabuleiros, barras de progresso e esse tipo de coisa.

E duas coisas que foram além do que eu planejei originalmente:

- **`docs/apendices/`**: explicações mais fundas sobre temas que só aparecem de leve nas aulas (custo de operações, algoritmos de busca, como funciona uma tabela hash, ambiente de desenvolvimento avançado). Não cai na disciplina, é só pra quem ficou curioso.
- **`docs/projetos/`**: programas maiores e completos, escritos usando só o que as aulas ensinam. O [`copa_penaltis`](docs/projetos/copa_penaltis/README.md) é uma disputa de pênaltis interativa inteira, com seleções reais e tudo.

O [`docs/guia_de_estudo.md`](docs/guia_de_estudo.md) amarra tudo isso: como usar o repositório, o mapa das listas pras aulas, e uma referência de erros comuns.

---

## Por onde começar

Abra [`docs/aulas/00_boas_vindas.md`](docs/aulas/00_boas_vindas.md).

---

## O que ainda quero fazer

- **GitHub Pages**: transformar o material em um site navegável, com busca e sumário lateral. A ideia está clara, falta tempo e foco.
- Mais exercícios de debug no nível difícil (hoje são só 3, contra 8 de fácil e 8 de médio).

---

## Exemplos disponíveis

Cada arquivo corresponde a uma aula. O nome segue o mesmo padrão de `docs/aulas/`.

| Arquivo | Aula | Conteúdo |
|---------|------|----------|
| `docs/exemplos/03_python_basico.py` | Aula 03 | Variáveis, tipos, conversão e operações básicas |
| `docs/exemplos/04_operadores.py` | Aula 04 | Operadores aritméticos, relacionais, lógicos e de atribuição |
| `docs/exemplos/05_entrada_saida.py` | Aula 05 | `print`, `input`, f-string e formatação |
| `docs/exemplos/06_condicionais.py` | Aula 06 | `if`, `elif`, `else` e `match` |
| `docs/exemplos/07_repeticao.py` | Aula 07 | `while`, `for`, `range`, `break`, `continue` e laços aninhados |
| `docs/exemplos/08_strings.py` | Aula 08 | Indexação, fatiamento, métodos e formatação de strings |
| `docs/exemplos/09_listas.py` | Aula 09 | Criação, acesso, métodos e iteração em listas |
| `docs/exemplos/10_matrizes.py` | Aula 10 | Matrizes (listas de listas) e percurso com índices |
| `docs/exemplos/11_dicionarios.py` | Aula 11 | Dicionários: criação, acesso, iteração e contagem |
| `docs/exemplos/12_tuplas_sets.py` | Aula 12 | Tuplas (imutabilidade, desempacotamento) e conjuntos |
| `docs/exemplos/13_funcoes.py` | Aula 13 | Funções, `*args`, `**kwargs`, lambda e recursão |
| `docs/exemplos/14_arquivos.py` | Aula 14 | Leitura, escrita e manipulação de arquivos texto |
| `docs/exemplos/15_modulos.py` | Aula 15 | Módulos `math`, `random`, `os` e `datetime` |
| `docs/exemplos/16_objetos_classes.py` | Aula 16 | Classes, atributos, métodos e `__str__` |
| `docs/exemplos/17_poo.py` | Aula 17 | Herança, encapsulamento e polimorfismo |
| `docs/exemplos/18_avancado.py` | Aula 18 | Compreensões, exceções, `zip`, `enumerate` e type hints |

---

## Licença

O código-fonte (arquivos `.py`) está sob licença [MIT](LICENSE). O conteúdo escrito (aulas, FAQ, glossário, apêndices e demais `.md`) está sob [Creative Commons BY-SA 4.0](LICENSE-CONTENT).

`docs/listas/` é material oficial da disciplina CI182/CI240 da UFPR, elaborado no âmbito da monitoria sob supervisão da professora responsável. Nenhuma das duas licenças acima cobre esses arquivos; eles estão aqui só como referência de apoio.
