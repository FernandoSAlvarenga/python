import tkinter as tk
import string # precisei importar pra identificar caracter especial. Quis fazer diferente.  
#eu não estava conseguindo, pesquisei na internet, para só depois conseguir.
def calcular_caracteres():
    conteudo_texto = campo_texto.get(1.0, tk.END)
    total_caracteres = len(conteudo_texto) - 1  # Oi Professor, aqui deleta o caracter da nova linha adicionado automaticamente pelo Text widget, penei aqui. 
    
    caracteres_vazios = conteudo_texto.count(' ') + conteudo_texto.count('\t')
    caracteres_especiais = sum(1 for char in conteudo_texto if char in string.punctuation)
    caracteres_nao_vazios = total_caracteres - caracteres_vazios - caracteres_especiais
    
    etiqueta_resultado.config(text=f"Total de caracteres: {total_caracteres}\n"
                                   f"Caracteres vazios: {caracteres_vazios}\n"
                                   f"Caracteres especiais: {caracteres_especiais}\n"
                                   f"Caracteres preenchidos: {caracteres_nao_vazios}")

janela_principal = tk.Tk()
janela_principal.title("Contador de Caracteres Detalhado")

campo_texto = tk.Text(janela_principal)
campo_texto.pack()

botao_calcular = tk.Button(janela_principal, text="Calcular Caracteres", command=calcular_caracteres)
botao_calcular.pack()

etiqueta_resultado = tk.Label(janela_principal, text="")
etiqueta_resultado.pack()

janela_principal.mainloop()