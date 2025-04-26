# Blocos de código/ funcionalidades reutilizaveis
# Ex: print()
# Funções tipicamente tem nome, parâmetros e retorno


def mensagem():
    print("Olá Mundo")

mensagem()


def mensagens(nome):
    print(f"O nome é {nome}")
    # Chamando a função 
mensagens('Julia')

def duplicar(numero):
    resultado = numero * 2
    return resultado
# Retorno precisa ser explicito

print(duplicar(5))


# Função com input para escolher um numero e somando dois, retornando o resultado
valor = int(input("Escolha um número para somar com 4: "))

def somar(valor):
    resultado_soma = valor + 4
    return resultado_soma
print(somar(valor))

# -------- Python - tem dois parametros, posicional e palavra-chave --------

def coffe_machine(qntd_cafe, qntd_agua):
    print(f"Fazendo café com {qntd_cafe}mg de pó e {qntd_agua}ml de água")


# Parametro Posicional
coffe_machine(150,20)

# Parametro Palavra chave
coffe_machine(qntd_agua=150, qntd_cafe=20)


# Criar uma função codificar que irá receber dois parametros, um texto_original e outro chamado deslocamemto
# Dentro da função usar um loop para aumentar as letras pelo numero de deslocamento
# Ex: a => b
# Dica: Pesquisar

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def codificar(texto_original, deslocamento):
    texto_codificado = ''
    for alfabeto_deslocado in texto_original:
        if alfabeto_deslocado in alfabeto:
            indice_original = alfabeto.index(alfabeto_deslocado)
            novo_indice = (indice_original + deslocamento) %len(alfabeto)
            texto_codificado += alfabeto[novo_indice]
        else:
            texto_codificado += alfabeto_deslocado
    return texto_codificado
        

print(codificar("julia",2))
