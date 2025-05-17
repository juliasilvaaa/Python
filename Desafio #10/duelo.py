import arts, random, json
# Criar uma função que irá carregar o json em um dicionario chamado termos

# Constante - Caixa alta
BASE = "Desafio #10/dados.json"


def carregar_dados(cam_arquivo):
    with open(cam_arquivo, mode="r", encoding="UTF-8") as arquivo:
        return json.load(arquivo)
    

termos = carregar_dados(BASE)
print(termos)



def formatar_dados(termo):
    nome_termo = termo["term"]
    descricao_termo = termo["description"]
    return f"{nome_termo}, um {descricao_termo}"
print(termos[0])


def verificar_escolha(escolha, pontos_a, pontos_b):
    if escolha == 'a':
        if numpesquisas_a > numpesquisas_b:
            print("Você acertou parabéns")
            return True
        else:
            print("Você perdeu")
            return False
    else:
        if numpesquisas_b > numpesquisas_a:
            print("Você acertou parabéns")
            return True
        else:
            print("Voce perdeu")
            return False



# Criar uma função que irá sortear um termo na lista termos, nome função

def sortear_termo(lista):
    sorteio = random.choice(lista)
    return sorteio

print(sortear_termo(termos))
print(arts.logo)

termo_a = sortear_termo(termos)
termo_b = sortear_termo(termos)
print(arts.vs)


numpesquisas_a = termo_a['searches']
numpesquisas_b = termo_b['searches']


# Impedir que sorteie denovo
while termo_b == termo_a:
    termo_b = sortear_termo(termos)
    print("Sorteamos iguais")


# Formatando dados
print(formatar_dados(termo_a))
print(formatar_dados(termo_b))

# Perguntar qual opção o usario escolhe A ou B e guardar em variaveis o numero de pesquisas do termo_a e termo_b

