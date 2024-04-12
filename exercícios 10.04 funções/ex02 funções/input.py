#2. Maior número: Crie uma função que recebe dois números como parâmetros e retorna o maior entre eles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


if numero1 > numero2:
    print(f' O Número {numero1} é maior que {numero2}')
else:
    print(f' O Número {numero2} é maior que {numero1}')

