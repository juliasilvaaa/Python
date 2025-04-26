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

movimentos = [papel, tesoura, pedra]
escolha_jogador = (input("Escolha entre \n 0 - Papel \n 1 - Tesoura \n 2 - Pedra \n"))


# Se escolha do jogador não estiver entre... 
if escolha_jogador not in ["0","1","2"]:
    print("Opçao Inválida")

# Todo 4
# Printar a escolha dp jogador em uma lista, os desenhos estao em uma lista
# Primeiro item da lista [0]
escolha_jogador = int(escolha_jogador)
print(movimentos[escolha_jogador])

# Sortear numero da CPU
import random
# Lembre-se do random int(0,2)
escolha_cpu = random.randint(0,2)
print(movimentos[escolha_cpu])

#Montar um IF de condições de vitoria do jogador, vitória do CPU e empate
# Usar operadores AND, OR
print(escolha_cpu)
if(escolha_jogador == 0 and escolha_cpu == 1) or (escolha_jogador == 1 and escolha_cpu == 2) or (escolha_jogador == 2 and escolha_cpu == 0):
    print("CPU venceu")
elif escolha_jogador == escolha_cpu:
    print("Empate")
else:
    print("Jogador Venceu!")








