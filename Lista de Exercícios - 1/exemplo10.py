#Q.10
import random

def determine_vencedor(usuario, computador):
    if usuario == computador:
        return "Empate!"
    elif usuario == "pedra":
        return "Você ganhou!" if computador == "tesoura" else "Você perdeu!"
    elif usuario == "papel":
        return "Você ganhou!" if computador == "pedra" else "Você perdeu!"
    elif usuario == "tesoura":
        return "Você ganhou!" if computador == "papel" else "Você perdeu!"

escolhas_possiveis = ["pedra", "papel", "tesoura"]

usuario_escolha = input("Escolha pedra, papel ou tesoura: ").lower()

if usuario_escolha in escolhas_possiveis:
    computador_escolha = random.choice(escolhas_possiveis)
    
    print(f"Você escolheu {usuario_escolha}.")
    print(f"O computador escolheu {computador_escolha}.")
    
    resultado = determine_vencedor(usuario_escolha, computador_escolha)
    print(resultado)
else:
    print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
