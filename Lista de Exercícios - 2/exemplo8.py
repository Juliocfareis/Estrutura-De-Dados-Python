class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0  

aluno1 = Aluno("Alice", [85, 90, 78, 92])
aluno2 = Aluno("Bob", [])

media_aluno1 = aluno1.calcular_media()
media_aluno2 = aluno2.calcular_media()

print(f"Média das notas de {aluno1.nome}: {media_aluno1}")
print(f"Média das notas de {aluno2.nome}: {media_aluno2}")
