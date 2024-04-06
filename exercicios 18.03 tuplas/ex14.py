#Crie um código que remova um determinado elemento de uma tupla

tupla = (20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 )

posicao_remove = 10

lista = list(tupla)
lista.remove(posicao_remove)

tupla_atualizada = tuple(lista)

print(tupla_atualizada)