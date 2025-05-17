# Ler = R READ 
# Gravar um novo W Write
# Adicionar nova coisa A append

# with open("teste.txt", mode="r") as arquivo:
#     print(arquivo) #Objeto do arquivo teste.txt
#     conteudo = arquivo.read() # Leitura do conteudo do arquivo
#     print(conteudo)

# Alerta : Tomar cuidado para não salvar por cima de coisas importantes
# with open("teste.txt", mode="w", encoding="UTF-8") as arquivo:
#     arquivo.write("Estou escrevendo pelo PYTHON")


# Estrutura de um dicionario
produtos = {
    "GTA VI": 700,
    "God of War": 300,
    "Minecraft": 29
}

# Salvar esse dicionario em um arquivo

# Em operações de gravação, o arquivo não precisa exitir 
# Abrindo o arquivo mesmo que não exista, no modo write                         # Arquivo - nome que preferir
# with open("carrinho_compras.txt", mode="w", encoding="UTF-8") as arquivo:
#     arquivo.write(produtos) 

with open("carrinho_compras.txt", mode="w", encoding="UTF-8") as arquivo:
   # Para cada jogo e valor, desmembrando o dicionario em strings para salvar
   for jogo, valor in produtos.items():
       arquivo.write(f"{jogo}: {valor}\n")

carrinho_usuario = {}
with open("carrinho_compras.txt", mode="r", encoding="UTF-8") as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)
    # Para cada item do meu conteúdo
    for item in conteudo:
        # Limpar o conteúdo
        item = item.strip()
        # Slip para dividir a partir do :
        descricao, valor = item.split(":", 1)     
        print(f"{descricao} | {valor}")
        # Pegamos o nome do produto e salvamos como uma chave no dicionario, o valor do produto vira a 'descricao' do dicionario
        carrinho_usuario[descricao] = valor
        print(carrinho_usuario)

# JSON -  JavaScript Object Notation
# JSON ele é um padrão para salvar e enviar informações entre sistemas
# Será usados em APIs (comunicação entre software), como BD não relacional

import json
with open("carrinho_compras.json", mode="w") as arquivo:
    json.dump(produtos, arquivo)

with open("carrinho_compras.json", mode="r") as arquivo:
    carrinho_json = json.load(arquivo)
    print(carrinho_json)

