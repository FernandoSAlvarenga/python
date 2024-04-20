'''5. Ponto Geográfico
Crie uma classe PontoGeografico com os atributos:
latitude: latitude do ponto
longitude: longitude do ponto
Implemente os métodos getters e setters para:
latitude
longitude
Crie um objeto da classe PontoGeografico e realize as seguintes operações:
Acesse e imprima a latitude do ponto.
Altere a latitude do ponto.
Acesse e imprima a longitude do ponto.
Altere a longitude do ponto.'''


class ponto_geografico:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
                
    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude
    
    def set_latitude(self, novo_latitude):
        self.latitude = novo_latitude

    def set_longitude(self, novo_longitude):
        self.longitude = novo_longitude
    
dados1 = ponto_geografico(-30.042815247794483, -51.21890035770982)

print(f"latitude original do ponto_geografico: {dados1.get_latitude()}")  #Acesse e imprima a latitude do carro. 

dados1.set_latitude(-30.04286052402076)
print(f'A nova latitude é {dados1.get_latitude()}') #Altere o latitude do carro. 

print(f'O longitude do ponto_geografico é: {dados1.get_longitude()}') #Acesse e imprima o longitude do carro.  

novo_longitude = dados1.set_longitude(-51.21901904545017) 
print(f'A nova longitude  é: {dados1.get_longitude()}') #Altere o longitude do carro.








