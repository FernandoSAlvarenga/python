import tkinter as tk
from tkinter import messagebox
import mysql.connector
import datetime

# Conectar ao MySQL
elo = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # Coloque a senha do seu MySQL se configurado
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
        host='localhost',
        user='root',
        password='',  # Coloque a senha do seu MySQL se configurado
        database='pizzadofe'
    )
    cursor = elo.cursor()

    # Criar tabelas
    cursor.execute('''
        CREATE TABLE pedidos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            numero_pedido INT UNIQUE,
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
            numero_cliente INT UNIQUE,
            nome VARCHAR(255) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            data_nascimento DATE NOT NULL,
            telefone VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL,
            endereco VARCHAR(255) NOT NULL
        )
    ''')

    elo.commit()

def criar_tela_clientes():
    tela_clientes = tk.Toplevel(janela)
    tela_clientes.title("Clientes")

    def adicionar_cliente():
        nome = entrada_nome.get()
        sobrenome = entrada_sobrenome.get()
        data_nascimento = entrada_data_nascimento.get()
        telefone = entrada_telefone.get()
        email = entrada_email.get()
        endereco = entrada_endereco.get()

        if not nome or not sobrenome or not data_nascimento or not telefone or not email or not endereco:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos do cliente.")
            return

        try:
            # Pegar o próximo número de cliente disponível
            cursor.execute("SELECT MAX(numero_cliente) FROM clientes")
            max_numero_cliente = cursor.fetchone()[0]
            if max_numero_cliente is None:
                max_numero_cliente = 0
            numero_cliente = max_numero_cliente + 1

            # Mostra o número do cliente ao usuário
            messagebox.showinfo("Número do Cliente", f"Número do Cliente: {numero_cliente}")

            cursor.execute("INSERT INTO clientes (numero_cliente, nome, sobrenome, data_nascimento, telefone, email, endereco) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (numero_cliente, nome, sobrenome, data_nascimento, telefone, email, endereco))
            elo.commit()
            messagebox.showinfo("Cliente Adicionado", "Novo cliente cadastrado com sucesso!")
            tela_clientes.destroy()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao adicionar cliente: {err}")

    lbl_titulo_cliente = tk.Label(tela_clientes, text="Novo Cliente", font=("Helvetica", 16))
    lbl_titulo_cliente.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    lbl_nome = tk.Label(tela_clientes, text="Nome:")
    lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entrada_nome = tk.Entry(tela_clientes)
    entrada_nome.grid(row=1, column=1, padx=5, pady=5)

    lbl_sobrenome = tk.Label(tela_clientes, text="Sobrenome:")
    lbl_sobrenome.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entrada_sobrenome = tk.Entry(tela_clientes)
    entrada_sobrenome.grid(row=2, column=1, padx=5, pady=5)

    lbl_data_nascimento = tk.Label(tela_clientes, text="Data de Nascimento (AAAA-MM-DD):")
    lbl_data_nascimento.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entrada_data_nascimento = tk.Entry(tela_clientes)
    entrada_data_nascimento.grid(row=3, column=1, padx=5, pady=5)

    lbl_telefone = tk.Label(tela_clientes, text="Telefone:")
    lbl_telefone.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    entrada_telefone = tk.Entry(tela_clientes)
    entrada_telefone.grid(row=4, column=1, padx=5, pady=5)

    lbl_email = tk.Label(tela_clientes, text="Email:")
    lbl_email.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    entrada_email = tk.Entry(tela_clientes)
    entrada_email.grid(row=5, column=1, padx=5, pady=5)

    lbl_endereco = tk.Label(tela_clientes, text="Endereço:")
    lbl_endereco.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    entrada_endereco = tk.Entry(tela_clientes)
    entrada_endereco.grid(row=6, column=1, padx=5, pady=5)

    botao_adicionar_cliente = tk.Button(tela_clientes, text="Adicionar Cliente", command=adicionar_cliente)
    botao_adicionar_cliente.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    botao_fechar = tk.Button(tela_clientes, text="Fechar", command=tela_clientes.destroy)
    botao_fechar.grid(row=8, column=0, columnspan=2, padx=5, pady=5)


def fazer_pedido():
    tela_pedidos = tk.Toplevel(janela)
    tela_pedidos.title("Fazer Pedido")

    lbl_numero_pedido = tk.Label(tela_pedidos, text=f"Número do Pedido: {numero_pedido}", font=("Helvetica", 12))
    lbl_numero_pedido.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    lbl_numero_cliente = tk.Label(tela_pedidos, text="Número do Cliente:", font=("Helvetica", 12))
    lbl_numero_cliente.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    entrada_numero_cliente = tk.Entry(tela_pedidos)
    entrada_numero_cliente.grid(row=1, column=1, padx=5, pady=5)

    def finalizar_pedido():
        numero_cliente_digitado = entrada_numero_cliente.get()

        try:
            numero_cliente = int(numero_cliente_digitado)
            if numero_cliente <= 0:
                messagebox.showerror("Erro", "Número do cliente deve ser um número inteiro positivo.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Número do cliente deve ser um número inteiro positivo.")
            return

        # Aqui você pode implementar a lógica para o pedido (ex: selecionar itens, calcular total, etc.)
        # Por enquanto, vamos apenas mostrar uma mensagem para ilustrar o funcionamento

        messagebox.showinfo("Pedido Finalizado", f"Pedido para o cliente {numero_cliente} realizado com sucesso!")
        tela_pedidos.destroy()

    botao_finalizar_pedido = tk.Button(tela_pedidos, text="Finalizar Pedido", command=finalizar_pedido)
    botao_finalizar_pedido.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    botao_cancelar = tk.Button(tela_pedidos, text="Cancelar", command=tela_pedidos.destroy)
    botao_cancelar.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    janela.protocol("WM_DELETE_WINDOW", janela.quit)


def abrir_tela_clientes():
    criar_tela_clientes()


def abrir_tela_pedidos():
    fazer_pedido()


janela = tk.Tk()
janela.title("Pizzaria do Fe")

# Variáveis para manter números de cliente e pedido visíveis
numero_cliente = 0
numero_pedido = 0

# Criar um menu inicial
menu = tk.Menu(janela)
janela.config(menu=menu)

menu_clientes = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Clientes", menu=menu_clientes)
menu_clientes.add_command(label="Cadastrar Novo Cliente", command=abrir_tela_clientes)

menu_pedidos = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Pedidos", menu=menu_pedidos)
menu_pedidos.add_command(label="Fazer Novo Pedido", command=abrir_tela_pedidos)

# Mostrar a janela principal
janela.mainloop()