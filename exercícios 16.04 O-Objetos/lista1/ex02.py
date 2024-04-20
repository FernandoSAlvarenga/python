'''2. Produto 
Crie uma classe Produto com os atributos: 
nome: nome do produto 
preco: preço do produto 
Implemente os métodos getters e setters para: 
nome 
preco 
Crie um objeto da classe Produto e realize as seguintes operações: 
Acesse e imprima o nome do produto. 
Altere o nome do produto. 
Acesse e imprima o preço do produto. 
Aplique um desconto no preço do produto. 
Acesse e imprima o novo preço do produto. '''

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_preco(self, novo_preco):
        self.preco = novo_preco
    
    
nome1 = produto("Capacete", 250)

print(f"Nome original do Produto: {nome1.get_nome()}")  

print(f'O preco do produto é: {nome1.get_preco()}')

nome1.set_nome('Capacete LS2')
print(f'Novo nome do Produto é {nome1.get_nome()}') #ok

novo_preco = nome1.get_preco() * 0.10

print(f'O valor do desconto do {nome1.get_nome()} é: {novo_preco}')
print(f'O valor total do produto com o desconto é: {nome1.get_preco() - novo_preco}')
