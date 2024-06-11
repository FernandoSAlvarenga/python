# 1: Criando um Menu Principal e Submenus
# Crie uma janela principal com um título.
# Crie um menu principal e adicione um item principal.
# Crie submenus para o item principal, com opções como "Novo", "Abrir" e "Sair".
# Adicione comandos a cada opção de submenu para executar ações simples, como imprimir uma mensagem no consolse. 

import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica.

# Cria a janela principal
janela_principal = tk.Tk()  # Cria uma instância da classe Tk, que representa a janela principal da aplicação.

# Define o título da janela principal
janela_principal.title("Menu Principal")  # Define o título da janela principal como "Menu Principal".

# Cria o menu principal
barra_de_menus = tk.Menu(janela_principal)  # Cria um objeto do tipo Menu que será usado como menu principal da janela.

# Configura a janela principal para usar o menu criado
janela_principal.config(menu=barra_de_menus)  # Configura a janela principal para utilizar o menu criado como seu menu principal.

# Cria um menu suspenso com o rótulo "Arquivo"
menu_arquivo = tk.Menu(barra_de_menus, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Arquivo" e define a opção `tearoff` como 0 (não destacável).

# Adiciona o menu "Arquivo" ao menu principal
barra_de_menus.add_cascade(label="Arquivo", menu=menu_arquivo)  # Adiciona o menu "Arquivo" ao menu principal como um item suspenso.

# Adiciona uma opção "Novo" ao menu "Arquivo"
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo criado!"))  # Adiciona uma opção "Novo" ao menu "Arquivo" que, quando clicada, imprime "Novo arquivo criado!" no console.

# Adiciona uma opção "Abrir" ao menu "Arquivo"
menu_arquivo.add_command(label="Abrir", command=lambda: print("Abrindo arquivo..."))  # Adiciona uma opção "Abrir" ao menu "Arquivo" que, quando clicada, imprime "Abrindo arquivo..." no console.

# Adiciona uma linha divisória ao menu "Arquivo"
menu_arquivo.add_separator()  # Adiciona uma linha divisória ao menu "Arquivo" para separar as opções "Novo" e "Abrir" da opção "Sair".

# Adiciona uma opção "Sair" ao menu "Arquivo"
menu_arquivo.add_command(label="Sair", command=janela_principal.quit)  # Adiciona uma opção "Sair" ao menu "Arquivo" que, quando clicada, chama o método `quit()` da janela principal para fechar a aplicação.

# Inicia o loop principal da interface gráfica
janela_principal.mainloop()  # Inicia o loop principal da interface gráfica, que fica à espera de eventos do usuário e atualiza a interface de acordo.