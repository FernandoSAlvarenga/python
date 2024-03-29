#6. Encontrar o Número de Vezes que um Valor Aparece em uma 

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

num_pesquisa = int(input('Digite números para pesquisa: '))
num_vezes = lista.count(num_pesquisa)
print(f'Quantidade de vezes que o {num_pesquisa} aparece é: {num_vezes}')






