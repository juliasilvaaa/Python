# Desafio - Competiçao de Powerlifters 2025

# 2 atletas Chris e Ramon Dino
# Sua missão é criar um codigo que ira determinar qual dos atletas é o vencedor
# Regras:

# 1 - Os atletas se desafiam em 4 modalidas, cada modalidade concede uma pontuação de 0 a 200
# 2 - Apos o término das 4 modalidades, calculamos a media de pontos dos dois atletas
# 3 - Por fim, vence o atleta que atingir a maior média, um empate é possivel

# Para calcular a média 
# Some os pontos do atletas, divida a soma pelo numero de pontos 
# Lembre se da ordem das operações na matématica

# Chris Bumstead : 127, 185, 134, 199
# Ramon Dino : 115, 100, 136, 197

# Ordem - / * - +

chris = (127 + 185 + 134 + 199 / 4) 
ramon = (115 + 100 + 136 + 197 / 4) 

if chris > ramon:
    print("O Chris é o vencedor")
elif chris == ramon:
    print("Os atletas empataram")
else: 
    print("O ramon é o vencedor")
