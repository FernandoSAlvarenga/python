# 14. Remover um Elemento de uma Lista:

lista = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de adicionar números à lista: ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Digite uma tecla, não um número.")
while True:
    valor = input('Digite números para a lista: ')
    if valor == tecla_parada:
        break
    valor = int(valor)
    lista.append(valor) 
print(f'A lista digitada é: {lista}')

while True:
    num_removido = int(input('Digite o código para ser retirado da lista: '))# estava em loop por não ter essa entrada de dados.
    if num_removido in lista:
        lista.remove(num_removido)
        break
    else:
        print(f'Este número {num_removido} não esta na lista!')
    
print(f'O número deletado foi: {num_removido}, a lista atualizada é: {lista}')