class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Ford", "Mustang", 2023)

print("Detalhes do Carro 1:")
print(carro1.detalhes())

print("\nDetalhes do Carro 2:")
print(carro2.detalhes())
