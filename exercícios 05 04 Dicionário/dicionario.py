meu_dicionario =  dict()
uniao_dicionarios = {'Matheus': 20, 'Peres': 30}
operacao = None
dicionario_unido = dict()
while True:
    # Menu principal
    if not operacao:
        operacao = input("Digite a operação desejada (01 = Teoria, 02 = Comandos, 03 = Sair): ")

    
    if operacao == "01":
        print("################################## Dicionários em Python ##################################")
        print("Os dicionários em Python são estruturas de dados que armazenam coleções não ordenadas de pares chave-valor.")
        print("Eles são úteis para armazenar dados de forma organizada e acessível, como informações de usuários, configurações de um programa ou dados de um experimento científico.")
        print("Em dicionários, chaves e valores são os dois componentes básicos que formam cada par chave-valor, a estrutura fundamental de um dicionário.\n")
       
        print("Chaves: São identificadores únicos que servem para acessar e referenciar os valores armazenados no dicionário\n As chaves podem ser de diversos tipos de dados, como strings, números, tuplas imutáveis e até mesmo outros dicionários\n Cada chave deve ser única dentro do dicionário, ou seja, não pode haver duas chaves iguais.As chaves são usadas para indexar os valores no dicionário, como se fossem rótulos ou etiquetas.\n")

        print("Valores: São os dados que estão associados a cada chave no dicionário. Os valores podem ser de qualquer tipo de dado, como strings, números, listas,\n objetos e até mesmo funções.Um valor pode estar associado a mais de uma chave, mas cada chave só pode ter um único valor associado a ela. Os valores podem ser acessados através da chave correspondente.\n")

        print("Exemplo: meu_dicionario = {'nome': 'Anacleto','idade': 32,'cidade': 'Xanxerê','profissao': 'Gestor de Mídias Sociais'}")
        print("Chave: 'nome' Valor: 'Anacleto'\n Chave: 'idade' Valor: 32\n Chave: 'cidade' Valor: 'Xanxerê:\n Chave:'profissao' Valor: 'Gestor de Mídias Sociais'")

        operacao = None
        # Comandos
    elif operacao == "02":
        while True:
            # Menu de comandos
            operacao_comandos = input("Digite a operação desejada em Comandos (01 = Criação, 02 = Operações, 03 = Acessando, 04 = Sair): ")
            # Criação de dicionários
            if operacao_comandos == "01":
                print("################################## Criação de Dicionários ##################################")
                print("A maneira mais comum de criar um dicionário é usar chaves e valores separados por vírgulas e entre chaves.")
                print("Exemplo:\nmeu_dicionario = {'nome': 'Lucas', 'idade': 30, 'profissao': 'Desenvolvedor'}")

                meu_dicionario = {'nome': 'Lucas', 'idade': 30, 'profissao': 'Desenvolvedor'}
                print(f"Criado: {meu_dicionario}")

                print("################################## Criação de Dicionários Vazios ##################################")
                print("É possível criar um dicionário vazio usando o construtor dict().")
                print("Exemplo:\nmeu_dicionario_vazio = dict()")

                meu_dicionario_vazio = dict()
                print(f"Criado: {meu_dicionario_vazio}")
                meu_dicionario_com_argumentos = dict(nome="Ana", idade=25, cidade="São Paulo")
                print(f"Dicionário criado com argumentos: {meu_dicionario_com_argumentos}")

                # Cria um dicionário a partir de outro dicionário
                outro_dicionario = dict(meu_dicionario_com_argumentos)
                print(f"Dicionário a partir de outro dicionário: {outro_dicionario}")
                print("É possível criar um dicionário vazio declarando a variavel como { }.")
                print("Exemplo:\ndicionario_vazio = { }")

                dicionario_vazio = {}
                print(f'Criando: {dicionario_vazio}')


                print("################################## Usando o método update() ##################################")
                print("A operação de união pode ser realizada usando o método update().")
                print(" dicionario1 = {'nome': 'Ana', 'idade': 25}")
                print("dicionario2 = {'cidade': 'São Paulo', 'profissao': 'Desenvolvedora'}")
                dicionario1 = {"nome": "Ana", "idade": 25}
                dicionario2 = {"cidade": "São Paulo", "profissao": "Desenvolvedora"}
                print("dicionario1.update(dicionario2)")
                dicionario1.update(dicionario2)
                print("Se houver chaves iguais nos dois dicionários, o valor associado à chave em dicionario2 substituirá o valor em dicionario1.")

                print(f"Dicionários combinados: {dicionario1}")
                

                print("################################## Usando o o operador de desempacotamento ** ##################################")
                print("o operador de desempacotamento **  é usado para desempacotar os pares chave-valor de cada dicionário e criá-los em um novo dicionário, dicionario_unido. O operador ** funciona desde a versão Python 3.5.")
                print("dicionario1 = {'nome': 'Ana', 'idade': 25}")
                print("dicionario2 = {'cidade': 'São Paulo', 'profissao': 'Desenvolvedora'}")
                dicionario1 = {"nome": "Ana", "idade": 25}
                dicionario2 = {"cidade": "São Paulo", "profissao": "Desenvolvedora"}
                print(" dicionario_unido = {**dicionario1, **dicionario2}")

                dicionario_unido = {**dicionario1, **dicionario2}

                print(f"Dicionários unidos: {dicionario_unido}\n")
                print("################################## Usando o o operador de desempacotamento dict.fromkeys() ##################################")
                print("o dict.fromkeys() é usado para pegar soemte as chaves dos dicionaros caso usado sozinho, retornando somente as chaves com os valores como none")
                dicionario_unido = dict.fromkeys(dicionario1.keys() | dicionario2.keys())
                print(f"Dicionários unidos: {dicionario_unido}")

                dicionario_combinado = {}
                #magine que você tem duas caixas de livros:
                dicionario_combinado.update(dict.fromkeys(dicionario1.keys()))#Esta linha usa o método update() para adicionar os pares chave-valor do dicionario1 ao dicionario_combinado.O dict.fromkeys() cria um novo dicionário com as chaves do dicionario1 e os valores padrão (None).O método update() sobrescreve os valores existentes no dicionario_combinado com os valores do novo dicionário criado com dict.fromkeys().
                
                dicionario_combinado.update(dict.fromkeys(dicionario2.keys()))
                #Imagine que você tem três caixas de livros:
                #Pega os títulos dos livros da Caixa 1: dict.fromkeys(dicionario1.keys())
                #Cria uma nova caixa vazia com esses títulos: dict.fromkeys(dicionario1.keys())
                #Coloca os livros da Caixa 1 na Caixa 3: dicionario_combinado.update(dict.fromkeys(dicionario1.keys()))
                #Pega os títulos dos livros da Caixa 2: dict.fromkeys(dicionario2.keys())
                #Cria novos espaços vazios na Caixa 3 com esses títulos: dict.fromkeys(dicionario2.keys())
                #Coloca os livros da Caixa 2 na Caixa 3: dicionario_combinado.update(dict.fromkeys(dicionario2.keys()))


                
                for chave in dicionario_combinado:
                    if chave in dicionario1:
                        dicionario_combinado[chave] = dicionario1[chave]
                    elif chave in dicionario2:
                        dicionario_combinado[chave] = dicionario2[chave]

                print(dicionario_combinado)
                # Depois de criar espaços vazios na Caixa 3 (dicionario_combinado) para os livros das Caixas 1 e 2 (dicionario1 e dicionario2), precisamos preencher esses espaços.

                # Este trecho de código age como um bibliotecário que organiza os livros:

                # O bibliotecário pega cada etiqueta (chave) na Caixa 3:

                # for chave in dicionario_combinado:
                # Ele verifica se a etiqueta (chave) combina com um título na Caixa 1:

                # if chave in dicionario1:
                # Se sim, ele pega o livro correspondente da Caixa 1 e o coloca no espaço vazio da Caixa 3 com a mesma etiqueta.
                # dicionario_combinado[chave] = dicionario1[chave]
                # Se a etiqueta não combina com a Caixa 1, o bibliotecário verifica a Caixa 2:

                # elif chave in dicionario2:
                # Se a etiqueta combina com um título na Caixa 2, ele pega o livro correspondente da Caixa 2 e o coloca no espaço vazio da Caixa 3 com a mesma etiqueta.
                # dicionario_combinado[chave] = dicionario2[chave]
                # Se a etiqueta não combina com nenhuma caixa, o espaço vazio permanece vazio.

                # Depois de verificar todas as etiquetas:

                # O código final (print(dicionario_combinado)) mostra o conteúdo final da Caixa 3, preenchida com os livros correspondentes às Caixas 1 e 2.


            # Operações com dicionários
            elif operacao_comandos == "02":
                print("################################## Operações com Dicionários ##################################")
                while True:
                    # Menu de operações com dicionários
                    operacao_dicionarios = input("Digite a operação desejada em Operações (01 = União, 02 = Interseção, 03 = Diferença, 04 = manipulando 05 = Sair): ")

                    # União de dicionários
                    if operacao_dicionarios == "01":
                        print("################################## União de Dicionários ##################################")
                        print("################################## Usando o método update() ##################################")
                        print("A operação de união pode ser realizada usando o método update().")
                        print('Quando usar: Se você precisa combinar dicionários de qualquer tamanho.Se você precisa lidar com chaves duplicadas de forma personalizada.Se você precisa de mais flexibilidade e controle sobre a atualização do dicionário.')
                        print("Exemplo:\nmeu_dicionario.update({'Matheus': 20, 'Peres': 30})")

                        meu_dicionario.update({'Matheus': 20, 'Peres': 30})
                        print(f"União: {meu_dicionario}")
                        print("################################## Usando o o operador de desempacotamento ** ##################################")
                        print("o operador de desempacotamento **  é usado para desempacotar os pares chave-valor de cada dicionário e criá-los em um novo dicionário, dicionario_unido. O operador ** funciona desde a versão Python 3.5.")
                        print("Quando usar: Se você precisa combinar dicionários pequenos e simples.Se você deseja sobrescrever valores existentes no dicionário original.Se você busca uma sintaxe concisa e legível. ")
                        dicionario1 = {"nome": "Ana", "idade": 25}
                        dicionario2 = {"cidade": "São Paulo", "profissao": "Desenvolvedora"}

                        dicionario_unido = {**dicionario1, **dicionario2}

                        print(f"Dicionários unidos: {dicionario_unido}")
                        print("################################## Usando o o operador de desempacotamento dict.fromkeys() ##################################")
                        print("o operador de desempacotamento Se você estiver usando uma versão anterior do Python é dict.fromkeys()")
                        dicionario_unido = dict.fromkeys(dicionario1.keys() | dicionario2.keys())
                        print(f"Dicionários unidos: {dicionario_unido}")

                        dicionario_combinado = {}
                        #magine que você tem duas caixas de livros:
                        dicionario_combinado.update(dict.fromkeys(dicionario1.keys()))#Esta linha usa o método update() para adicionar os pares chave-valor do dicionario1 ao dicionario_combinado.O dict.fromkeys() cria um novo dicionário com as chaves do dicionario1 e os valores padrão (None).O método update() sobrescreve os valores existentes no dicionario_combinado com os valores do novo dicionário criado com dict.fromkeys().
                        
                        dicionario_combinado.update(dict.fromkeys(dicionario2.keys()))
                        #Imagine que você tem três caixas de livros:
                        #Pega os títulos dos livros da Caixa 1: dict.fromkeys(dicionario1.keys())
                        #Cria uma nova caixa vazia com esses títulos: dict.fromkeys(dicionario1.keys())
                        #Coloca os livros da Caixa 1 na Caixa 3: dicionario_combinado.update(dict.fromkeys(dicionario1.keys()))
                        #Pega os títulos dos livros da Caixa 2: dict.fromkeys(dicionario2.keys())
                        #Cria novos espaços vazios na Caixa 3 com esses títulos: dict.fromkeys(dicionario2.keys())
                        #Coloca os livros da Caixa 2 na Caixa 3: dicionario_combinado.update(dict.fromkeys(dicionario2.keys()))


                        
                        for chave in dicionario_combinado:
                            if chave in dicionario1:
                                dicionario_combinado[chave] = dicionario1[chave]
                            elif chave in dicionario2:
                                dicionario_combinado[chave] = dicionario2[chave]

                        print(dicionario_combinado)
                        # Depois de criar espaços vazios na Caixa 3 (dicionario_combinado) para os livros das Caixas 1 e 2 (dicionario1 e dicionario2), precisamos preencher esses espaços.

                        # Este trecho de código age como um bibliotecário que organiza os livros:

                        # O bibliotecário pega cada etiqueta (chave) na Caixa 3:

                        # for chave in dicionario_combinado:
                        # Ele verifica se a etiqueta (chave) combina com um título na Caixa 1:

                        # if chave in dicionario1:
                        # Se sim, ele pega o livro correspondente da Caixa 1 e o coloca no espaço vazio da Caixa 3 com a mesma etiqueta.
                        # dicionario_combinado[chave] = dicionario1[chave]
                        # Se a etiqueta não combina com a Caixa 1, o bibliotecário verifica a Caixa 2:

                        # elif chave in dicionario2:
                        # Se a etiqueta combina com um título na Caixa 2, ele pega o livro correspondente da Caixa 2 e o coloca no espaço vazio da Caixa 3 com a mesma etiqueta.
                        # dicionario_combinado[chave] = dicionario2[chave]
                        # Se a etiqueta não combina com nenhuma caixa, o espaço vazio permanece vazio.

                        # Depois de verificar todas as etiquetas:

                        # O código final (print(dicionario_combinado)) mostra o conteúdo final da Caixa 3, preenchida com os livros correspondentes às Caixas 1 e 2.

                    # Interseção de dicionários
                    elif operacao_dicionarios == "02":
                        print("################################## Interseção de Dicionários ##################################")
                        print("é o processo de encontrar os elementos que estão presentes em ambos os dicionários.\n Isso pode ser útil para comparar dois conjuntos de dados, encontrar chaves ou valores em comum ou para remover elementos de um dicionário que não estão presentes em outro.\n")
                        print("##################################Comparação de chaves##################################")
                        print("Este método é simples e eficiente para dicionários pequenos.Ele percorre as chaves de um dicionário e verifica se elas estão presentes no outro dicionário.As chaves em comum são então adicionadas a um novo dicionário.")
                        dicionario1 = {"a": 1, "b": 2, "c": 3}
                        dicionario2 = {"b": 4, "c": 5, "d": 6}

                        intersecao = {}

                        for chave in dicionario1:
                            if chave in dicionario2:
                                intersecao[chave] = dicionario1[chave]

                        print(intersecao)
                        print("##################################Operadores de conjunto:##################################")
                        print("O operador & pode ser usado para encontrar a interseção de dois conjuntos.Os conjuntos podem ser criados a partir dos dicionários usando a função dict.keys().")
                        dicionario1 = {"a": 1, "b": 2, "c": 3}
                        dicionario2 = {"b": 4, "c": 5, "d": 6}

                        intersecao = set(dicionario1.keys()) & set(dicionario2.keys())

                        print(intersecao)
                    
                    #Diferença
                    elif operacao_dicionarios == "03":
                        print("################################## Diferença de Dicionários ##################################")
                        print("##################################Comparação de chaves.##################################")
                        print("Usando um loop for para iterar sobre as chaves de um dicionário.Verifique se cada chave está presente no outro dicionário usando o operador in.Adicione as chaves que não estão presentes ao outro dicionário a um novo dicionário ou conjunto.")
                        dicionario1 = {"a": 1, "b": 2, "c": 3}
                        dicionario2 = {"b": 4, "c": 5, "d": 6}

                        diferenca_chaves = {}
                        for chave in dicionario1:
                            if chave not in dicionario2:
                                diferenca_chaves[chave] = dicionario1[chave]

                        print(diferenca_chaves)

                        # Cria os dicionários
                        dicionario1 = {"a": 1, "b": 2, "c": 3}
                        dicionario2 = {"b": 4, "c": 5, "d": 6}

                        # Encontra as chaves em `dicionario1` que não estão em `dicionario2`
                        diferenca_chaves = set(dicionario1.keys()) - set(dicionario2.keys())

                        # Cria um dicionário com as diferenças de valor
                        diferenca_valores = {chave: dicionario1[chave] for chave in diferenca_chaves}
                        #A expressão chave: dicionario1[chave] define uma chave-valor para cada iteração.
                        #A chave é a variável chave que itera sobre o conjunto diferenca_chaves.
                        #O valor é o valor associado à chave chave no dicionário dicionario1.
                        #Iteração sobre o conjunto diferenca_chaves:
                        #O conjunto diferenca_chaves contém as chaves que estão presentes em dicionario1 mas não em dicionario2.
                        #Para cada chave em diferenca_chaves, a expressão chave: dicionario1[chave] é avaliada e o resultado é adicionado ao dicionário diferenca_valores.
                        #O dicionário diferenca_valores conterá as chaves que estão em dicionario1 mas não em dicionario2, e os valores associados a essas chaves em dicionario1.
                        # Imprime as diferenças
                        print(f"Chaves em dicionario1 que não estão em dicionario2: {diferenca_chaves}")
                        print(f"Diferenças de valor: {diferenca_valores}")


                        print("##################################Comparação de valores.##################################")
                        print("Usando um loop for para iterar sobre os pares chave-valor de um dicionário.Verifique se cada par chave-valor está presente no outro dicionário usando o operador in. Adicione os pares chave-valor que não estão presentes ao outro dicionário a um novo dicionário.")
                        dicionario1 = {"a": 1, "b": 2, "c": 3}
                        dicionario2 = {"b": 4, "c": 5, "d": 6}

                        diferenca_valores = {}
                        #Itera sobre cada par de chave-valor no dicionário dicionario1.
                        for chave, valor in dicionario1.items():
                         #Verifica se a chave e o valor do par atual não estão presentes no dicionário
                         if (chave, valor) not in dicionario2.items():
                            diferenca_valores[chave] = valor

                        print(diferenca_valores)
                        print('Sem os parênteses: A expressão verifica se a tupla invertida está presente na lista. Isso nunca será verdadeiro, pois a tupla invertida não é uma tupla válida.\n Com os parênteses: A expressão verifica se a tupla está presente na lista. Isso pode ser verdadeiro, se a chave e o valor estiverem presentes em dicionario2')
                    elif operacao_dicionarios == "04":
                        print("################################## Manipulando Dicionários ##################################")
                        print("################################## dict.get('chave', valor_padrao) ##################################")
                        print("dict.get('chave', valor_padrao) é um método de dicionário que busca o valor associado à chave especificada. Se a chave não for encontrada, o método retorna o valor padrão especificado.")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        sobrenome = meu_dicionario.get("sobrenome", "Não Informado")

                        print(f"Sobrenome: {sobrenome}")  
                        

                        print("################################## setdefault('chave', valor) ##################################")
                        print("verifica se a chave especificada existe no dicionário. Se a chave não existir, o método a cria e define seu valor como o valor especificado. Se a chave já existir, o método simplesmente retorna o valor associado à chave.")
                        dicionariometodoset = {"nome": "João"}

                        dicionariometodoset.setdefault("sobrenome", "Silva")

                        print(dicionariometodoset)
                        print("Vantagens de usar dict.setdefault():É mais conciso e legível que usar instruções if para verificar se a chave existe e, se não, criá-la e definir seu valor.Evita código redundante para verificar se a chave existe.É útil para inicializar valores em um dicionário com base em chaves que podem ou não existir.")
                        print("################################## dicionario.update(dicionario) ##################################")
                        print("O método update()  é uma ferramenta para atualizar dicionários de forma eficiente. Ele permite adicionar, modificar ou remover pares chave-valor de um dicionário existente, simplificando a manipulação de dados.")
                    
                        meu_dicionario = {"nome": "João"}

                        novo_dicionario = {"idade": 25, "cidade": "São Paulo"}

                        meu_dicionario.update(novo_dicionario)

                        print(meu_dicionario)
                        print("################################## dicionario.pop(chave) ##################################")
                        print(" O método pop() é utilizado para remover um elemento (par chave-valor) de um dicionário.pop() é um método aplicado ao dicionário meu_dicionario.Entre parênteses, fornecemos a chave  que queremos remover.Ao executar esse código, o par chave-valor será completamente eliminado do dicionário meu_dicionario.")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        meu_dicionario.pop("idade")

                        print(meu_dicionario)

                        print("Para removermos só a idade precisamos usar de algumas opções")
                        print("Usando o método get() com valor padrão:")
                        print("O método get() permite recuperar o valor associado a uma chave, definindo um valor padrão caso a chave não exista. Você pode usar essa funcionalidade para verificar se o valor da chave 'idade' é 25 e, se for, definir um novo valor.")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        nova_idade = meu_dicionario.get("idade", None)

                        if nova_idade == 25:
                            meu_dicionario["idade"] = None

                        print(meu_dicionario)
                        
                        
                        
                        print("Usando If")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        if meu_dicionario["idade"] == 25:
                            meu_dicionario["idade"] = None

                        print(meu_dicionario)
                        
                        
                        print("Usando For")
                        meu_dicionario = {"nome": "João", "idade": 25, "amigos": ["Ana", "Maria", 25]}

                        for chave in meu_dicionario:
                            if meu_dicionario["idade"] == 25:
                                meu_dicionario["idade"] = None

                        print(meu_dicionario)




                        print("##################################dicionario.popitem()##################################")
                        print("O método popitem() é usado para remover um item aleatório do dicionário.O resultado da remoção é armazenado em duas variáveis: chave e valor.A variável chave armazena a chave do item removido.A variável valor armazena o valor do item removido.")

                        meu_dicionario = {"nome": "João", "idade": 25}

                        chave, valor = meu_dicionario.popitem()

                        print(f"Chave: {chave}, Valor: {valor}")





                        print("##################################dicionario.clear()##################################")
                        print("O metodo clear() limpa o dicionário")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        meu_dicionario.clear()

                        print(meu_dicionario)
                        
                        print("################################## in ##################################")

                        meu_dicionario = {"nome": "João"}

                        chave_existe = "nome" in meu_dicionario

                        print(f"A chave 'nome' existe? {chave_existe}")



                        print("##################################dicionario.Keys()##################################")
                        print("Retorna as chaves do dicionário")

                        meu_dicionario = {"nome": "João", "idade": 25}

                        chaves = meu_dicionario.keys()

                        print(chaves)
                        
                        print("##################################dicionario.values()##################################")
                        print("Retorna os valores do dicionário")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        valores = meu_dicionario.values()

                        print(valores)

                        print("##################################dicionario.items()##################################")
                        print("Retorna os uma lista de tuplas, onde cada tupla consiste em uma chave e um valor do dicionário")
                        meu_dicionario = {"nome": "João", "idade": 25}

                        itens = meu_dicionario.items()

                        print(itens) 
                       
                       


                        print("##################################dicionario.copy()##################################")
                        print("Retorna uma copia do dicionario") 
                        meu_dicionario = {"nome": "João"}

                        copia_dicionario = meu_dicionario.copy()

                        copia_dicionario["idade"] = 25

                        print(meu_dicionario)  # Dicionário original não modificado
                        print(copia_dicionario)
                        print('##################################dict.fromkeys()##################################')
                        print("O método dict.fromkeys() é uma maneira concisa de criar um dicionário com um valor padrão para todas as chaves.Você pode usar qualquer tipo de objeto como chave ou valor em um dicionário.A ordem das chaves em um dicionário não é garantida.")
                        frutas = dict.fromkeys(["banana", "maçã", "laranja"], "Não informado")

                        print(frutas)

                               
                        print("##################################loop for com dicionario.items()##################################")
                        print("O loop for é usado para iterar sobre uma sequência de elementos.No caso de um dicionário, a sequência é a lista de pares de chaves e valores.A variável chave recebe a chave do par atual em cada iteração.A variável valor recebe o valor associado à chave atual em cada iteração.​​")

                        meu_dicionario = {"nome": "João", "idade": 25}

                        for chave, valor in meu_dicionario.items():
                            print(f"Chave: {chave}, Valor: {valor}")


                      
                        print('################################## Criando um dicionário com input do usuário:##################################')
                        nome = input("Digite seu nome: ")
                        idade = int(input("Digite sua idade: "))

                       
                        pessoa = {"nome": nome, "idade": idade}

                        print(f"Dados da pessoa: {pessoa}")
                        print('################################## Criando um dicionário com input do usuário:##################################')
                       
                        cliente = {"nome": "João"}

                        
                        sobrenome = input("Digite seu sobrenome: ")

                        
                        cliente["sobrenome"] = sobrenome

                        print(f"Dados do cliente atualizados: {cliente}")
                        print("################################## Criando um dicionário com input do usuário:##################################")
                        produtos = {"camiseta": 20, "calca": 30}
                        produto_pesquisado = input("Digite o nome do produto: ")
                        if produto_pesquisado in produtos:
                            preco = produtos[produto_pesquisado]
                            print(f"Preço do {produto_pesquisado}: R${preco}")
                        else:
                            print(f"Produto '{produto_pesquisado}' não encontrado.")
                    elif operacao_dicionarios == "05":
                        break
                    else:
                        print('Valor invalido')
            #Acessando dicionário
            elif operacao_comandos == "03":
                print('################################## Acessando Dicionários ##################################')
                print("Para acessar o valor associado a uma chave específica em um dicionário: dicionario['chave']")
                print("Exemplo:")
                print("meu_dicionario = {'nome': 'João', 'idade': 25}")
                meu_dicionario = {"nome": "João", "idade": 25}
                print(" nome = meu_dicionario['nome']")
                nome = meu_dicionario["nome"]
                print("idade = meu_dicionario['idade']")
                idade = meu_dicionario["idade"]
                print(f"Nome: {nome}, Idade: {idade}")
                print('################################## Usando o método get() ##################################')
                print("O método get() é uma maneira mais segura de acessar valores em um dicionário, pois ele retorna None se a chave não for encontrada, evitando erros.")
                print(" meu_dicionario = {'nome': 'carlos', 'idade': 55}")
                meu_dicionario = {"nome": "carlos", "idade": 55}
                print("nome = meu_dicionario.get('nome')")
                nome = meu_dicionario.get("nome")
                print("sobrenome = meu_dicionario.get('sobrenome')")
                sobrenome = meu_dicionario.get("sobrenome")
                print(f"Nome: {nome}, Sobrenome: {sobrenome}")
                print('################################## Verificando se uma chave existe: ##################################')
                print("Utilize o operador in para verificar se uma chave existe em um dicionário:.")
                print(" meu_dicionario = {'nome': 'carlos', 'idade': 55}")
                meu_dicionario = {"nome": "carlos", "idade": 55}
                print("chave_existe = nome in meu_dicionario")
                chave_existe = "nome" in meu_dicionario
                print(f"A chave 'nome' existe? {chave_existe}")
                print('##################################  Percorrendo um dicionário: ##################################')
                print("Para iterar sobre as chaves e valores de um dicionário, utilize um loop for:")
                print(" meu_dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}")
                meu_dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
                print("for chave, valor in meu_dicionario.items():")
                for chave, valor in meu_dicionario.items():
                    print(f"Chave: {chave}, Valor: {valor}")
                    #meu_dicionario.items(): Este método retorna uma lista de tuplas contendo as chaves e valores do dicionário.
                    #for chave, valor in meu_dicionario.items(): Esta linha itera sobre a lista de tuplas retornada pelo método items(). A cada iteração, a chave e o valor da tupla atual são atribuídos às variáveis chave e valor, respectivamente.
                    #f"Chave: {chave}, Valor: {valor}": Esta f-string formata a chave e o valor atual de forma legível. A f-string é então utilizada como argumento da função print().
            #Saindo
            elif operacao_comandos =="04":
                break
            else:
                print('Valor invalido')
    elif operacao =="03":
        break
    else:
        print('Valor invalido')