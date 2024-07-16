from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

# Função para conectar ao banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Deixe vazio se não tiver senha
        database="pagina_inicial"  # Substitua pelo nome do seu banco de dados
    )

# Rota para exibir o formulário HTML
@app.route('/')
def formulario():
    return render_template('formulario.html')

# Rota para processar o envio do formulário
@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        email = request.form['email']
        telefone = request.form['telefone']
        
        try:
            bd = conectar_bd()
            cursor = bd.cursor()
            
            sql = "INSERT INTO contatos (nome, endereco, email, telefone) VALUES (%s, %s, %s, %s)"
            valores = (nome, endereco, email, telefone)
            
            cursor.execute(sql, valores)
            bd.commit()
            
            cursor.close()
            bd.close()
            
            return redirect('/sucesso')
        
        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dados no banco de dados: {erro}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o formulário."), 500

# Rota para página de sucesso
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)