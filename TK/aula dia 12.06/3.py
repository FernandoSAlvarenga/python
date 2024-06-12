import tkinter as tk# Importa o módulo tkinter para criar a interface gráfica.

def calcular_total():#Esta linha define uma função chamada calcular_total. Essa função será executada quando o usuário clicar no botão "Pedir".
 
  tamanho = var_tamanho.get()#Esta linha obtém o valor selecionado no menu suspenso var_tamanho. Esse valor representa o tamanho da pizza escolhida pelo usuário.
  quantidade = int(entrada_quantidade.get())#Esta linha obtém o valor digitado no campo de entrada entrada_quantidade. Esse valor representa a quantidade de pizzas que o usuário deseja pedir.A função int() converte o valor digitado para um número inteiro.

  if tamanho == "Pequena":
    preco_unitario = 15.00
  elif tamanho == "Média":
    preco_unitario = 22.00
  else:
    preco_unitario = 28.00
  #Este bloco de código verifica o tamanho da pizza selecionada e define o preço unitário correspondente:  

  total = preco_unitario * quantidade
  #Esta linha multiplica o preço unitário da pizza pela quantidade para calcular o total a pagar.
  
  resultado_total.config(text=f"Total a pagar: R$ {total:.2f}")
  #Esta linha atualiza o texto do rótulo resultado_total para mostrar o total a pagar, formatado com duas casas decimais.A string f"Total a pagar: R$ {total:.2f}" utiliza formatação de string para inserir o valor de total no texto.

# Criar a janela principal
janela = tk.Tk()# Cria uma instância da classe Tk, que representa a janela principal da aplicação.
janela.title("Pedindo Pizza")# Define o título da janela principal como "Pedindo Pizza".

# Criar Label para tamanho e quantidade
rotulo_tamanho = tk.Label(janela, text="Tamanho:")
rotulo_quantidade = tk.Label(janela, text="Quantidade:")
# Cria um Label com o texto "Tamanho:" utilizando a classe tk.Label.
# O Label é associado à janela principal (janela).
# O texto do Label é definido como "Tamanho:".
# rotulo_quantidade:
# Cria outro Label com o texto "Quantidade:" utilizando a classe tk.Label.
# O Label é associado à janela principal (janela).
# O texto do Label é definido como "Quantidade:".

# Criar o OptionMenu para o tamanho
var_tamanho = tk.StringVar(janela)
var_tamanho.set("Pequena")  # Definir o tamanho inicial como "Pequena"
opcoes_tamanho = ["Pequena", "Média", "Grande"]
menu_tamanho = tk.OptionMenu(janela, var_tamanho, *opcoes_tamanho)
# Cria uma variável do tipo tk.StringVar para armazenar o tamanho selecionado.
# A variável é associada à janela principal (janela).
# O valor inicial da variável é definido como "Pequena".
# opcoes_tamanho:
# Cria uma lista contendo as opções de tamanho disponíveis: ["Pequena", "Média", "Grande"].
# menu_tamanho:
# Cria um menu suspenso (OptionMenu) utilizando a classe tk.OptionMenu.
# O menu suspenso é associado à janela principal (janela).
# A variável var_tamanho é usada para armazenar o valor selecionado no menu.
# As opções de tamanho disponíveis são definidas pela lista opcoes_tamanho.

# Criar o campo de entrada para a quantidade
entrada_quantidade = tk.Entry(janela)
# Cria um campo de entrada de texto (Entry) utilizando a classe tk.Entry.
# O campo de entrada é associado à janela principal (janela).
# O usuário poderá digitar a quantidade de pizzas desejada neste campo.

# Criar o botão "Pedir"
botao_pedir = tk.Button(janela, text="Pedir", command=calcular_total)
# Cria um botão (Button) utilizando a classe tk.Button.
# O botão é associado à janela principal (janela).
# O texto do botão é definido como "Pedir".
# Ao clicar no botão, a função calcular_total será executada.

# Criar o Label para exibir o total
resultado_total = tk.Label(janela, text="")
# Cria um Label utilizando a classe tk.Label.
# O Label é associado à janela principal (janela).
# O texto inicial do Label é vazio ("").
# Este Label será utilizado para mostrar o total a pagar após o cálculo.

# Posicionar os elementos na interface
rotulo_tamanho.pack()
menu_tamanho.pack()
rotulo_quantidade.pack()
entrada_quantidade.pack()
botao_pedir.pack()
resultado_total.pack()
# Este bloco de código utiliza a função pack() para posicionar os elementos criados na interface gráfica.
# A ordem de utilização do pack() define a ordem em que os elementos serão exibidos na tela.

# Executar o loop principal da interface
janela.mainloop()