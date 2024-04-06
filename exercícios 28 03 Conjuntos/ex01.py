# 1. Escreva um programa que verifique se um determinado elemento está presente em um conjunto. Utilize if e else para exibir mensagens informativas

conjunto_element={'do', 're', 'mi', 'fa', 'so', 'la', 'si'}
#lista = []
consulta_element = input('Digite um nome para verificação: ')
if consulta_element in conjunto_element:
    print('Este elemento esta presente(a)!')
    print(type(conjunto_element))
    print(type(consulta_element))
else:
    print('Não é seu amigo(a)!')