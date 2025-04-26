# Loop - Repetição

# For - Para (Já sabe quantas vezes mais ou menos vamos executar essa repetição)
# While - Enquanto  (Quando não tem uma ideia muito clara de quantas repetições)
# RANGE => faixa/intervalo


# Simulando Series de Academia
# Cada série com 10 repetições
print("-------- Acadademia --------") 
# Se executar dessa forma não vai ser completo até o 10, vai iniciar do 0
for serie in range(10):  
    print(f"Estou fazendo a serie {serie} 🏋️‍♀️")

# Para começar do 1 até o 11, contando 10 numeros
for pessoas in range(1,11):  
    print(f"Há {pessoas} matriculadas na academia 🏋️‍♀️")

# Criando uma lista de itens e um loop para a quantidade da lista
pessoas = ["Thau", "Kaike", "Fernando"]
for pessoa in pessoas:
    print(f"{pessoa} é matriculado na academia")



opcao = ""
# Enquanto opção for diferente de sair continuar imprimindo o loop
while opcao != "SAIR":
    opcao = input("Digite SAIR para encerrar o loop:")


# Não esquecer da condição de saída
num = 1
while num < 11:
    print(f"Vou contar até 10, observe: {num}")
    # Somando mais um a cada contagem
    num += 1


# ---------- Joguinho ----------
# game_over = false
# game_over = true
# while game_over == False:
#  Enquanto não tirar 6 - Continua o jogo

import random
dado = 0
jogadas = 0

print(' ---------- Dados ------------')
while dado !=6:
    dado = random.randint(1,6)
    print(f"Jogando o dados... tiramos: {dado}")
    jogadas += 1 
# Printando fora do loop, para exibir a qntd de jogadas para obter o 6
print(f"Conseguimos o 6 em {jogadas} jogadas")


# LOOP COM CONDICIONAIS
# Receber N números informar qual é par ou ímpar

# Leitura do código - Para o número no intervalo de 
for num in range(0,13):
    # Um número é par se o resto da divisão do número por 2, for 0
    # Caso não seja 0, é ímpar
    # O operador '%' pega o resto da divisão
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")


# Gerenciador de Matriculas
print("---------  Matriculas - Academia  ----------")
matriculados = ["Thau", "Kaike", "Fernando"]
resposta = input("Digite o nome de uma pessoa: ")
if resposta in matriculados:
    print(f"{resposta} está matriculado na academia\n")
else:
    print(f"{resposta} não está matriculado na academia")

