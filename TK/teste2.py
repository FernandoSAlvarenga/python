import tkinter as tk
from tkinter import messagebox
import mysql.connector



# Conectar ao MySQL
elo = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='pizzadofe'
)

# Verificar se o banco de dados existe
cursor = elo.cursor()
cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "pizzadofe";')
num_results = cursor.fetchone()[0]

# Se o banco de dados não existe, criá-lo
if num_results == 0:
    cursor.execute('CREATE DATABASE pizzadofe;')
    elo.commit()

    # Reconectar especificando o banco de dados recém-criado
    elo = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='pizzadofe'
    )
    cursor = elo.cursor()

    # Criar tabelas
    cursor.execute('''
        CREATE TABLE pedidos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data DATE NOT NULL,
            tamanho VARCHAR(255),
            quantidade INT,
            valor_total DECIMAL(10,2) NOT NULL
        )
    ''')
    #Criar contatos
    cursor.execute('''
        CREATE TABLE clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            telefone VARCHAR(20) NOT NULL
        )
    ''')

    elo.commit()

def fazer_pedido():
    tamanho = var_tamanho.get()
    
    try:
        quantidade = int(entrada_quantidade.get())
        if quantidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de pizzas.")
        return

    sabores_selecionados = []
    for i, sabor_var in enumerate(sabores_vars):
        if sabor_var.get() == 1:
            sabores_selecionados.append(sabores[i])

    if tamanho == "Pequena" and len(sabores_selecionados) != 1:
        messagebox.showerror("Erro", "Pizza pequena só pode ter 1 sabor.")
        return
    elif tamanho == "Média" and len(sabores_selecionados) > 2:
        messagebox.showerror("Erro", "Pizza média só pode ter até 2 sabores.")
        return
    elif tamanho == "Grande" and len(sabores_selecionados) > 4:
        messagebox.showerror("Erro", "Pizza grande só pode ter até 4 sabores.")
        return

    ingredientes_selecionados = []
    for i, ing_var in enumerate(ingredientes_vars):
        if ing_var.get() == 1:
            ingredientes_selecionados.append(ingredientes[i])

    total = precos[tamanho] * quantidade
    total_ingredientes = sum(precos_ingredientes[ing] for ing in ingredientes_selecionados) * quantidade

    mensagem_sabores = ", ".join(sabores_selecionados)
    mensagem_ingredientes = ", ".join(ingredientes_selecionados)
    mensagem_pedido = f"Pedido realizado: {quantidade} pizza(s) {tamanho} com os sabores: {mensagem_sabores}.\n"
    mensagem_pedido += f"Ingredientes adicionais: {mensagem_ingredientes}.\n"
    mensagem_pedido += f"Total a pagar: R${(total + total_ingredientes):.2f}"
    
    if messagebox.askyesno("Confirmar Pedido", mensagem_pedido):
        messagebox.showinfo("Pedido Realizado", "Seu pedido foi confirmado!")

tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 17.00, "Média": 25.00, "Grande": 32.00}

sabores = [
    "Frango",
    "4 Queijos",
    "Iscas de Carne ao Alho e Óleo",
    "Brócolis com Queijo Cremoso"
]

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

lbl_sabores = tk.Label(janela, text="Sabores:")
lbl_sabores.grid(row=3, column=0, padx=5, pady=5, sticky="w")

sabores_vars = []
for i, sabor in enumerate(sabores):
    var_sabor = tk.IntVar(janela)
    cb_sabor = tk.Checkbutton(janela, text=sabor, variable=var_sabor)
    cb_sabor.grid(row=4 + i, column=0, padx=5, pady=2, sticky="w")
    sabores_vars.append(var_sabor)

lbl_ingredientes = tk.Label(janela, text="Ingredientes Adicionais:")
lbl_ingredientes.grid(row=4 + len(sabores), column=0, padx=5, pady=5, sticky="w")

ingredientes_vars = []
for i, ingrediente in enumerate(ingredientes):
    var_ingrediente = tk.IntVar(janela)
    cb_ingrediente = tk.Checkbutton(janela, text=ingrediente, variable=var_ingrediente)
    cb_ingrediente.grid(row=5 + len(sabores) + i, column=0, padx=5, pady=2, sticky="w")
    ingredientes_vars.append(var_ingrediente)

lbl_quantidade = tk.Label(janela, text="Quantidade de Pizzas:")
lbl_quantidade.grid(row=5 + len(sabores) + len(ingredientes), column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(janela)
entrada_quantidade.grid(row=5 + len(sabores) + len(ingredientes), column=1, padx=5, pady=5)

botao_pedido = tk.Button(janela, text="Pedir", command=fazer_pedido)
botao_pedido.grid(row=6 + len(sabores) + len(ingredientes), column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()