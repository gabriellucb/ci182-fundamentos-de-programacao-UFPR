"""Resposta: Aula 17 | POO
Exercício: Animal com herança, encapsulamento de energia e polimorfismo.
"""


class Animal:
    def __init__(self, nome, som):
        self.nome    = nome
        self.som     = som
        self._energia = 100

    def fazer_som(self):
        print(f"{self.nome} faz {self.som}.")

    def alimentar(self, qtd):
        self._energia += qtd
        if self._energia > 100:
            self._energia = 100
        print(f"{self.nome} comeu. Energia: {self._energia}.")

    def brincar(self):
        if self._energia < 20:
            print(f"{self.nome} está cansado demais para brincar. Energia: {self._energia}.")
            return
        self._energia -= 20
        print(f"{self.nome} brincou! Energia: {self._energia}.")

    def __str__(self):
        return f"{self.nome} (energia: {self._energia})"


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "au au")

    def fazer_som(self):
        print(f"{self.nome} late: AU AU AU!")


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "miau")

    def fazer_som(self):
        print(f"{self.nome} mia suavemente: miau...")


rex    = Cachorro("Rex")
bolinha = Cachorro("Bolinha")
mimi   = Gato("Mimi")
felix  = Gato("Felix")

animais = [rex, bolinha, mimi, felix]

print("=== SONS ===")
for animal in animais:
    animal.fazer_som()

print("\n=== ENERGIA ===")
rex.brincar()
rex.brincar()
rex.brincar()
rex.brincar()
rex.brincar()
rex.brincar()
rex.alimentar(50)
rex.brincar()

print("\n=== ESTADO FINAL ===")
for animal in animais:
    print(f"  {animal}")
