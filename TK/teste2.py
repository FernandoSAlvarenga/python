import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import datetime

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
            data DATETIME NOT NULL,
            tamanho VARCHAR(255),
            quantidade INT,
            valor_total DECIMAL(10,2) NOT NULL,
            cliente_id INT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_cliente VARCHAR(10) NOT NULL UNIQUE,
            nome VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            telefone VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')

    elo.commit()

def adicionar_cliente():
    id_cliente = entrada_id_cliente.get()
    nome = entrada_nome_cliente.get()
    endereco = entrada_endereco_cliente.get()
    telefone = entrada_telefone_cliente.get()
    email = entrada_email_cliente.get()

    if not id_cliente or not nome or not endereco or not telefone or not email:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos do cliente.")
        return

    try:
        cursor.execute("INSERT INTO clientes (id_cliente, nome, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s)",
                       (id_cliente, nome, endereco, telefone, email))
        elo.commit()
        messagebox.showinfo("Cliente Adicionado", "Novo cliente cadastrado com sucesso!")
    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao adicionar cliente: {err}")

def fazer_pedido():
    nome = entrada_nome.get()
    endereco = entrada_endereco.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()

    if not nome or not endereco or not telefone or not email:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos do cliente.")
        return

    cursor.execute("SELECT id, nome FROM clientes WHERE telefone = %s", (telefone,))
    cliente = cursor.fetchone()
    if cliente:
        cliente_id = cliente[0]
        cliente_nome = cliente[1]
    else:
        if messagebox.askyesno("Cliente Não Encontrado", "Cliente não encontrado. Deseja cadastrar um novo cliente?"):
            adicionar_cliente()
            return
        else:
            return

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
    total_pedido = total + total_ingredientes
    mensagem_sabores = ", ".join(sabores_selecionados)
    mensagem_ingredientes = ", ".join(ingredientes_selecionados)
    mensagem_pedido = f"Pedido realizado: {quantidade} pizza(s) {tamanho} com os sabores: {mensagem_sabores}.\n"
    mensagem_pedido += f"Ingredientes adicionais: {mensagem_ingredientes}.\n"
    mensagem_pedido += f"Total a pagar: R${(total_pedido):.2f}\n"
    mensagem_pedido += f"ID do Cliente: {cliente_id}\n"
    mensagem_pedido += f"Nome do Cliente: {cliente_nome}"

    if messagebox.askyesno("Confirmar Pedido", mensagem_pedido):
        messagebox.showinfo("Pedido Realizado", "Seu pedido foi confirmado!")
        cursor.execute("INSERT INTO pedidos (data, tamanho, quantidade, valor_total, cliente_id) VALUES (%s, %s, %s, %s, %s)",
                       (datetime.datetime.now(), tamanho, quantidade, total_pedido, cliente_id))
        elo.commit()


tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 17.00, "Média": 25.00, "Grande": 32.00}

sabores = [
    "Frango",
    "4 Queijos",
    "Iscas de Carne ao Alho e Óleo",
    "Brócolis com Queijo Cremoso"
]

ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 6.00, "Pepperoni": 7.00, "Bacon": 8.00}

janela = tk.Tk()
janela.title("Pedido de Pizza")

# Abas para Clientes e Pedidos
abas = ttk.Notebook(janela)
aba_clientes = ttk.Frame(abas)
aba_pedidos = ttk.Frame(abas)
abas.add(aba_clientes, text='Clientes')
abas.add(aba_pedidos, text='Pedidos')
abas.pack(expand=1, fill='both')

# Interface para Clientes
lbl_titulo_cliente = tk.Label(aba_clientes, text="Novo Cliente", font=("Helvetica", 16))
lbl_titulo_cliente.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

lbl_id_cliente = tk.Label(aba_clientes, text="ID do Cliente:")
lbl_id_cliente.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_id_cliente = tk.Entry(aba_clientes)
entrada_id_cliente.grid(row=1, column=1, padx=5, pady=5)

lbl_nome_cliente = tk.Label(aba_clientes, text="Nome:")
lbl_nome_cliente.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_nome_cliente = tk.Entry(aba_clientes)
entrada_nome_cliente.grid(row=2, column=1, padx=5, pady=5)

lbl_endereco_cliente = tk.Label(aba_clientes, text="Endereço:")
lbl_endereco_cliente.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entrada_endereco_cliente = tk.Entry(aba_clientes)
entrada_endereco_cliente.grid(row=3, column=1, padx=5, pady=5)

