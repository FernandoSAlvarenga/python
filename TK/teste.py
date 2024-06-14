import tkinter as tk
from tkinter import messagebox

class PizzaOrderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pedido de Pizza")
        self.geometry("400x300")

        # Dados da Pizza
        self.tamanhos = ["Pequena", "Média", "Grande"]
        self.precos = {"Pequena": 15.00, "Média": 22.00, "Grande": 28.00}
        self.ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
        self.precos_ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}

        # Widgets
        tk.Label(self, text="Escolha o Tamanho da Pizza").pack()
        self.tamanho_var = tk.StringVar(self)
        self.tamanho_var.set(self.tamanhos[0])  # Padrão: Pequena
        tk.OptionMenu(self, self.tamanho_var, *self.tamanhos).pack()

        tk.Label(self, text="Quantidade de Pizzas").pack()
        self.quantidade_entry = tk.Entry(self)
        self.quantidade_entry.pack()

        tk.Label(self, text="Escolha os Ingredientes Adicionais").pack()
        self.ingredientes_vars = {}
        for ingrediente in self.ingredientes:
            self.ingredientes_vars[ingrediente] = tk.IntVar()
            tk.Checkbutton(self, text=ingrediente, variable=self.ingredientes_vars[ingrediente]).pack()

        tk.Button(self, text="Pedir", command=self.fazer_pedido).pack()

        self.total_label = tk.Label(self, text="")
        self.total_label.pack()

    def fazer_pedido(self):
        quantidade = self.quantidade_entry.get()
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma quantidade válida de pizzas.")
            return

        tamanho = self.tamanho_var.get()
        preco_pizza = self.precos[tamanho]
        preco_total = quantidade * preco_pizza

        ingredientes_total = 0
        for ingrediente, var in self.ingredientes_vars.items():
            if var.get():
                ingredientes_total += self.precos_ingredientes[ingrediente]

        preco_total += ingredientes_total

        messagebox.showinfo("Pedido Confirmado", f"Total a pagar: R${preco_total:.2f}")

if __name__ == "__main__":
    app = PizzaOrderApp()
    app.mainloop()