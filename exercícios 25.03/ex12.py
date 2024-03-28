# 12. Dividir uma Lista em Duas:

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
tamanho = len(lista) #precisei criar a variável tamanho usando len(lista) para quantificar o tamanho da lista
metade = tamanho // 2 # precisei criar a variável metade
parte1 = lista[:metade] # não tinha declarado a variável metade
parte2 = lista[metade:]
print(f'A lista digitada é: {lista} e a primeira parte da lista é: {parte1}, a segunda parte da lista é: {parte2}')