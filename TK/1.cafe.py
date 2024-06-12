'''1. Escolha de Café: 
Crie um programa que apresente um menu com opções de café (expresso, cappuccino, latte 
macchiato) e permita ao usuário selecionar sua bebida preferida. Exiba uma mensagem 
informando a escolha do usuário'''
import tkinter as tk
from tkinter import messagebox

# Função chamada quando o botão é clicado
def escolher_cafe():
    escolha = variavel.get()
    if escolha == 1:
        messagebox.showinfo("Escolha", "Você escolheu Expresso!")
    elif escolha == 2:
        messagebox.showinfo("Escolha", "Você escolheu Cappuccino!")
    elif escolha == 3:
        messagebox.showinfo("Escolha", "Você escolheu Latte Macchiato!")
    else:
        messagebox.showerror("Erro", "Escolha inválida. Por favor, selecione uma opção.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Escolha seu Café")

# Variável para armazenar a escolha do usuário
variavel = tk.IntVar()

# Criando os botões de opção
rb_expresso = tk.Radiobutton(janela, text="Expresso", variable=variavel, value=1)
rb_cappuccino = tk.Radiobutton(janela, text="Cappuccino", variable=variavel, value=2)
rb_latte = tk.Radiobutton(janela, text="Latte Macchiato", variable=variavel, value=3)

# Posicionando os botões de opção
rb_expresso.pack(anchor='w')
rb_cappuccino.pack(anchor='w')
rb_latte.pack(anchor='w')

# Criando o botão de confirmação
botao = tk.Button(janela, text="Escolher", command=escolher_cafe)
botao.pack()

# Iniciando o loop da interface gráfica
janela.mainloop()