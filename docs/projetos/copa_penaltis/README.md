# Copa do Mundo de Pênaltis

Todo torcedor conhece a sensação: o Brasil chega nos pênaltis e o coração some. A ideia aqui é te botar no comando disso. Você pega a Seleção do começo do mata-mata até a final, escala os batedores, escolhe o goleiro, bate os pênaltis do Brasil e defende quando é o adversário na bola. Se chegar até o fim, vem o aguardado hexa. Se não... bom, fica pra próxima Copa.

No fim de cada campanha você vê o aproveitamento de cada batedor, e o resultado fica salvo pra quando você abrir o jogo de novo.

## Como jogar

```bash
python3 main.py
```

A primeira coisa que ele pergunta é a dificuldade:

| Dificuldade | O que muda |
| --- | --- |
| Fácil | Começa já nas oitavas (pula o grupo "Fraco"): quatro fases |
| Normal | Chaveamento completo, dos dezesseis avos à final: cinco fases |
| Difícil | O piso sobe: já começa contra o grupo Médio e ainda pega três seleções de elite seguidas no fim |

## Estrutura do código

Como a Aula 15 fala de módulos, quis que o projeto praticasse o que ensina em vez de virar um `main.py` gigante. Então ele é dividido assim:

| Arquivo | Conteúdo |
| --- | --- |
| `jogadores.py` | As classes `Jogador`, `Goleiro` e `Selecao`; a lógica de confiança e a escolha de direção/lado; o ranking `CONFIANCA_INDIVIDUAL` |
| `campeonato.py` | Fases, grupos de dificuldade, bandeiras, as escalações reais dos adversários e o sorteio |
| `partida.py` | As regras de uma disputa de pênaltis: cada cobrança, o fim antecipado e a morte súbita |
| `visual.py` | A parte bonita: cores do terminal, molduras, barra de confiança e o quadro do placar |
| `main.py` | A escalação do Brasil e o loop do campeonato; é por onde o jogo começa |

## O chaveamento (no Normal)

São cinco fases, cada uma mais dura que a anterior. O adversário de cada uma é **sorteado** dentro de um grupo de dificuldade, então o caminho até a final nunca é igual duas vezes:

| Fase | Grupo | Possíveis adversários |
| --- | --- | --- |
| Dezesseis avos de final | Fraco | Uruguai, Colômbia, México, Estados Unidos, Japão, Suíça, Cabo Verde |
| Oitavas de final | Médio | Holanda, Bélgica, Croácia, Marrocos, Noruega |
| Quartas de final | Forte | Alemanha, Inglaterra, Portugal |
| Semifinal | Elite | Argentina, França ou Espanha |
| Final | Elite | uma das seleções de elite que não caíram antes |

As fases de elite sorteiam seleções diferentes entre si, então você nunca pega o mesmo time de elite duas vezes na mesma Copa. Perdeu em qualquer fase, acabou. No Fácil o chaveamento começa nas oitavas; no Difícil ele já começa pegado e chega a três elites seguidas.

## Escalação

Você monta os 5 batedores a partir de um elenco de 10, na ordem em que vão cobrar. A lista aparece ordenada por confiança, do mais confiante ao menos, e vai sumindo quem você já escalou (continua ordenada) até fechar os cinco. Depois é a vez do goleiro: os três do Brasil têm estilos de defesa diferentes, então a escolha pesa.

Essa escalação vale pra Copa inteira, não só pra uma partida, e a confiança de cada jogador viaja junto com ele. Se um jogo empatar depois das cinco cobranças e for pra morte súbita, aí você escolhe reserva por reserva quem vai bater, respeitando a regra de verdade: todo mundo bate uma vez antes de alguém repetir.

## Características dos batedores

Nos times mais fracos, a característica de cada jogador **geralmente** define confiança e estilo de chute de uma vez só:

| Característica | Efeito |
| --- | --- |
| Alta Confiança | Confiança inicial alta, quase não sente a pressão da fase |
| Baixa Confiança | Confiança inicial baixa, sente a pressão da fase com tudo |
| Finalizador Técnico | Prefere bater no meio; devastador se o goleiro já pulou |
| Chute Forte | Chute difícil de segurar mesmo quando o goleiro acerta o lado, mas erra o alvo com mais frequência |
| Padrão | Sem vantagem nem desvantagem especial |

