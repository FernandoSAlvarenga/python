num1 = int(input('Digite o número: '))

fat = 1
i = 2
while i <= num1:
    fat = fat*i
    i += 1
print(f'O fatorial de {num1} é {fat}')