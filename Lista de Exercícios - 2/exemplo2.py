class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
livro2 = Livro("1984", "George Orwell")

print("Detalhes do Livro 1:")
print(livro1.detalhes())

print("\nDetalhes do Livro 2:")
print(livro2.detalhes())

