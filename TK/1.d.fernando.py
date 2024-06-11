'''Exercício 3: Criando Menus Hierárquicos com Submenus em Cascata
• Crie um menu principal com submenus para "Arquivo", "Editar" e "Ajuda".
• Crie submenus em cascata para cada item principal, com opções como "Novo",
"Abrir", "Desfazer", "Copiar", "Conteúdo" e "Sobre".
• Adicione comandos a cada opção de submenu para executar ações simples, como
imprimir uma mensagem no console'''


import tkinter as tk

def novo_arquivo():
    print("Novo arquivo selecionado.")

def abrir_arquivo():
    print("Abrir arquivo selecionado.")

def desfazer():
    print("Desfazer ação selecionada.")

def copiar():
    print("Copiar ação selecionada.")

def conteudo_ajuda():
    print("Conteúdo da ajuda selecionado.")

def sobre():
    print("Sobre selecionado.")

def sair():
    print("Sair selecionado.")
    root.destroy()

# janela principal
root = tk.Tk()
root.title("Menus Hierárquicos com Submenus em Cascata")

# menu principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# submenu "Arquivo"
menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)

# submenu "Editar"
menu_editar = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Desfazer", command=desfazer)
menu_editar.add_command(label="Copiar", command=copiar)

# submenu "Ajuda"
menu_ajuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Conteúdo", command=conteudo_ajuda)
menu_ajuda.add_command(label="Sobre", command=sobre)

# Loop principal da interface gráfica
root.mainloop()