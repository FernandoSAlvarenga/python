#10. Inverter a Ordem dos Elementos de uma Lista
lista = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
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
print(f'A lista foi digitada na seguinte ordem: {lista}')
lista.reverse()
print(f'A lista invertida ficou assim: {lista}')