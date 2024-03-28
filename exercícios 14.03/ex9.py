saldo = 0

while True:
    print("Bem-vindo ao BF - Banco do Fe.")
    print("1. Verificar Saldo")
    print("2. Fazer Depósito")
    print("3. Fazer Saque")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Saldo disponível:", saldo)
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        print("Depósito de", valor_deposito, "efetuado com sucesso.")
    elif opcao == 3:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor_saque
            print("Saque de", valor_saque, "efetuado com sucesso.")
    elif opcao == 4:
        print("Obrigado por usar o Sistema de Caixa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")