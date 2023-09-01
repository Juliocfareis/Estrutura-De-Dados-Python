#Q.7
limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))

numero_anterior = 0
numero_atual = 1

print("Sequência de Fibonacci:")
while numero_atual <= limite:
    print(numero_atual, end=" ")
    proximo_numero = numero_anterior + numero_atual
    numero_anterior = numero_atual
    numero_atual = proximo_numero

print() 
