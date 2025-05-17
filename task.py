#TODO #1 Crie uma classe chamada Deus com os atributos nome, domínio e símbolo.

class Deus:
    def __init__(self, nome, dominio, simbolo, seguidores = 0):
        self.nome = nome
        self.dominio = dominio
        self.simbolo = simbolo
        self.seguidores = seguidores
    def __str__(self):
        #TODO #2 Crie um método chamado apresentar() que irá imprimir uma introdução básica sobre o deus
        return f"O deus: {self.nome} tem o dominio {self.dominio} e como símbolo {self.simbolo} "
    
 #TODO #3 Crie um método chamado realizar_milagre() que irá imprimir um algo como "{deus} realiza um milagre divino relacionado ao(à) {domínio}"
    def realizar_milagre(self):
        import random
        milagres = ["Ressureição", "Invisibilidade", "Dinheiro Infinito"] 
        print(f"O {self.nome} realizou o milagre de {random.choice(milagres)}")  

deus1 = Deus("Julia", "Materialista", "&")  
deus2 = Deus("Kaike", "Religioso", "%")  

deus1.realizar_milagre()

#TODO #4 Crie uma classe de controle chamada Olimpo, o único atributo dessa classe deve ser deuses, inicializada como uma lista VAZIA.
class Olimpo:
    def __init__(self):
        self.deuses = []
    def adicionar_deus(self, deus):
        #TODO #5 Crie um método chamado adicionar_deus, que irá receber um Objeto deus como parâmetro e irá colocá-lo na lista deuses(feito na etapa #4)
        self.deuses.append(deus)
        print(f"O {deus.nome} foi adicionado")

#TODO #6 Crie um método chamado mostrar_deuses(), que irá exibir todos os Deuses presente no Olimpo.
    def mostrar_deuses(self):
        for deus in self.deuses:
            print(f"Todos os Deuses: {deus.nome}")
        #TODO #7 Crie um novo atributo na classe Deus chamado seguidores, inicialize esse atributo como 0 por padrão.
        #TODO #8 Crie um método chamado adicionar_seguidores() que recebe uma quantidade como parâmetro e adiciona X novos seguidores para o deus, invoque esse método para adicionar 100 seguidores para um deus qualquer e 500 para outro deus qualquer.
    # def seguidores(self, quantidade):
    def maior_deus(self):
        max_deus = self.deuses[0]
        for deus in self.deuses:
            if deus.seguidores > max_deus.seguidores:
                max_deus = deus
        print(f"O maior deus do olimpo é o {max_deus}")

        





# Adicionando deuses
zeus = Deus("Zeus", "Céu", "&")
olimpo = Olimpo()

olimpo.adicionar_deus(zeus)
olimpo.adicionar_deus(deus1)
olimpo.adicionar_deus(deus2)

# Exibindo Deuses
olimpo.mostrar_deuses()



#TODO #9 Crie um método chamado maior_deus() na classe Olimpo que deve mostrar qual deus tem o maior número de seguidores. Dica: Use um dicionário para armazenar o nome e os seguidores do deus com mais seguidores.
