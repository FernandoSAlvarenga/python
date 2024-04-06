# 11. Concatenar Duas Listas:
lista1 = []
lista2 = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Digite uma tecla, não um número.")

while True:
    valor1 = input('Digite números para a lista 1: ')
    if valor1 == tecla_parada:
        break
    valor1 = int(valor1)
    lista1.append(valor1)
    
while True:
    valor2 = input('Digite números para a lista 2: ')
    if valor2 == tecla_parada:
        break
    valor2 = int(valor2)
    lista2.append(valor2) 
lista_concatenada = lista1 + lista2
print(f'A lista 1 é: {lista1} e a lista 2 digitada é: {lista2}, a lista concatenada é: {lista_concatenada}')