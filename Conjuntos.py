meu_subconjunto={}
uniao_conjuntos={'Matheus', 'Peres'}
meu_conjunto = {'Lucas', 30, True}
while True:
  operacao = input("Digite a operação desejada (01 = Teoria,02 = Comandos,03 = Sair): ")

  if operacao == "01":
    print("################################## Conjuntos em Python ##################################")
    print("Os conjuntos em Python são estruturas de dados que armazenam coleções não ordenadas e sem elementos duplicados.")
    print("Eles são úteis para realizar operações matemáticas como união, interseção e diferença entre conjuntos.")

  elif operacao == "02":
    while True:
      operacao_comandos = input("Digite a operação desejada em Comandos (01 = Criação,02 = Operações,03 = Acessando,04 = Sair): ")

      if operacao_comandos == "01":
        print("################################## Criação de Conjuntos ##################################")
        print("A maneira mais comum de criar um conjunto é usar chaves e separar os elementos por vírgulas.")
        print("Exemplo:\nmeu_conjunto = {'Lucas', 30, True}")

        meu_conjunto = {'Lucas', 30, True}
        print(f"Criado: {meu_conjunto}")

        print("################################## Criação de Conjuntos Vazios ##################################")
        print("É possível criar um conjunto vazio usando o construtor set().")
        print("Exemplo:\nmeu_conjunto_vazio = set()")

        meu_conjunto_vazio = set()
        print(f"Criado: {meu_conjunto_vazio}")
      elif operacao_comandos == "02":
         print("################################## Operações com Conjuntos ##################################")
         while True:
          operacao_conjuntos = input("Digite a operação desejada em Operações (01 = União,02 = Interseção,03 = Diferença,04 = Diferença Simétrica,05 = Subconjunto,06 = Superconjunto,07 = Sair): ")

          if operacao_conjuntos == "01":
            print("################################## União de Conjuntos ##################################")
            print("A união de dois conjuntos A e B é o conjunto que contém todos os elementos de A e de B.")
            print("Exemplo:\nmeu_conjunto_uniao = meu_conjunto | {'Matheus', 'Peres'}")

            meu_conjunto_uniao = meu_conjunto | {'Matheus', 'Peres'}#| em Python é chamado de operador de união de conjuntos.
            meu_conjunto_uniao1 = meu_conjunto | uniao_conjuntos#| em Python é chamado de operador de união de conjuntos.
            print(f"União: {meu_conjunto_uniao}")
            print(f"União1: {meu_conjunto_uniao1}")

            print("################################## Usando o método union() ##################################")
            print("A mesma operação de união pode ser realizada usando o método union().")
            print("Exemplo:\nmeu_conjunto_uniao = meu_conjunto.union({'Matheus', 'Peres'})")

            meu_conjunto_uniao = meu_conjunto.union({'Matheus', 'Peres'})
            meu_conjunto_uniao = meu_conjunto.union(uniao_conjuntos)
            print(f"União: {meu_conjunto_uniao}")

          elif operacao_conjuntos == "02":
            print("################################## Interseção de Conjuntos ##################################")
            print("A interseção de dois conjuntos A e B é o conjunto que contém os elementos que estão em ambos A e B.")
            print("Exemplo:\nmeu_conjunto_intersecao = meu_conjunto & {'Lucas', 'Matheus'}")

            meu_conjunto_intersecao = meu_conjunto & {'Lucas', 'Matheus'}
            print(f"Interseção: {meu_conjunto_intersecao}")

            print("################################## Usando o método intersection() ##################################")
            print("A mesma operação de interseção pode ser realizada usando o método intersection() Essa operação é muito útil quando precisamos descobrir elementos que duas listas possuem em comum:.")
            print("Exemplo:\nmeu_conjunto_intersecao = meu_conjunto.intersection({'Lucas', 'Matheus'})")

            meu_conjunto_intersecao = meu_conjunto.intersection({'Lucas', 'Matheus'})
            print(f"Interseção: {meu_conjunto_intersecao}")

          elif operacao_conjuntos == "03":
            print("################################## Diferença de Conjuntos ##################################")
            print("A diferença de dois conjuntos A e B é o conjunto que contém os elementos de A que não estão em B. A diferença entre dois conjuntos")
            print("Exemplo:\nmeu_conjunto_diferenca == meu_conjunto.difference({'Lucas'})")
            meu_conjunto_diferenca = meu_conjunto - {'Lucas'}
            print(f"Diferença: {meu_conjunto_diferenca}")

            print("################################## Usando o método difference() ##################################")
            print("A mesma operação de diferença pode ser realizada usando o método difference().")
            print("Exemplo:\nmeu_conjunto_diferenca = meu_conjunto.difference({'Lucas'})")

            meu_conjunto_diferenca = meu_conjunto.difference({'Lucas'})
            print(f"Diferença: {meu_conjunto_diferenca}")
          elif operacao_conjuntos == "04":
            print("################################## Diferença Simétrica de Conjuntos ##################################")
            print("A diferença simétrica de dois conjuntos A e B é o conjunto que contém os elementos que estão em A ou em B, mas não em ambos.")
            print("Exemplo:\nmeu_conjunto_diferenca_simetrica = meu_conjunto.symmetric_difference({'Pedro', 'Carlos'})")

            meu_conjunto_diferenca_simetrica = meu_conjunto.symmetric_difference({'Pedro', 'Carlos'})
            print(f"Diferença Simétrica: {meu_conjunto_diferenca_simetrica}")

          elif operacao_conjuntos == "05":
            print("################################## Subconjunto ##################################")
            meu_conjunto = {'João', 'Maria', 'Lucas', 'Ana'}
            meu_subconjunto = {'Lucas', 'Ana'}
            print("Um conjunto A é subconjunto de outro conjunto B se todos os elementos de A estão em B.")
            print("Exemplo:\nmeu_subconjunto = {'Lucas', 'Ana'}")
            print(f"{'Lucas', 'Ana'} é subconjunto de {meu_conjunto} ? {meu_subconjunto.issubset(meu_conjunto)}")

          elif operacao_conjuntos == "06":
            print("################################## Superconjunto ##################################")
            meu_conjunto = {'João', 'Maria', 'Lucas', 'Ana'}
            print(meu_conjunto)
            print("Um conjunto A é superconjunto de outro conjunto B se todos os elementos de B estão em A.")
            print("Exemplo:\nmeu_superconjunto = {'João', 'Maria', 'Lucas', 'Ana', 'Pedro', 'Carlos'}")
            
            
            print(f"{meu_conjunto} é superconjunto de {'Lucas', 'Ana'}{meu_conjunto.issuperset({'Lucas', 'Ana'})}")



          elif operacao_conjuntos == "07":
            print("Saindo...")
            break
          else:
            print("Operação inválida. Digite uma opção válida.")
      elif operacao_comandos =="03":
        print("################################## Acessando ##################################")
        while True:
          acessando_conjuntos = input("Digite a operação desejada em acessando (01 = Percorrer,02 = Acessar elementos específicos (com limitações), 03= Sair): ")
          if acessando_conjuntos=="01":
            print("################################## Percorrer o Conjunto ##################################")
            print("Percorrer um conjunto significa iterar por cada elemento do conjunto e executar uma ação específica para cada um. Essa ação pode ser simplesmente imprimir o elemento, realizar um cálculo, ou qualquer outra operação que você deseje.")
            print("################################## Usando um loop for ##################################")
            print("conjunto = {'banana', 'maçã', 'laranja'}")
            conjunto = {"banana", "maçã", "laranja"}
            print("for fruta in conjunto:")
            for fruta in conjunto:
              print(fruta)
            print("O loop for itera por cada elemento do conjunto conjunto.Em cada iteração, a variável fruta recebe o valor do elemento atual.O código dentro do loop é executado para cada valor de fruta.")
            print("################################## Usando a função map ##################################")
            print("conjunto = {'banana', 'maçã', 'laranja'}")
            conjunto = {"banana", "maçã", "laranja"}
            print("frutas_maiúsculas = map(str.upper, conjunto)")
            frutas_maiúsculas = map(str.upper, conjunto)
            print("for fruta in frutas_maiúsculas:")
            for fruta in frutas_maiúsculas:
              print(fruta)
            print("A função map aplica uma função a cada elemento do conjunto e retorna um novo conjunto com os resultados.No exemplo acima, a função str.upper() converte cada elemento para letras maiúsculas.O loop for imprime os elementos do novo conjunto frutas_maiúsculas")
            print("################################## Verificar se um Elemento Existe ##################################")
            print(" if 'banana' in conjunto:")
            if "banana" in conjunto:
              print("A banana está no conjunto.")
          elif acessando_conjuntos=='02':
            print("################################## Acessar elementos específicos (com limitações) ##################################")
            print("Em Python, conjuntos não suportam indexação como listas ou tuplas. Isso significa que você não pode acessar um elemento específico em um conjunto usando sua posição.No entanto, existem algumas maneiras de acessar elementos específicos em um conjunto, com algumas limitações:")
            print("################################## Usando o método pop ##################################")
            print("O método pop() remove e retorna um elemento aleatório do conjunto")
            print("conjunto = {'banana', 'maçã', 'laranja'}")
            conjunto = {"banana", "maçã", "laranja"}
            print("elemento_removido = conjunto.pop()")
            elemento_removido = conjunto.pop()
            print(f"Elemento removido: {elemento_removido}")
            print("##################################  Usando um loop for com uma condição ##################################")
            print("Você pode usar um loop for para iterar por cada elemento do conjunto e verificar se ele atende à sua condição.")
            print("conjunto = {'banana', 'maçã', 'laranja'}")
            conjunto = {"banana", "maçã", "laranja"}
            print("fruta_procurada = 'maçã'")
            fruta_procurada = "maçã"
            print("for fruta in conjunto:")
            for fruta in conjunto:
              print("if fruta == fruta_procurada:")
              if fruta == fruta_procurada:
                print(f"Encontramos a fruta {fruta_procurada}!")
          elif acessando_conjuntos=='03':
            print('saido')
            break
      elif operacao_comandos=="03":
        print("Saindo...")
        break
      else:
        print("Operação inválida. Digite uma opção válida.")

        
      
       