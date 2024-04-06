# 2. Interseção de conjuntos: Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença em ambos os conjuntos

conjunto_element={'do', 're', 'mi', 'si'}
conjunto_element2={'fa', 'so', 'la', 'si'}
conjunto_comum=set()
if conjunto_element != conjunto_element2:
    conjunto_comum = conjunto_element & conjunto_element2
    print(f'{conjunto_comum}')
else:
    print(f'Não contém.')