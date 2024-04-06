estoque = {}

while True:
    print("\nSistema de Controle de Estoque")
    print("1. Consultar Produto")
    print("2. Adicionar Produto")
    print("3. Remover Produto")
    print("4. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        produto_consulta = input("Digite o nome do produto: ")
        if produto_consulta in estoque:
            print("Produto:", produto_consulta)
            print("Quantidade:", estoque[produto_consulta])
        else:
            print("Produto não encontrado no estoque.")
    elif opcao == 2:
        produto_adicionar = input("Digite o nome do produto: ")
        quantidade_adicionar = int(input("Digite a quantidade a ser adicionada: "))
        estoque[produto_adicionar] = estoque.get(produto_adicionar, 0) + quantidade_adicionar
        print("Produto adicionado com sucesso.")
    elif opcao == 3:
        produto_remover = input("Digite o nome do produto: ")
        quantidade_remover = int(input("Digite a quantidade a ser removida: "))
        if produto_remover in estoque:
            if quantidade_remover <= estoque[produto_remover]:
                estoque[produto_remover] -= quantidade_remover
                print("Produto removido com sucesso.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado no estoque.")
    elif opcao == 4:
        print("Obrigado por usar o Sistema de Controle de Estoque. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")