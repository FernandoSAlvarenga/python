'''3. Aluno 
Crie uma classe Aluno com os atributos: 
matricula: número da matrícula 
nome: nome do aluno 
curso: nome do curso 
Implemente os métodos getters e setters para: 
matricula 
nome 
curso 
Crie um objeto da classe Aluno e realize as seguintes operações: 
Acesse e imprima o número da matrícula do aluno. 
Altere o número da matrícula do aluno. 
Acesse e imprima o nome do aluno. 
Altere o nome do aluno. 
Acesse e imprima o nome do curso do aluno. 
Altere o nome do curso do aluno. '''

class aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
    def get_nome(self):
        return self.nome

    def get_matricula(self):
        return self.matricula
    
    def get_curso(self):
        return self.curso
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_matricula(self, novo_matricula):
        self.matricula = novo_matricula
    
    def set_curso(self, novo_curso):
        self.curso = novo_curso
    
dados1 = aluno("Fernando", 123456, "fullstack")

print(f'O matricula do aluno é: {dados1.get_matricula()}') #Acesse e imprima o número da matrícula do aluno. 

novo_matricula = dados1.set_matricula(654321) 
print(f'A nova matrícula é: {dados1.get_matricula()}') #Altere o número da matrícula do aluno. 

print(f"Nome original do aluno: {dados1.get_nome()}")  #Acesse e imprima o nome do aluno. 

dados1.set_nome('Ferdinando')
print(f'Novo nome do aluno é {dados1.get_nome()}') #Altere o nome do aluno. 

print(f'O curso do aluno é: {dados1.get_curso()}') #Acesse e imprima o nome do curso do aluno.

dados1.set_curso('Python') 

print(f'O novo curso é: {dados1.get_curso()}') #Altere o nome do curso do aluno
