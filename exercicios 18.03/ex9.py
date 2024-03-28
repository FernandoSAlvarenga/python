#Crie um código que gere uma tupla contendo os números ímpares de 1 a 10
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14 , 15, 16, 17, 18, 19, 20 )

print(tuple(filter(lambda x: x % 2 != 0, tupla)))