tupla = (10, 100, 30, 40 ,50 )

soma_valor = sum(tupla)
media = soma_valor // len(tupla) #a divisão estava com uma barra(/), o resultado retornava float. Matheus explicou para retornar int, precisava de duas barras (//)
print("A soma dos valores: ", media)
print(soma_valor)# pus este print para poder tentar identificar porque meu resultado era float. esse resulta é int