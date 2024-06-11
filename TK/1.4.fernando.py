import tkinter as tk
from tkinter import filedialog, messagebox
import string

def calcular_caracteres():
    conteudo_texto = campo_texto.get(1.0, tk.END)
    total_caracteres = len(conteudo_texto) - 1   
    
    caracteres_vazios = conteudo_texto.count(' ') + conteudo_texto.count('\t')
    caracteres_especiais = sum(1 for char in conteudo_texto if char in string.punctuation)
    caracteres_nao_vazios = total_caracteres - caracteres_vazios - caracteres_especiais
    
    etiqueta_resultado.config(text=f"Total de caracteres: {total_caracteres}\n"
                                   f"Caracteres vazios: {caracteres_vazios}\n"
                                   f"Caracteres especiais: {caracteres_especiais}\n"
                                   f"Caracteres preenchidos: {caracteres_nao_vazios}")

def salvar_conteudo():
    conteudo_texto = campo_texto.get(1.0, tk.END)
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                   filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo_texto)
            messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

def carregar_conteudo():
    caminho_arquivo = filedialog.askopenfilename(defaultextension=".txt", 
                                                 filetypes=[("Text files", ".txt"), ("All files", ".*")])
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo_texto = arquivo.read()
            campo_texto.delete(1.0, tk.END)
            campo_texto.insert(tk.END, conteudo_texto)
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

janela_principal = tk.Tk()
janela_principal.title("Contador de Caracteres Detalhado")

campo_texto = tk.Text(janela_principal)
campo_texto.pack()

botao_calcular = tk.Button(janela_principal, text="Calcular Caracteres", command=calcular_caracteres)
botao_calcular.pack()

botao_salvar = tk.Button(janela_principal, text="Salvar", command=salvar_conteudo)
botao_salvar.pack()

botao_carregar = tk.Button(janela_principal, text="Importar texto", command=carregar_conteudo)
botao_carregar.pack()

etiqueta_resultado = tk.Label(janela_principal, text="")
etiqueta_resultado.pack()

janela_principal.mainloop()