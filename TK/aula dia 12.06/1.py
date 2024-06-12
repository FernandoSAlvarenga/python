import tkinter as tk

# Criando a janela principal
janela_principal = tk.Tk()
janela_principal.title("Escolha seu Café")

# Lista de opções de café
opcoes_cafe = ["Expresso", "Cappuccino", "Latte Macchiato"]

# Variável para armazenar a seleção atual
selecao_cafe_atual = tk.StringVar()

# Define o café selecionado inicialmente como vazio
selecao_cafe_atual.set("")

# Função para capturar a seleção do usuário
def cafe_selecionado(cafe_escolhido):
    
    mensagem = f"Café Selecionado: {cafe_escolhido}"
    label_cafe["text"] = mensagem

# Criando a label para exibir a seleção (inicialmente "Café Selecionado:")
label_cafe = tk.Label(janela_principal, text="Café Selecionado:")
label_cafe.pack()

# Criando o OptionMenu
menu_cafe = tk.OptionMenu(janela_principal, selecao_cafe_atual, "", *opcoes_cafe, command=cafe_selecionado)
menu_cafe.pack()

# Botão para fechar a janela
botao_fechar = tk.Button(janela_principal, text="Fechar", command=janela_principal.destroy)
botao_fechar.pack()

# Executando a interface gráfica
janela_principal.mainloop()