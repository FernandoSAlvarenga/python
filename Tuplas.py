saldo = 0
minha_tupla=("Lucas",30,True)
minha_tupla_string=("Lucas","Matheus","Peres")
minha_tupla_int=(30,40,50)
minha_tupla_4_elementos=("Lucas",30,True,'Porto Alegre',"Matheus",35,False,'Canoas')
lista_nomes = ["lucas", "Fabio", "Reinaldo"]
while True:
  operacao = input("Digite a operação desejada (01=Teoria,02=Comandos,03=Sair): ")
  if operacao == "01":
    print("##################################Tuplas em Python##################################")
    print("O que é uma tupla? Uma tupla em Python é uma estrutura de dados que armazena uma coleção ordenada de valores.'\nÉ similar a uma lista, mas com uma diferença crucial: as tuplas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação.")
   
    print("##################################Imutabilidade##################################")
    print("Uma vez que uma tupla é criada, seus elementos não podem ser alterados. Isso significa que você não pode adicionar, remover ou modificar elementos da tupla.")
   
    print("##################################Vantagens e desvantagens##################################")
    print("As tuplas são mais eficientes em termos de memória e desempenho do que as listas. No entanto, sua imutabilidade pode ser uma desvantagem em algumas situações.")
    
    print("##################################Quando usar tuplas##################################")
    print("As tuplas são uma boa escolha para armazenar dados que não precisam ser alterados, como coordenadas de pontos, datas ou informações de contato.")
  elif operacao == "02":
    while True:
      opercao_comandos = input("Digite a operação desejada (01 = Criação,02 = Construtor,03 = Acessando,04 = Fatiamento,05 = Operações,06 = Conversão,07 = Funções e Métodos,08 = Sair): ")
      if opercao_comandos == "01":
         print("##################################Criando tuplas##################################")
         print("A maneira mais comum de criar uma tupla é usar parênteses e separar os elementos por vírgulas.")
         print("################################### Tupla com um elemento##################################")
         print('minha_tupla = ("Olá",)')
         print("###################################Tupla com três elementos##################################")
         print("minha_tupla = (Lucas, 30, True)")

      if opercao_comandos == "02":
        print("##################################Construindo tuplas##################################")
        print("Você também pode usar o construtor tuple() para criar uma tupla a partir de uma sequência iterável, como uma lista ou string.")
        print('lista_nomes = [lucas, Fabio, Reinaldo]\n minha_tupla_nomes = tuple(lista_nomes)')
        minha_tupla_nomes = tuple(lista_nomes)
        print(f"Que retorna: {minha_tupla_nomes}")

      elif opercao_comandos == "03":
        print("##################################Acessando Elementos##################################")
        print("Os elementos de uma tupla podem ser acessados usando índices, que são números entre colchetes. O primeiro elemento tem índice 0, o segundo índice 1, e assim por diante.")
        print("minha_tupla=(Lucas,30,True")
        print("nome = minha_tupla[0]")
        nome = minha_tupla[0]
        print(f"retornando {nome}")
        print("idade = minha_tupla[1]")
        idade = minha_tupla[1]
        print(f"retornando {idade}")
        print("verdadeiro_falso = minha_tupla[2]")
        verdadeiro_falso = minha_tupla[2]
        print(f"retornando {verdadeiro_falso}")
      
      if opercao_comandos == "04":
        print("##################################Fatiamento##################################")
        print("Você pode usar fatiamento para obter uma subtupla de uma tupla. O fatiamento usa a mesma sintaxe que as strings.")
        print('O índice -1 em Python se refere ao último elemento da sequência.')
        print("cidade = minha_tupla[-1]")
        cidade = minha_tupla_4_elementos[-1]
        print(f"retornando {cidade}")
        print("verdadeiro_falso = minha_tupla[-1]")
        verdadeiro_falso = minha_tupla[-1]
        print(f"retornando {verdadeiro_falso}")
        print("cidade = minha_tupla[-2]")
        cidade = minha_tupla_4_elementos[-2]
        print(f"retornando {cidade}")
        print("verdadeiro_falso = minha_tupla[-2]")
        verdadeiro_falso = minha_tupla[-2]
        print(f"retornando {verdadeiro_falso}")
        print("##################################Criando uma nova tupla com uma de Base##################################")
        print("A sintaxe minha_tupla[1:3] significa que a  minha_tupla_menor conterá os elementos da tupla original desde o índice 1 (inclusive) até o índice 3 (exclusive).")
        print("minha_tupla_menor = minha_tupla[1:3]")
        minha_tupla_menor = minha_tupla[1:3]
        print(f"retornando {minha_tupla_menor}")
        print("A sintaxe minha_tupla[0:2] significa que a  minha_tupla_menor conterá os elementos da tupla original desde o índice 0 (inclusive) até o índice 2a (exclusive).")
        print("minha_tupla_menor = minha_tupla[0:2]")
        minha_tupla_menor = minha_tupla[0:2]
        print(f"retornando {minha_tupla_menor}")
        print("A sintaxe minha_tupla[1:] significa que a  minha_tupla_menor conterá os elementos da tupla original desde o índice 1 (inclusive) até o índice final.")
        print("minha_tupla_menor = minha_tupla[1:]")
        minha_tupla_menor = minha_tupla[1:]
        print(f"retornando {minha_tupla_menor}")

      elif opercao_comandos == "05":
         print("###################################Operações com Tuplas###################################")
         print("###################################Concatenação###################################")
         print("Você pode concatenar duas tuplas usando o operador +.")
         print("tupla_concatenada = minha_tupla + minha_tupla_4_elementos")
         tupla_concatenada = minha_tupla + minha_tupla_4_elementos
         print(f'retorna{tupla_concatenada}')
         print("###################################Repetição###################################")
         print("tupla_repetida = minha_tupla*"  )
         tupla_repetida = minha_tupla * 3
         print(f"retorna{tupla_repetida}")
      elif opercao_comandos == "06":
        print("###################################Conversão com Tuplas###################################")
        print("Você pode converter uma tupla em uma lista usando a função list().")
        print("Exemplo\n minha_lista = list(minha_tupla)")
        minha_lista = list(minha_tupla)
        print(f"retorna{minha_lista}")
        print("Você pode converter uma tupla em uma string usando a função str().")
        print("Exemplo\n minha_string = str(minha_tupla)")
        minha_string =str(minha_tupla)
        print(f"retorna{minha_tupla}")
      elif opercao_comandos == "07":
         while True:
             opercao_funcoes_metodos = input("Digite a operação desejada (01 = len(),02 = min,03 = max,04 = tuple.count(),05 = tuple.index(), 06 = sorted(),07 = sair): ")
             if opercao_funcoes_metodos=="01":
               print("###################################Usando a função len###################################")
               print("A função len() retorna o número de elementos em uma sequência.")
               print("Exemplo\n tamanho_da_tupla=len(minha_tupla)")
               print(f'lembrando que o total da nossa tupla é: {len(minha_tupla)}')
             elif opercao_funcoes_metodos=="02":
               print("###################################Usando a função min###################################")
               print("A função min() retorna o menor elemento da tupla.")
               print("Exemplo\n tamanho_da_tupla=len(minha_tupla)")
               print(f'menor elemento da tupla é: {min(minha_tupla_int)}')
             elif opercao_funcoes_metodos=="03":
               print("###################################Usando a função max###################################")
               print("A função max() retorna o maior elemento da tupla.")
               print("Exemplo\n tamanho_da_tupla=len(minha_tupla)")
               print(f'maior elemento da tupla tupla é: {max(minha_tupla_int)}')
               
             elif opercao_funcoes_metodos=="04":
                print("###################################Usando o Método tuple.count()###################################")
                print("O Metodo tuple.count() retorna o número de vezes que um elemento aparece na tupla.")
                print("Exemplo\n numero_de_lucas = minha_tupla.count(lucas)")
                numero_de_lucas = minha_tupla_string.count('Lucas')
                print(f"O número de lucas na tupla é: {numero_de_lucas}")
             elif opercao_funcoes_metodos=="05":
                print("###################################Usando o Método tuple.index()###################################")
                print("O Metodo tuple.index() retorna o índice da primeira ocorrência de um elemento específico na tupla.")
                print("Exemplo\n  indice_lucas = minha_tupla_string.index('Lucas')")
                indice_lucas =  minha_tupla_string.index('Lucas')
                print(f"O primeiro índice  de lucas na tupla é: {indice_lucas}")
             elif opercao_funcoes_metodos=="06":
                print("################################### Usando a função sorted()###################################")
                print("A função sorted() pode ser usada para ordenar qualquer sequência iterável, incluindo tuplas.")
                print("Exemplo\n  tupla_ordenada = sorted(minha_tupla_int)")
                tupla_ordenada = sorted(minha_tupla_int)
                print(f"retorna: {tupla_ordenada}")
                print("Exemplo\n  tupla_ordenada = sorted(minha_tupla_string)")
                tupla_ordenada = sorted(minha_tupla_string)
                print(f"retorna: {tupla_ordenada}")
                print("Exemplo\n  tupla_ordenada = sorted(minha_tupla_string)")
                tupla_ordenada = sorted(minha_tupla_string, reverse=True)
                print(f"retorna: {tupla_ordenada}")
             
             
             
             elif opercao_funcoes_metodos=="07":
               break
             else:
               print("Operação inválida.")
      elif opercao_comandos == "08":
        break
      else:
        print("Operação inválida.")
   
  elif operacao == "03":
    break
  else:
    print("Operação inválida.")
