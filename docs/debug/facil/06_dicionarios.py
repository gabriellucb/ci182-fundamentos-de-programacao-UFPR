# ────────────────────────────────────────────────────────────
# Nível: Fácil  │  Tema: Dicionários
# ────────────────────────────────────────────────────────────
#
# O programa representa um cadastro de aluno e deve exibir
# todas as informações formatadas e a média das notas.
#
# Saída esperada (dados fixos no código):
#
#   Nome:   Maria Clara
#   Curso:  Ciência da Computação
#   Notas:  [8.5, 7.0, 9.2, 6.8]
#   Média:  7.88
#
# Encontre e corrija o erro.
# ────────────────────────────────────────────────────────────

aluno = {
    "nome":    "Maria Clara",
    "curso":   "Ciência da Computação",
    "periodo": 3,
    "turma":   "A",
    "notas":   [8.5, 7.0, 9.2, 6.8],
}

media = sum(aluno["notas"]) / len(aluno)

print(f"Nome:   {aluno['nome']}")
print(f"Curso:  {aluno['curso']}")
print(f"Notas:  {aluno['notas']}")
print(f"Média:  {media:.2f}")
