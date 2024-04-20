'''4. Carro 
Crie uma classe Carro com os atributos: 
marca: marca do carro 
modelo: modelo do carro 
ano: ano de fabricação do carro 
Implemente os métodos getters e setters para: 
marca 
modelo 
ano 
Crie um objeto da classe Carro e realize as seguintes operações: 
Acesse e imprima a marca do carro. 
Altere a marca do carro. 
Acesse e imprima o modelo do carro. 
Altere o modelo do carro. 
Acesse e imprima o ano de fabricação do carro. 
Altere o ano de fabricação do carro. '''

class carro:
    def __init__(self, marca, modelo, ano_fabric):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabric = ano_fabric
        
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo
    
    def get_ano_fabric(self):
        return self.ano_fabric
    
    def set_marca(self, novo_marca):
        self.marca = novo_marca

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def set_ano_fabric(self, novo_ano_fabric):
        self.ano_fabric = novo_ano_fabric
    
dados1 = carro("Ford", 'Ka', 2015)

print(f"marca original do carro: {dados1.get_marca()}")  #Acesse e imprima a marca do carro. 

dados1.set_marca('peugeot')
print(f'Nova marca do carro é {dados1.get_marca()}') #Altere o marca do carro. 

print(f'O modelo do carro é: {dados1.get_modelo()}') #Acesse e imprima o modelo do carro.  

novo_modelo = dados1.set_modelo(208) 
print(f'O novo modelo do carro é: {dados1.get_modelo()}') #Altere o modelo do carro.

print(f'O ano_fabric do carro é: {dados1.get_ano_fabric()}') #Acesse e imprima o ano de fabricação do carro. 

dados1.set_ano_fabric(2022) 

print(f'O novo ano fabricação é: {dados1.get_ano_fabric()}') #Altere o marca do ano_fabric do carro








