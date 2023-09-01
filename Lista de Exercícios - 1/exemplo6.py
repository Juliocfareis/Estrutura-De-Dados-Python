#Q.6
numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("O número deve ser positivo.")
else:

    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é: {fatorial}")
