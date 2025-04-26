import random

# 1 - Crie o loop que irá somar todos os numeros de 1 a 100 e impirmir o resultado

soma = 0
print(" ----- Somando de 1 a 100 ----- ")
for somando in range(1,101):  
    soma +=1
    print(f"Resultado da soma: {soma}")


# 2 - Pergunte um numero para o usuario e imprima a tabuada desse número de 1 a 10 

number = int(input("Qual número? "))

tabuada = 1

print(f"------- Tabuada do {number} -------")
for tabuada in range(1,11):
    multiplicacao = number * tabuada
    print(f"{number} X {tabuada} = {multiplicacao}")


# 3 - Sorteie um numero entre 111 e 999 até que a combinação seja 777, imprimir o numero de tentativas para conseguir 777

sorteio_number = 0
tentativas = 0

while sorteio_number !=777:
    sorteio_number = random.randint(111,999)
    print(f"Sorteando número: {sorteio_number}")
    tentativas +=1

print(f" ------ Conseguimos o 777 em {tentativas} tentativas ----------")

# 4 - Faça um loop que retorna o !fatorial de um número
# O fatorial de um número qualquer é a multiplicação de todos os número inteiros de 1 até N
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120

fatorial = 1 
numero = int(input("Digite um número para saber o fatorial: "))
for num in range(1, numero+1):
     fatorial *= num
     print(f"O fatorial de {numero} é {fatorial}")


# 5 - Faça um looop onde Hades irá percorrer uma lista de almas e condenar ou salvar cada uma delas, 
#      ao final do loop imprima quantas almas foram salvas e quantas foram condenadas

almas = ["justa", "injusta", "neutra","justa", "injusta", "neutra","justa", "injusta", "neutra","justa", "injusta", "neutra","justa", "injusta", "neutra","justa", "injusta", "neutra"]

condenadas = 0
redimidas = 0

for alma in almas:
    if alma == "justa" or alma == "neutra":
         redimidas +=1
    elif alma == "injusta":
         condenadas +=1
    else: 
         print("Nenhuma Alma foi salva ou condenada")

print(f"Foram condenadas {condenadas} almas e salvas {redimidas} almas")


   


