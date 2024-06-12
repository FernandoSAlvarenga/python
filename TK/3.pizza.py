import tkinter as tk
from tkinter import messagebox

def fazer_pedido():
    tamanho = var_tamanho.get()
    quantidade = int(entrada_quantidade.get())
    num_sabores = var_sabores.get()

    if tamanho == "Pequena" and num_sabores != 1:
        messagebox.showerror("Erro", "Pizza pequena só pode ter 1 sabor.")
        return
    elif tamanho == "Média" and num_sabores not in [1, 2]:
        messagebox.showerror("Erro", "Pizza média só pode ter 1 ou 2 sabores.")
        return

    mensagem = f"Pedido realizado: {quantidade} pizza(s) {tamanho} com {num_sabores} sabor(es)."
    messagebox.showinfo("Pedido Realizado", mensagem)

janela = tk.Tk()
janela.title("Pedido de Pizza")

lbl_tamanho = tk.Label(janela, text="Tamanho da Pizza:")
lbl_tamanho.grid(row=0, column=0, padx=5, pady=5)
opcoes_tamanho = ["Pequena", "Média", "Grande"]
var_tamanho = tk.StringVar(janela)
var_tamanho.set(opcoes_tamanho[0])
menu_tamanho = tk.OptionMenu(janela, var_tamanho, *opcoes_tamanho)
menu_tamanho.grid(row=0, column=1, padx=5, pady=5)

lbl_quantidade = tk.Label(janela, text="Quantidade de Pizzas:")
lbl_quantidade.grid(row=1, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=1, column=1, padx=5, pady=5)

lbl_sabores = tk.Label(janela, text="Número de Sabores:")
lbl_sabores.grid(row=2, column=0, padx=5, pady=5)
var_sabores = tk.IntVar(janela)
var_sabores.set(1) 
rb_1_sabor = tk.Radiobutton(janela, text="1", variable=var_sabores, value=1)
rb_2_sabores = tk.Radiobutton(janela, text="2", variable=var_sabores, value=2)
rb_4_sabores = tk.Radiobutton(janela, text="4", variable=var_sabores, value=4)
rb_1_sabor.grid(row=2, column=1, padx=5, pady=5, sticky="w")
rb_2_sabores.grid(row=2, column=1, padx=5, pady=5)
rb_4_sabores.grid(row=2, column=1, padx=5, pady=5, sticky="e")

botao_pedido = tk.Button(janela, text="Pedir", command=fazer_pedido)
botao_pedido.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()