#Q.5
numeros = input("Digite uma lista de números separados por espaços: ").split()

numeros = [int(numero) for numero in numeros]

if len(numeros) == 0:
    print("A lista está vazia.")
else:

    maior_valor = max(numeros)
    menor_valor = min(numeros)
    
    print(f"O maior valor na lista é: {maior_valor}")
    print(f"O menor valor na lista é: {menor_valor}")