import tkinter as tk

def fechar_janela():
 #Função para fechar a janela principal.
  janela.destroy()

def limpar_campo_de_texto():
  #Função para limpar o campo de entrada de texto.
  campo_de_texto.delete(0, tk.END)

def atualizar_selecao():
  #Função para atualizar o rótulo de seleção.
  selecoes = []
  if opcao1_selecionada.get():
    selecoes.append("Opção 1")
  if opcao2_selecionada.get():
    selecoes.append("Opção 2")
  texto_selecao = "Selecionado: " + ", ".join(selecoes)
  rotulo_selecao.config(text=texto_selecao)

def mostrar_opcao_selecionada(opcao):
  #Função para atualizar o rótulo da opção selecionada no menu suspenso.
  rotulo_opcao["text"] = f"Opção Selecionada: {opcao}"

# Criando a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Interface Completa")

# Rótulo e botão para fechar a janela
rotulo_titulo = tk.Label(janela, text="Minha Primeira Interface Completa")
rotulo_titulo.pack()
botao_fechar = tk.Button(janela, text="Fechar Janela", command=fechar_janela)
botao_fechar.pack()

# Campo de entrada de texto e botão para limpar
campo_de_texto = tk.Entry(janela)
campo_de_texto.pack()
botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campo_de_texto)
botao_limpar.pack()

# Caixas de seleção e rótulo de seleção
opcao1_selecionada = tk.BooleanVar()
opcao2_selecionada = tk.BooleanVar()
caixaselecao1 = tk.Checkbutton(janela, text="Opção 1", variable=opcao1_selecionada, command=atualizar_selecao)
caixaselecao1.pack()
caixaselecao2 = tk.Checkbutton(janela, text="Opção 2", variable=opcao2_selecionada, command=atualizar_selecao)
caixaselecao2.pack()
rotulo_selecao = tk.Label(janela, text="Selecionado: ")
rotulo_selecao.pack()

# Menu suspenso e rótulo de opção
opcoes_menu = ["Opção A", "Opção B", "Opção C"]
opcao_selecionada = tk.StringVar(janela)
opcao_selecionada.set(opcoes_menu[0])
menu_suspenso = tk.OptionMenu(janela, opcao_selecionada, *opcoes_menu, command=mostrar_opcao_selecionada)
menu_suspenso.pack()
rotulo_opcao = tk.Label(janela, text="Opção Selecionada: ")
rotulo_opcao.pack()

# Executando a interface gráfica
janela.mainloop()