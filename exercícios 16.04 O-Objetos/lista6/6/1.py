class Ponto2D:
    def __init__(self, x, y):
      
        #Inicializa o ponto com coordenadas x e y.
       
        self.x = x
        self.y = y

    def __str__(self):
       
        #Retorna uma string representando o ponto no formato "(x, y)".
     
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        
        #Compara dois pontos para verificar se são iguais (mesmas coordenadas).
       
        if not isinstance(other, Ponto2D):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
       
        #Define a adição de dois pontos, resultando em um novo ponto com a soma das coordenadas.
      
        if not isinstance(other, Ponto2D):
            raise TypeError("Tipo de operando não suportado para soma: 'Ponto2D' e 'tipo'")
        nova_x = self.x + other.x
        nova_y = self.y + other.y
        return Ponto2D(nova_x, nova_y)
    
# Crie os pontos utilizando a entrada do usuário
x1 = int(input("Digite a coordenada x do primeiro ponto: "))
y1 = int(input("Digite a coordenada y do primeiro ponto: "))

x2 = int(input("Digite a coordenada x do segundo ponto: "))
y2 = int(input("Digite a coordenada y do segundo ponto: "))

ponto1 = Ponto2D(x1, y1)
ponto2 = Ponto2D(x2, y2)

# Imprima as informações dos pontos
print(f"Primeiro ponto: {ponto1}")
print(f"Segundo ponto: {ponto2}")

# Calcule a soma dos pontos e imprima o resultado
ponto3 = ponto1 + ponto2
print(f"Soma dos pontos: {ponto3}")

# Compare os pontos e imprima o resultado
if ponto1 == ponto2:
    print("Pontos iguais")
else:
    print("Pontos diferentes")

# Verifique se o terceiro ponto é igual a qualquer um dos outros pontos
if ponto1 == ponto3 or ponto2 == ponto3:
    print("O terceiro ponto é igual a pelo menos um dos outros pontos")
else:
    print("O terceiro ponto não é igual a nenhum dos outros pontos")