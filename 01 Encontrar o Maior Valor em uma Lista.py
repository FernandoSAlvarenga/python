# 01 Encontrar o Maior Valor em uma Lista
lista = []
while True:
  tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
  if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
    break
  else:
    print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
  
  valor = input("Digite um número inteiro e pressione enter para agregar o valor à lista (ou pressione {} para parar): ".format(tecla_parada))
  if valor == tecla_parada:
    break
  try:
    numero = int(valor)
  except ValueError:
    print("Valor inválido. Digite um número inteiro.")
  else:
   
    lista.append(numero)
if lista != []:
    print("Lista de números inteiros:", lista)
else:
   print("Sua lista está vazia")
try:
    maior_valor = lista[0] # Define o maior valor como o primeiro elemento da lista.
    for i in range(1, len(lista)):# Itera pela lista a partir do segundo elemento
        if lista[i] > maior_valor:# Compara cada elemento com o maior valor atual
           maior_valor = lista[i]# Atualiza o maior valor se encontrar um elemento maior
    print(f"O maior valor é: {maior_valor}")# Exibe o maior valor encontrado
    #simplificação
    print(f"O maior valor é: {max(lista)}")
except ValueError:
  print("Para saber o maior valor, a lista deve ter pelo menos um elemento")

  