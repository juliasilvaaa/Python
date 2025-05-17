# Objetos

# Formatações
# PascalCase
# snake_case
# camelCase
# UPPERCASE
# lowecase
# Capitalize


# Esquema/Planta/Código genetico de um 'dog'
class Dog:
    # Atributos do cachorro (raça, idade  nome)
    def __init__(self, especie, nome, idade):
        self.especie = especie
        self.nome = nome
        self.idade = idade
       
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e é um {self.especie}"
    # Primeiro metódo (comportamento do objeto)
    def latir(self):
        print(f"{self.nome} diz: Au Au Au Au")
    def buscar_osso(self):
        import random
        osso_animal = ["galinha", "boi", "humano"]                                 # Choice - Vai sortear um osso de animal da lista que criamos 
        print(f"{self.nome} foi buscar um osso... e retornou com um belissimo osso de {random.choice(osso_animal)}")
    def aniversario(self):
        idade_nova = self.idade + 1
        print (f"Parabéns agora seu cachorro {self.nome} tem {idade_nova} anos ")
    def brinquedo(self):
        import random
        brinquedo_dog = ["bolinha", "galinha", "pelucia"]
        print(f"O {self.nome} pega seu brinquedo {random.choice(brinquedo_dog)} e joga para o alto!")
   



class Canil:
    def __init__(self):
        self.dogs = []
    def abrigar_dog(self,dog):
        self.dogs.append(dog)
        print(f"O {dog.nome} foi acolhido no Canil")
    def brincar_todos(self):
        print("\nTodos os cachorros estão brincando")
        for um_dog in self.dogs:
            um_dog.brinquedo()


# Instanciar/Criar um objeto cachorro
# Criando uma variavel para armazenar os dados
dog1 = Dog("Golden", "Kaike Jr", 12)  
dog2= Dog("Poodle", "Thau", 13)  
canil = Canil()


print(dog1) 
# Eles herdaram o comportamento 'latir'
dog1.latir()
dog2.latir()
dog1.buscar_osso()
dog2.buscar_osso()

# Desafios 
# Crie um novo metodo chamado aniversario que aumenta a idade do dog em 1 ano
# A saida do metodo deve ser "{nome do cachorro} está fazendo aniversario e agora tem {anos} anos de idade"
dog1.aniversario()
dog2.aniversario()

# Crie um novo atributo chamado briquedo_favorito, depois crie um metodo chamado brincar() com a saida "{nome do cachorro} pega seu {brinquedo} e joga para o alto"
dog1.brinquedo()
dog2.brinquedo()

# Abrigando dogs no canil
canil.abrigar_dog(dog1)
canil.abrigar_dog(dog2)

# Brincar com todos os cachorros
canil.brincar_todos()



