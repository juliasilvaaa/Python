from art import splash
# Livro sagrado com alguns deuses já inseridos


import json

# Lendo o arquivo
with open("lista_deuses.json", mode="r") as arquivo:
    lista_deuses = json.load(arquivo)

# Le o programa
def resgatar_livro(filejson):
    with open(filejson, mode="r") as arquivo:
      return json.load(arquivo)

# Funcao para salvar passando o parametro 
def salvar_livro(dicionario):
    with open("lista_deuses.json", mode="w") as arquivo:
            json.dump(dicionario, arquivo, ensure_ascii=False)
            print("Salvando o livro dos Deuses")


livro_dos_deuses = resgatar_livro("lista_deuses.json")

# Loop principal do programa
executando = True
while executando:
    print(splash)
    print("\n-- O Livro dos Deuses --")
    print("1. Consultar um deus")
    print("2. Adicionar um novo deus")
    print("3. Atualizar um deus existente")
    print("4. Listar todos os deuses")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do deus: ")
        if nome in livro_dos_deuses:
            print(f"{nome}: {livro_dos_deuses[nome]}")
        else:
            print("Este deus não está no livro.")

    elif escolha == "2":
        nome = input("Nome do novo deus: ")
        if nome in livro_dos_deuses:
            print("Este deus já está registrado.")
        else:
            descricao = input("Descrição do deus: ")
            livro_dos_deuses[nome] = descricao
            print(f"{nome} adicionado com sucesso.")

    elif escolha == "3":
        nome = input("Digite o nome do deus a ser atualizado: ")
        if nome in livro_dos_deuses:
            nova_desc = input("Nova descrição: ")
            livro_dos_deuses[nome] = nova_desc
            print(f"{nome} foi atualizado.")
        else:
            print("Deus não encontrado.")

    elif escolha == "4":
        print("\nTodos os deuses registrados:")
        for nome, descricao in livro_dos_deuses.items():
            print(f"{nome}: {descricao}")

    elif escolha == "5":
        salvar_livro(livro_dos_deuses)
        print("Encerrando o Livro dos Deuses...")
        executando = False
        

    else:
        print("Opção inválida. Tente novamente.")


