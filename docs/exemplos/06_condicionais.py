"""Laudo Clínico do Estudante: condicionais, operadores lógicos, comparações.

Todo semestre tem aquela semana onde você olha pro calendário e percebe
que a prova é daqui a dois dias e você viu quarenta porcento do conteúdo.
Esse programa recebe seus dados e emite um diagnóstico técnico e honesto 
sobre suas chances de sobrevivência na prova.

Esse é um código grande de propósito, para ver o uso de diversos condicionais
e outros conceitos de uma vez só.

Conceitos: if, elif, else, and, or, not, ==, !=, <, >, <=, >=, aninhamento.
"""

LARGURA = 54

print("=" * LARGURA)
print(f"{'LAUDO CLÍNICO DO ESTUDANTE':^{LARGURA}}")
print("=" * LARGURA)
print()

nome        = input("Paciente: ")
curso       = input("Curso: ")
periodo     = int(input("Período atual: "))
tempo_livre = int(input("Quantas horas por dia tem livres: "))

print()
print("[SINAIS VITAIS]")
horas_sono   = float(input("Horas dormidas ontem: "))
cafeina      = int(input("Cafés/Energéticos consumidos hoje: "))
horas_estudo = float(input("Horas estudadas ontem: "))
conteudo     = float(input("Conteúdo dominado até agora (%): "))
dias_prova   = int(input("Dias até a próxima prova: "))
materias_rep = int(input("Matérias com risco de reprovação: "))

horas_livres   = dias_prova * tempo_livre
conteudo_falta = 100.0 - conteudo

sono_insuficiente = horas_sono < 6
cafeinado_demais  = cafeina > 4
estudo_solido     = horas_estudo >= 4 and conteudo >= 50
tempo_ok          = dias_prova >= 3


# Análise do estado
if horas_sono < 3:
    estado   = "ZUMBI"
    obs_sono = "funcionamento básico comprometido"
elif horas_sono < 5 and cafeina >= 5:
    estado   = "COLAPSADO"
    obs_sono = "o coração pediu arrego"
elif horas_sono < 5:
    estado   = "SONAMBULO"
    obs_sono = "metade presente, metade já no sonho"
elif horas_sono < 7 and cafeina >= 4:
    estado   = "ARTIFICIALMENTE ESTIMULADO"
    obs_sono = "cafeína tampando o buraco do sono"
elif horas_sono < 7:
    estado   = "NO LIMITE"
    obs_sono = "operando na economia de energia"
elif horas_sono >= 8 and cafeina == 0:
    estado   = "DESCANSADO"
    obs_sono = "suspeito de não ter prova na semana"
else:
    estado   = "SOBREVIVENDO"
    obs_sono = "dentro da média nacional do estudante"


# Análise de risco
if dias_prova == 0:
    risco     = "DESESPERADOR"
    obs_risco = "a prova é HOJE, abre o material agora!!!"
elif dias_prova == 1 and conteudo < 40:
    risco     = "CRÍTICO"
    obs_risco = "24h, foque no que mais cai na prova"
elif dias_prova <= 2 and conteudo < 60:
    risco     = "ALTO"
    obs_risco = "Se não for o suficiente, da pra trocar umas horas de sono pelo estudo"
elif dias_prova <= 5 and conteudo < 40:
    risco     = "ALTO"
    obs_risco = "tempo existe, se dedique"
elif dias_prova <= 5 and conteudo >= 70:
    risco     = "MODERADO"
    obs_risco = "revisão estratégica resolve"
elif dias_prova > 5 and conteudo >= 80:
    risco     = "BAIXO"
    obs_risco = "tranquilo, revisa os pontos fracos"
else:
    risco     = "MODERADO"
    obs_risco = "controlável com disciplina"


# Análise de estudo
if horas_estudo == 0:
    qualidade  = "AUSENTE"
    obs_estudo = "conteúdo não entra por osmose"
elif horas_estudo < 1:
    qualidade  = "SIMBÓLICO"
    obs_estudo = "abriu o material, já é alguma coisa"
elif horas_estudo < 2 and conteudo < 30:
    qualidade  = "ILUSÓRIO"
    obs_estudo = "horas e progresso não estão alinhados"
