'''1. Classe Pessoa e Aluno: 
Crie uma classe Pessoa com os atributos nome, idade e sexo. 
Crie uma classe Aluno que herde da classe Pessoa. 
Adicione à classe Aluno o atributo matricula. 
# The instruction `Implemente métodos get_matricula(), set_matricula(), apresentar() nas` is asking
# you to implement methods within the classes `Pessoa` and `Aluno`. Here's what each method should do:
Implemente métodos get_matricula(), set_matricula(), apresentar() nas 
classes Pessoa e Aluno. 
Crie objetos pessoa1 e aluno1 e chame os métodos adequados.'''

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade
    
    def get_sexo(self):
        return self.sexo
    
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, minha idade é {self.idade}, minha identificação de genero é {self.sexo} ')

dados1 = Pessoa("Fernando", 42, "Masculino")    
dados1.apresentar()

class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula):
        super().__init__(nome, idade, sexo)  # Chamada ao construtor da classe pessoa
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, novo_matricula):
        self.matricula = novo_matricula
        
    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, minha idade é {self.idade}, minha identificação de genero é {self.sexo}, minha matrícula é {self.matricula} ')

dados1 = Aluno("Fernando", 42, "Masculino",12121212121)    
dados1.apresentar()




















'''dados1 = aluno("Fernando", 123456, "fullstack")

print(f'O matricula do aluno é: {dados1.get_matricula()}') #Acesse e imprima o número da matrícula do aluno. 

novo_matricula = dados1.set_matricula(654321) 
print(f'A nova matrícula é: {dados1.get_matricula()}') #Altere o número da matrícula do aluno. 

print(f"Nome original do aluno: {dados1.get_nome()}")  #Acesse e imprima o nome do aluno. 

dados1.set_nome('Ferdinando')
print(f'Novo nome do aluno é {dados1.get_nome()}') #Altere o nome do aluno. 

print(f'O curso do aluno é: {dados1.get_curso()}') #Acesse e imprima o nome do curso do aluno.

dados1.set_curso('Python') 

print(f'O novo curso é: {dados1.get_curso()}') #Altere o nome do curso do aluno'''