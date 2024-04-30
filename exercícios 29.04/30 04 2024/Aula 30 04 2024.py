import tkinter as tk


class InterfaceGrafica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Introdução Tkinter")

        # Rótulo e botão para fechar a janela
        self.rotulo_titulo = tk.Label(self.root, text="O Inicio")
        self.rotulo_titulo.pack()

        # Botão para abrir nova janela
        self.botao1 = tk.Button(self.root, text="1. A Criação da Janela Principal", command=lambda: self.abrir_topico("Criação da Janela Principal"))
        self.botao1.pack()
        self.botao2 = tk.Button(self.root, text="2. Widgets: Blocos de Construção", command=lambda: self.abrir_topico("Widgets: Blocos de Construção"))
        self.botao2.pack()
       
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
                
                def exemplo_Menus():
                    def abrir_arquivo():
                        print("Abrindo um arquivo...")

                    def salvar_arquivo():
                        print("Salvando um arquivo...")

                    def sair_aplicacao():
                        print("Saindo da aplicação...")

                    # Criar a janela principal
                    janela = tk.Tk()
                    janela.title("Exemplo de Menu")

                    # Criar a barra de menus
                    barra_menus = tk.Menu(janela)

                    # Criar o menu Arquivo
                    menu_arquivo = tk.Menu(barra_menus, tearoff=0)
                    menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
                    menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
                    menu_arquivo.add_separator()
                    menu_arquivo.add_command(label="Sair", command=sair_aplicacao)

                    barra_menus.add_cascade(label="Arquivo", menu=menu_arquivo)

                    # Adicione mais menus (Editar, Ajuda, etc.) seguindo a mesma estrutura

                    # Configurar a barra de menus
                    janela.config(menu=barra_menus)

                    # Iniciar o loop principal do evento
                    


                self.botao2 = tk.Button(nova_janela, text="Exemplo de Menus", command=exemplo_Menus)
                self.botao2.pack()

            def OptionMenu():
                nova_janela = tk.Toplevel(self.root)
                nova_janela.title('OptionMenu')
                conteudo_label = tk.Label(nova_janela, text="OptionMenu: cria menus suspensos que permitem ao usuário selecionar uma opção dentre uma lista predefinida",font=("Arial", 10, "bold"))
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