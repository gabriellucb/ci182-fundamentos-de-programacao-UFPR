# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Condicionais
# ────────────────────────────────────────────────────────────
#
# O programa calcula a multa por excesso de velocidade
# de acordo com as faixas do Código de Trânsito Brasileiro:
#
#   Dentro do limite              →  sem multa
#   Até 20% acima do limite      →  Infração leve       — R$  88,38
#   Mais de 20% até 50% acima   →  Infração média      — R$ 130,16
#   Mais de 50% até 100% acima  →  Infração grave      — R$ 195,23
#   Mais de 100% acima           →  Infração gravíssima — R$ 880,41
#
#   Reincidentes pagam 50% a mais.
#
# Exemplo (limite: 60 km/h, velocidade: 78 km/h, não reincidente):
#
#   Excesso: 30.0%
#   Situação: Infração média
#   Multa: R$ 130.16
#
# O programa tem mais de um erro. Encontre e corrija todos.
# ────────────────────────────────────────────────────────────

velocidade_limite = int(input("Velocidade permitida (km/h): "))
velocidade_real   = int(input("Velocidade registrada (km/h): "))
reincidente       = input("Reincidente? (s/n): ")

excesso_percentual = velocidade_real / velocidade_limite * 100

if velocidade_real <= velocidade_limite:
    situacao = "Dentro do limite"
    multa    = 0.0
elif excesso_percentual <= 50:
    situacao = "Infração leve"
    multa    = 88.38
elif excesso_percentual <= 20:
    situacao = "Infração média"
    multa    = 130.16
elif excesso_percentual <= 100:
    situacao = "Infração grave"
    multa    = 195.23
else:
    situacao = "Infração gravíssima"
    multa    = 880.41

if reincidente != "s":
    multa = multa * 1.5

print(f"\nExcesso: {excesso_percentual:.1f}%")
print(f"Situação: {situacao}")
print(f"Multa: R$ {multa:.2f}")
