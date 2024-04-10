#Crie um dicionário que mapeie nomes de frutas para seus preços. Em  seguida, utilize os métodos keys(), values() e items() para 
# imprimir as chaves, valores e pares chave-valor do dicionário, respectivamente.

frutas = {'banana':5.99, 'maça': 7.99, 'pera': 18.99, 'kiwi': 24.99, 'ameixa':18.99}

print('Chaves: ')
for chave in frutas.keys():
    print(chave)
    
print('\n Valores: ')
for valor in frutas.values():
    print(valor)
    
print('Pares: ')
for chave, valor in frutas.items():
    print(f'Chave: {chave}, Valor: {valor}')