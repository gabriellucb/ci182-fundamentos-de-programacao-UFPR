"""Card de jogador de futebol — f-string, alinhamento, sep, end, \n e \t.

Talvez você ja perdeu algumas horas comparando stats de jogador no Ultimate Team.
Esse programa gera o card formatado de qualquer jogador criado pelo usuário
com as barras de atributo calculadas na hora.

Os símbolos usados na saída (█ e ░) são caracteres Unicode, strings normais. 
Para usá-los no seu código, copie daqui mesmo ou pesquise "unicode block elements" 
em qualquer tabela online. No VS Code você também consegue pelo comando: 
Ctrl+Shift+P -> "Insert Unicode character".

Conceitos: input(), split(), int(), f-string com alinhamento <> e ^,
           fill + ^, sep, end, \\n, \\t.
"""

print("=== GERADOR DE CARD DE JOGADOR ===\n")

nome    = input("Nome do jogador: ")
posicao = input("Posição (ex: ATA, MEI, ZAG, GOL): ")
nac     = input("Nacionalidade (ex: BRA, ARG, FRA): ")

print("\nDigite os 6 atributos separados por espaço (0–99):")
print("  PAC   FIN   PAS   DRI   DEF   FIS\n")

pac_s, fin_s, pas_s, dri_s, def_s, fis_s = input("Stats: ").split()

pac    = int(pac_s)
fin    = int(fin_s)
pas    = int(pas_s)
dri    = int(dri_s)
defesa = int(def_s)
fis    = int(fis_s)

overall = round((pac + fin + pas + dri + defesa + fis) / 6)

BAR = 16

bar_pac = "█" * int(pac    / 99 * BAR) + "░" * (BAR - int(pac    / 99 * BAR))
bar_fin = "█" * int(fin    / 99 * BAR) + "░" * (BAR - int(fin    / 99 * BAR))
bar_pas = "█" * int(pas    / 99 * BAR) + "░" * (BAR - int(pas    / 99 * BAR))
bar_dri = "█" * int(dri    / 99 * BAR) + "░" * (BAR - int(dri    / 99 * BAR))
bar_def = "█" * int(defesa / 99 * BAR) + "░" * (BAR - int(defesa / 99 * BAR))
bar_fis = "█" * int(fis    / 99 * BAR) + "░" * (BAR - int(fis    / 99 * BAR))

LARGURA = 40

print()
print("Gerando card", end="")
print(".", end="")
print(".", end="")
print(".", end="\n\n")

topo = str(overall) + "  •  " + posicao + "  •  " + nac

print("=" * LARGURA)
print(f"{topo:^{LARGURA}}")
print(f"{nome:^{LARGURA}}")
print("=" * LARGURA)
print()
print(f"\t{'PAC':<6} {bar_pac} {pac:>2}")
print(f"\t{'FIN':<6} {bar_fin} {fin:>2}")
print(f"\t{'PAS':<6} {bar_pas} {pas:>2}")
print(f"\t{'DRI':<6} {bar_dri} {dri:>2}")
print(f"\t{'DEF':<6} {bar_def} {defesa:>2}")
print(f"\t{'FIS':<6} {bar_fis} {fis:>2}")
print()
print("=" * LARGURA)
print(posicao, nac, str(overall) + " OVR", sep="  ·  ")
