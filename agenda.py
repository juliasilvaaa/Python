# Criando mini agenda

print(" ----- Bem vindo a agenda SENAI JANDIRA -----")

# Perguntas para que depois possamos devolver a resposta da pessoa  
nome = input("Digite o nome: ") # Para depois conseguir puxar colocar o nome da informação que o usuario vai digitar antes do input para depois conseguir retornar
cidade = input("Digite a cidade: ")
telefone = input("Digite o telefone: ")

# Resgatar as variaveis para retornar uma mensagem de que a informacao foi salva 
print("\n O contato : " + nome + " foi salvo ❤️ " + " cidade: " + cidade + " com o telefone: " + telefone)  # Windows + ponto final = abre seção dos emojis para incluir no codigo

# Forma mais moderna de retornar 

# F string - Chamando variavel com chaves sem precisar usar espaço e +
print(f"O contato {nome} foi salvo com o telefone {telefone} na cidade {cidade}")

