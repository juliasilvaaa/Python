# Condicionais - Fluxograma 

# Sinais de Comparação
# > Maior
# < Menor 
# >= Maior ou igual
# <= Menor ou igual 
# == Comparação de igualdade
# != Diferente

# ----------- Calculadora de Idade ------------

idade = int(input("Qual é sua idade? ")) # Usando o Int para conversão do string para numero

# SE - Condição se a idade é maior ou igual a 18 
# # Bloco aberto com :

if idade >= 18:  # Teste Logico - Se for maior ou igual a 18
    print("Você é maior de idade")   # Resultado
else: # Se não
    print("Você é menor de idade")

# ------------- Temperatura -----------------

temperatura = int(input("Qual a temperatura agora? "))

# Mais do que 30 graus = quente 
# Menos que 10 graus = frio
# Caso contrário = Agradavél

if temperatura > 30:
    print("A temperatura está quente")

    # Condição Intermediária - Se não se = ELSE IF -> ELIF
elif temperatura < 10:  # O elif precisa novamente da condicional (temperatura)
    print("Está frio")
else: # Else não tem condição
    print("Está agradável")


# ---------------- Valores Booleanos -> Tipo de DADO -------------

# Se o dinheiro for mais do que 10 E estiver com fome, compro um BK, caso contrário Salgado

dinheiro = 15
fome = True  # True - representa verdadeiro, quer dizer que está com fome
    # Em casos de valor booleano ele já sabe o valor


if dinheiro > 10 and fome:
    print("Vou comprar BK")
else:
    print("Não tenho dinheiro, vou de salgado")



# -------------- Prova da Policia Militar ------------
# Requisitos
# Idade >= 18
# Altura >= 1.75
# Ficha criminal deve estar limpa, ou seja True ou False

# Descobrir se a pessoa atende esses requisitos para a prova

idade = 20
altura = 1.61
ficha_criminal = False



# Se deixar de usar o and, você faz um if a mais
# Quando usamos o AND se uma condicional der false, será a resposta false. Já o OR se um é verdadeiro ele torna todo verdadeiro
if idade >= 18 and altura >= 1.75 and ficha_criminal:  # Por ela ser booleano não precisa fazer comparação
    print("Está apto para a prova")
else: 
    print("Não atende alguns critérios")







