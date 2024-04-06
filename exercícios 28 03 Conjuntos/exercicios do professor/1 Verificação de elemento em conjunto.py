#1Verificação de elemento em conjunto:
#Escreva um programa que verifique se um determinado elemento está presente em um conjunto. Utilize if e else para exibir mensagens informativas.
conjunto = {"a", "b", "c"}
elemento = "b"

if elemento in conjunto:
  print(f"O elemento {elemento} está presente no conjunto.")
else:
  print(f"O elemento {elemento} não está presente no conjunto.")