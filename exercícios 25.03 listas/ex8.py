#8. Gerar uma Lista com Valores Pares de 1 a 10:

lista = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Digite uma tecla, não um número.")

while True:
    valor = input('Digite números de 1 a 10 para a lista: ')
    if valor == tecla_parada:
        break
    valor = int(valor)
    lista.append(valor)   
for lista in range(110):

    if(lista%2==0):
        print(f' Os números pares são: {lista}')
