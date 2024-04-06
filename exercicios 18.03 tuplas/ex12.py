#Crie um código que divida uma tupla em duas tuplas menores
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14 , 15, 16, 17, 18, 19, 20, 21, 22 )

tamanho = len(tupla)
metade = tamanho//2

tupla1 = tupla[:metade]
tupla2 = tupla[metade:]


print(f'A tupla inicial tinha o tamanho de {tamanho}, dividindo as tuplas: {tupla1} {tupla2}')