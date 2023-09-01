#Q.4
numero = int(input("Digite um número: "))

print(f"Números pares de 0 até {numero}:")
for i in range(0, numero + 1):
    if i % 2 == 0:
        print(i)