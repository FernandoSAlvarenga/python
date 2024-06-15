import tkinter as tk  # Importa o módulo tkinter para construir interfaces gráficas
from tkinter import messagebox  # Importa a classe messagebox de tkinter para mostrar caixas de diálogo

# Função para processar o pedido quando o botão "Pedir" é clicado
def fazer_pedido():
    tamanho = var_tamanho.get()  # Obtém o tamanho selecionado da pizza
    try:
        quantidade = int(entrada_quantidade.get())  # Obtém a quantidade de pizzas (convertido para int)
        if quantidade <= 0:
            raise ValueError  # Lança um erro se a quantidade for menor ou igual a zero
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de pizzas.")
        return  # Mostra uma mensagem de erro se a quantidade não for válida e retorna

    num_sabores = var_sabores.get()  # Obtém o número de sabores selecionado

    # Verifica se o número de sabores é válido para o tamanho selecionado
    if tamanho == "Pequena" and num_sabores != 1:
        messagebox.showerror("Erro", "Pizza pequena só pode ter 1 sabor.")
        return
    elif tamanho == "Média" and num_sabores not in [1, 2]:
        messagebox.showerror("Erro", "Pizza média só pode ter 1 ou 2 sabores.")
        return
    elif tamanho == "Grande" and num_sabores not in [1, 2, 4]:
        messagebox.showerror("Erro", "Pizza grande só pode ter 1, 2 ou 4 sabores.")
        return

    total_pizzas = quantidade  # Total de pizzas é a quantidade especificada
    total = precos[tamanho] * total_pizzas  # Calcula o preço total das pizzas com base no tamanho

    # Monta a descrição detalhada do pedido
    itens_cobrados = f"Descrição do Pedido:\n\n"
    itens_cobrados += f"Tamanho: {tamanho}\n"
    itens_cobrados += f"Quantidade: {quantidade}\n"
    itens_cobrados += f"Sabores: {num_sabores}\n"

    ingredientes_selecionados = []
    # Verifica quais ingredientes adicionais foram selecionados
    for ing in ingredientes:
        if ingredientes_vars[ing].get() == 1:
            ingredientes_selecionados.append(ing)
    
    # Se houver ingredientes selecionados, adiciona-os à descrição do pedido e calcula o custo total
    if ingredientes_selecionados:
        itens_cobrados += "Ingredientes Adicionais:\n"
        for ing in ingredientes_selecionados:
            preco_por_ingrediente = precos_ingredientes[ing]
            total_ingrediente = preco_por_ingrediente * total_pizzas
            itens_cobrados += f"- {ing}: R${preco_por_ingrediente:.2f} x {total_pizzas} = R${total_ingrediente:.2f}\n"
            total += total_ingrediente
    
    itens_cobrados += f"\nTotal a pagar: R${total:.2f}"  # Adiciona o total geral ao pedido

    mensagem_pedido = f"Pedido realizado: {quantidade} pizza(s) {tamanho} com {num_sabores} sabor(es).\n\n{itens_cobrados}"
    # Pergunta ao usuário se deseja confirmar o pedido
    if messagebox.askyesno("Confirmar Pedido", mensagem_pedido):
        messagebox.showinfo("Pedido Realizado", "Seu pedido foi confirmado!")  # Mostra uma mensagem de confirmação do pedido

# Definição dos tamanhos disponíveis e seus preços
tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 17.00, "Média": 25.00, "Grande": 32.00}

# Definição dos ingredientes disponíveis e seus preços
ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 6.00, "Pepperoni": 9.00, "Bacon": 7.00}

# Criação da janela principal da aplicação tkinter
janela = tk.Tk()
janela.title("Pedido de Pizza")  # Define o título da janela

# Criação e posicionamento dos elementos na janela (rótulos, menus, entradas, botões, etc.)
# Aqui estão presentes labels, entradas de texto, opções de menu, botões e checkboxes.

janela.mainloop()  # Inicia o loop principal da interface gráfica tkinter