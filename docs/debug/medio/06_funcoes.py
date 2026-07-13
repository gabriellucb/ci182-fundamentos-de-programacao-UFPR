# ────────────────────────────────────────────────────────────
# Nível: Médio  │  Tema: Funções
# ────────────────────────────────────────────────────────────
#
# O programa converte uma temperatura em Celsius para
# Fahrenheit e Kelvin e, depois, confirma a conversão inversa.
#
# Saída esperada (temperatura: 100):
#
#   100.0°C = 212.0°F = 373.15 K
#     Se 212.0 fosse Fahrenheit, seria 100.0°C
#
# Saída esperada (temperatura: 0):
#
#   0.0°C = 32.0°F = 273.15 K
#     Se 32.0 fosse Fahrenheit, seria 0.0°C
#
# Encontre e corrija os erros.
# ────────────────────────────────────────────────────────────

def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def celsius_para_kelvin(c):
    return c + 237.15

def fahrenheit_para_celsius(f):
    return (f + 32) * 5 / 9

def exibir_conversoes(celsius):
    f = celsius_para_kelvin(celsius)
    k = celsius_para_kelvin(celsius)
    print(f"{celsius:.1f}°C = {f:.1f}°F = {k:.2f} K")

def resumo(f):
    c = fahrenheit_para_celsius(f)
    print(f"  Se {f:.1f} fosse Fahrenheit, seria {c:.1f}°C")

temperatura = float(input("Temperatura em Celsius: "))
exibir_conversoes(temperatura)
resumo(temperatura)
