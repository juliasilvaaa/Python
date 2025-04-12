# Bibliotecas - Vários arquivos 
# Módulo - Um arquivo que contém funções

# Usando um modulo do python (Random - da acesso a várias funções de sorteio - aleátorias)
import random
# Sortear número do 1 até o 6 ( 6 possibilidades )
print(random.randint(1,6))


# Lista
jogadores_corinthians = ["Ángel Romero", "Hugo Souza", "Talles Magno", "Yuri Alberto"]
# Sortear Jogadores
jogadores = random.choice(jogadores_corinthians)
jogadores2 = random.choice(jogadores_corinthians)

print(f"A batalha será entre {jogadores} VS {jogadores2}")


# Números Decimais/Quebrados
print(random.random()) # de 0 até 1 


# Embaralhar - Shuffle
random.shuffle(jogadores_corinthians)
print(jogadores_corinthians)


# Simulando Bola 8 mágica 
pergunta = input("Digite sua pergunta\n")
print(f"Você perguntou :{pergunta}")

# Criando lista com as respostas 
respostas = ["Sim", "Não", "Nunca"]
resposta_sorteada = random.choice(respostas) # Sorteando 
# Retornando 
print(resposta_sorteada)