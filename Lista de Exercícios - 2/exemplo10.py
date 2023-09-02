class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            print(f"O salário de {self.nome} foi aumentado em R${aumento:.2f}.")
        else:
            print("O percentual de aumento deve ser maior que zero.")

    def consultar_salario(self):
        return self.salario

funcionario1 = Funcionario("Alice", 3000, "Analista")
funcionario2 = Funcionario("Bob", 4500, "Gerente")

funcionario1.aumentar_salario(10)
funcionario2.aumentar_salario(5)

print(f"Novo salário de {funcionario1.nome}: R${funcionario1.consultar_salario():.2f}")
print(f"Novo salário de {funcionario2.nome}: R${funcionario2.consultar_salario():.2f}")
