"""Resposta: Aula 09 | Listas
Exercício: coleta notas até "fim"/"f", exibe estatísticas,
remove os extremos e conta quantas ficaram acima da média original.
"""

notas = []
while True:
    entrada = input("Digite uma nota (ou 'fim'/'f' para encerrar): ")
    if entrada.lower() in ["fim", "f"]:
        break
    notas.append(float(entrada))

if len(notas) < 3:
    print("São necessárias pelo menos 3 notas para calcular a média aparada.")
else:
    media_original = sum(notas) / len(notas)

    print(f"\nNotas originais: {notas}")
    print(f"Notas ordenadas: {sorted(notas)}")
    print(f"Maior nota:      {max(notas):.1f}")
    print(f"Menor nota:      {min(notas):.1f}")
    print(f"Média original:  {media_original:.2f}")

    notas_aparadas = notas[:]
    notas_aparadas.remove(max(notas_aparadas))
    notas_aparadas.remove(min(notas_aparadas))

    media_aparada = sum(notas_aparadas) / len(notas_aparadas)

    print(f"\nApós remover maior e menor: {notas_aparadas}")
    print(f"Média aparada:              {media_aparada:.2f}")

    acima = 0
    for n in notas:
        if n > media_original:
            acima += 1

    print(f"\nNotas acima da média original: {acima}")
