'''2. Seleção de Tamanho de Camiseta: 
Desenvolva um programa que ofereça um menu com opções de tamanho de camisetas (P, 
M, G, GG). Permita que o usuário escolha seu tamanho e exiba uma mensagem 
confirmando a seleção. '''

import tkinter as tk
from tkinter import messagebox


def escolher_tamanho():
    tamanho = variavel.get()
    if tamanho in ['P', 'M', 'G', 'GG']:
        mensagem = f"Você selecionou o tamanho: {tamanho}"
        messagebox.showinfo("Tamanho Selecionado", mensagem)
    else:
        messagebox.showerror("Erro", "Escolha inválida. Por favor, selecione um tamanho.")


janela = tk.Tk()
janela.title("Seleção de Tamanho de Camiseta")


variavel = tk.StringVar()


rb_p = tk.Radiobutton(janela, text="P", variable=variavel, value='P')
rb_m = tk.Radiobutton(janela, text="M", variable=variavel, value='M')
rb_g = tk.Radiobutton(janela, text="G", variable=variavel, value='G')
rb_gg = tk.Radiobutton(janela, text="GG", variable=variavel, value='GG')


rb_p.pack(anchor='w')
rb_m.pack(anchor='w')
rb_g.pack(anchor='w')
rb_gg.pack(anchor='w')


botao = tk.Button(janela, text="Confirmar", command=escolher_tamanho)
botao.pack()


janela.mainloop()