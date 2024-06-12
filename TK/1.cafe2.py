'''1. Escolha de Café: 
Crie um programa que apresente um menu com opções de café (expresso, cappuccino, latte 
macchiato) e permita ao usuário selecionar sua bebida preferida. Exiba uma mensagem 
informando a escolha do usuário '''
import tkinter as tk
from tkinter import messagebox


def mostrar_desenho_cafe(escolha):
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Café Selecionado")


    
    cafe = ""
    if escolha == 1:
        cafe = "Expresso"
    elif escolha == 2:
        cafe = "Cappuccino"
    elif escolha == 3:
        cafe = "Latte Macchiato"

    mensagem = f"Você selecionou o café: {cafe}"
    label = tk.Label(nova_janela, text=mensagem)
    label.pack()


    def preparar_cafe():
        messagebox.showinfo("Preparando", f"Preparando seu {cafe}...")


    botao_preparar = tk.Button(nova_janela, text="Preparar", command=preparar_cafe)
    botao_preparar.pack()


def escolher_cafe():
    escolha = variavel.get()
    if escolha in [1, 2, 3]:
        mostrar_desenho_cafe(escolha)
    else:
        messagebox.showerror("Erro", "Escolha inválida. Por favor, selecione uma opção.")


janela = tk.Tk()
janela.title("Escolha seu Café")


variavel = tk.IntVar()


rb_expresso = tk.Radiobutton(janela, text="Expresso", variable=variavel, value=1)
rb_cappuccino = tk.Radiobutton(janela, text="Cappuccino", variable=variavel, value=2)
rb_latte = tk.Radiobutton(janela, text="Latte Macchiato", variable=variavel, value=3)


rb_expresso.pack(anchor='w')
rb_cappuccino.pack(anchor='w')
rb_latte.pack(anchor='w')


botao = tk.Button(janela, text="Escolher", command=escolher_cafe)
botao.pack()


janela.mainloop()