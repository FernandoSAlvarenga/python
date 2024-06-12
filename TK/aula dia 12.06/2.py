import tkinter as tk

# Criando a janela principal
janela_principal = tk.Tk()
janela_principal.title("Seleção de Tamanho de Camiseta")

# Lista de opções de tamanho
opcoes_tamanho = ["P", "M", "G", "GG"]

# Variável para armazenar a seleção atual
selecao_tamanho = tk.StringVar()
selecao_tamanho.set(opcoes_tamanho[0])  # Define o tamanho selecionado inicialmente como "P"

# Função para capturar a seleção do usuário e atualizar a label
def tamanho_selecionado(tamanho):
    mensagem_label["text"] = f"Você selecionou o tamanho: {tamanho}"

# Criando a label para exibir a mensagem
mensagem_label = tk.Label(janela_principal, text="Tamanho Selecionado: ")
mensagem_label.pack()

# Criando o OptionMenu
menu_tamanho = tk.OptionMenu(janela_principal, selecao_tamanho, *opcoes_tamanho, command=tamanho_selecionado)
menu_tamanho.pack()

# Botão para fechar a janela
botao_fechar = tk.Button(janela_principal, text="Fechar", command=janela_principal.destroy)
botao_fechar.pack()

# Executando a interface gráfica
janela_principal.mainloop()