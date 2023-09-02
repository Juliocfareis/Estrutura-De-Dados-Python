class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} está falando.")

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pessoa1.falar()
pessoa2.falar()
