#Q.8
nomes = input("Digite uma lista de nomes separados por espaços: ").split()

nomes_com_a = [nome for nome in nomes if nome.startswith("A")]

if len(nomes_com_a) == 0:
    print("Não foram encontrados nomes que começam com a letra 'A' na lista.")
else:
    print("Nomes que começam com a letra 'A':")
    for nome in nomes_com_a:
        print(nome)
