"""Banda de garagem tentando estourar: encapsulamento, herança, polimorfismo, abstração.

Você monta uma banda com vocalista, guitarrista e baterista e decide o que
fazer a cada rodada: ensaiar ou arriscar um show num bar. Cada músico calcula
sua contribuição pro show do próprio jeito, e se o moral desabar demais, ele
larga a banda no meio da turnê. A banda "estoura" quando a fama bate 100.

Conceitos: encapsulamento, herança, polimorfismo, abstração.
"""

import random


class Musico:
    def __init__(self, nome, habilidade):
        self.nome = nome
        self.habilidade = habilidade
        self._moral = 70

    def ensaiar(self):
        self.habilidade = min(self.habilidade + 3, 100)
        self._moral = min(self._moral + 10, 100)

    def perder_moral(self, valor):
        self._moral = max(self._moral - valor, 0)

    def moral(self):
        return self._moral

    def surtou(self):
        return self._moral <= 0

    def qualidade_do_show(self):
        return self.habilidade * 0.5 + self._moral * 0.5

    def __str__(self):
        return f"{self.nome} (habilidade {self.habilidade}, moral {self._moral})"


class Vocalista(Musico):
    def __init__(self, nome, habilidade, alcance_vocal):
        super().__init__(nome, habilidade)
        self.alcance_vocal = alcance_vocal

    def qualidade_do_show(self):
        return self.habilidade * 0.5 + self._moral * 0.3 + self.alcance_vocal * 0.2


class Guitarrista(Musico):
    def __init__(self, nome, habilidade, tecnica_de_solo):
        super().__init__(nome, habilidade)
        self.tecnica_de_solo = tecnica_de_solo

    def qualidade_do_show(self):
        return self.habilidade * 0.5 + self._moral * 0.2 + self.tecnica_de_solo * 0.3


class Baterista(Musico):
    def __init__(self, nome, habilidade, resistencia):
        super().__init__(nome, habilidade)
        self.resistencia = resistencia

    def qualidade_do_show(self):
        return self.habilidade * 0.4 + self._moral * 0.3 + self.resistencia * 0.3


class Banda:
    def __init__(self, nome, musicos):
        self.nome = nome
        self.musicos = musicos
        self._fama = 0
        self._dinheiro = 50.0

    def fama(self):
        return self._fama

    def dinheiro(self):
        return self._dinheiro

    def ensaiar(self):
        print(f"\n{self.nome} ensaia no fundo da garagem.")
        for musico in self.musicos:
            musico.ensaiar()
            print(f"  {musico}")

    def qualidade_do_show(self):
        total = 0
        for musico in self.musicos:
            total += musico.qualidade_do_show()  # polimorfismo: cada um calcula do seu jeito
        return total / len(self.musicos)

    def tocar_no_bar(self):
        qualidade = self.qualidade_do_show()
        publico = int((10 + self._fama) * (qualidade / 100) * random.uniform(0.7, 1.3))
        cache = publico * random.uniform(1.0, 3.0)
        ganho_fama = qualidade / 10

        self._dinheiro += cache
        self._fama += ganho_fama

        print(f"\n{self.nome} sobe ao palco com qualidade {qualidade:.1f}.")
        print(f"  Público: {publico} pessoas, cachê: R$ {cache:.2f}")
        print(f"  Fama ganha: +{ganho_fama:.1f} (total: {self._fama:.1f})")

        if qualidade < 50:
            desgaste = random.randint(25, 40)
            print("  O show foi fraco, e todo mundo sentiu.")
        else:
            desgaste = random.randint(10, 25)

        for musico in self.musicos:
            musico.perder_moral(desgaste)

        self._verificar_saidas()

    def _verificar_saidas(self):
        restantes = []
        for musico in self.musicos:
            if musico.surtou():
                print(f"  {musico.nome} surtou e saiu da banda no meio da turnê.")
            else:
                restantes.append(musico)
        self.musicos = restantes

    def __str__(self):
        return (f"{self.nome}: fama {self._fama:.1f}, dinheiro R$ {self._dinheiro:.2f}, "
                f"{len(self.musicos)} músico(s)")


def exibir_status(banda):
    print(f"\n=== {banda} ===")
    for musico in banda.musicos:
        print(f"  {musico}")


def menu():
    print("\n1. Ensaiar")
    print("2. Tocar num bar")
    print("3. Ver status da banda")
    print("4. Sair")
    return input("Escolha: ")


def main():
    FAMA_PARA_ESTOURAR = 100

    print("=== BANDA DE GARAGEM ===")
    print("A banda começa quase invisível. Ensaie, arrisque um bar, e reze pra moral aguentar.")

    banda = Banda("Ferrugem no Amplificador", [
        Vocalista("Duda", 55, 60),
        Guitarrista("Rafa", 60, 50),
        Baterista("Enzo", 50, 65),
    ])

    exibir_status(banda)

    while True:
        if not banda.musicos:
            print("\nA banda ficou sem ninguém. Fim de carreira antes mesmo de começar.")
            break

        if banda.fama() >= FAMA_PARA_ESTOURAR:
            print(f"\n{banda.nome} estourou! Fama de {banda.fama():.1f} "
                  "e um contrato de gravadora batendo na porta.")
            break

        escolha = menu()

        if escolha == "1":
            banda.ensaiar()
        elif escolha == "2":
            banda.tocar_no_bar()
        elif escolha == "3":
            exibir_status(banda)
        elif escolha == "4":
            print(f"\nVocê encerra a turnê aqui. {banda}")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
