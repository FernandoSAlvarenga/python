while True:
            operacao_teoria = input("Digite a operação desejada em Comandos (00= Teoria ,01 = Classes, 02 = Objetos,03 = Atributos, 04 = Métodos,05 = Herança 06 = Polimorfismo, 07 = Encapsulamento,08=Abstração,09=Modificadores de Acesso,10=sair): ")
            if operacao_teoria =="01":
                print("##################################Classe##################################")
                print("As classes servem como modelos para a criação de objetos. São como plantas que definem a estrutura e o comportamento de objetos específicos.")
                print("Assim como uma planta define as características de uma árvore (tamanho, cor das folhas, tipo de fruto), uma classe define as características de um objeto (atributos e métodos)\n")
                print("Atributos")
                print("São as características de um objeto.")
                print("Representam informações que definem o estado do objeto.")
                print("Exemplos: nome, idade, cor, tamanho, etc.\n")    
                print("Métodos:")
                print("São as ações que um objeto pode realizar.")   
                print("Representam o comportamento do objeto.")    
                print("Exemplos: comer, correr, falar, calcular, etc.\n")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower() == "s":#A função lower() em Python é usada para converter todas as letras maiúsculas em uma string em caracteres minúsculos.
                    class Pessoa:
                        def __init__(self, nome, idade, sexo):#atributos
                            self.nome = nome
                            self.idade = idade
                            self.sexo = sexo

                        def falar(self):
                            print(f"Olá, meu nome é {self.nome}")# métodos

                    pessoa1 = Pessoa("João", 25, "M")
                    pessoa2 = Pessoa("Maria", 30, "F")

                    pessoa1.falar()
                    pessoa2.falar()
            elif operacao_teoria =="02":
                print("##################################Objetos##################################")
                print("Representam um bloco de construção modular que reúne dados (atributos) e comportamentos (métodos) para modelar entidades do mundo real.\n")
                print("Imagine um objeto 'Carro'\n")
                print("Atributos (dados): cor, modelo, ano, velocidade.\n")
                print("Métodos (comportamentos): ligar, desligar, acelerar, frear.\n")
                print("Características dos objetos em Python")
                print("Herança: Permite que um objeto herde atributos e métodos de outro, promovendo reutilização de código.")
                print("Polimorfismo: Permite que objetos de diferentes classes respondam à mesma mensagem de maneiras distintas.")
                print("Encapsulamento: Protege os dados internos, controlando o acesso externo.")
                print("Abstração: Oculta detalhes da implementação, expondo apenas o essencial.")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower() == "s":
                    class Animal:
                        def __init__(self, nome):#atributos
                            self.nome = nome

                        def falar(self):
                            print(f"Olá, meu nome é {self.nome}")# métodos

                    class Cachorro(Animal):
                        def latir(self):
                            print("Au au!")

                    # Criando objetos
                    cachorro1 = Cachorro("Rex")

                    # Acessando atributos
                    print(f"Nome do cachorro: {cachorro1.nome}")

                    # Chamando métodos
                    cachorro1.falar()
                    cachorro1.latir()

                    # A classe Cachorro herda da classe Animal.
                    # O objeto cachorro1 tem acesso aos atributos e métodos da classe Animal e da classe Cachorro               
            elif operacao_teoria =="03":
                 print("##################################Atributos##################################")
                 print("Os atributos representam as características de um objeto. São como variáveis que armazenam informações relevantes sobre o estado do objeto.")
                 print("Assim como um carro possui características como cor, modelo e ano de fabricação, um objeto em POO possui atributos que definem suas características.")
                 print("Atributos de instância: São específicos para cada objeto criado a partir da classe.")
                 continuar_atibutos_instancia = input("Deseja printar o código abaixo sobre Atributos de instância ? (s/n) ")
                 if continuar_atibutos_instancia.lower() == "s":
                     class Carro:# Classe Carro: Define o modelo para a criação de objetos "carro".
                        def __init__(self, cor, modelo, ano):#atributos. O Método __init__: É o construtor da classe, responsável por inicializar os atributos quando um objeto é criado.
                            self.cor = cor#self.cor: Armazena a cor do carro.
                            self.modelo = modelo#self.modelo: Armazena o modelo do carro.
                            self.ano = ano#self.ano: Armazena o ano de fabricação do carro.

                        #O parâmetro self atua como uma referência ao objeto atual dentro do método. Ao utilizar self.atributo, o método acessa o valor do atributo correspondente para aquele objeto específico.
                        def ligar(self):#Método ligar: Simula a ação de ligar o carro.
                            print(f"O carro {self.modelo} {self.cor} de {self.ano} ligou!")#Utiliza f-strings para formatar a mensagem com os valores dos atributos.
                       
                        #O parâmetro self atua como uma referência ao objeto atual dentro do método. Ao utilizar self.atributo, o método acessa o valor do atributo correspondente para aquele objeto específico.
                        def desligar(self):#Método desligar: Simula a ação de desligar o carro.
                            print(f"O carro {self.modelo} {self.cor} de {self.ano} desligou!")#Utiliza f-strings para formatar a mensagem com os valores dos atributo
                    
                    # Criando objetos
                     carro1 = Carro("vermelho", "Onix", 2020)
                     carro2 = Carro("azul", "Fiat Argo", 2021)
                     
                     # Acessando metodos
                     carro1.ligar()
                     carro1.desligar()
                      # Acessando metodos
                     carro2.ligar()
                     carro2.desligar()
                 print("Atributos de classe: São compartilhados por todos os objetos da classe.")
                 continuar_atibutos_classe = input("Deseja printar o código abaixo sobre Atributos de classe ? (s/n) ")
                 if continuar_atibutos_classe.lower() == "s":
                    class Pessoa:# Esta linha declara o início da definição da classe "Pessoa". O nome da classe é "Pessoa", e ela serve como um molde para a criação de objetos que representam indivíduos.
                        especie = "humana"#Esta linha define um atributo de classe chamado especie com o valor "humana". Esse atributo é compartilhado por todos os objetos criados a partir da classe "Pessoa". Ele representa a espécie a qual todas as pessoas pertencem nesse caso.

                        def __init__(self, nome):#Esta linha define o método construtor da classe, responsável por inicializar os atributos de um objeto quando ele é criado. O método construtor recebe um parâmetro chamado nome
                            self.nome = nome#Dentro do método construtor, a instrução self.nome = nome atribui o valor do parâmetro nome ao atributo nome do objeto. Isso significa que cada objeto "Pessoa" terá um atributo nome com o valor específico fornecido na sua criação.

                    # Criando objetos
                    pessoa1 = Pessoa("João")#cria um novo objeto "Pessoa" chamado pessoa1 e inicializa seu atributo nome com o valor "João".
                    pessoa2 = Pessoa("Maria")#cria um novo objeto "Pessoa" chamado pessoa2 e inicializa seu atributo nome com o valor "Maria".

                    # Acessando atributos
                    print(f"Nome da pessoa 1: {pessoa1.nome}")
                    print(f"Nome da pessoa 2: {pessoa2.nome}")
                    print(f"Espécie da pessoa 1: {pessoa1.especie}")
                    print(f"Espécie da pessoa 2: {pessoa2.especie}")

                    pessoa1.nome = "José"
                    #Podemos modificar os valores dos atributos após a criação do objeto.
                    print(f"Novo nome da pessoa 1: {pessoa1.nome}")
            elif operacao_teoria =="04":
                print("##################################Métodos##################################")
                print("os métodos definem as ações que um objeto pode realizar. Encapsulam funcionalidades e comportamentos específicos, tornando o código mais organizado e reutilizável.")
                print("Assim como um animal possui comportamentos como latir, correr e comer, um objeto em POO possui métodos que definem suas ações.")
                print("Definindo métodos:")
                print("Métodos são declarados dentro da classe.")
                print("Possuem um nome e uma lista de parâmetros entre parênteses.")
                print("O corpo do método é definido por um bloco de código indentado.")
                continuar_metodo_pessoa = input("Deseja printar o código abaixo sobre método ? (s/n)")
                if continuar_metodo_pessoa.lower() == "s":
                    class Pessoa:
                        def __init__(self, nome):
                            self.nome = nome

                        def falar(self):
                            print(f"Olá, meu nome é {self.nome}")

                    # Criando objeto
                    pessoa1 = Pessoa("João")

                    # Chamando método
                    pessoa1.falar()

                    # O método falar() não recebe parâmetros.
                    # O corpo do método imprime uma mensagem com o nome do objeto.
                continuar_metodo_animal = input("Deseja printar o código abaixo sobre interação com o método ? (s/n) ")
                if continuar_metodo_pessoa.lower() == "s":    
                    #Os métodos podem receber parâmetros para personalizar seu comportamento.    
                    class Animal:
                        def falar(self, som):
                            print(f"O animal faz {som}")

                    # Criando objeto
                    cachorro1 = Animal()

                    # Chamando método com parâmetro
                    som = input("Digite o som do animal: ")
                    cachorro1.falar(som) 
                print("##################################Getters##################################")
                print("São métodos que acessam os valores dos atributos privados da classe.")
                print("Seguem a convenção de usar o prefixo get_ seguido pelo nome do atributo.")
                print("Não recebem argumentos.")
                print("Retornam o valor do atributo correspondente.")
                continuar_metodo_animal = input("Deseja printar o código abaixo sobre interação com o método ? (s/n) ")
                if continuar_metodo_pessoa.lower() == "s":
                    class Pessoa:
                        def __init__(self, nome, idade, sexo):
                            self.nome = nome
                            self.idade = idade
                            self.sexo = sexo

                        def falar(self):
                            print(f"Olá, meu nome é {self.nome}")

                        # Getters
                        def get_nome(self):
                            return self.nome

                        def get_idade(self):
                            return self.idade

                        def get_sexo(self):
                            return self.sexo

                        # Setters
                        def set_nome(self, novo_nome):
                            self.nome = novo_nome

                        def set_idade(self, nova_idade):
                            self.idade = nova_idade

                        def set_sexo(self, novo_sexo):
                            self.sexo = novo_sexo

                    # Exemplo de uso
                    pessoa1 = Pessoa("João", 25, "M")

                    print(f"Nome original: {pessoa1.get_nome()}")  # Nome original: João

                    pessoa1.set_nome("Maria")

                    print(f"Nome após alteração: {pessoa1.get_nome()}")  # Nome após alteração: Maria    
                print("##################################Getters##################################")
                print("São métodos que modificam os valores dos atributos privados da classe.")
                print("Seguem a convenção de usar o prefixo set_ seguido pelo nome do atributo.")
                print("Recebem um argumento que representa o novo valor do atributo.")
                print("Não retornam nenhum valor.")
                print("Atualizam o valor do atributo correspondente com o valor recebido.")
                continuar_metodo_animal = input("Deseja printar o código abaixo sobre interação com o método ? (s/n) ")
                if continuar_metodo_pessoa.lower() == "s":
                    class Pessoa:
                        def __init__(self, nome, idade, sexo):
                            self.nome = nome
                            self.idade = idade
                            self.sexo = sexo

                        def falar(self):
                            print(f"Olá, meu nome é {self.nome}")

                        # Getters
                        def get_nome(self):
                            return self.nome

                        def get_idade(self):
                            return self.idade

                        def get_sexo(self):
                            return self.sexo

                        # Setters
                        def set_nome(self, novo_nome):
                            self.nome = novo_nome

                        def set_idade(self, nova_idade):
                            self.idade = nova_idade

                        def set_sexo(self, novo_sexo):
                            self.sexo = novo_sexo

                    # Exemplo de uso
                    pessoa1 = Pessoa("João", 25, "M")

                    print(f"Nome original: {pessoa1.get_nome()}")  # Nome original: João

                    pessoa1.set_nome("Maria")

                    print(f"Nome após alteração: {pessoa1.get_nome()}")
                
            elif operacao_teoria=="05":
                print("##################################Herança##################################")
                print("A herança é o que permite que uma classe (classe derivada) herde atributos e métodos de outra classe (classe base). Isso promove o reuso de código, organização e modularidade em seus projetos.\n")
                print(" Reuso de código: Evita a duplicação de código ao permitir que classes derivadas aproveitem funcionalidades já implementadas em classes base. Isso torna o código mais enxuto, eficiente e fácil de manter.\n")
               
                print("Organização: Promove uma estrutura hierárquica clara no código, organizando classes em uma relação de pai-filho. Essa organização facilita a compreensão e a manutenção do código, especialmente em projetos complexos.")
                print("Modularidade: Permite dividir o código em módulos menores e coesos, cada um com suas responsabilidades bem definidas. Essa modularidade facilita o desenvolvimento, teste e reuso de componentes de software.")
                print("Especialização: Permite que classes derivadas especializem o comportamento herdado da classe base, adicionando novas funcionalidades ou modificando as existentes. Isso torna o código mais flexível e adaptável às necessidades específicas de cada classe.")
                                
                # A palavra-chave super() é utilizada em dois contextos distintos, mas relacionados:

                # Chamada de métodos de classes bases:

                # O principal objetivo do super() é permitir a chamada de métodos da classe base a partir de uma classe derivada. 
                # Isso é crucial na herança, onde classes derivadas herdam atributos e métodos de suas classes bases. 
                # Ao utilizar o super(), podemos acessar e executar métodos da classe base dentro da classe derivada, mesmo que esses métodos tenham sido sobrescritos na classe derivada.
                 #Redefinição de métodos:
                 #Ao redefinir um método da classe base na classe derivada, você pode utilizar o super() para chamar a implementação original do método antes de executar seu próprio código personalizado. Isso garante que a funcionalidade básica da classe base seja preservada enquanto você adiciona novas funcionalidades na classe derivada.
                 #Chamada de métodos da classe base: Em alguns casos, pode ser necessário chamar diretamente métodos da classe base a partir da classe derivada. O super() facilita essa chamada, permitindo que você acesse os métodos da classe base como se estivessem na própria classe derivada.
                class Animal:
                    def __init__(self, nome):
                        self.nome = nome

                    def comer(self):
                        print(f"{self.nome} está comendo...")

                class Cachorro(Animal):
                    def __init__(self, nome, raca):
                        super().__init__(nome)  # Chamada ao construtor da classe base
                        self.raca = raca

                    def comer(self):
                        super().comer()  # Chamando o método comer da classe base
                        print(f"... e latindo enquanto come!")

                golden_retriever = Cachorro("Rex", "Golden Retriever")
                golden_retriever.comer()  # Imprime: "Rex está comendo... e latindo enquanto come!"



                #Acessando atributos de classes bases:

                # O super() também pode ser utilizado para acessar atributos da classe base a partir da classe derivada. 
                # No entanto, essa prática é desincentivada na maioria dos casos, pois pode levar a código mais complexo e menos legível. 
                # Em geral, é recomendável acessar atributos diretamente através da instância da classe ou utilizando métodos específicos da classe base.



               

                # O uso do super() para acessar atributos da classe base deve ser feito com cautela, pois pode tornar o código mais complexo e menos legível.
                # É preferível utilizar métodos específicos da classe base para acessar seus atributos, se disponíveis.
                # Em casos específicos, o acesso direto via super() pode ser necessário, mas deve ser bem documentado para evitar confusões.
                class Animal:
                    """Classe base para representar animais."""

                    def __init__(self, nome, especie):
                        self.nome = nome
                        self.especie = especie

                    def comer(self):
                        print(f"{self.nome} está comendo...")

                class Cachorro(Animal):
                    """Classe derivada de Animal para representar cachorros."""

                    def __init__(self, nome, especie, raca):
                        super().__init__(nome, especie)  # Chamada ao construtor da classe base
                        self.raca = raca

                    def latir(self):
                        print(f"{self.nome} (da raça {self.raca}) está latindo!")

                # Criando objetos
                golden_retriever = Cachorro("Rex", "Cachorro", "Golden Retriever")

                # Acessando atributos e métodos herdados
                print(golden_retriever.nome)  # Acessando atributo herdado de Animal
                golden_retriever.comer()  # Chamando método herdado de Animal
                golden_retriever.latir()  # Chamando método específico de Cachorro

                class Animal:
                    def __init__(self, nome, especie):
                        self.nome = nome
                        self.especie = especie

                    def comer(self):
                        print(f"{self.nome} da espécie {self.especie} está comendo.")

                    def emitir_som(self):
                        raise NotImplementedError  # Método abstrato para ser implementado nas classes derivadas
                class Peixe:
                    def __init__(self, tipo, habitat):
                        self.tipo = tipo
                        self.habitat = habitat

                    def comer(self):
                        print(f"O peixe {self.tipo} do habitat {self.habitat} está comendo.")

                    def nadar(self):
                        print(f"O peixe {self.tipo} do habitat {self.habitat} está nadando.")
            elif operacao_teoria=="06":
                print("##################################Polimorfismo##################################")
                print("permiti que objetos de diferentes classes respondam à mesma mensagem de maneiras distintas. Essa flexibilidade é crucial para construir programas mais robustos, adaptáveis e reutilizáveis.")
                class FormaGeometrica:
                    def calcular_area(self):#Este método é abstrato (utiliza NotImplementedError), o que significa que ele não possui uma implementação concreta na classe base. As classes derivadas (Quadrado, Triangulo, Circulo) serão responsáveis por implementar este método de acordo com a fórmula específica para calcular a área de cada forma geométrica.
                        raise NotImplementedError 
                    
                class Quadrado(FormaGeometrica):
                     def __init__(self, lado):#__init__: Este construtor inicializa o quadrado com um lado. calcular_area: Esta implementação específica calcula a área de um quadrado, utilizando a fórmula lado * lado.
                        self.lado = lado

                     def calcular_area(self):
                        return self.lado * self.lado
                
                class Triangulo(FormaGeometrica):
                    def __init__(self, base, altura):#__init__: Este construtor inicializa o triângulo com base e altura. calcular_area: Esta implementação específica calcula a área de um triângulo, utilizando a fórmula (base * altura) / 2.
                        self.base = base
                        self.altura = altura

                    def calcular_area(self):
                        return (self.base * self.altura) / 2
                
                class Circulo(FormaGeometrica):#__init__: Este construtor inicializa o círculo com um raio. calcular_area: Esta implementação específica calcula a área de um círculo, utilizando a fórmula 3.1415 * raio * raio.
                    def __init__(self, raio):
                        self.raio = raio

                    def calcular_area(self):
                        return 3.1415 * self.raio * self.raio
                
                quadrado1 = Quadrado(5)
                triangulo1 = Triangulo(6, 4)
                circulo1 = Circulo(3)

                print(f"Área do quadrado: {quadrado1.calcular_area()}")  
                print(f"Área do triângulo: {triangulo1.calcular_area()}")  
                print(f"Área do círculo: {circulo1.calcular_area()}")                                                                        
                #Polimorfismo em Ação: Ao chamar o método calcular_area() em cada objeto, o despacho dinâmico do Python seleciona e executa a implementação específica da classe derivada correspondente ao tipo do objeto:                
                #Herança: As classes derivadas (Quadrado, Triangulo, Circulo) herdam da classe base (FormaGeometrica), reutilizando a estrutura e implementando

                class Animal:
                    def comunicar(self):
                        raise NotImplementedError  # Método abstrato

                class Cachorro(Animal):
                    def comunicar(self):
                        print("Au au!")

                class Gato(Animal):
                    def comunicar(self):
                        print("Miau!")

                class Passaro(Animal):
                    def comunicar(self):
                        print("Canto do pássaro!")

                cachorro1 = Cachorro()
                gato1 = Gato()
                passaro1 = Passaro()

                cachorro1.comunicar()  # Au au!
                gato1.comunicar()  # Miau!
                passaro1.comunicar()  # Canto do pássaro!
            elif operacao_teoria=="07": 
                print("##################################Encapsulamento##################################")
                print("fornecendo mecanismos para proteger os dados internos de classes e objetos, controlando o acesso a eles de forma organizada e segura. Imagine uma caixa forte em um banco: os dados valiosos (atributos) estão guardados dentro dela (dentro da classe), e apenas mecanismos específicos (métodos) permitem o acesso autorizado (acesso controlado).")
                print("Esconder a Implementação\n")
                print("Os detalhes internos de como os dados são armazenados e manipulados são escondidos do mundo externo. Isso promove simplicidade, permitindo que os usuários da classe interajam com ela através de uma interface bem definida, sem precisar se preocupar com a implementação interna.")
                print("Expor Comportamento\n")
                print("A classe expõe um conjunto de métodos públicos que permitem aos usuários acessar e manipular seus dados de forma controlada. Esses métodos servem como uma interface bem definida, garantindo que os dados sejam acessados e modificados de acordo com as regras da classe.")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower() == "s":
                    class ContaCorrente:
                        def __init__(self, saldo):
                            self.__saldo = saldo  # Atributo privado com modificador `__` O modificador duplo __ torna o atributo privado dentro da classe ContaCorrente.
                            #Esconder a Implementação: O código externo não pode acessar diretamente o atributo __saldo. Isso protege o saldo da conta contra modificações acidentais ou mal-intencionadas.
                            #O acesso ao saldo só é possível através dos métodos públicos get_saldo() e sacar(), que controlam as regras de negócio para consulta e modificação do saldo.
                        def get_saldo(self):
                            return self.__saldo  # Método público para consultar o saldo

                        def depositar(self, valor):
                            if valor > 0:
                                self.__saldo += valor
                            else:
                                print("Valor inválido para depósito!")

                        def sacar(self, valor):
                            if valor > 0 and valor <= self.__saldo:
                                self.__saldo -= valor
                            else:
                                print("Saldo insuficiente ou valor inválido para saque!")
                        def transferir(self, valor, conta_destino):
                            if valor > 0 and valor <= self.__saldo:
                                self.__saldo -= valor
                                conta_destino.__saldo += valor
                            else:
                                print("Valor inválido ou saldo insuficiente para transferência!")
                        def extrato(self):
                            print("---------- Extrato da Conta ----------")
                            print(f"Saldo Atual: R$ {self.__saldo:.2f}")
                    conta1 = ContaCorrente(1000)
                    conta2 = ContaCorrente(500)

                    conta1.depositar(200)
                    conta1.extrato()  

                    conta1.transferir(500, conta2)
                    conta1.extrato() 
                    conta2.extrato()  


                                # A classe ContaCorrente esconde a implementação interna dos atributos e métodos, expondo apenas uma interface pública através dos métodos.
                                # O usuário da classe não precisa se preocupar com os detalhes de como o saldo é armazenado ou manipulado, apenas interage com a conta através dos métodos públicos.
                                # O objetivo do encapsulamento é esconder a implementação, não a acessibilidade. O código externo ainda pode acessar atributos privados utilizando técnicas avançadas, mas essa prática não é recomendada.
                                # Equilíbrio: O encapsulamento deve ser utilizado de forma equilibrada. Classes muito fechadas podem dificultar a reutilização e a extensibilidade do código.
                
                    #Expor Comportamento:
                    # A classe ContaCorrente não expõe a implementação interna de como o saldo é armazenado ou manipulado.
                    # O usuário da classe interage com a conta através dos métodos públicos, que representam o comportamento da classe em relação ao saldo.
                    # Por exemplo, o método depositar() recebe um valor como parâmetro e atualiza o saldo internamente, mas o código externo não precisa saber como essa atualização é feita.       
            elif operacao_teoria =="08":
                print("##################################Abstração##################################")
                print("A abstração é  que permite ocultar os detalhes de implementação de um objeto, expondo apenas as funcionalidades essenciais para o usuário. Isso torna o código mais modular, reutilizável e fácil de entender.")
                print("pode ser implementada usando classes abstratas e métodos abstratos. Uma classe abstrata é uma classe que define um conjunto de métodos abstratos, os quais devem ser implementados por suas classes derivadas (filhas).")
                print("A classe Animal não implementa o método fazer_som(), pois é um método abstrato. Isso significa que qualquer classe que herda de Animal deve implementar esse método para fornecer sua própria definição de como o animal faz som.")
                print("O módulo abc é necessário para usar classes abstratas e métodos abstratos em Python.")
                print("Um método abstrato não pode ser implementado na classe abstrata em si. Ele deve ser implementado nas classes derivadas.")
                print("Classes abstratas são úteis para definir interfaces comuns para classes relacionadas, promovendo a reutilização de código e facilitando a extensibilidade do programa.")
                print("Este exemplo simples demonstra como a abstração pode ser utilizada em Python para criar classes mais flexíveis e reutilizáveis.")



                # Importação do módulo abc:

                # A linha from abc import ABC, abstractmethod importa as classes ABC e abstractmethod do módulo abc.
                # A classe ABC é usada para definir classes abstratas.
                # O decorador abstractmethod é usado para marcar métodos abstratos.
                # Classe abstrata Animal:
                from abc import ABC, abstractmethod


                class Animal(ABC): # A classe Animal é definida usando a palavra-chave class seguida do nome da classe (Animal).
                    """Classe abstrata para representar um animal."""

                    @abstractmethod
                    def fazer_som(self):
                        """Método abstrato para definir o som do animal."""
                        pass


                class Cachorro(Animal):
                    """Classe derivada para representar um cachorro."""

                    def fazer_som(self):
                        """Implementação do método fazer_som para Cachorro."""
                        return "Au Au!"


                class Gato(Animal):
                    """Classe derivada para representar um gato."""

                    def fazer_som(self):
                        """Implementação do método fazer_som para Gato."""
                        return "Miau!"


                # Instanciando objetos e utilizando o método fazer_som
                cachorro = Cachorro()
                gato = Gato()

                print(cachorro.fazer_som())  # Imprime "Au Au!"
                print(gato.fazer_som())  # Imprime "Miau!"

                

               
                # A classe herda da classe ABC usando a sintaxe (ABC).
                # O método fazer_som() é definido como um método abstrato usando o decorador @abstractmethod.
                # Um método abstrato não possui implementação na classe abstrata e deve ser implementado nas classes derivadas.
                # Classes derivadas Cachorro e Gato:

                # As classes Cachorro e Gato são definidas da mesma forma que a classe Animal, mas herdam da classe Animal.
                # Cada classe implementa o método abstrato fazer_som() de acordo com suas características.
                # A classe Cachorro retorna "Au Au!".
                # A classe Gato retorna "Miau!".
                # Instanciando objetos e usando o método fazer_som():

                # As linhas cachorro = Cachorro() e gato = Gato() criam objetos das classes Cachorro e Gato, respectivamente.
                # As linhas print(cachorro.fazer_som()) e print(gato.fazer_som()) chamam o método fazer_som() em cada objeto e imprimem o resultado.
                # Observações:

                # Este código demonstra um exemplo simples de abstração em Python.
                # Na prática, as classes abstratas podem ser usadas para definir interfaces mais complexas e hierarquias de classes mais elaboradas.
                # A abstração é um conceito fundamental na POO para criar código mais modular, reutilizável e fácil de manter.
            elif operacao_teoria =="09":
                print("##################################Modificadores de Acesso##################################")
                print("Os modificadores de acesso permitem controlar a visibilidade de atributos e métodos dentro de uma classe, definindo quem pode acessá-los e modificá-los.")
                print("Modificadores:")
                print("Public: Atributos e métodos públicos podem ser acessados e modificados por qualquer código dentro do programa.")       
                print("Private: Atributos e métodos privados só podem ser acessados e modificados por métodos da mesma classe.")
                print("Protected: Atributos e métodos protected só podem ser acessados e modificados por métodos da mesma classe e de classes herdeiras.\n")
                print("Compreendendo os Modificadores\n")
                
                print("Public (Público)\n")

                print("Visibilidade Aberta: Atributos e métodos públicos podem ser acessados e modificados por qualquer parte do programa, sem restrições.")
                print("Utilização: Ideal para elementos que representam o comportamento principal da classe e que precisam ser utilizados por outras partes do código.")
                print("Exemplo: nome_publico, get_nome_publico(), get_preco_publico().\n")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower() == "s":
                    class Produto:
                        def __init__(self, nome, preco, quantidade):
                            self.nome_publico = nome
                            self.preco_publico = preco
                            self.quantidade_publica = quantidade

                        def get_nome_publico(self):
                            return self.nome_publico

                        def get_preco_publico(self):
                            return self.preco_publico

                        def get_quantidade_publica(self):
                            return self.quantidade_publica

                    def principal():
                    # Criação do produto com nome "Camisa", preço R$50 e quantidade 10
                     produto = Produto("Camisa", 50, 10)

                    # Consultando o nome do produto
                     print(f"Nome do produto: {produto.get_nome_publico()}")

                    # Consultando o preço do produto
                     print(f"Preço do produto: R${produto.get_preco_publico()}")

                     # Consultando a quantidade em estoque
                     print(f"Quantidade em estoque: {produto.get_quantidade_publica()}")

                     # Modificando o nome do produto diretamente (acesso público)
                     produto.nome_publico = "Camiseta"
                     print(f"Nome do produto após modificação: {produto.get_nome_publico()}")

                    # Modificando o preço do produto diretamente (acesso público)
                     produto.preco_publico = 45
                     print(f"Preço do produto após modificação: R${produto.get_preco_publico()}")

                    # Modificando a quantidade em estoque diretamente (acesso público)
                     produto.quantidade_publica = 15
                     print(f"Quantidade em estoque após modificação: {produto.get_quantidade_publica()}")

                    if __name__ == "__main__":
                        principal()
                    #   Garante que a função principal() seja executada apenas quando o script for executado diretamente, e não quando for importado como módulo.

                print("Private (Privado)\n")

                print("Visibilidade Restrita: Atributos e métodos privados só podem ser acessados e modificados por métodos dentro da mesma classe em que foram declarados.")
                print("Utilização: Recomendado para elementos que contêm detalhes de implementação interna que não precisam ser expostos ao código externo.")
                print("Exemplo: __saldo_privado, __atualizar_saldo_privado(), __validar_deposito_privado().\n")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower() == "s":
                    class Produto:
                        def __init__(self, nome, preco, quantidade):
                            self._nome_protegido = nome  # Atributo protegido com nome '_nome_protegido'
                            self._preco_protegido = preco  # Atributo protegido com nome '_preco_protegido'
                            self._quantidade_protegida = quantidade  # Atributo protegido com nome '_quantidade_protegida'

                        def get_nome_publico(self):
                            return self._nome_protegido

                        def get_preco_publico(self):
                            return self._preco_protegido

                        def get_quantidade_publica(self):
                            return self._quantidade_protegida

                        # Métodos para modificar os atributos (acesso protegido):
                        def _set_nome_protegido(self, novo_nome):
                            if isinstance(novo_nome, str):
                                self._nome_protegido = novo_nome
                            else:
                                raise TypeError("O nome do produto deve ser uma string.")

                        def _set_preco_protegido(self, novo_preco):
                            if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
                                self._preco_protegido = novo_preco
                            else:
                                raise TypeError("O preço do produto deve ser um número positivo ou zero.")

                        def _set_quantidade_protegida(self, nova_quantidade):
                            if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
                                self._quantidade_protegida = nova_quantidade
                            else:
                                raise TypeError("A quantidade em estoque deve ser um número inteiro não negativo.")
                        def principal():
                            # Criação do produto com nome "Camisa", preço R$50 e quantidade 10
                            produto = Produto("Camisa", 50, 10)

                            # Consultando o nome do produto
                            print(f"Nome do produto: {produto.get_nome_publico()}")

                            # Consultando o preço do produto
                            print(f"Preço do produto: R${produto.get_preco_publico()}")

                            # Consultando a quantidade em estoque
                            print(f"Quantidade em estoque: {produto.get_quantidade_publica()}")

                            # Modificando o nome do produto diretamente (acesso público)
                            produto.nome_publico = "Camiseta"
                            print(f"Nome do produto após modificação: {produto.get_nome_publico()}")

                            # Modificando o preço do produto diretamente (acesso público)
                            produto.preco_publico = 45
                            print(f"Preço do produto após modificação: R${produto.get_preco_publico()}")

                            # Modificando a quantidade em estoque diretamente (acesso público)
                            produto.quantidade_publica = 15
                            print(f"Quantidade em estoque após modificação: {produto.get_quantidade_publica()}") 

                    if __name__ == "__main__":
                        principal()
                   
                
                print("Protected (Protegido)\n")

                print("Visibilidade Intermediária: Atributos e métodos protected podem ser acessados e modificados por métodos da mesma classe em que foram declarados e por métodos de classes derivadas.")
                print("Utilização: Útil para elementos que servem como base para funcionalidades mais específicas em classes derivadas.")
                continuar = input("Deseja printar o código abaixo? (s/n) ")
                if continuar.lower()=="s":
                    class Produto:
                        def __init__(self, nome, preco, quantidade):
                            self._nome_protegido = nome  # Atributo com acesso protegido (prefixo sublinhado simples)
                            self._preco_protegido = preco
                            self._quantidade_protegida = quantidade

                        def get_nome_publico(self):
                            return self._nome_protegido

                        def get_preco_publico(self):
                            return self._preco_protegido

                        def get_quantidade_publica(self):
                            return self._quantidade_protegida

                        # Métodos protegidos para modificar atributos (acessíveis dentro da classe e subclasses)
                        def _set_nome_protegido(self, novo_nome):
                            if isinstance(novo_nome, str):
                                self._nome_protegido = novo_nome
                            else:
                                raise TypeError("O nome do produto deve ser uma string.")

                        def _set_preco_protegido(self, novo_preco):
                            if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
                                self._preco_protegido = novo_preco
                            else:
                             raise TypeError("O preço do produto deve ser um número positivo ou zero.")

                        def _set_quantidade_protegida(self, nova_quantidade):
                            if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
                                self._quantidade_protegida = nova_quantidade
                            else:
                             raise TypeError("A quantidade em estoque deve ser um número inteiro não negativo.")

                        def principal():
                            # Criação do produto com nome "Camisa", preço R$50 e quantidade 10
                            produto = Produto("Camisa", 50, 10)

                            # Consultando o nome do produto
                            print(f"Nome do produto: {produto.get_nome_publico()}")

                            # Consultando o preço do produto
                            print(f"Preço do produto: R${produto.get_preco_publico()}")

                            # Consultando a quantidade em estoque
                            print(f"Quantidade em estoque: {produto.get_quantidade_publica()}")

                            # Modificando o nome do produto diretamente (acesso público)
                            produto.nome_publico = "Camiseta"
                            print(f"Nome do produto após modificação: {produto.get_nome_publico()}")

                            # Modificando o preço do produto diretamente (acesso público)
                            produto.preco_publico = 45
                            print(f"Preço do produto após modificação: R${produto.get_preco_publico()}")

                            # Modificando a quantidade em estoque diretamente (acesso público)
                            produto.quantidade_publica = 15
                            print(f"Quantidade em estoque após modificação: {produto.get_quantidade_publica()}")

                        if __name__ == "__main__":
                         principal()  
            elif operacao_teoria=="10":
                print("Sair")
                break
            elif operacao_teoria=="00":
                print("##################################Programação Orientada a Objetos ##################################")
                print("A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de 'objetos'. Estes objetos são entidades que encapsulam dados e comportamentos, combinando informações e funcionalidades em unidades modulares e reutilizáveis.Em outras palavras, a POO trata o código como se fosse um conjunto de objetos que interagem entre si. Cada objeto possui características próprias, como seus dados (atributos) e as ações que pode realizar (métodos).A principal vantagem da POO é a organização e o reuso de código que ela proporciona. Ao agrupar dados e comportamentos em objetos, o código se torna mais legível, modular e fácil de manter. Além disso, a POO facilita a criação de aplicações complexas, pois permite que os objetos sejam facilmente reutilizados em diferentes contextos.")
                print("Em vez de focar em procedimentos e funções, a POO organiza o código em torno de objetos, entidades que encapsulam dados e comportamentos, como se fossem miniprogramas com vida própria.\n")

                print("Conceitos Essenciais\n")
                print("Objetos: São as unidades básicas da POO, representando entidades do mundo real ou virtual. Cada objeto possui:")
                print("Atributos: Armazenam as características do objeto, como nome, cor, tamanho, etc.")
                print("Métodos: Definem as ações que o objeto pode realizar, como calcular, imprimir, interagir com outros objetos, etc.")
                print("Classes: São modelos que definem a estrutura dos objetos, como um molde que cria objetos com características semelhantes. As classes definem os atributos e métodos que todos os objetos da classe herdam.")
                print("Encapsulamento: Esconde os detalhes internos de um objeto, expondo apenas os métodos que permitem interagir com ele. Isso promove segurança e modularidade.")
                print("Abstração: Foca nas características essenciais de um objeto, ignorando detalhes irrelevantes. Permite criar interfaces simples e reutilizáveis.")
                print("Herança: Permite que classes herdem atributos e métodos de outras classes, promovendo reuso de código e organização hierárquica.")
                print("Polimorfismo: Permite que objetos de diferentes classes respondam à mesma mensagem de maneiras distintas, proporcionando flexibilidade e adaptabilidade.\n")
            else:
                print("Operação Invalida")
            




                

	                    



    