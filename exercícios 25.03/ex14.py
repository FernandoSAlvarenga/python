# 14. Remover um Elemento de uma Lista:

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
print(f'A lista digitada é: {lista}')

while True:
    deletar_codigo = int(input('Digite o código para ser retirado da lista: '))# estava em loop por não ter essa entrada de dados.
    if deletar_codigo in lista:
        lista.remove(deletar_codigo)
        break
    else:
        print(f'Este código {deletar_codigo} não esta na lista!')
    
print(f'O Código deletado foi: {deletar_codigo}, a lista atualizada é: {lista}')