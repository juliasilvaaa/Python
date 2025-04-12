# Gerador de Senhas

import random
letras = ["a", "b","c","d"]
numeros = ["1", "2","3", "4"]
simbolos = ["!", "@", "%", "&"]

caractere1 = random.choice(letras)
caractere2 = random.choice(numeros)
caractere3 = random.choice(simbolos)

nova_senha = caractere1 + caractere2 + caractere3
print(nova_senha)

