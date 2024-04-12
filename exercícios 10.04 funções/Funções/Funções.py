while True:
    
    
    operacao = input("Digite a operação desejada (01 = Teoria, 02 = Funções Built-in,03 = Funções Personalizadas:,04 = sair ): ")

    
    if operacao == "01":
        print("##################################Funções em Python ##################################")
        print("funções são blocos de código reutilizáveis que realizam tarefas específicas. Elas são definidas usando a palavra-chave def, seguida pelo nome da função e parênteses. As funções oferecem diversas vantagens, como:")
        print("Organização: Permitem dividir tarefas complexas em partes menores e gerenciáveis, tornando o código mais legível e fácil de entender.")
        print("Reutilização: Evitam a repetição de código, simplificando a manutenção e o desenvolvimento de programas.")
        print("Modularidade: Facilitam a criação de módulos independentes que podem ser facilmente importados e utilizados em outros projetos.")
        print("Eficiência: Permitem otimizar o código, evitando a execução desnecessária de instruções.")
    elif operacao == "02":
         print("##################################Funções Built-in##################################")
         print("São funções pré-definidas que já estão disponíveis no Python. Exemplos: print(), input(), len(), abs().")
         valor = -20
         print('O valor absoluto de -20 é:', abs(valor))
         nome = "José"
         print(len(nome))
    elif operacao == "03":
        while True:
            operacao_comandos = input("Digite a operação desejada em Comandos (01 = Criação, 02 = Parâmetros e Valores de Retorno, 03 = Visualização e Depuração de Funções,04 = Variáveis Locais 05 = Variáveis Globais Palavras-chave global, 06 = Palavras-chave nonlocal,07=Argumentos Nomeados,08=Valores Padrão,09=Passando Funções como Argumentos,10 = Funções Recursivas em Python,11 = sair): ")
            if operacao_comandos == "01":
                print("################################## Criação de Funções##################################")
                print("Para criar uma função, você usa a palavra-chave def seguida do nome da função, parênteses para os parâmetros (se houver) e dois pontos.") 
                print("Depois, você coloca o código da função dentro de um bloco indentado.")
                print("def saudacao():\n print('Olá, mundo!')\n saudacao()")
                def saudacao():
                    print("Olá, mundo!")

                saudacao() 
                print("Em Python, def é uma palavra-chave que marca o início da definição de uma função. É como se avisasse o Python que você está criando um bloco de código reutilizável, projetado para realizar uma tarefa específica.") 
                print("Início da Definição: Quando você vê def no começo de um bloco de código, significa que você está definindo uma função.")
                print("Nome da Função: Depois do def vem o nome que você escolhe para sua função. Esse nome deve ser descritivo e refletir o propósito da função. Por exemplo, uma função que calcula área poderia se chamar calcula_area.")
                print("Parâmetros (Opcional): Após o nome da função, você pode incluir opcionalmente parênteses (). Esses parênteses podem conter parâmetros. A função pode usar esses parâmetros dentro do seu código para realizar sua tarefa.")
                print("Dois pontos (:) :  Dois pontos : seguem os parênteses (mesmo que não haja parâmetros). Esse dois pontos basicamente separa o cabeçalho da função (incluindo o nome e parâmetros) do corpo da função.")
                print("Corpo da Função: O bloco de código indentado após os dois pontos define a funcionalidade principal da função. É aqui que você escreve as instruções que a função deve seguir para completar sua tarefa.")
                print("def funciona como o ponto de partida para definir funções em Python, permitindo a criação de blocos de código reutilizáveis e modulares.")
            elif operacao_comandos == "02":
                print("##################################Parâmetros e Valores de Retorno em Funções##################################")
                print("As funções em Python podem receber valores como entrada, chamados de parâmetros. São como peças de um carro para a função para que ela possa realizar seu trabalho.")
                print("Exemplo:")
                print("def soma(x, y):\n return x + y")
                print("Considere a função soma(x, y) que soma dois números:")
                print("Aqui, x e y são os parâmetros da função. Ao chamar a função, você precisa fornecer valores para esses parâmetros:")
                print("resultado = soma(2, 3)")
                print("As funções em Python podem retornar valores usando a instrução return. É como se a função devolvesse um resultado após concluir sua tarefa.")
                def soma(x, y):
                    return x + y

                resultado = soma(2, 3) 
                print(resultado)   
            elif operacao_comandos == "03":
                print("##################################Visualização e Depuração de Funções##################################")
                print("Print: Utilizar a função print dentro das funções é um método simples para visualizar valores intermediários durante a execução e facilitar a depuração.")
                def soma(x, y):
                    print(f"Valores recebidos: x = {x}, y = {y}")
                    resultado = x + y
                    print(f"Resultado da soma: {resultado}")
                    return resultado

                numero_1 = 5
                numero_2 = 10

                soma_final = soma(numero_1, numero_2)

                print(f"Soma final: {soma_final}")


                
                print("Ao executar o código, o debugger pdb será ativado, permitindo que você inspecione variáveis, avance linha por linha e examine o estado interno da função.")
                print("O que é pdb.set_trace()?É uma função do módulo pdb embutido em Python.Ele funciona como uma ferramenta poderosa para depurar seu código inserindo um ponto de interrupção temporário na linha exata onde você o chama.Quando a execução do programa chega a esse ponto de interrupção, ele pausa e entra no prompt interativo do depurador Python (PDB).")
                import pdb


                def soma(a, b):
                    return a + b

                x = 5
                y = 10

                resultado = soma(x, y)

               
                pdb.set_trace()

                print(f"Resultado: {resultado}")
                import pdb

                def calcular_area(comprimento, largura):
                    if comprimento < 0 or largura < 0:
                        raise ValueError("Comprimento e largura devem ser não negativos")
                    area = comprimento * largura
                    pdb.set_trace() 
     
                    return area

                try:
                    resultado = calcular_area(-2, 5)  
                    print(resultado)
                except ValueError as e:
                    print(e)
            elif operacao_comandos == "04":
                 print("##################################Variáveis Locais em Funções##################################")
                 print("As variáveis declaradas dentro de uma função são locais e só existem dentro daquela função.Elas são criadas quando a função é chamada e destruídas quando a função termina.Isso significa que outras funções não podem acessar diretamente essas variáveis.")
                 
                 def soma(x, y):
                  resultado = x + y
                  return resultado

                 numero_1 = 5
                 numero_2 = 10

                 soma_local = soma(numero_1, numero_2)

                 print(f"Soma local: {soma_local}")  # Imprime 15

                 try:
                    print(f"Resultado dentro da função: {resultado}")  # Erro: 'resultado' não está definido
                 except NameError as e:
                    print(f"Erro: {e}")  
            elif operacao_comandos =="05":
                print("##################################Variáveis Globais em Funções##################################")
                print("As variáveis declaradas fora de qualquer função são globais e podem ser acessadas por todas as funções no módulo.Cuidado: Modificar variáveis globais dentro de funções pode ter efeitos colaterais indesejados em outras partes do código.")
                print("A palavra-chave global é usada para modificar uma variável global dentro de uma função.")
                numero_global = 10

                def multiplica(x):
                    global numero_global
                    numero_global *= x
                    return numero_global

                resultado_multiplicacao = multiplica(5)


                print(f"Resultado multiplicação: {resultado_multiplicacao}")  
                print(f"Número global: {numero_global}") 

                print("É recomendável usar variáveis locais sempre que possível para evitar efeitos colaterais e melhorar a legibilidade do código.Use variáveis globais com moderação e cuidado.As palavras-chave nonlocal e global podem ser úteis em alguns casos específicos, mas devem ser usadas com cautela.")
            elif operacao_comandos =="06":
                 print("##################################Palavras-chave nonlocal em Funções##################################")
                 print("A palavra-chave nonlocal é usada para modificar uma variável não local (declarada em uma função pai) dentro de uma função aninhada.")
                 def funcao_externa():
                    numero_nao_local = 10

                    def funcao_interna():
                        nonlocal numero_nao_local
                        numero_nao_local *= 2
                        print(f"Número não local dentro da função interna: {numero_nao_local}")

                        funcao_interna()

                    funcao_externa()

                    print(f"Número não local fora da função: {numero_nao_local}")
                    print("É recomendável usar variáveis locais sempre que possível para evitar efeitos colaterais e melhorar a legibilidade do código.Use variáveis globais com moderação e cuidado.As palavras-chave nonlocal e global podem ser úteis em alguns casos específicos, mas devem ser usadas com cautela.")
            elif operacao_comandos=="07":
                 print("##################################Argumentos Nomeados em Funções##################################")
                 print("Permitem passar valores para parâmetros em ordem diferente da definida na função.Úteis quando a ordem dos parâmetros não é intuitiva ou quando você deseja destacar um valor específico.")
                 def saudacao(nome, mensagem="Olá"):
                    print(f"{mensagem}, {nome}!")

                 saudacao(nome="João")  
                 saudacao(mensagem="Bem-vindo", nome="Maria") 
            elif operacao_comandos=="08":
                print("##################################Valores Padrão em Funções##################################")
                print("Permitem definir valores para parâmetros que não são passados na chamada da função.Úteis para tornar a função mais flexível e evitar erros caso um parâmetro não seja especificado.")
                print("Os argumentos nomeados e os valores padrão podem ser usados juntos.Ao usar valores padrão, coloque os parâmetros com valor padrão ao final da lista de parâmetros.")
                def area_retangulo(comprimento, largura=10):
                    return comprimento * largura

                area_1 = area_retangulo(5)  
                area_2 = area_retangulo(5, 8)  

                print(f"Área 1: {area_1}")
                print(f"Área 2: {area_2}")   
            elif operacao_comandos=="09":
                 print("##################################Passando Funções como Argumentos:##################################")
                 print("Funções podem ser passadas como argumentos para outras funções.Isso permite que você crie funções genéricas que operam em outras funções.")
                 def aplicar_funcao(funcao, valor):
                    return funcao(valor)

                 def dobro(x):
                    return x * 2

                 resultado_dobro = aplicar_funcao(dobro, 5)  # 'dobro' é passada como argumento

                 print(f"Resultado do dobro: {resultado_dobro}")  # Imprime 10
            elif operacao_comandos=="10":
                  print("##################################Funções Recursivas em Python##################################")
                  print("Uma função recursiva é uma função que chama a si mesma durante sua execução.Essa técnica é útil para resolver problemas que podem ser divididos em subproblemas menores do mesmo tipo.")
                  print("Estrutura de uma Função Recursiva:\n Possui dois elementos principais:Caso base: Condição que indica quando a função deve parar de se chamar. Caso recursivo: Parte da função que se chama a si mesma, utilizando o resultado obtido para resolver o subproblema.")
                  def fatorial(numero):
 
                    print(f"Calculando fatorial({numero})...")
                    if numero == 0:
                        print(f"Fatorial({numero}) = 1")
                        return 1
                    else:
                        resultado = numero * fatorial(numero - 1)
                        print(f"Fatorial({numero}) = {numero} * fatorial({numero - 1})")
                        print(f"Fatorial({numero - 1}) = {resultado}")
                        return resultado

                  numero_fatorial = 6

                  resultado_fatorial = fatorial(numero_fatorial)

                  print(f"Fatorial de {numero_fatorial}: {resultado_fatorial}")
                  def descascar_cebola(cebola):
                        """
                        Descascando uma cebola recursivamente e imprimindo cada movimento.

                        Argumentos:
                            cebola: Uma lista que representa a cebola, com cada camada sendo um elemento da lista.

                        Retorno:
                            A cebola descascada, que é uma lista vazia.
                        """
                        if cebola == []:
                            print("Cebola descascada!")
                            return []
                        else:
                            print(f"Removendo camada {cebola[0]} da cebola.")
                            return descascar_cebola(cebola[1:])

                    # Exemplo de uso
                  cebola = ["Casca 1", "Casca 2", "Casca 3", "Miolo"]
                  descascar_cebola(cebola)
            elif operacao_comandos=="11":
                break
            else:
                print('Valor invalido')
    elif operacao =="04":
        break
    else:
        print('Valor invalido')





































































