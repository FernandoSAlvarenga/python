


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
tipo_operacao1 = input("Digite a operação: ")


if tipo_operacao1 == '+' :
    print(f"Soma: {numero1 + numero2}")
elif tipo_operacao1 == '-' :
    print(f"Subtração: {numero1 - numero2}")
elif tipo_operacao1 == '*' :
    print(f"multiplicação: {numero1 * numero2}")
elif tipo_operacao1 == '/' :
    print(f"Divisão: {numero1 / numero2}")