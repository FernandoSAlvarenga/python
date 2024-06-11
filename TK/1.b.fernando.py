'''Exercício 1: Criando um Menu Principal e Submenus
• Crie uma janela principal com um título.
• Crie um menu principal e adicione um item principal.
• Crie submenus para o item principal, com opções como "Novo", "Abrir" e "Sair".
• Adicione comandos a cada opção de submenu para executar ações simples, como
imprimir uma mensagem no console.'''


import tkinter as tk
from tkinter import messagebox

def novo_arquivo():
    print("Novo arquivo selecionado.")

def abrir_arquivo():
    print("Abrir arquivo selecionado.")

def sair():
    print("Sair selecionado.")
    root.destroy()


root = tk.Tk()
root.title("Menu Principal e Submenus")

# menu principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# item principal no menu
item_principal = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=item_principal)

# submenus
item_principal.add_command(label="Novo", command=novo_arquivo)
item_principal.add_command(label="Abrir", command=abrir_arquivo)
item_principal.add_separator()
item_principal.add_command(label="Sair", command=sair)

# Loop principal da interface gráfica
root.mainloop()