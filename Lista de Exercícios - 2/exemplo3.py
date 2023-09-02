class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

retangulo1 = Retangulo(4, 6)
retangulo2 = Retangulo(5, 10)

print("Área do Retângulo 1:", retangulo1.calcular_area())
print("Área do Retângulo 2:", retangulo2.calcular_area())
