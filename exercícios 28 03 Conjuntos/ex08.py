# Escreva um programa que implemente um jogo de adivinhação, onde o jogador tenta adivinhar os 
#elementos de um conjunto. Utilize while para controlar o loop do jogo e if para verificar a adivinhação.

conjunto_1 = ('1', '2', '3', '4','5')
num_escolhido = set()

conjunto_nulo = set()


while True:
    print('BEM VINDO!' *16)
    tecla_parada = input("Cadastre uma tecla de parada (Ex.: /*-+. ): ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Somente caracteres (ex. /*-+).")
        
while True:
    num_1 = input('Digite um numero da sorte: ')
    if num_1 == tecla_parada and conjunto_nulo != ():
                
        break
    elif not num_1.isdigit():
        print(f"Somente números ou a tecla de parada: {tecla_parada} .")

    else:
        num_1 = int(num_1)
        num_escolhido.add(num_1)

conjunto_lista = list(conjunto_1)

num_da_sorte = conjunto_lista[0]
print(num_da_sorte)
while True:
    print(num_da_sorte)
    if num_da_sorte == num_escolhido:
        print('Parabéns, acertou!')
    else:
        print('Tente novamente!')
    break   