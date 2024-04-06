#2. Encontrar a Soma dos Valores em uma Lista
lista = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Digite uma tecla, não um número.")

while True:
    num_add = input('Digite o número para add a lista: ')# estava em loop por não ter essa entrada de dados.
    if num_add == tecla_parada:
        break
    elif not num_add.isdigit():
        print("Digite somente números ou a tecla de parada.")
        continue
    else:
        num_add = int(num_add)
        if num_add in lista:
            print(f'O número adicionado {num_add}, já esta na lista, verifique a lista atualizada: {lista}') 
            continue
        lista.append(num_add)
soma_lista = sum(lista)
print(f'A soma da lista {lista} é: ', soma_lista)