'''1. Crie uma interface gráfica com um título, um rótulo e um botão.  
O título da janela deve ser "Minha Primeira Interface". 
O rótulo deve exibir o texto "Olá, Tkinter!". 
O botão deve ter o texto "Clique em Mim". '''

import tkinter as tk

#começar literalmente pelo exercício:


    janela = tk.Tk()
    janela.title("Minha Primeira Interface")
    janela.geometry("300x200")

    rotulo = tk.Label(janela, text="Olá, Tkinter!")
    rotulo.pack()

    botao = tk.Button(janela, text="Clique em mim!")
    botao.pack()



