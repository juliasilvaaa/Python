# Importar o modulo random
# Criar tres listas 1 - Letras, 2 - Números, 3 - Símbolos
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
simbolos = ["+", "?", "!", "(", "*", "&", "$", "@"]

# Exibir Boas Vindas
print("\n------- Bem vindo ao Gerador de Senhas --------\n")

# Perguntar ao usuario quantas letras, numeros e simbolos ele quer na senha
# Crie 3 perguntas distintas, com variaveis distintas 

print("Escolha a sua senha ")
escolha_letras = int(input("Quantas letras? :"))
escolha_numeros = int(input("Quantos números :"))
escolha_simbolos = int(input("Quantos símbolos? :"))


# Criar lista vazia senha
senha =[]

# Faça uma soma total de caracteres da senha, guardar em uma variavel

tamanho_senha = escolha_letras + escolha_numeros + escolha_simbolos

# LOOP - Para sortear a senha
#  Método append


#  Para escolha letras enquanto a escolha letras tiver a senha que está vazia, adicione conforme a escolha do usuario buscando na lista 
for escolha_letras in range(0, escolha_letras):
    senha.append(random.choice(letras))

for escolha_numeros in range(0, escolha_numeros):
    senha.append(random.choice(numeros))

for escolha_simbolos in range(0, escolha_simbolos):
    senha.append(random.choice(simbolos))


# Embaralhando a senha e organizando 
random.shuffle(senha)
senha_final = ''.join(senha)


print(f"Sua senha é: '{senha_final}' com um total de {tamanho_senha} caracteres")    


# pip install pyinstaller ( Instala o pacote para gerar EXECUTAVÉIS a partir dos arquivos py)
# pyinstaller 'nome_projeto'.py ( Gera o executável do seu programa )