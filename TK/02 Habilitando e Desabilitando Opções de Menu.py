import tkinter as tk  # Importa o módulo tkinter para criar a interface gráfica.

# Define a função para alternar o estado das opções de arquivo
def alternar_opcoes_arquivo():
   
    global esta_arquivo_aberto  # Declara que a variável `esta_arquivo_aberto` é global dentro da função.

    esta_arquivo_aberto = not esta_arquivo_aberto  # Inverte o valor atual da variável `esta_arquivo_aberto`.

    menu_arquivo.entryconfig("Novo", state=tk.NORMAL if esta_arquivo_aberto else tk.DISABLED)  # Configura o estado da opção "Novo" no menu "Arquivo":
                                                                                                   # - `tk.NORMAL` se `esta_arquivo_aberto` for True (ativa).
                                                                                                   # - `tk.DISABLED` se `esta_arquivo_aberto` for False (desativa).

    menu_arquivo.entryconfig("Abrir", state=tk.NORMAL if esta_arquivo_aberto else tk.DISABLED)  # Configura o estado da opção "Abrir" no menu "Arquivo":
                                                                                                    # - `tk.NORMAL` se `esta_arquivo_aberto` for True (ativa).
                                                                                                    # - `tk.DISABLED` se `esta_arquivo_aberto` for False (desativa).

# Cria a janela principal
janela_principal = tk.Tk()  # Cria uma instância da classe Tk, que representa a janela principal da aplicação.

# Define o título da janela principal
janela_principal.title("Menu Principal")  # Define o título da janela principal como "Menu Principal".

# Cria o menu principal
barra_de_menus = tk.Menu(janela_principal)  # Cria um objeto do tipo Menu que será usado como menu principal da janela.

# Configura a janela principal para usar o menu criado
janela_principal.config(menu=barra_de_menus)  # Configura a janela principal para utilizar o menu criado como seu menu principal.

# Variável global para controlar o estado das opções de arquivo
esta_arquivo_aberto = False  # Inicializa a variável global `esta_arquivo_aberto` com o valor False (opções desativadas).

# Cria o menu suspenso "Arquivo" e adiciona opções com comandos
menu_arquivo = tk.Menu(barra_de_menus, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Arquivo".
barra_de_menus.add_cascade(label="Arquivo", menu=menu_arquivo)  # Adiciona o menu "Arquivo" ao menu principal como um item suspenso.

# Adiciona a opção "Novo" ao menu "Arquivo" (desativada por padrão)
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo criado!"), state=tk.DISABLED)

# Adiciona a opção "Abrir" ao menu "Arquivo" (desativada por padrão)
menu_arquivo.add_command(label="Abrir", command=lambda: print("Abrindo arquivo..."), state=tk.DISABLED)

# Adiciona uma linha divisória ao menu "Arquivo"
menu_arquivo.add_separator()

# Adiciona a opção "Alternar Opções" ao menu "Arquivo"
menu_arquivo.add_command(label="Alternar Opções", command=alternar_opcoes_arquivo)

# Inicia o loop principal da interface gráfica
janela_principal.mainloop()  # Inicia o loop principal da interface gráfica, que fica à espera de eventos do usuário e atualiza a interface de acordo.