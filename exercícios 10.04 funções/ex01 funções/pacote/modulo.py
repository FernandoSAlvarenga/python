import pacote1.calculadora

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

pacote1.calculadora.soma(num1, num2) # aqui estou puxando (usando) a função soma do arquivo pacote1.calculadora. Não preciso repetir código, uso de outro arquivo. 
pacote1.calculadora.divisao(num1, num2) 
pacote1.calculadora.multiplicacao(num1, num2)
pacote1.calculadora.subtracao(num1, num2)