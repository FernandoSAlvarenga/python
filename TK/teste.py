import tkinter as tk
from tkinter import messagebox

def fazer_pedido():
    tamanho = var_tamanho.get()
    try:
        quantidade = int(entrada_quantidade.get())
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de pizzas.")
        return

    num_sabores = var_sabores.get()
    if tamanho == "Pequena" and num_sabores != 1:
        messagebox.showerror("Erro", "Pizza pequena só pode ter 1 sabor.")
        return
    elif tamanho == "Média" and num_sabores not in [1, 2]:
        messagebox.showerror("Erro", "Pizza média só pode ter 1 ou 2 sabores.")
        return
    elif tamanho == "Grande" and num_sabores not in [1, 2, 4]:
        messagebox.showerror("Erro", "Pizza grande só pode ter 1, 2 ou 4 sabores.")
        return

    total_pizzas = quantidade
    total = precos[tamanho] * total_pizzas

    itens_cobrados = f"Descrição do Pedido:\n\n"
    itens_cobrados += f"Tamanho: {tamanho}\n"
    itens_cobrados += f"Quantidade: {quantidade}\n"
    itens_cobrados += f"Sabores: {num_sabores}\n"

    ingredientes_selecionados = []
    for ing in ingredientes:
        if ingredientes_vars[ing].get() == 1:
            ingredientes_selecionados.append(ing)
    
    if ingredientes_selecionados:
        itens_cobrados += "Ingredientes Adicionais:\n"
        for ing in ingredientes_selecionados:
            preco_por_ingrediente = precos_ingredientes[ing]
            total_ingrediente = preco_por_ingrediente * total_pizzas
            itens_cobrados += f"- {ing}: R${preco_por_ingrediente:.2f} x {total_pizzas} = R${total_ingrediente:.2f}\n"
            total += total_ingrediente
    
    itens_cobrados += f"\nTotal a pagar: R${total:.2f}"

    mensagem_pedido = f"Pedido realizado: {quantidade} pizza(s) {tamanho} com {num_sabores} sabor(es).\n\n{itens_cobrados}"
    if messagebox.askyesno("Confirmar Pedido", mensagem_pedido):
        messagebox.showinfo("Pedido Realizado", "Seu pedido foi confirmado!")

tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 17.00, "Média": 25.00, "Grande": 32.00}

ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 6.00, "Pepperoni": 9.00, "Bacon": 7.00}

janela = tk.Tk()
janela.title("Pedido de Pizza")

lbl_titulo = tk.Label(janela, text="Escolha o Tamanho da Pizza", font=("Helvetica", 16))
lbl_titulo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

lbl_precos = tk.Label(janela, text=f"Pequena: R${precos['Pequena']:.2f}\nMédia: R${precos['Média']:.2f}\nGrande: R${precos['Grande']:.2f}")
lbl_precos.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lbl_tamanho = tk.Label(janela, text="Tamanho da Pizza:")
lbl_tamanho.grid(row=2, column=0, padx=5, pady=5)
var_tamanho = tk.StringVar(janela)
var_tamanho.set(tamanhos[0])
menu_tamanho = tk.OptionMenu(janela, var_tamanho, *tamanhos)
menu_tamanho.grid(row=2, column=1, padx=5, pady=5)

lbl_quantidade = tk.Label(janela, text="Quantidade de Pizzas:")
lbl_quantidade.grid(row=3, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=3, column=1, padx=5, pady=5)

lbl_sabores = tk.Label(janela, text="Número de Sabores:")
lbl_sabores.grid(row=4, column=0, padx=5, pady=5)
var_sabores = tk.IntVar(janela)
var_sabores.set(1)
rb_1_sabor = tk.Radiobutton(janela, text="1", variable=var_sabores, value=1)
rb_2_sabores = tk.Radiobutton(janela, text="2", variable=var_sabores, value=2)
rb_4_sabores = tk.Radiobutton(janela, text="4", variable=var_sabores, value=4)
rb_1_sabor.grid(row=4, column=1, padx=5, pady=5, sticky="w")
rb_2_sabores.grid(row=4, column=1, padx=5, pady=5)
rb_4_sabores.grid(row=4, column=1, padx=5, pady=5, sticky="e")

lbl_ingredientes = tk.Label(janela, text="Ingredientes Adicionais:")
lbl_ingredientes.grid(row=5, column=0, padx=5, pady=5)

ingredientes_vars = {}
precos_ingredientes_lbls = {}
for i, ing in enumerate(ingredientes):
    ingredientes_vars[ing] = tk.IntVar()
    ingredientes_cb = tk.Checkbutton(janela, text=ing, variable=ingredientes_vars[ing])
    ingredientes_cb.grid(row=6 + i, column=0, padx=5, pady=5, sticky="w")
    
    preco_lbl = tk.Label(janela, text=f"R${precos_ingredientes[ing]:.2f}")
    preco_lbl.grid(row=6 + i, column=1, padx=5, pady=5)

botao_pedido = tk.Button(janela, text="Pedir", command=fazer_pedido)
botao_pedido.grid(row=6 + len(ingredientes), column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()