elif horas_estudo < 3:
    qualidade  = "MÍNIMO"
    obs_estudo = "o esforço existe, mas da para melhorar"
elif horas_estudo >= 5 and conteudo >= 60:
    qualidade  = "BOM"
    obs_estudo = "sólido, continue assim"
elif horas_estudo >= 7 and conteudo >= 80:
    qualidade  = "EXCELENTE"
    obs_estudo = "você é o tipo que salva a média da turma"
else:
    qualidade  = "REGULAR"
    obs_estudo = "dá para melhorar isso aí"


em_risco_grave = materias_rep >= 3 or (materias_rep >= 2 and conteudo < 40)
corpo_ok       = not sono_insuficiente and not cafeinado_demais


# Veredito
if em_risco_grave and not corpo_ok:
    veredicto = "SITUAÇÃO CRÍTICA"
    rx_1      = "Reduza o café. Durma pelo menos 6h. Isso não é só um conselho."
    rx_2      = "Priorize uma matéria por vez, da mais pesada à mais fácil."
elif em_risco_grave:
    veredicto = "EM RISCO"
    rx_1      = "Várias matérias na corda bamba."
    rx_2      = "Qualidade > quantidade, foque no que mais cai."
elif not corpo_ok and not estudo_solido:
    veredicto = "COLAPSO IMINENTE"
    rx_1      = "Sem sono e sem estudo. Não vai acabar bem."
    rx_2      = "Pare, durma, recomece com cabeça fria. Sério."
elif estudo_solido and corpo_ok and tempo_ok:
    veredicto = "NO CAMINHO CERTO"
    rx_1      = "Mantenha o ritmo."
    rx_2      = "Você vai bem, não relaxe agora."
elif estudo_solido and not tempo_ok:
    veredicto = "BOA DISCIPLINA, TEMPO CURTO"
    rx_1      = "Estudo sólido, prazo apertado."
    rx_2      = "Seja cirúrgico e foque no que mais pesa na prova."
elif not estudo_solido and tempo_ok:
    veredicto = "TEMPO HÁ, FALTA CONSISTÊNCIA"
    rx_1      = "Você tem tempo mas precisa melhorar o método de estudo."
    rx_2      = "Senta e abre o material."
else:
    veredicto = "SITUAÇÃO AMBÍGUA"
    rx_1      = "Dados inconclusivos, mas estudar mais nunca fez mal."
    rx_2      = "Na dúvida dorme cedo, acorda cedo, não toma muita cafeína e estuda."


# Relatório final
print()
print("=" * LARGURA)
print(f"  Paciente  : {nome}")
print(f"  Curso     : {curso}  |  {periodo}º período")
print("=" * LARGURA)
print()
print(f"  'ESTADO FÍSICO' [{estado}]")
print(f"  Sono: {horas_sono}h  Café: {cafeina}x  |  {obs_sono}")
print()
print(f"  'RISCO ACADÊMICO' [{risco}]")
print(f"  Prova em {dias_prova}d  |  {conteudo}% dominado  |  {obs_risco}")
print(f"  Matérias em risco : {materias_rep}  |  Horas livres est. : {horas_livres}h")
if dias_prova > 0:
    print(f"  Meta diária       : {round(conteudo_falta / dias_prova, 1)}% do conteúdo restante por dia")
print()
print(f"  'ESTUDO' [{qualidade}]")
print(f"  {horas_estudo}h ontem  |  {obs_estudo}")
print()
if periodo == 1 and risco != "BAIXO":
    print("  >> Nota: primeiros semestres são pesados mesmo; é normal.")
    print()
elif periodo != 1 and materias_rep > 2:
    print(f"  >> Atenção: com {periodo} períodos, esse padrão vira histórico.")
    print()
print("-" * LARGURA)
print(f"{'VEREDICTO: ' + veredicto:^{LARGURA}}")
print("-" * LARGURA)
print()
print("  Prescrição:")
print(f"    {rx_1}")
print(f"    {rx_2}")
print()
print("=" * LARGURA)
print(f"{'Boa sorte. Você consegue.':^{LARGURA}}")
print("=" * LARGURA)
