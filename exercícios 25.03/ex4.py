#4. Encontrar a Posição do Menor Valor em uma Lista:

lista = []

while len(lista) <= 5:
    lista_digitada = int(input('Digite o número: '))
    lista.append(lista_digitada)
print(f'O menor valor é: {min(lista)}')