lbl_telefone_cliente = tk.Label(aba_clientes, text="Telefone:")
lbl_telefone_cliente.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entrada_telefone_cliente = tk.Entry(aba_clientes)
entrada_telefone_cliente.grid(row=4, column=1, padx=5, pady=5)

lbl_email_cliente = tk.Label(aba_clientes, text="Email:")
lbl_email_cliente.grid(row=5, column=0, padx=5, pady=5, sticky="w")
entrada_email_cliente = tk.Entry(aba_clientes)
entrada_email_cliente.grid(row=5, column=1, padx=5, pady=5)

botao_adicionar_cliente = tk.Button(aba_clientes, text="Adicionar Cliente", command=adicionar_cliente)
botao_adicionar_cliente.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Interface para Pedidos
lbl_titulo_pedido = tk.Label(aba_pedidos, text="Dados do Cliente", font=("Helvetica", 16))
lbl_titulo_pedido.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

lbl_nome = tk.Label(aba_pedidos, text="Nome:")
lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_nome = tk.Entry(aba_pedidos)
entrada_nome.grid(row=1, column=1, padx=5, pady=5)

lbl_endereco = tk.Label(aba_pedidos, text="Endereço:")
lbl_endereco.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_endereco = tk.Entry(aba_pedidos)
entrada_endereco.grid(row=2, column=1, padx=5, pady=5)

lbl_telefone = tk.Label(aba_pedidos, text="Telefone:")
lbl_telefone.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entrada_telefone = tk.Entry(aba_pedidos)
entrada_telefone.grid(row=3, column=1, padx=5, pady=5)

lbl_email = tk.Label(aba_pedidos, text="Email:")
lbl_email.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entrada_email = tk.Entry(aba_pedidos)
entrada_email.grid(row=4, column=1, padx=5, pady=5)

lbl_titulo_pizza = tk.Label(aba_pedidos, text="Escolha a sua Pizza", font=("Helvetica", 16))
lbl_titulo_pizza.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

lbl_precos = tk.Label(aba_pedidos, text=f"Pequena: R${precos['Pequena']:.2f}\nMédia: R${precos['Média']:.2f}\nGrande: R${precos['Grande']:.2f}")
lbl_precos.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

lbl_tamanho = tk.Label(aba_pedidos, text="Tamanho da Pizza:")
lbl_tamanho.grid(row=7, column=0, padx=5, pady=5)
var_tamanho = tk.StringVar(aba_pedidos)
var_tamanho.set(tamanhos[0])
menu_tamanho = tk.OptionMenu(aba_pedidos, var_tamanho, *tamanhos)
menu_tamanho.grid(row=7, column=1, padx=5, pady=5)

lbl_sabores = tk.Label(aba_pedidos, text="Sabores:")
lbl_sabores.grid(row=8, column=0, padx=5, pady=5, sticky="w")

sabores_vars = []
for i, sabor in enumerate(sabores):
    var_sabor = tk.IntVar(aba_pedidos)
    cb_sabor = tk.Checkbutton(aba_pedidos, text=sabor, variable=var_sabor)
    cb_sabor.grid(row=9 + i, column=0, padx=5, pady=2, sticky="w")
    sabores_vars.append(var_sabor)

lbl_ingredientes = tk.Label(aba_pedidos, text="Ingredientes Adicionais:")
lbl_ingredientes.grid(row=9 + len(sabores), column=0, padx=5, pady=5, sticky="w")

ingredientes_vars = []
for i, ingrediente in enumerate(ingredientes):
    var_ingrediente = tk.IntVar(aba_pedidos)
    cb_ingrediente = tk.Checkbutton(aba_pedidos, text=ingrediente, variable=var_ingrediente)
    cb_ingrediente.grid(row=10 + len(sabores) + i, column=0, padx=5, pady=2, sticky="w")
    ingredientes_vars.append(var_ingrediente)

lbl_quantidade = tk.Label(aba_pedidos, text="Quantidade de Pizzas:")
lbl_quantidade.grid(row=10 + len(sabores) + len(ingredientes), column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(aba_pedidos)
entrada_quantidade.grid(row=10 + len(sabores) + len(ingredientes), column=1, padx=5, pady=5)

botao_pedido = tk.Button(aba_pedidos, text="Pedir", command=fazer_pedido)
botao_pedido.grid(row=11 + len(sabores) + len(ingredientes), column=0, columnspan=2, padx=5, pady=5)

janela.mainloop()