Do grupo Médio pra cima, a característica passa a ser só o estilo de chute (Finalizador Técnico, Chute Forte ou Padrão), e a confiança de cada um vem de um ranking individual de qualidade (`CONFIANCA_INDIVIDUAL`, no `jogadores.py`). É por isso que um Mbappé já começa lá em cima e quase não sente a pressão: ele só vacila mais se a cobrança for decisiva ou se o goleiro estiver embalado.

Do lado do Brasil, **Neymar, Vinícius Jr e Raphinha** também têm nota individual, e o Neymar é o batedor mais confiante do jogo inteiro (como manda a fama). O resto do elenco segue pelo arquétipo da característica.

## Características dos goleiros

| Característica | Efeito |
| --- | --- |
| Parede | Quando acerta o lado, defende com chance bem mais alta |
| Antecipa | Quase nunca fica parado no meio; cai mais vezes pro lado pra onde a bola costuma ir |
| Lado Preferido | Tende a pular sempre pro mesmo lado |
| Inseguro | Defende com chance mais baixa mesmo acertando o lado |

## Nervosismo: a confiança que muda o tempo todo

A confiança de cada jogador não fica parada. Ela mexe a cada cobrança, juntando três coisas:

1. **A base**, que vem da característica ou do ranking, como expliquei acima.
2. **O peso da fase**, que cresce a cada rodada do chaveamento. Ele derruba a mira de todo mundo, mas machuca muito mais um `Baixa Confiança` do que um `Alta Confiança`.
3. **O que acabou de acontecer**: marcar sobe um pouco a confiança, errar derruba bem mais. E uma cobrança que pode fechar o jogo carrega uma pressão extra só naquele instante.

Isso tudo **persiste entre as fases**. Quem errou nos dezesseis avos chega mais trêmulo na final. De uma fase pra outra, batedores e goleiro recuperam só metade do caminho de volta ao valor inicial, não zeram o estrago.

E tem o **goleiro embalado**: goleiro que defende fica quente, e cada defesa seguida joga uma pressão a mais em cima do próximo cobrador. É aquele terror da vida real de bater contra quem está pegando tudo. Basta ele levar um gol pra sequência zerar.

## Regras da disputa

- Você **escolhe primeiro** (a direção do seu chute, ou o lado do seu goleiro), e só depois o jogo revela no que deu. Escolher certo não garante nada: dá pra chutar pra fora no nervoso mesmo mandando pro canto que você queria.
- São até 5 cobranças por lado, mas o confronto pode acabar antes se a conta já não fechar pro outro lado (regra de verdade).
- Qualquer cobrança que possa decidir o jogo entra como **decisiva**, com pressão extra, não só a última: vale tanto o "marca e classifica" quanto o "erra e está fora".
- Empatou depois das cinco de cada lado, vai pra **morte súbita**: um de cada lado, e decide na hora em que um faz e o outro perde.

E o goleiro adversário você conhece jogando: a **primeira** cobrança contra ele é no escuro. Depois dela o jogo te conta o tipo dele ("Deu pra sentir: fulano é do tipo Parede"), como se você tivesse estudado o goleiro na primeira batida. Dali pra frente, use a informação a seu favor.

## No fim da Copa

Terminou a campanha (campeão, vice ou eliminado), o jogo mostra o aproveitamento de cada batedor, do melhor pro pior, e aponta o **Cara da Copa**: quem mais converteu cobrança decisiva. Cada campanha também fica guardada num `historico.txt`, então quando você abrir o jogo de novo ele lembra quantas Copas você já jogou, quantos títulos levou e como foram as últimas.

## Na tela

Tentei deixar o jogo com cara de jogo, não de planilha: tem cores, bandeira das seleções e um placar que mostra uma bolinha por cobrança (⚽ gol, ✗ erro, · quem ainda não bateu), além de uma barra de confiança pra cada batedor. As mensagens também não despejam tudo de uma vez, tem uma pausinha antes de cada resultado pra dar aquele suspense, e a narração de cada lance varia pra não cansar. Essa parte toda mora no `visual.py`. Se o seu terminal não aceitar cores ou emoji, tranquilo: é só apagar os códigos de cor lá no começo do `visual.py` que o jogo roda igual.