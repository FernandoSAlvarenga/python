def fatorial(x):
    fat = 1
    i = 2
    while i <= x:
        fat = fat*i
        i += 1
    print(f'O fatorial de {x} é {fat}')