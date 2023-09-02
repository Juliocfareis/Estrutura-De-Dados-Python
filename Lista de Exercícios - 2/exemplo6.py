class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Camiseta", 20, 3)
produto2 = Produto("Notebook", 800, 1)

total_produto1 = produto1.calcular_total()
total_produto2 = produto2.calcular_total()

print(f"Total do {produto1.nome}: R${total_produto1}")
print(f"Total do {produto2.nome}: R${total_produto2}")
