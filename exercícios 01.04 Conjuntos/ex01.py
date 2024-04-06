# 1. Verificação de Elemento: Crie um conjunto com os nomes de seus amigos.
# Peça ao usuário para digitar um nome. Verifique se o nome está no conjunto e informe o usuário se ele é seu amigo ou não.

amigos_conjunto={'Tay', 'The', 'Mat', 'Kat'}
lista = []
consulta_amigo = input('Digite um nome para verificação: ')
if consulta_amigo in amigos_conjunto:
    print('É seu amigo(a)!')
    print(type(amigos_conjunto))
    print(type(consulta_amigo))
else:
    print('Não é seu amigo(a)!')
#lista.append(consulta_amigo)
#lista = set(lista)
#mais_amigos = amigos_conjunto | lista
#print(type(lista))
#print(type(mais_amigos))
#print(mais_amigos)