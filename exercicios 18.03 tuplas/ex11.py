#Crie um código que concatene duas tuplas em uma única tupla

tupla1 = (1, 3, 5, 7, 9)
tupla2 = (2, 4, 6, 8, 10)

tupla_contatenada = sorted(tupla1 + tupla2) #sorted apresenta os itens dentro da tupla de forma ordenada.

print(f'A tupla concatenada fica assim: {tupla_contatenada}')