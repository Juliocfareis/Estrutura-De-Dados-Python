class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14159 * self.raio ** 2
        return area

raio_circulo = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio_circulo)
area = circulo.calcular_area()
print(f"A área do círculo com raio {raio_circulo} é {area:.2f}")

