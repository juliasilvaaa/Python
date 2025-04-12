pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Crie uma lista com as variaveis do jogo

# Informar o jogador sobre os movimentos = > 0 - Pedra , 1 - Papel, 2 - Tesoura

# Pergunta ao jogador qual movimento ele quer e guarde em uma variavel chamada escolha_jogador, caso a escolha não seja nenhuma das informadas retornar: Escolha Invalida
import random

# Lista e escolha do usuário

print("----------------- Jokenpó ----------------- ")
movimentos = ["Papel", "Tesoura", "Pedra"]
escolha_jogador = int(input("Escolha entre \n 0 - Papel \n 1 - Tesoura \n 2 - Pedra \n"))


# Se caso o usuario digitar um numero invalido
if escolha_jogador == 0:
    print(movimentos[escolha_jogador])
    print(papel)
elif escolha_jogador == 1:
    print(movimentos[escolha_jogador])
    print(tesoura)
elif escolha_jogador == 2:
    print(movimentos[escolha_jogador])
    print(pedra)
else:
    print("Escolha Inválida")


# Escolha CPU
movimentos_cpu = ["Papel", "Tesoura", "Pedra"]
escolha_cpu = random.choice(movimentos_cpu)
print(escolha_cpu)







