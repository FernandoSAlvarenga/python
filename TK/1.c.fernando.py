'''Exercício 2: Habilitando e Desabilitando Opções de Menu
• Crie um menu principal com submenus para "Novo" e "Abrir".
• Crie uma variável para controlar o estado das opções (ativadas ou desativadas).
• Adicione um item ao menu para alternar o estado das opções.
• Utilize o estado da variável para ativar ou desativar as opções de "Novo" e "Abrir"
dinamicamente.'''


import tkinter as tk
from tkinter import messagebox

def novo_arquivo():
    print("Novo arquivo selecionado.")

def abrir_arquivo():
    print("Abrir arquivo selecionado.")

def sair():
    print("Sair selecionado.")
    root.destroy()

def alternar_estado():
    global opcoes_ativadas
    opcoes_ativadas = not opcoes_ativadas
    
    estado = tk.NORMAL if opcoes_ativadas else tk.DISABLED
    item_principal.entryconfig("Novo", state=estado)
    item_principal.entryconfig("Abrir", state=estado)

    estado_texto = "Desativar Opções" if opcoes_ativadas else "Ativar Opções"
    menu_ativar_desativar.entryconfig(0, label=estado_texto)

#  janela principal
root = tk.Tk()
root.title("Menu Principal e Submenus")

# Variável para controlar o estado das opções
opcoes_ativadas = True

#  menu principal
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

#  item principal no menu
item_principal = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=item_principal)

# s submenus
item_principal.add_command(label="Novo", command=novo_arquivo)
item_principal.add_command(label="Abrir", command=abrir_arquivo)
item_principal.add_separator()
item_principal.add_command(label="Sair", command=sair)

# menu para alternar estado das opções
menu_ativar_desativar = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opções", menu=menu_ativar_desativar)
menu_ativar_desativar.add_command(label="Desativar Opções", command=alternar_estado)

# Loop principal da interface gráfica
root.mainloop()
