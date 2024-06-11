import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica.

# Cria a janela principal
janela_principal = tk.Tk()  # Cria uma instância da classe Tk, que representa a janela principal da aplicação.
janela_principal.title("Menu Principal")  # Define o título da janela principal como "Menu Principal".

# Cria o menu principal
barra_de_menus = tk.Menu(janela_principal)  # Cria um objeto do tipo Menu que será usado como menu principal da janela.
janela_principal.config(menu=barra_de_menus)  # Configura a janela principal para utilizar o menu criado como seu menu principal.

# Cria submenus em cascata
menu_arquivo = tk.Menu(barra_de_menus, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Arquivo" e define a opção `tearoff` como 0 (não destacável).
barra_de_menus.add_cascade(label="Arquivo", menu=menu_arquivo)  # Adiciona o menu "Arquivo" ao menu principal como um item suspenso.

menu_editar = tk.Menu(barra_de_menus, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Editar" e define a opção `tearoff` como 0 (não destacável).
barra_de_menus.add_cascade(label="Editar", menu=menu_editar)  # Adiciona o menu "Editar" ao menu principal como um item suspenso.

menu_ajuda = tk.Menu(barra_de_menus, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Ajuda" e define a opção `tearoff` como 0 (não destacável).
barra_de_menus.add_cascade(label="Ajuda", menu=menu_ajuda)  # Adiciona o menu "Ajuda" ao menu principal como um item suspenso.

# Adiciona opções aos submenus
# Submenu "Arquivo":
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo criado!"))  # Adiciona a opção "Novo" ao menu "Arquivo" que, quando clicada, imprime "Novo arquivo criado!" no console.
menu_arquivo.add_command(label="Abrir", command=lambda: print("Abrindo arquivo..."))  # Adiciona a opção "Abrir" ao menu "Arquivo" que, quando clicada, imprime "Abrindo arquivo..." no console.
menu_arquivo.add_separator()  # Adiciona uma linha divisória ao menu "Arquivo" para separar as opções "Novo" e "Abrir" da opção "Sair".
menu_arquivo.add_command(label="Sair", command=janela_principal.quit)  # Adiciona a opção "Sair" ao menu "Arquivo" que, quando clicada, chama o método `quit()` da janela principal para fechar a aplicação.

# Submenu "Editar":
menu_editar.add_command(label="Desfazer", command=lambda: print("Desfazendo ação..."))  # Adiciona a opção "Desfazer" ao menu "Editar" que, quando clicada, imprime "Desfazendo ação..." no console.
menu_editar.add_command(label="Refazer", command=lambda: print("Refazendo ação..."))  # Adiciona a opção "Refazer" ao menu "Editar" que, quando clicada, imprime "Refazendo ação..." no console.
menu_editar.add_separator()  # Adiciona uma linha divisória ao menu "Editar" para separar as opções "Desfazer" e "Refazer" das opções "Copiar" e "Colar".
menu_editar.add_command(label="Copiar", command=lambda: print("Copiando seleção..."))  # Adiciona a opção "Copiar" ao menu "Editar" que, quando clicada, imprime "Copiando seleção..." no console.
menu_editar.add_command(label="Colar", command=lambda: print("Colando conteúdo..."))  # Adiciona a opção "Colar" ao menu "Editar" que, quando clicada, imprime "Colando conteúdo..." no console.

menu_ajuda.add_command(label="Conteúdo", command=lambda: print("Abrindo conteúdo de ajuda"))
menu_ajuda.add_command(label="Sobre", command=lambda: print("Sobre o aplicativo..."))

# Inicia o loop principal da interface
janela_principal.mainloop()