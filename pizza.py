# Desafio 
# Missão: Desenvolver um sistema automatizado para calcular o valor de um pedido de pizza

# 1 - Perguntar o tamanho da pizza ( P = pequena, M = média, G = grande )
# - Pequena custa R$ 20
# - Média custa R$30
# - Grande custa R$45

# 2 - Perguntar se o cliente quer adicional de queijo por mais R$5
# 3 - Perguntar se o cliente quer adicional de borda por mais  R$7

# No final, o programa deve calcular e exibir o valor total do pedido


print("\n---------------- Pizzaria --------------------\n")

# Perguntar qual o pedido do cliente guardando nas suas devidas variaveis 
escolha = input("Qual tamanho da pizza? \n P - Pequena \n M - Média \n G - Grande \n")
adicional_queijo = input("Deseja adicionar queijo? ")
borda = input("Deseja borda adicional? ")


# Definir o valor escolha como zero para determinar ele depois 
valor_escolha = 0

# Escolhas definidas inicialmente como false 
escolha1 = False
escolha2 = False

# Definindo o valor dos adicionais como zero inicialmente 
valor_borda = 0
valor_queijo = 0

# Escolha tamanho pizza de acordo com o que o cliente digitar 
if escolha == "P":
    valor_escolha = 20
elif escolha == "M":
    valor_escolha = 30
elif escolha == "G":
    valor_escolha = 45
else:
    # Caso não seja nenhuma escolha definindo a pizza pequena como padrâo
    valor_escolha = 20

# Adicional queijo 
if adicional_queijo == "Sim":
    escolha1 = True
    # Se o cliente digitar Sim, a variavel se torna true com o valor do queijo
    valor_queijo = 5
else:
    escolha1 = False


# Adicional Borda
if borda == "Sim":
    escolha2 = True
    valor_borda = 7
else:
    escolha2 = False

# Calculo total da pizza com os adicionais se caso o cliente selecionar 
valor_total = valor_escolha + valor_queijo + valor_borda

# Retornar o valor total.
print(f"O valor Total da pizza é de: {valor_total}")