# Estrutura de Dados para armazenar vários dados de diferentes tipos 
# Você pode ter uma lista com números, com texto, com booleanos ou outros tipos de dados 
# Lista ==> Python 
# Arrays ==> JavaScript

notas_julia = [100,200,11]

print(notas_julia)
# O indice se inicia em 0 zero
print(notas_julia[-1]) # Ultimo Indice

# ----- Lista de Jogadores -----

jogadores_corinthians = ["Ángel Romero", "Hugo Souza", "Talles Magno", "Yuri Alberto"]

# Inserir itens na lista usando (Append - Insere ao final da lista)
jogadores_corinthians.append("Memphis Depay")

print(jogadores_corinthians)

# Inserir itens na lista usando insert escolhendo a posição através do índice
jogadores_corinthians.insert(0, "Matheus Bidu")
print(jogadores_corinthians)

# Removendo itens da lista pelo nome 
jogadores_corinthians.remove("Talles Magno")
print(jogadores_corinthians)

# Verifica se o valor está na lista
if "Hugo Souza" in jogadores_corinthians:  # IN - Está (Se hugo está na lista....)
    print("Este jogador está na lista")
else:
    print("Esse jogador não está na lista")


# Organizar em ordem alfabética 
jogadores_corinthians.sort() # Limitação de acentuação, mas é possviel criar outros críterios 
print(jogadores_corinthians)

# Organizar de trás para frente
jogadores_corinthians.reverse()
print(jogadores_corinthians)

