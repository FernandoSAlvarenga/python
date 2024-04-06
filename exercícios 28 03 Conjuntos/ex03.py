#3. Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença no primeiro conjunto e não no segundo.

conjunto_1 = set()
conjunto_2 = set()

conjunto_nulo = set()
diferenca = set()

while True:
    tecla_parada = input("Cadastre uma tecla de parada (Ex.: /*-+. ): ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Somente caracteres (ex. /*-+).")
        
while True:
    valor = input('Digite números do primeiro conjunto: ')
    if valor == tecla_parada and conjunto_nulo != ():
                
        break
    elif not valor.isdigit():
        print(f"Somente números ou a tecla de parada: {tecla_parada} .")

    else:
        valor = int(valor)
        conjunto_1.add(valor)
    
while True:
    valor_2 = input('Digite números do segundo conjunto: ')
    if valor_2 == tecla_parada and conjunto_nulo != ():
        break
    elif not valor_2.isdigit():
        print(f"Somente números ou a tecla de parada: {tecla_parada}.")
    else:
        valor_2 = int(valor_2)
        conjunto_2.add(valor_2)

for elemento in conjunto_1:
    if  elemento not in conjunto_2 or elemento in conjunto_1 and elemento not in conjunto_2:
        diferenca.add(elemento) 
print(conjunto_2)        
for elemento in conjunto_2:
    if elemento not in conjunto_1 or elemento in conjunto_2 and elemento not in conjunto_1:
        diferenca.add(elemento)
print(f'A diferença entre os conjuntos é: {diferenca}')
