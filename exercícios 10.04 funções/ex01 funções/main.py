import modulo #aqui eu importei o arquivo módulo

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

modulo.soma(num1, num2) # aqui estou puxando (usando) a função soma do arquivo modulo. Não preciso repetir código, uso de outro arquivo. 
modulo.divisao(num1, num2) 
modulo.multiplicacao(num1, num2)
modulo.subtracao(num1, num2)