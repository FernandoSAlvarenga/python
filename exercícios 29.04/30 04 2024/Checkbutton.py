import tkinter as tk

def mostrar_selecao():
  
  selecionado = var.get()

  
  if selecionado:
    print("Opção selecionada!")
  else:
    print("Nenhuma opção selecionada.")


janela = tk.Tk()
janela.title("Exemplo de Checkbox")


var = tk.BooleanVar()


caixa_selecao = tk.Checkbutton(janela, text="Selecionar", variable=var, command=mostrar_selecao)
caixa_selecao.pack()


janela.mainloop()