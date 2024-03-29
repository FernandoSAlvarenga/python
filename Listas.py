minha_lista = ["Lucas", 30, True]
minha_lista_string = ["Lucas", "Matheus", "Peres"]
minha_lista_int = [30, 40, 50]
minha_lista_Float = [30.5, 40.5, 50.5]
minha_lista_Bolean = [True,False]
minha_lista_4_elementos = ["Lucas", 30, True, "Porto Alegre", "Matheus", 35, False, "Canoas"]
lista_nomes = ['Lucas', 'Rodolfo', 'Aristeu']
while True:
  operacao = input("Digite a operação desejada (01 = Teoria,02 = Comandos,03 = Sair): ")
  if operacao == "01":
    print("##################################Listas em Python##################################")
    print("As listas em Python são estruturas de dados que armazenam uma coleção ordenada de valores. Elas são mutáveis, o que significa que seus elementos podem ser adicionados, removidos ou modificados após a criação.")
   
    print("##################################mutabilidade##################################")
    print("Ao contrário das tuplas, as listas podem ser modificadas após a criação. Você pode adicionar, remover ou modificar elementos da lista usando diversos métodos.")
   
    print("##################################Vantagens e desvantagens##################################")
    print("As listas são mais flexíveis do que as tuplas, mas podem ser menos eficientes em termos de memória e desempenho..")
    
    print("##################################Quando usar Listas##################################")
    print("As listas são uma boa escolha para armazenar dados que precisam ser alterados, como uma lista de compras ou uma lista de tarefas.")
  elif operacao == "02":
    while True:
      opercao_comandos = input("Digite a operação desejada em Comandos (01 = Criação,02 = Operações,03 = Acessando, 04 = Construindo,05 = Fatiamento,06 = Funções e Métodos,07 = Sair): ")
      if opercao_comandos == "01":
         print("##################################Criação de Listas##################################")
         print("A maneira mais comum de criar uma lista é usar colchetes e separar os elementos por vírgulas.")
         print("###################################Lista com um elemento##################################")
         print("inha_lista_um_elemento = ['Olá',]")
         print("###################################Lista com três elementos##################################")
         print("minha_lista_tres_elementos = ('Lucas', 30, True)")
         print("###################################Lista com três elementos string##################################")
         print("minha_lista_string = ['Lucas', 'Matheus', 'Peres']")
         print("###################################Lista com três elementos int##################################")
         print("minha_lista_int = [30, 40, 50]")
      elif opercao_comandos == "02":
         print("###################################Operações com Listas###################################")
         while True:
           opercao_listas = input("Digite a operação desejada em Oprações (01 = Adição, 02 =Remoção, 03 = Modificação,04 = Converter em string,05 = Converter em tupla,06 = Concatenar,07 = Repetição,08 = Sair): ")
           
           if opercao_listas=="01":
             print("##################################Adição##################################")
             print("Você pode adicionar elementos ao final da lista usando o método append() ou inserir elementos em qualquer posição usando o método insert().")
             print("Adicionando um elemento ao final da lista usando o método append(): lista.append('Tiburcio')")
              # Adicionando um elemento ao final da lista usando o método append()
             lista_nomes.append('Tiburcio')
             print("Imprimindo a lista atualizada:print(lista)")
              # Imprimindo a lista atualizada
             print(lista_nomes)  
             # Saída: ["Lucas", "Rodolfo", "Aristeu", "Tiburcio"]
             print("inserindo um elemento em uma posição específica usando o método insert(): lista.insert(1, 'Edesvom')")
              # Inserindo um elemento em uma posição específica usando o método insert()
             lista_nomes.insert(1, 'Edesvom')
             print("Imprimindo a lista atualizada: print(lista)")
              # Imprimindo a lista atualizada
             print(lista_nomes)  
             # Saída:["Lucas","Edesvom", "Rodolfo", "Aristeu", "Tiburcio"]
           elif opercao_listas=="02":
             print("##################################Remoção##################################")
             print("Você pode remover elementos da lista usando o método remove() ou o método pop().")
             print("Removendo um elemento específico da lista usando o método remove() :lista_nomes.remove('Lucas')")
             # Removendo um elemento específico da lista usando o método remove()
             lista_nomes.remove('Lucas')
             print("Imprimindo a lista atualizada: print(lista_nomes)")
             # Imprimindo a lista atualizada
             print(lista_nomes)  
             # Saída: ['Rodolfo', 'Aristeu']
             print("Removendo o último elemento da lista usando o método pop(): ultimo_item = lista_nomes.pop()")
             # Removendo o último elemento da lista usando o método pop()
             ultimo_item = lista_nomes.pop()
             print("Imprimindo a lista atualizada: print(ultimo_item)")
             # Imprimindo o elemento removido
             print(ultimo_item)  
             # Saída: Aristeu
             print("Imprimindo a lista atualizada:print(lista_nomes)")
             # Imprimindo a lista atualizada
             print(lista_nomes)  
             # Saída: ['Rodolfo']
           elif opercao_listas=="03":
              print("##################################Modificação##################################")
              print("Você pode modificar elementos da lista usando o operador de atribuição =.")
              print("# Modificando um elemento da lista usando o operador de atribuição =: lista_nomes[1] = 'Teles'")
              print(lista_nomes)
              # Modificando um elemento da lista usando o operador de atribuição =
              lista_nomes[1] = 'Teles'
              print("Imprimindo a lista atualizada:print(lista_nomes)")
              # Imprimindo a lista atualizada
              print(lista_nomes)  # Saída: ['Lucas', 'Teles', 'Aristeu']
           elif opercao_listas=="04":
            print("Você pode converter uma lista em uma string usando a função str().")
            print("Exemplo\n minha_string = str(minha_lista)")
            minha_string = str(minha_lista)
            print(f"retorna{minha_string}")
            tipo = type(minha_string)
            print(f"retorna{tipo}")

           elif opercao_listas=="05":
             print("Você pode converter uma lista em uma tupla usando o construtor tuple().")
             print("Exemplo\n minha_tupla = tuple(minha_lista)")
             minha_tupla = tuple(minha_lista)
             print(f"retorna{minha_tupla}")
           elif opercao_listas=="06":
              print("##################################Concatenar listas##################################")
              print("O operador "+" pode ser usado para concatenar duas listas, criando uma nova lista com os elementos das duas listas originais.")
              print("lista_concatenada = minha_lista_string + lista_nomes.")
              lista_concatenada = minha_lista_string + lista_nomes
              print(lista_concatenada)
              print("##################################Método extend()##################################")
              print("O método extend() de uma lista pode ser usado para adicionar os elementos de outra lista à lista original.")
              print("lista_nomes.extend(minha_lista_int)")
              lista_nomes.extend(minha_lista_int)
              print(lista_nomes)
              print("################################## Função zip()##################################")
              print("A função zip() pode ser usada para criar uma lista de tuplas, onde cada tupla contém os elementos da mesma posição nas listas originais.")
              print(" lista_conctenada = list(zip(lista_nomes, lista_nomes))")
              lista_conctenada = list(zip(lista_nomes, lista_nomes))
              print(lista_conctenada)
              departamentos = ["Frutas", "Legumes", "Carnes", "Laticínios"]
              produtos = ["Maçã", "Batata", "Frango", "Leite"]

              lista_compras = list(zip(departamentos, produtos))

              print(lista_compras)
              # Saída: [('Frutas', 'Maçã'), ('Legumes', 'Batata'), ('Carnes', 'Frango'), ('Laticínios', 'Leite')]


           elif opercao_listas=="07":
            print("################################## Repetição em Listas##################################")
            print("Existem diversas maneiras de repetir elementos em listas em Python. Aqui estão algumas das mais comuns:")
            print("##################################Multiplicação de listas##################################")
            print("O operador * pode ser usado para multiplicar uma lista por um número inteiro, repetindo seus elementos o número especificado de vezes.")
            print("lista = ['a', 'b', 'c']")
            lista = ['a', 'b', 'c']
            print("lista_repetida = lista * 3")

            lista_repetida = lista * 3
            print(" print(lista_repetida)")
            print(lista_repetida)
            print("##################################Laço for##################################")
            print("Um laço for pode ser usado para iterar sobre os elementos de uma lista e executar um bloco de código para cada elemento.")
            lista = ["a", "b", "c"]
            print("lista = ['a', 'b', 'c']")
            print("for elemento in lista:")
            for elemento in lista:
              print(elemento * 3)

            print("##################################List Comprehension##################################")
            print("Uma List Comprehension pode ser usada para criar uma nova lista com os elementos da lista original repetidos o número especificado de vezes.")
            lista = ['a', 'b', 'c']
            print("lista = ['a', 'b', 'c']")

            lista_repetida = [elemento * 3 for elemento in lista]
            print("lista_repetida = [elemento * 3 for elemento in lista]")

            print(lista_repetida)


           elif opercao_listas=="08":
             break
           else:
             print("opeeração invalida")
      elif opercao_comandos=="03":
         print("##################################Acessando Listas##################################")
         print("Os elementos de uma lista podem ser acessados usando índices, que são números entre colchetes. O primeiro elemento tem índice 0, o segundo índice 1, e assim por diante.")
         print("minha_lista = [Lucas, 30, True]")
         print("nome = minha_lista[0]")
         nome = minha_lista[0]
         print(f"retornando {nome}")
         print("idade = minha_lista[1]")
         idade = minha_lista[1]
         print(f"retornando {idade}")
         print("verdadeiro_falso = minha_lista[2]")
         verdadeiro_falso = minha_lista[2]
         print(f"retornando {verdadeiro_falso}")
         # Inicialização da lista
         minha_lista_nomes = []
         # Loop para validação da entrada
         while len(minha_lista_nomes) < 3:
            nomes = input("Digite os nomes separados por vírgula (máximo de 3): ").split(",")
            # Verificação do limite
            if len(nomes) > 3:
                print("Limite de 3 itens excedido. Tente novamente.")
                continue
            # Adição dos nomes à lista
            minha_lista_nomes.extend(nomes)
          # Acesso aos elementos
         print(f"\nPrimeiro elemento: {minha_lista_nomes[0]}")
         print(f"Segundo elemento: {minha_lista_nomes[1]}")
         print(f"Terceiro elemento: {minha_lista_nomes[2]}")
         # Observação
         print("\nLembre-se: você pode acessar qualquer elemento da lista usando seu índice.")
      elif opercao_comandos=="04":
        print("##################################Construindo listas##################################")
        print("Você também pode usar o construtor list() para criar uma lista a partir de uma sequência iterável, como uma string.")
        print('lista_nomes = ["lucas", Fabio, Reinaldo]\n minha_lista_nomes = list(lista_nomes)')
        print("Exemplo: Criando uma lista a partir de uma sequência iterável usando o construtor `list()`.")
        # Inicialização da lista
        minha_lista_nomes = []
        # Loop para validação da entrada
        while len(minha_lista_nomes) < 3:
            nomes = input("Digite os nomes separados por vírgula (máximo de 3): ").split(",")
            # Verificação do limite
            if len(nomes) > 3:
                print("Limite de 3 itens excedido. Tente novamente.")
                continue
            # Adição dos nomes à lista
            minha_lista_nomes.extend(nomes)
        # Saída formatada
        print(f"\nSua lista de nomes é: {minha_lista_nomes}")
      elif opercao_comandos=="05":
        print("##################################Fatiamento##################################")
        print("Você pode usar fatiamento para obter uma sublista de uma lista. O fatiamento usa a mesma sintaxe que as strings.")
        print('O índice -1 em Python se refere ao último elemento da sequência.')
        print("cidade = minha_lista_4_elementos[-1]")
        cidade = minha_lista_4_elementos[-1]
        print(f"retornando {cidade}")
        print("verdadeiro_falso = minha_lista[-1]")
        verdadeiro_falso = minha_lista[-1]
        print(f"retornando {verdadeiro_falso}")
        print("cidade = minha_lista_4_elementos[-2]")
        cidade = minha_lista_4_elementos[-2]
        print(f"retornando {cidade}")
        print("verdadeiro_falso = minha_lista[-2]")
        verdadeiro_falso = minha_lista[-1]
        print(f"retornando {verdadeiro_falso}")
        print("##################################Criando uma nova lista com uma de Base##################################")
        print("A sintaxe minha_lista_menor[1:3] significa que a  minha_lista_menor conterá os elementos da lista original desde o índice 1 (inclusive) até o índice 3 (exclusive).")
        print("minha_lista_menor = minha_lista[1:3]")
        minha_lista_menor = minha_lista_4_elementos[1:3]
        print(f"retornando {minha_lista_menor}")
        print("A sintaxe minha_lista[0:2] significa que a  minha_lista_menor conterá os elementos da lista original desde o índice 0 (inclusive) até o índice 2 (exclusive).")
        print("minha_lista_menor = minha_lista[0:2]")
        minha_lista_menor = minha_lista_4_elementos[0:2]
        print(f"retornando {minha_lista_menor}")
        print("A sintaxe minha_lista[1:] significa que a  minha_lista_menor conterá os elementos da lista original desde o índice 1 (inclusive) até o índice final.")
        print("minha_lista_menor = minha_lista[1:]")
        minha_lista_menor = minha_lista_4_elementos[1:]
        print(f"retornando {minha_lista_menor}")
      elif opercao_comandos=="06":
        while True:
          operacao_funcoes_metodos = input("Digite a operação desejada (01 = len(),02 = min,03 = max,04 = list.count(),05 = list.index(),06 = sorted(),07 = sair): ")
          if operacao_funcoes_metodos == "01":
            print("###################################Usando a função len()###################################")
            print("A função len() retorna o número de elementos em uma lista.")
            print("Exemplo\n tamanho_da_lista=len(minha_lista)")
            print(f'lembrando que o total da nossa lista é:{len(minha_lista)}')
          elif operacao_funcoes_metodos == "02":
            print("###################################Usando a função min###################################")
            print("###################################Usando a função min string em Lista Homogênea###################################")
            print("A função min() retorna o menor elemento da lista.")
            print("Exemplo\n tamanho_da_lista=min(minha_lista)")
            print(f'menor elemento da lista é: {min(minha_lista_string)}')
            print("###################################Usando a função min Int em Lista Homogênea###################################")
            print("A função min() retorna o menor elemento da lista.")
            print("Exemplo\n tamanho_da_lista=min(minha_lista)")
            print(f'menor elemento da lista é: {min(minha_lista_int)}')
            print("###################################Usando a função min Float em Lista Homogênea###################################")
            print("A função min() retorna o menor elemento da lista.")
            print("Exemplo\n tamanho_da_lista=min(minha_lista)")
            print(f'menor elemento da lista é: {min(minha_lista_Float)}')
            print("###################################Usando a função min Bolean em Lista Homogênea###################################")
            print("A função min() retorna o menor elemento da lista.")
            print("Exemplo\n tamanho_da_lista=min(minha_lista)")
            print(f'menor elemento da lista é: {min(minha_lista_Bolean)}')
            
            print("###################################Usando a função min em lista Heterogênea###################################")
            # Convertendo os elementos para string
            lista_str = [str(elemento) for elemento in minha_lista]
            # Encontrando o menor elemento
            menor_elemento = min(lista_str)
            print(f"Menor elemento: {menor_elemento}") 
          elif operacao_funcoes_metodos == "03":
           print("###################################Usando a função max###################################")
           print("###################################Usando a função max() string em Lista Homogênea###################################")
           print("A função max() retorna o maior elemento da lista.")
           print("Exemplo\n tamanho_da_lista=max(minha_lista)")
           print(f'maior elemento da lista tupla é: {max(minha_lista_string)}')
           print("###################################Usando a função max() Int em Lista Homogênea###################################")
           print("A função max() retorna o maior elemento da lista.")
           print("Exemplo\n tamanho_da_lista=max(minha_lista)")
           print(f'maior elemento da lista é: {max(minha_lista_int)}')
           print("###################################Usando a função max() Float em Lista Homogênea###################################")
           print("A função max() retorna o maior elemento da lista.")
           print("Exemplo\n tamanho_da_lista=max(minha_lista)")
           print(f'maior elemento da lista é: {max(minha_lista_Float)}')
           print("###################################Usando a função max() Bolean em Lista Homogênea###################################")
           print("A função max() retorna o maior elemento da lista.")
           print("Exemplo\n tamanho_da_lista=max(minha_lista)")
           print(f'maior elemento da lista é: {max(minha_lista_Bolean)}')
            # Convertendo os elementos para string
           lista_str = [str(elemento) for elemento in minha_lista]
            # Encontrando o maior elemento
           maior_elemento = max(lista_str)
           print(f"Maior elemento: {maior_elemento}")
          elif operacao_funcoes_metodos == "04":
           print("###################################Usando o Método list.count()###################################")
           print("O Metodo list.count() retorna o número de vezes que um elemento aparece na lista.")
           print("Exemplo\n numero_de_lucas = minha_lista.count('Lucas')")
           numero_de_lucas = minha_lista.count('Lucas')
           print(f"O número de lucas na lista é: {numero_de_lucas}")
          elif operacao_funcoes_metodos == "05":
            print("###################################Usando o Método list.index()###################################")
            print("O Metodo list.index() retorna o índice da primeira ocorrência de um elemento específico na lista.")
            print("Exemplo\n  indice_lucas = minha_lista.index('Lucas')")
            try:
              indice_lucas = minha_lista.index('Lucas')
              print(f"O primeiro índice de lucas na lista é: {indice_lucas}")
            except ValueError:
              print("Elemento 'Lucas' não encontrado na lista")
          elif operacao_funcoes_metodos=="06":
            print("################################### Usando a função sorted()###################################")
            print("A função sorted() pode ser usada para ordenar qualquer sequência iterável, incluindo listas.")
            print("Exemplo\n  tupla_ordenada = sorted(minha_lista_int)")
            tupla_ordenada = sorted(minha_lista_int)
            print(f"retorna: {tupla_ordenada}")
            print("Exemplo\n  tupla_ordenada = sorted(minha_lista_string)")
            tupla_ordenada = sorted(minha_lista_string)
            print(f"retorna: {tupla_ordenada}")
            print("Exemplo\n  tupla_ordenada = sorted(minha_lista_string, reverse=True)")
            tupla_ordenada = sorted(minha_lista_string, reverse=True)
            print(f"retorna: {tupla_ordenada}")
          elif operacao_funcoes_metodos=="07":
            break
          else:
            print("Operação inválida")
      elif opercao_comandos == "07":
        break
      else:
        print("Operação inválida.")
  elif operacao == "03":
    break
  else:
    print("Operação inválida.")
