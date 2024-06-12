import tkinter as tk
from tkinter import messagebox
arquivo_aberto = False

class InterfaceGrafica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Introdução Tkinter")

        # Rótulo e botão para fechar a janela
        self.rotulo_titulo = tk.Label(self.root, text="O Inicio", width=40)
        self.rotulo_titulo.pack()

        # Botão para abrir nova janela
        self.botao1 = tk.Button(self.root, text="1. A Criação da Janela Principal", command=lambda: self.abrir_topico("Criação da Janela Principal"))
        self.botao1.pack(pady=5)
        self.botao2 = tk.Button(self.root, text="2. Widgets: Blocos de Construção", command=lambda: self.abrir_topico("Widgets: Blocos de Construção"))
        self.botao2.pack(pady=5)
        self.botao3 = tk.Button(self.root, text="3. Grid: Gerenciandores de layout",state=tk.DISABLED ,command=lambda: self.abrir_topico("Grid: Gerenciandores de layout"))
        self.botao3.pack()
       
        # self.botao11 = tk.Button(self.root, text="1 - A Criação da Janela Principal", command=self.Criacao_de_Janela_Principal)  # Chamada da função (se necessário)
        # self.botao11.pack()
        # self.botao22 = tk.Button(self.root, text="2 -  Widgets: Blocos de Construção", command=self.Widgets_Blocos_de_Construção)  # Chamada da função (se necessário)
        # self.botao22.pack()
        
    def abrir_topico(self, topico):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title(topico)

        # Conteúdo específico de cada tópico deve ser implementado aqui
        # Exemplo de conteúdo para o tópico "1. A Criação da Janela Principal"
        if topico =="Criação da Janela Principal":
            conteudo_label_titulo = tk.Label(nova_janela, text=" A Criação da Janela Principal", font=("Arial", 12, "bold"))
            conteudo_label_titulo.pack(pady=5)
            
            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Importando a Biblioteca",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="O primeiro passo é importar a biblioteca Tkinter. A biblioteca Tkinter fornece as ferramentas básicas para a construção da interface gráfica.\nimport tkinter as tk")
            conteudo_label_texto.pack(pady=5)
            #import tkinter as tk

            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Criando a Instância da Janela Principal",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="Após importar a biblioteca, é hora de criar a instância da janela principal. Utilize a classe Tk() do Tkinter para essa finalidade.\njanela = tk.Tk()")
            conteudo_label_texto.pack()
            conteudo_label_obs = tk.Label(nova_janela, text="Lembrando que essa instancia pode ser feita para qualquer nomenclatura. não se apegando somente o exemplo acima.\nchinforinfola = tk.Tk()")
            conteudo_label_obs.pack(pady=5)
            #janela = tk.Tk()
            #chinforinfola = tk.Tk()

            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Configurar a Janela",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="Você pode configurar diversos aspectos da janela principal, como título, tamanho, posição e layout.")
            conteudo_label_texto.pack(pady=5) 

            conteudo_label_titulo_exemplo = tk.Label(nova_janela, text="Título: Utilize o método title() para definir o título da janela.")
            conteudo_label_titulo_exemplo.pack()
            conteudo_label_exemplo = tk.Label(nova_janela, text="janela.title('Minha Aplicação').")
            conteudo_label_exemplo.pack(pady=5)
            #janela.title("Minha Aplicação")


            conteudo_label_titulo_exemplo = tk.Label(nova_janela, text="Tamanho: Utilize os métodos geometry() ou config() para definir o tamanho da janela.")
            conteudo_label_titulo_exemplo.pack()
            conteudo_label_exemplo = tk.Label(nova_janela, text="janela.geometry('300x200') # Largura x Altura\n janela.config(width=300, height=200) # Largura e Altura")
            conteudo_label_exemplo.pack(pady=5)
            #janela.geometry("300x200") # Largura x Altura
            #janela.config(width=300, height=200) # Largura e Altura                

            conteudo_label_titulo_exemplo = tk.Label(nova_janela, text="Posição: Utilize o método geometry() ou config() para definir a posição da janela na tela.")
            conteudo_label_titulo_exemplo.pack()
            conteudo_label_exemplo = tk.Label(nova_janela, text="janela.geometry('+100+50')\n janela.config(x=100, y=50) # Largura e Altura")
            conteudo_label_exemplo.pack(pady=5)
            # janela.geometry("+100+50") # Posição X e Y
            # janela.config(x=100, y=50) # Posição X e Y


            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Adicionar Widgets",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="Widgets são os elementos que compõem a interface gráfica, como botões, rótulos, caixas de texto, etc. Você pode adicionar widgets à janela principal utilizando seus métodos específicos.")
            conteudo_label_texto.pack(pady=5)

            conteudo_label_titulo_exemplo = tk.Label(nova_janela, text="Criando um rótulo.")
            conteudo_label_titulo_exemplo.pack()
            conteudo_label_exemplo = tk.Label(nova_janela, text="rotulo = tk.Label(janela, text='Olá, Mundo!')\nrotulo.pack()")
            conteudo_label_exemplo.pack(pady=5)
            # rotulo = tk.Label(janela, text="Olá, Mundo!")
            # rotulo.pack()

            conteudo_label_titulo_exemplo = tk.Label(nova_janela, text="Criando um botão.")
            conteudo_label_titulo_exemplo.pack()
            conteudo_label_exemplo = tk.Label(nova_janela, text="botao = tk.Button(janela, text='Clique aqui')\nbotao.pack().pack()")
            conteudo_label_exemplo.pack(pady=5)
            # botao = tk.Button(janela, text="Clique aqui")
            # botao.pack()

            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Executar a Interface",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="Para que a interface gráfica seja exibida e fique responsiva às interações do usuário, utilize o método mainloop() da instância da janela principal.\njanela.mainloop()")
            conteudo_label_texto.pack(pady=5) 
            #janela.mainloop()  
             
            conteudo_label_sub_titulo = tk.Label(nova_janela, text="Exemplo",font=("Arial", 10, "bold"))
            conteudo_label_sub_titulo.pack()
            conteudo_label_texto = tk.Label(nova_janela, text="import tkinter as tk\n\njanela = tk.Tk()\njanela.title('Minha Aplicação')\njanela.geometry('300x200')\n\nrotulo = tk.Label(janela, text='Olá, Mundo!')\nrotulo.pack()\n\nbotao = tk.Button(janela, text='Clique aqui')\nbotao.pack()\n\njanela.mainloop()")
            conteudo_label_texto.pack() 
          
            # import tkinter as tk

            # janela = tk.Tk()
            # janela.title("Minha Aplicação")
            # janela.geometry("300x200")

            # rotulo = tk.Label(janela, text="Olá, Mundo!")
            # rotulo.pack()

            # botao = tk.Button(janela, text="Clique aqui")
            # botao.pack()

            # janela.mainloop()


            def executar_codigo():
                janela = tk.Tk()
                janela.title("Minha Aplicação")
                janela.geometry("300x200")

                rotulo = tk.Label(janela, text="Olá, Mundo!")
                rotulo.pack()

                botao = tk.Button(janela, text="Clique aqui")
                botao.pack()

            self.botao1 = tk.Button(nova_janela, text="Exemplo", command=executar_codigo)
            self.botao1.pack()
        if topico=="Widgets: Blocos de Construção":


            conteudo_label = tk.Label(nova_janela, text="Widgets: Blocos de Construção",font=("Arial", 12, "bold"))
            conteudo_label.pack(pady=5)

            conteudo_label_sub_titulo = tk.Label(nova_janela, text="widgets são os blocos de construção básicos. Cada widget tem sua própria aparência e funcionalidade, e eles podem ser combinados para criar interfaces")
            conteudo_label_sub_titulo.pack()
            conteudo_label = tk.Label(nova_janela, text="widgets mais comuns do Tkinter",font=("Arial", 10, "bold"))
            conteudo_label.pack(pady=5)
            def Label_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Label')
                conteudo_label = tk.Label(nova_janela, text="Labels: Exibem texto na tela.",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: label = tk.Label(nova_janela, text='Olá, mundo!')\nlabel.pack()")
                conteudo_label.pack()
                label = tk.Label(nova_janela, text="Olá, mundo!")
                label.pack()
                conteudo_label = tk.Label(nova_janela, text=" Neste exemplo, label é uma variável que armazena uma referência ao novo widget de rótulo. nova_janela é a referência ao widget pai do rótulo. O texto 'Olá, mundo!' é o texto que será exibido pelo rótulo.")
                conteudo_label.pack(pady=5)
                conteudo_label = tk.Label(nova_janela, text="Configurações de Label .",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="O widget Label do Tkinter é usado para exibir texto na tela. Ele possui diversas opções de configuração que permitem personalizar sua aparência e comportamento.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: Define o texto que será exibido pelo rótulo. (Tipo: str)\nfont: Define a fonte do texto. (Tipo: str ou tuple)\nforeground: Define a cor da fonte do texto. (Tipo: str)\nbackground: Define a cor de fundo do rótulo. (Tipo: str)\njustify: Define o alinhamento do texto dentro do rótulo. (Tipo: str - left, center, right)\npadx: Define o espaçamento horizontal em pixels ao redor do texto. (Tipo: int)\npady: Define o espaçamento vertical em pixels ao redor do texto. (Tipo: int)\nwidth: Define a largura do rótulo em pixels. (Tipo: int)\nheight: Define a altura do rótulo em pixels. (Tipo: int)\nborderwidth: Define a largura da borda do rótulo em pixels. (Tipo: int)\nrelief: Define o estilo da borda do rótulo. (Tipo: str - flat, raised, sunken, ridge, groove)\ncursor: Define o tipo de cursor a ser exibido quando o mouse está sobre o rótulo. (Tipo: str - none, arrow, watch, cross, plus, tcross, pgdown, pgup, left, right, top, bottom, x, y, questionhour, star)\nwraplength: Define o comprimento máximo da linha de texto antes de quebrar para a próxima linha. (Tipo: int)")
                conteudo_label.pack()
                def exemplo_label():
                    window = tk.Tk()
                    window.title("Exemplo de Label")

                    label = tk.Label(window, 
                    text="Olá, Mundo!", 
                    font=("Arial", 24, "bold"), 
                    foreground="red", 
                    background="yellow", 
                    justify="center", 
                    padx=20, 
                    pady=10, 
                    width=200, 
                    height=50, 
                    borderwidth=5, 
                    relief="ridge", 
                    cursor="cross")
                    label.pack()

                self.botao1 = tk.Button(nova_janela, text="Exemplo de Label", command=exemplo_label)
                self.botao1.pack(pady=5)
            def Button_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Button')
                conteudo_label = tk.Label(nova_janela, text="Buttons: Os botões são widgets fundamentais para a interação do usuário com a interface gráfica (GUI) no Tkinter. Eles permitem que os usuários iniciem ações na sua aplicação.",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: button = tk.Button(window, text='Clique em mim!', command=greet)\nbutton.pack()")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Quando o usuário clica no botão, a função greet é chamada.")
                conteudo_label.pack()
                def exemplo_botao():
                    def greet():
                        print("Você clicou no botão!")

                    window = tk.Tk()
                    window.title("Exemplo de Button")

                    button = tk.Button(window, text="Clique em mim!", command=greet)
                    button.pack()


                self.botao2 = tk.Button(nova_janela, text="Exemplo de Botão", command=exemplo_botao)
                self.botao2.pack()
                conteudo_label = tk.Label(nova_janela, text="O widget Button além do texto do botão, você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Configurações comuns de botões.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: (Obrigatório) Define o texto exibido no botão. (Tipo: str)\nfont: Define a fonte do texto do botão. (Tipo: str ou tuple)\nforeground: Define a cor da fonte do texto do botão. (Tipo: str)\nbackground: Define a cor de fundo do botão. (Tipo: str)\nactiveforeground: Define a cor da fonte do texto do botão quando ele está sendo pressionado. (Tipo: str)\nactivebackground: Define a cor de fundo do botão quando ele está sendo pressionado. (Tipo: str)\ndisabledforeground: Define a cor da fonte do texto do botão quando ele está desabilitado. (Tipo: str)\ndisabledbackground: Define a cor de fundo do botão quando ele está desabilitado. (Tipo: str)\ncommand: Define a função a ser chamada quando o botão é clicado. (Tipo: função)\nstate: Define o estado do botão (normal, active, disabled). (Tipo: str)\nimage: Define uma imagem a ser exibida no botão. (Tipo: PhotoImage object)\ncompound: Define como o texto e a imagem serão posicionados dentro do botão (left, top, right, bottom, center). (Tipo: str)\npady: Define o espaçamento vertical em pixels ao redor do texto ou imagem do botão. (Tipo: int)\npadx: Define o espaçamento horizontal em pixels ao redor do texto ou imagem do botão. (Tipo: int)\nwidth: Define a largura do botão em pixels. (Tipo: int)\nheight: Define a altura do botão em pixels. (Tipo: int)\nborderwidth: Define a largura da borda do botão em pixels. (Tipo: int)\nrelief: Define o estilo da borda do botão (flat, raised, sunken, ridge, groove). (Tipo: str)\ncursor: Define o tipo de cursor a ser exibido quando o mouse está sobre o botão. (Tipo: str)")
                conteudo_label.pack()
                def exemplo_botao1():
                    def greet():
                        print("Você clicou no botão!")

                    window = tk.Tk()
                    window.title("Exemplo de Button")

                    button1 = tk.Button(window, text="Clique aqui", command=greet)
                    button1.pack()

                    # Botão com aparência personalizada
                    button2 = tk.Button(window, 
                                        text="Confirmar", 
                                        font=("Arial", 14, "bold"), 
                                        foreground="white", 
                                        background="blue", 
                                        activeforeground="red", 
                                        activebackground="yellow", 
                                        padx=10, 
                                        pady=5,command=greet)
                    button2.pack()



                self.botao2 = tk.Button(nova_janela, text="Exemplo de Botão", command=exemplo_botao1)
                self.botao2.pack()
            def Entries_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Entry')
                conteudo_label = tk.Label(nova_janela, text="Entries: permite que os usuários insiram texto de linha única na interface gráfica do usuário",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: entry = tk.Entry(janela)\nentry.pack()")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="O usuário pode digitar seu nome no Entry.")
                conteudo_label.pack()
                def exemplo_entry():
                    janela = tk.Tk()
                    janela.title("Exemplo de Entry")

                    label = tk.Label(janela, text="Digite seu nome:")
                    label.pack()

                    entry = tk.Entry(janela)
                    entry.pack()

                    def pegar_texto():
                        print(entry.get())

                    botao = tk.Button(janela, text="Obter Texto", command=pegar_texto)
                    botao.pack()
                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de entry", command=exemplo_entry)
                self.botao2.pack()
                conteudo_label = tk.Label(nova_janela, text="O widget entry você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: (Obrigatório) Define o texto exibido no botão. (Tipo: str)\nfont: Define a fonte do texto do botão. (Tipo: str ou tuple)\nforeground: Define a cor da fonte do texto do botão. (Tipo: str)\nbackground: Define a cor de fundo do botão. (Tipo: str)\nwidth: Define a largura do Entry em caracteres. (Tipo: int)\nshow: Define quais caracteres exibir quando o usuário insere texto. Útil para ocultar senhas (por exemplo, show=* exibe asteriscos para cada caractere). (Tipo: str)\nstate: Define o estado do Entry (normal, readonly, disabled). (Tipo: str)\ndisabledforeground: Define a cor do texto quando o Entry está desabilitado. (Tipo: str)\ndisabledbackground: Define a cor de fundo do Entry quando ele está desabilitado. (Tipo: str)\njustify: Define o alinhamento do texto dentro do Entry (left, center, right). (Tipo: str)\nvalidate: Define uma função para validar a entrada do usuário. Esta função recebe o texto atual como argumento e deve retornar True (para permitir a entrada) ou False (para impedir a entrada). (Tipo: função)\nvalidatecommand: Semelhante a validate, mas permite passar um argumento adicional para a função de validação. (Tipo: função)")
                conteudo_label.pack()
            def Checkboxes_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Checkboxes')
                conteudo_label = tk.Label(nova_janela, text="Checkboxes: usadas para permitir que os usuários selecionem várias opções de um conjunto de escolhas",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: caixa_selecao1 = tk.Checkbutton(janela, text=Opção 1, variable=var1, command=lambda: estado_caixas_selecao(var1, var2))\ncaixa_selecao1.pack()")
                conteudo_label.pack()
                
                conteudo_label = tk.Label(nova_janela, text="O widget Checkboxes você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: (Obrigatório) Define o texto exibido no botão. (Tipo: str)\nvariable: Vincula a caixa de seleção a um IntVar ou StringVar para armazenar seu estado.\nonvalue: Define o valor a ser armazenado na variável quando a caixa de seleção é marcada (padrão 1).\noffvalue: Define o valor a ser armazenado na variável quando a caixa de seleção é desmarcada (padrão 0).\nstate: Define o estado inicial da caixa de seleção (normal, disabled, selected).\ncommand: Especifica uma função a ser chamada quando a caixa de seleção é clicada.\nactivebackground: Define a cor de fundo quando a caixa de seleção está ativa.\ndisabledforeground: Define a cor do texto quando a caixa de seleção está desabilitada.")
                conteudo_label.pack()
            def Radiobuttons_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Radiobuttons')
                conteudo_label = tk.Label(nova_janela, text="Radiobuttons:  Eles permitem que os usuários selecionem apenas uma opção de um conjunto predefinido de alternativas. Veja como usá-los",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: radio_opcao1 = tk.Radiobutton(janela, text=Opção 1, variable=escolha, value=opcao1, command=lambda: selecao_mudou(opcao1))\nradio_opcao1.pack()")
                conteudo_label.pack()
                def exemplo_entry():
                    def selecao_mudou(valor):
                        # Acesse o valor selecionado na variável "escolha"
                        print(f"Você selecionou: {valor}")

                    # Criar a janela principal
                    janela = tk.Tk()
                    janela.title("Exemplo de Radio Buttons")

                    # Criar a variável para armazenar a seleção do usuário
                    escolha = tk.StringVar()  # Variável para armazenar o valor selecionado (string)

                    # Criar os Radio Buttons com texto e valor associado à variável "escolha"
                    radio_opcao1 = tk.Radiobutton(janela, text="Opção 1", variable=escolha, value="opcao1", command=lambda: selecao_mudou("opcao1"))
                    radio_opcao1.pack()

                    radio_opcao2 = tk.Radiobutton(janela, text="Opção 2", variable=escolha, value="opcao2", command=lambda: selecao_mudou("opcao2"))
                    radio_opcao2.pack()



                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de Radio Buttons", command=exemplo_entry)
                self.botao2.pack()

                
                conteudo_label = tk.Label(nova_janela, text="O widget Radiobuttons você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: (Obrigatório) Define o texto exibido no botão. (Tipo: str)\nvariable: Vincula a caixa de seleção a um IntVar ou StringVar para armazenar seu estado.\nonvalue: Define o valor a ser armazenado na variável quando a caixa de seleção é marcada (padrão 1).\noffvalue: Define o valor a ser armazenado na variável quando a caixa de seleção é desmarcada (padrão 0).\nstate: Define o estado inicial da caixa de seleção (normal, disabled, selected).\ncommand: Especifica uma função a ser chamada quando a caixa de seleção é clicada.\nactivebackground: Define a cor de fundo quando a caixa de seleção está ativa.\ndisabledforeground: Define a cor do texto quando a caixa de seleção está desabilitada.")
                conteudo_label.pack()
            def Text_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Text')
                conteudo_label = tk.Label(nova_janela, text="Text: Permitem criar campos de entrada de texto multi-linha e áreas de exibição dentro da sua interface gráfica",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: texto = tk.Text(janela, width=40, height=10)\ntexto.pack()")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="No widget Text você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="font: Define a fonte do texto (nome da família, tamanho e estilo).\nfg: Define a cor da fonte do texto.bg: Define a cor do plano de fundo do texto.\nhighlightbackground: Define a cor de fundo quando o widget recebe foco.\nhighlightcolor: Define a cor da borda quando o widget recebe foco.\nbd: Define a largura da borda do widget.relief: Define o estilo da borda do widget (plano, em relevo, sulcado, etc.).\npadx: Define o espaçamento interno horizontal do widget.\npady: Define o espaçamento interno vertical do widget.\nspacing: Define o espaçamento entre linhas de texto.\ninsertbackground: Define a cor de fundo da posição do cursor de inserção.\ninsertborderwidth: Define a largura da borda da posição do cursor de inserção.\ninsertbordercolor: Define a cor da borda da posição do cursor de inserção.\ntabwidth: Define o tamanho da tabulação.wrap: Define o comportamento de quebra de linha (caractere, palavra, etc.).\nlmargin: Define a margem esquerda do texto.\nrmargin: Define a margem direita do texto.\ntopmargin: Define a margem superior do texto.\nbotmargin: Define a margem inferior do texto.\njustify: Define o alinhamento do texto esquerda, centro, direita, justificado\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="No widget Text você pode personalizar o conteúdo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: Define o texto inicial exibido no widget.\nwidth: Define a largura do widget em unidades de caracteres.\nheight: Define a altura do widget em unidades de linhas.\ntakefocus: Define se o widget pode receber foco.\ncursorcolor: Define a cor do cursor de texto.\nreadonly: Define se o texto é editável ou apenas para leitura.\nstate: Define o estado inicial do widget (normal, desabilitado, somente leitura).\nwrap: Define o comportamento de quebra de linha (caractere, palavra, etc.).\ntabs: Define o tamanho e a posição das tabulações.\ninsertonoff: Define se o cursor de inserção é exibido quando o widget está desabilitado.\nexportselection: Define se a seleção de texto pode ser exportada.\nshowselection: Define se a seleção de texto é destacada.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="No widget Text temos algumas funções")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Manipulação do Texto\ninsert(index, string, chars=None): Insere texto na posição especificada.\ndelete(index1, index2): Remove texto entre as posições indicadas.\nindex(string, start=0, end=tk.END, exact=True): Encontra a primeira ocorrência de uma string.\nreplace(index1, index2, string): Substitui texto entre as posições por uma nova string.\nmark(name, index): Cria uma marca em uma posição específica.\nmarkset(name, index): Move uma marca para uma nova posição.\nmarkpos(name): Obtém a posição de uma marca.\nxmark(x, y): Cria uma marca em uma posição relativa (x, y).\nxmarkpos(x, y): Obtém a posição de uma marca em coordenadas (x, y).\ntag(tagname, index1, index2, **kwargs): Cria uma tag com formatação para um intervalo de texto.\ntagadd(tagname, index1, index2): Adiciona um intervalo de texto a uma tag existente.\ntagremove(tagname, index1, index2): Remove um intervalo de texto de uma tag.\ntagconfigure(tagname, **kwargs): Configura as opções de formatação de uma tag.\ntagnodes(tagname): Retorna os índices de início e fim do texto associado à tag.\ntagrange(tagname): Retorna o intervalo completo (início e fim) do texto associado à tag.")

                def exemplo_Text():
                    def pegar_todo_texto():
                    # Obter todo o texto do widget Text
                     texto_completo = texto.get(1.0, tk.END)  # 1.0 indica a primeira linha
                                                            # tk.END indica o final do texto
                     print(f"Texto completo:\n{texto_completo}")

                    # Criar a janela principal
                    janela = tk.Tk()
                    janela.title("Exemplo de Text Widget")

                    # Criar o widget Text
                    texto = tk.Text(janela, width=40, height=10)  # Define largura e altura
                    texto.pack()

                    # (Opcional) Inserir texto padrão
                    texto.insert(tk.END, "Digite seu texto aqui...")

                    # Criar um botão para acionar a função
                    botao_pegar_texto = tk.Button(janela, text="Pegar Texto", command=pegar_todo_texto)
                    botao_pegar_texto.pack()
                self.botao2 = tk.Button(nova_janela, text="Exemplo de Text", command=exemplo_Text)
                self.botao2.pack()
                def exemplo_Text_func1():
                    def contar_caracteres():
                        texto = entrada_texto.get(1.0, tk.END)
                        numero_caracteres = len(texto) - 1
                        resultado_label.config(text=f"O texto possui {numero_caracteres} caracteres.")

                    def contar_letras(texto):
                        numero_letras = 0
                        for c in texto:
                            if c.isalpha():
                                numero_letras += 1
                                numero_letras -= 1
                                return numero_letras
                            
                           

                            # Cria a janela principal
                    janela = tk.Tk()
                    janela.title("Contador de Caracteres")

                            # Cria a caixa de entrada de texto
                    entrada_texto = tk.Text(janela)
                    entrada_texto.pack()

                            # Cria botões para contar caracteres e letras
                    botao_contar_caracteres = tk.Button(janela, text="Contar Caracteres", command=contar_caracteres)
                    botao_contar_caracteres.pack()

                    botao_contar_letras = tk.Button(janela, text="Contar Letras", command=lambda: resultado_label.config(text=f"O texto possui {contar_letras(entrada_texto.get(1.0, tk.END))} letras."))
                    botao_contar_letras.pack()

                            # Cria o rótulo para exibir o resultado
                    resultado_label = tk.Label(janela, text="")
                    resultado_label.pack()
                self.botao3 = tk.Button(nova_janela, text="Contador de Caractere", command=exemplo_Text_func1)
                self.botao3.pack()
            def Frames_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Frames')
                conteudo_label = tk.Label(nova_janela, text="Frames: usados para organizar e gerenciar o layout dos widgets da sua interface gráfica. Eles funcionam como contêineres que agrupam outros widgets, criando uma interface mais estruturada e visualmente atrativa",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: frame_superior = tk.Frame(janela, width=400, height=200, bg=lightblue)\nframe_superior.pack()")
                conteudo_label.pack()
                def exemplo_Frames():
                   
                    janela = tk.Tk()
                    janela.title("Exemplo Simples de Frame")
                    frame_entrada = tk.Frame(janela, padx=10, pady=10, bg="lightgreen")
                    frame_entrada.pack()
                    label_nome = tk.Label(frame_entrada, text="Digite seu nome:")
                    label_nome.pack()
                    entry_nome = tk.Entry(frame_entrada)
                    entry_nome.pack()


                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de Frames", command=exemplo_Frames)
                self.botao2.pack()   
            def Canvases_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Canvases')
                conteudo_label = tk.Label(nova_janela, text="Canvases: fornecem uma área de desenho para criar vários elementos gráficos. Elas permitem renderizar formas, linhas, imagens, texto e até mesmo incorporar outros widgets dentro delas",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: canvas = tk.Canvas(janela, width=400, height=300, bg=white)\ncanvas.pack()")
                conteudo_label.pack()
                def exemplo_Canvases():
                   
                    janela = tk.Tk()
                    janela.title("Exemplo Simples de Canvases")
                   
                    # Criar uma tela
                    canvas = tk.Canvas(janela, width=400, height=300, bg="Blue")
                    canvas.pack()

                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de Canvases", command=exemplo_Canvases)
                self.botao2.pack()
            def Menus_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('Menus')
                conteudo_label = tk.Label(nova_janela, text="Menus: que fornecem aos usuários acesso organizado a várias funcionalidades dentro de sua aplicação",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="No widget Menus você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Configurações Básicas.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="text: Define o texto que será exibido na opção do menu.\n command: Função a ser chamada quando a opção do menu for selecionada.\nstate: Controla o estado da opção do menu, podendo ser normal, disabled,active ou hidden.\nimage: Permite exibir um ícone ao lado da opção do menu.\ncompound: Define a posição do ícone em relação ao texto da opção.\naccelerator: Atribui uma tecla de atalho para a opção do menu.\nunderline: Sublinha o texto da opção do menu (padrão: False).\ntearoff: Permite que o submenu seja destacado da barra de menus (padrão: False).\n variable: Vincula a opção do menu a uma variável.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Configurações Avançadas para Submenus.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="type: Define o tipo de submenu, podendo ser cascade, tearoff, radiobutton ou checkbutton.\nmenu: Especifica o submenu a ser exibido quando a opção do menu for selecionada.\nselectcolor: Define a cor de fundo quando a opção do menu for selecionada.\nactivebackground: Define a cor de fundo quando a opção do menu estiver ativa (passando o mouse).\nactiveforeground: Define a cor da fonte quando a opção do menu estiver ativa.\ndisablebackground: Define a cor de fundo quando a opção do menu estiver desativada.\ndisableforeground: Define a cor da fonte quando a opção do menu estiver desativada.\n ")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Configurações para Personalização.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="font: Define a fonte do texto da opção do menu.\nforeground: Define a cor da fonte da opção do menu.\nbackground: Define a cor de fundo da opção do menu.\nborderwidth: Define a largura da borda da opção do menu.\nrelief: Define o estilo da borda da opção do menu (por exemplo, flat, raised, sunken).\npadx: Define o espaçamento horizontal entre o texto e as bordas da opção do menu.\npady: Define o espaçamento vertical entre o texto e as bordas da opção do menu.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Configurações para Eventos.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="command: Função a ser chamada quando a opção do menu for selecionada.\nbind: Vincula eventos do mouse ou teclado à opção do menu.\nevent: Define o evento a ser monitorado (por exemplo, <Button-1>, <Enter>, <Leave>).\ncallback: Função a ser chamada quando o evento ocorrer.\n")
                conteudo_label.pack()
                def exemplo_Menus():
                    def abrir_arquivo():
                        print("exemplo de arquivo...")
                        #Esta função simplesmente imprime a mensagem "exemplo de arquivo..." na tela.

                
                    def sair_aplicacao():
                        print("Saindo do exemplo.")
                        #Esta função imprime a mensagem "Saindo do exemplo." na tela.

                    # Criar a janela principal
                    janela = tk.Tk()#armazena essa instância e pode ser usada para acessar e manipular a janela principal.
                    janela.title("Exemplo de Menu")#define o título da janela como "Exemplo de Menu".

                    # Criar a barra de menus
                    barra_menus = tk.Menu(janela)#A linha barra_menus = tk.Menu(janela) cria um novo menu principal que será exibido na parte superior da janela.A variável barra_menus armazena esse menu e pode ser usada para adicionar itens a ele.

                    # Criar o menu Arquivo
                    menu_arquivo = tk.Menu(barra_menus, tearoff=0)#cria um novo submenu dentro da barra de menus principal, chamado de "Arquivo".O parâmetro tearoff=0 indica que o submenu não deve ser destacável da barra de menus principal.A variável menu_arquivo armazena esse submenu e pode ser usada para adicionar itens a ele.
                    menu_arquivo.add_command(label="exemplo1", command=abrir_arquivo)#adiciona um novo item ao menu Arquivo com o rótulo "exemplo1".Quando este item for clicado, a função abrir_arquivo() será executada.
                    menu_arquivo.add_separator()#adiciona uma linha divisória ao menu Arquivo para separar os itens.
                    menu_arquivo.add_command(label="Sair", command=sair_aplicacao)#adiciona outro item ao menu Arquivo com o rótulo "Sair".Quando este item for clicado, a função sair_aplicacao() será executada.

                    barra_menus.add_cascade(label="Exemplo", menu=menu_arquivo)#adiciona o submenu "Arquivo" à barra de menus principal.O rótulo "Exemplo" será exibido ao lado do menu na barra de menus.

                    # Adicione mais menus (Editar, Ajuda, etc.) seguindo a mesma estrutura

                    # Configurar a barra de menus
                    janela.config(menu=barra_menus)

                    # Iniciar o loop principal do evento
                self.botao2 = tk.Button(nova_janela, text="Exemplo de Menus", command=exemplo_Menus)
                self.botao2.pack(pady=5)
               
                def exemplo_Menus_desabilitando_menu():
                    # Cria a janela principal
                    janela = tk.Tk()#cria a janela principal da aplicação usando a biblioteca Tkinter.
                    janela.title("Exemplo de Menu")#Define o título da janela como "Exemplo de Menu".


                    # Cria a barra de menus
                    barra_menus = tk.Menu(janela)

                    # Cria o menu Arquivo Cria um submenu dentro da barra de menus principal chamado "Arquivo".
                    menu_arquivo = tk.Menu(barra_menus, tearoff=0)#ndica que o submenu não se separa da barra de menus principal.
                    barra_menus.add_cascade(label="Arquivo", menu=menu_arquivo)#Adiciona o submenu "Arquivo" à barra de menus principal.

                    # Função única para ações de arquivo
                    def acao_arquivo(acao):#Define uma função chamada acao_arquivo que recebe um parâmetro acao.
                        if acao == "abrir":#erifica se a ação solicitada é "abrir".Se for, imprime a mensagem "Abrindo um arquivo...".
                            print("Abrindo um arquivo...")
                        elif acao == "salvar":#Verifica se a ação solicitada é "salvar".Se for, imprime a mensagem "Salvando um arquivo...".
                            print("Salvando um arquivo...")

                    # Adiciona opções ao menu Arquivo

                    #Adiciona uma opção ao menu "Arquivo" com o rótulo "exemplo01".Quando a opção for clicada, a função acao_arquivo("abrir") será executada.A opção é inicialmente desativada (state=tk.DISABLED).
                    menu_arquivo.add_command(label="exemplo01", command=lambda: acao_arquivo("abrir"), state=tk.DISABLED)
                    # Adiciona outra opção ao menu "Arquivo" com o rótulo "exemplo02".Funciona similarmente à opção "exemplo01", mas com a ação "salvar".Também é inicialmente desativada.
                    menu_arquivo.add_command(label="exemplo02", command=lambda: acao_arquivo("salvar"), state=tk.DISABLED)
                    menu_arquivo.add_separator()#Adiciona uma linha divisória entre as opções.
                    menu_arquivo.add_command(label="Sair", command=janela.quit)#Adiciona uma opção "Sair" ao menu "Arquivo".Quando clicada, a função janela.quit() fecha a janela principal.

                    # Define a função para alternar o estado das opções
                    def alternar_opcoes_arquivo():
                        global arquivo_aberto  # Declara a variável arquivo_aberto como global dentro da função.Essa variável será usada para controlar se um arquivo está aberto ou não.

                        arquivo_aberto = not arquivo_aberto#Inverte o valor atual da variável arquivo_aberto.

                        menu_arquivo.entryconfig("exemplo01", state=tk.NORMAL if arquivo_aberto else tk.DISABLED)# Altera o estado da opção "exemplo01" para tk.NORMAL se arquivo_aberto for True, ou para tk.DISABLED caso contrário.
                        menu_arquivo.entryconfig("exemplo02", state=tk.NORMAL if arquivo_aberto else tk.DISABLED)# Faz o mesmo para a opção "exemplo02".

                    # Adiciona um item ao menu para alternar o estado das opções
                    menu_arquivo.add_command(label="Alternar Opções", command=alternar_opcoes_arquivo)# Adiciona uma opção "Alternar Opções" ao menu "Arquivo".Quando clicada, a função alternar_opcoes_arquivo será executada.

                    # Configura a barra de menus
                    janela.config(menu=barra_menus)#Define a barra de menus criada como a barra de menus principal da janela.

                
                    
                self.botao3 = tk.Button(nova_janela, text="Exemplo de Menus Desabilitando", command=exemplo_Menus_desabilitando_menu)
                self.botao3.pack(pady=5)

                def exemplo_Menus_cascateados():
                    # Funções para ações do menu
                    def abrir_arquivo():#Esta função simplesmente imprime a mensagem "exemplo01" na tela.
                        print("exemplo01")

                    def salvar_arquivo():#Esta função simplesmente imprime a mensagem "exemplo02" na tela.
                        print("exemplo02")

                    def sair_aplicacao():#Esta função simplesmente imprime a mensagem "exemplo03" na tela.
                        print("exemplo03")

                    # Cria a janela principal
                    janela = tk.Tk()#Cria a janela principal da aplicação usando a biblioteca Tkinter.
                    janela.title("Exemplo de Menu Cascateado")#Define o título da janela como "Exemplo de Menu Cascateado".

                    # Cria a barra de menus principal
                    barra_menus = tk.Menu(janela)#Cria a barra de menus que será exibida na parte superior da janela.

                    # Cria o menu Arquivo
                    #Cria um submenu dentro da barra de menus principal chamado "exemplo00".
                    menu_arquivo = tk.Menu(barra_menus, tearoff=0)#indica que o submenu não se separa da barra de menus principal.
                    barra_menus.add_cascade(label="exemplo00", menu=menu_arquivo)#Adiciona o submenu "Arquivo" à barra de menus principal.

                    # Adiciona opções ao menu Arquivo
                    #Adiciona uma opção ao menu "Arquivo" com o rótulo "exemplo01".Quando a opção for clicada, a função abrir_arquivo() será executada.
                    menu_arquivo.add_command(label="exemplo01", command=abrir_arquivo)
                    #Adiciona outra opção ao menu "Arquivo" com o rótulo "exemplo02".Funciona similarmente à opção "exemplo01", mas com a ação "salvar_arquivo".
                    menu_arquivo.add_command(label="exemplo02", command=salvar_arquivo)
                    menu_arquivo.add_separator()#Adiciona uma linha divisória entre as opções.
                    #Adiciona uma opção "exemplo03" ao menu "Arquivo".Quando clicada, a função sair_aplicacao() será executada.
                    menu_arquivo.add_command(label="exemplo03", command=sair_aplicacao)

                    # Cria o menu Editar
                    menu_editar = tk.Menu(barra_menus, tearoff=0)# Cria outro submenu dentro da barra de menus principal chamado "Editar". indica que o submenu não se separa da barra de menus principal.
                    barra_menus.add_cascade(label="exemplo01", menu=menu_editar)#Adiciona o submenu "Editar" à barra de menus principal.

                    # Adiciona opções ao menu Exemplo
                    menu_editar.add_command(label="exemplo02", command=lambda: print("exemplo"))#Adiciona uma opção ao menu "Editar" com o rótulo "exemplo02".Quando a opção for clicada, a função lambda será executada, imprimindo a mensagem "exemplo" na tela.
                    menu_editar.add_command(label="exemplo03", command=lambda: print("exemplo"))# Adiciona outra opção ao menu "Editar" com o rótulo "exemplo03".Funciona similarmente à opção "exemplo02", imprimindo a mensagem "exemplo" na tela.
                   
                    

                    # Configura a barra de menus principal
                    janela.config(menu=barra_menus)#Define a barra de menus criada como a barra de menus principal da janela.

                    # Inicia o loop principal do evento
                    janela.mainloop()
                   
                self.botao4 = tk.Button(nova_janela, text="Exemplo de Menus Cascateados ", command=exemplo_Menus_cascateados)
                self.botao4.pack(pady=5)
            def OptionMenu():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('OptionMenu')
                conteudo_label = tk.Label(nova_janela, text="OptionMenu: cria menus suspensos que permitem ao usuário selecionar uma opção dentre uma lista predefinida",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="No widget OptionMenu você pode personalizá-lo através de várias configurações.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Menu de Opções:.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="menu: Define o widget Menu que contém as opções a serem exibidas no menu suspenso.\n variable: Uma variável Tkinter que armazenará o valor da opção selecionada.\n value: Define o valor inicial da variável variable.\n default: Define a opção que será inicialmente selecionada.\n command: Uma função que será chamada quando uma nova opção for selecionada.\n takefocus: Indica se o OptionMenu pode receber o foco do teclado.\n exportselection: Controla se a seleção do menu suspenso é exportada para o X11.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Aparência:.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="indicatoron: Exibe ou oculta a seta indicadora.\n textvariable: Uma variável Tkinter que armazenará o texto do botão.\n font: Define a fonte do texto no botão.\n background: Define a cor de fundo do botão.\n foreground: Define a cor da fonte do texto no botão.\n borderwidth: Define a largura da borda do botão.\n relief: Define o relevo da borda do botão.\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Controle de Desativação:\n")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="disabledvariable: Uma variável Tkinter que controla se o OptionMenu está desativado.\nstate: Define o estado inicial do OptionMenu (normal, disabled, active).\n")
                conteudo_label.pack()
                def exemplo_OptionMenu():
                    # Criando a janela principal
                    window = tk.Tk()
                    window.title("Exemplo de OptionMenu")

                    # Lista de opções
                    frutas = ["Maçã", "Banana", "Laranja"]

                    # Variável para armazenar a seleção atual
                    selecao_fruta = tk.StringVar()
                    selecao_fruta.set(frutas[0])  # Define a fruta selecionada inicialmente

                    # Função para capturar a seleção do usuário
                    def fruta_selecionada(fruta):
                        print("Você selecionou:", fruta)

                    # Criando o OptionMenu
                    menu_fruta = tk.OptionMenu(window, selecao_fruta, *frutas, command=fruta_selecionada)
                    menu_fruta.pack()
                   
                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de OptionMenu", command=exemplo_OptionMenu)
                self.botao2.pack()
            def messagebox_expicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('messagebox')
                conteudo_label = tk.Label(nova_janela, text="messagebox:  é um módulo do Tkinter que oferece diversas funções para criar pop-ups informativas, interativas e personalizáveis em suas interfaces gráficas.\n Essas caixas de diálogo são elementos essenciais para comunicar-se com o usuário opção dentre uma lista predefinida",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text=" Funcionalidades Essenciais.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exibir mensagens: Apresente informações ao usuário, como avisos, erros ou instruções, através de mensagens simples com títulos e textos explicativos.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Obter confirmações: Confirme ações importantes antes de serem executadas, utilizando botões de Sim e Não ou OK e Cancelar, para garantir que o usuário esteja ciente das consequências.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Coletar informações: Permita que o usuário digite dados em campos de texto, coletando informações como nomes, emails, senhas ou outras entradas relevantes para a aplicação.")
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text=" Indicar progresso: Mantenha o usuário informado sobre o andamento de tarefas demoradas, utilizando barras de progresso com porcentagens e mensagens explicativas.")
                conteudo_label.pack()
                def exemplo_messagebox():
                    def mostrar_mensagem():
                        resposta = messagebox.askquestion("Confirmação", "Deseja realmente fechar a aplicação?")
                        if resposta == "yes":
                            janela.destroy()

                    janela = tk.Tk()

                    botao_fechar = tk.Button(janela, text="Fechar", command=mostrar_mensagem)
                    botao_fechar.pack()
                self.botao2 = tk.Button(nova_janela, text="Exemplo messagebox", command=exemplo_messagebox)
                self.botao2.pack()


            self.botao_Label = tk.Button(nova_janela, text="Label", command=Label_explicacao)
            self.botao_Label.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Button = tk.Button(nova_janela, text="Button", command=Button_explicacao)
            self.botao_Button.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_entries = tk.Button(nova_janela, text="Entries",command=Entries_explicacao)
            self.botao_entries.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Checkboxes = tk.Button(nova_janela, text="Checkboxes",command=Checkboxes_explicacao)
            self.botao_Checkboxes.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Radiobuttons = tk.Button(nova_janela, text="Radiobuttons",command=Radiobuttons_explicacao)
            self.botao_Radiobuttons.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Text = tk.Button(nova_janela, text="Text",command=Text_explicacao)
            self.botao_Text.pack(pady=5, side=tk.LEFT, expand=True)
            
            self.botao_Frames = tk.Button(nova_janela, text="Frames",command=Frames_explicacao)
            self.botao_Frames.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Canvases = tk.Button(nova_janela, text="Canvases",command=Canvases_explicacao)
            self.botao_Canvases.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_Menus = tk.Button(nova_janela, text="Menus",command=Menus_explicacao)
            self.botao_Menus.pack(pady=5, side=tk.LEFT, expand=True)

            self.botao_optionMenus = tk.Button(nova_janela, text="OptionMenu",command=OptionMenu)
            self.botao_optionMenus.pack(pady=5, side=tk.LEFT, expand=True)
            
            self.botao_messagebox = tk.Button(nova_janela, text="Messagebox",command= messagebox_expicacao)
            self.botao_messagebox.pack(pady=5, side=tk.LEFT, expand=True)
           
        if topico=="Grid: Gerenciandores de layout": 


            conteudo_label = tk.Label(nova_janela, text="Grid: Gerenciandores de layout",font=("Arial", 12, "bold"))
            conteudo_label.pack(pady=5)

            conteudo_label_sub_titulo = tk.Label(nova_janela, text="O grid no Tkinter é um gerenciador de layout poderoso e flexível que permite organizar widgets em uma grade de linhas e colunas.\n Ele oferece um controle preciso do posicionamento e dimensionamento dos elementos na interface gráfica, tornando-o ideal para criar layouts complexos e responsivos.")
            conteudo_label_sub_titulo.pack()
            conteudo_label = tk.Label(nova_janela, text="Funcionalidades Principais: \nPosicionamento preciso: Cada widget é posicionado em uma célula específica da grade, definida por coordenadas de linha e coluna.\nAlinhamento automático: Os widgets são automaticamente alinhados dentro de suas células, facilitando a criação de layouts organizados e visualmente agradáveis.\nGerenciamento de espaço: O grid permite distribuir o espaço livre entre as linhas e colunas de forma proporcional ou personalizada.\nLayout responsivo: Os widgets podem se adaptar automaticamente a diferentes tamanhos de tela, garantindo que a interface gráfica seja bem apresentada em diversos dispositivos.\nCombinação com outros gerenciadores: O grid pode ser usado em conjunto com outros gerenciadores de layout, como pack e place, para criar layouts mais complexos.",font=("Arial", 10,))
            conteudo_label.pack(pady=5)
            def row_explicacao():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('row')
                conteudo_label = tk.Label(nova_janela, text="row:  linha em que um widget será posicionado.",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="Exemplo: label_nome = tk.Label(janela, text=Nome:)\nlabel_nome.grid(row=0)\nPosiciona o Label Nome: na primeira linha (row=0)")
                conteudo_label.pack()
                
                conteudo_label = tk.Label(nova_janela, text="Funcionamento .",font=("Arial", 10, "bold"))
                conteudo_label.pack()
                conteudo_label = tk.Label(nova_janela, text="As linhas são numeradas a partir de 0, então row=0 indica a primeira linha, row=1 a segunda linha e assim por diante.\nSe você não especificar o valor da coluna, o widget será colocado na primeira coluna por padrão.\nÉ possível colocar vários widgets na mesma linha, definindo a mesma posição row para cada um.\nO espaçamento entre os widgets e as bordas da janela, ou entre os próprios widgets, pode ser ajustado usando as opções padx e pady no método grid().")
                conteudo_label.pack()
               
             
           
               
            self.botao_Label = tk.Button(nova_janela, text="row", command=row_explicacao)
            self.botao_Label.pack(pady=5, side=tk.LEFT, expand=True)

     

            
       
            
            


            





















            
           
            






        

    # def Criacao_de_Janela_Principal(self):  # Função para criar nova janela (opcional)
    #     nova_janela = tk.Toplevel(self.root)
    #     nova_janela.title("Nova Janela")
    #     label = tk.Label(nova_janela, text="Criação da Janela Principal")
    #     label.pack()
    # def  Widgets_Blocos_de_Construção(self):  # Função para criar nova janela (opcional)
    #     nova_janela = tk.Toplevel(self.root)
    #     nova_janela.title("Nova Janela")
    #     label = tk.Label(nova_janela, text="Widgets: Blocos de Construção")
    #     label.pack()
    # def  Layout_Organizando_a_Interface(self):  # Função para criar nova janela (opcional)
    #     nova_janela = tk.Toplevel(self.root)
    #     nova_janela.title("Nova Janela")
    #     label = tk.Label(nova_janela, text="Layout: Organizando a Interface")
    #     label.pack()
    def fechar_janela(self):
        self.root.destroy()

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":#Esta é uma instrução condicional. Ele verifica o valor da variável especial
    interface_grafica = InterfaceGrafica() #cria uma instância da calsse Esta classe e  responsável por configurar os elementos da interface gráfica
    interface_grafica.iniciar()#Esta linha chama o método chamado
    #__name__  Esta é uma variável interna do Python que armazena o nome do módulo atual. Quando um script é executado diretamente, __name__ é definido como a string "__main__". Quando o script é importado como um módulo por outro script, __name__ é definido como o nome do módulo importado