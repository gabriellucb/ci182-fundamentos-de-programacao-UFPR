"""Masmorra: listas de listas, laços aninhados, índices [i][j], enumerate.

Você acorda no chão de uma masmorra sem memória de como chegou aqui. Quem nunca né.
O mapa está riscado na parede: você é o @, os tesouros são $,
as armadilhas são ! e as paredes são #. Encontre os dois tesouros sem morrer.
Você tem três vidas. Boa sorte. Você vai precisar.

Conceitos: listas de listas, acesso [i][j], laços aninhados, enumerate,
           while, break, continue, acumuladores.

Os símbolos ♥ ♡ ★ ☠ são Unicode, strings normais, copie daqui se precisar.
"""

mapa = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '@', '.', '.', '#', '.', '.', '$', '#'],
    ['#', '.', '#', '.', '.', '!', '#', '.', '#'],
    ['#', '.', '#', '#', '.', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '!', '#'],
    ['#', '#', '.', '#', '#', '.', '#', '.', '#'],
    ['#', '$', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '.', '!', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

linhas  = len(mapa)
colunas = len(mapa[0])

jogador_linha = 0
jogador_col   = 0
total_tesouros = 0

for i, linha in enumerate(mapa):
    for j, celula in enumerate(linha):
        if celula == '@':
            jogador_linha = i
            jogador_col   = j
        elif celula == '$':
            total_tesouros += 1

tesouros_coletados = 0
vidas   = 3
passos  = 0
mensagem = f"Missão: encontre {total_tesouros} tesouros."

print("=== MASMORRA ===")
print("w norte  |  s sul  |  a oeste  |  d leste  |  sair encerrar")
print()

while vidas > 0:
    for linha in mapa:
        for celula in linha:
            print(celula, end=" ")
        print()

    print(f"\nVidas: {'♥ ' * vidas}{'♡ ' * (3 - vidas)}")
    print(f"Tesouros: {tesouros_coletados}/{total_tesouros}  |  Passos: {passos}")
    print(mensagem)

    if tesouros_coletados == total_tesouros:
        print(f"\nVocê encontrou todos os tesouros em {passos} passos. Saída desbloqueada.")
        break

    comando = input("\nMover: ").strip().lower()
    print()

    if comando == 'sair':
        print("Você abandona a masmorra. Honra zero, pelo menos está vivo.")
        break

    nova_linha = jogador_linha
    nova_col   = jogador_col

    if comando == 'w':
        nova_linha -= 1
    elif comando == 's':
        nova_linha += 1
    elif comando == 'a':
        nova_col -= 1
    elif comando == 'd':
        nova_col += 1
    else:
        mensagem = "Comando inválido. Use w, s, a ou d."
        continue

    if nova_linha < 0 or nova_linha >= linhas or nova_col < 0 or nova_col >= colunas:
        mensagem = "Os muros da masmorra não cedem."
        continue

    proxima = mapa[nova_linha][nova_col]

    if proxima == '#':
        mensagem = "Parede. Tente outro caminho."
        continue

    mapa[jogador_linha][jogador_col] = '.'

    if proxima == '$':
        tesouros_coletados += 1
        mensagem = f"★ Tesouro encontrado! ({tesouros_coletados}/{total_tesouros})"
    elif proxima == '!':
        vidas -= 1
        mapa[nova_linha][nova_col] = '.'
        if vidas > 0:
            mensagem = f"☠ Armadilha! Você perdeu uma vida. Restam: {vidas}."
        else:
            mapa[nova_linha][nova_col] = '@'
            print()
            for linha in mapa:
                for celula in linha:
                    print(celula, end=" ")
                print()
            print("\n☠  Não sobrou nada. Fim de jogo.")
            break
    else:
        mensagem = ""

    mapa[nova_linha][nova_col] = '@'
    jogador_linha = nova_linha
    jogador_col   = nova_col
    passos += 1
