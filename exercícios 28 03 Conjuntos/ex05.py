#Escreva um programa que determine se um conjunto é subconjunto de outro. 
# Utilize for para iterar pelos elementos do primeiro conjunto e if para verificar a presença no segundo. 

conjunto_1 = set()
conjunto_2 = set()

conjunto_nulo = set()
subconjunto = True

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
    if elemento not in conjunto_2:
        subconjunto = False
    break
if subconjunto:
    print(f'O Conjunto {conjunto_1} é subconjunto do conjunto {conjunto_2}')
else:
    print(f'O Conjunto {conjunto_1} não é subconjunto do conjunto {conjunto_2}')