from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
import mysql.connector
import secrets
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from io import BytesIO
from reportlab.pdfgen import canvas
from xlsxwriter import Workbook

# Configuração do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'
csrf = CSRFProtect(app)

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário MySQL
        password="",  # Substitua pela sua senha MySQL
        database="pagina_inicial",  # Substitua pelo nome do seu banco de dados
        
    )

# Classe para formulário de criação de conta
class CriarContaForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])

# Classe para formulário de contato
class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    mensagem = TextAreaField('Mensagem', validators=[InputRequired()])

# Verificação de sessão de usuário
def verificar_sessao():
    if 'username' in session:
        username = session['username']
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            
            sql = "SELECT * FROM sessoes WHERE username = %s"
            valores = (username,)
            
            cursor.execute(sql, valores)
            sessao = cursor.fetchone()
            
            cursor.close()
            bd.close()
            
            if sessao:
                return True
        except mysql.connector.Error as erro:
            print(f"Erro ao verificar sessão: {erro}")
    return False

# Rota para a página inicial
@app.route('/')
def index():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            
            # Supondo que a tabela 'pagina_inicial' tenha uma coluna chamada 'conteudo'
            sql = "SELECT * from contatos"
            cursor.execute(sql)
            dados_pagina_inicial = cursor.fetchall()
            
            cursor.close()
            bd.close()
            
            return render_template('index.html', dados=dados_pagina_inicial)
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar a tabela pagina_inicial: {erro}")
            return render_template('erro.html', mensagem_erro="Erro ao processar a página inicial."), 500
    else:
        return redirect(url_for('login'))

# Rota para a página 'Sobre'
@app.route('/sobre')
def sobre():
    if verificar_sessao():
        return render_template('sobre.html')
    else:
        return redirect(url_for('login'))

# Rota para o formulário de contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if verificar_sessao():
        form = ContatoForm()

        if form.validate_on_submit():
            nome = form.nome.data
            email = form.email.data
            mensagem = form.mensagem.data
            situacao = 'Pendente'

            try:
                bd = conectar_bd()
                cursor = bd.cursor()

                sql = "INSERT INTO contatos (nome, email, mensagem, situacao) VALUES (%s, %s, %s, %s)"
                valores = (nome, email, mensagem, situacao)

                cursor.execute(sql, valores)
                bd.commit()

                cursor.close()
                bd.close()

                flash('Mensagem enviada com sucesso!', 'success')
                return redirect(url_for('sucesso'))

            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no banco de dados: {erro}")
                flash('Erro ao enviar mensagem.', 'error')

        return render_template('contato.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            
            sql = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
            valores = (username, password)
            
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
            
            cursor.close()
            bd.close()
            
            if usuario:
                session['username'] = usuario['username']
                
                # Criar uma entrada na tabela de sessões
                token = secrets.token_hex(16)
                try:
                    bd = conectar_bd()
                    cursor = bd.cursor()
                    
                    sql = "INSERT INTO sessoes (username, token) VALUES (%s, %s)"
                    valores = (username, token)
                    
                    cursor.execute(sql, valores)
                    bd.commit()
                    
                    cursor.close()
                    bd.close()
                    
                except mysql.connector.Error as erro:
                    print(f"Erro ao criar sessão: {erro}")
                    return render_template('erro.html', mensagem_erro="Erro ao processar o login."), 500
                
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Nome de usuário ou senha incorretos.', 'error')
        
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar banco de dados: {erro}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o login."), 500
    
    return render_template('login.html')

# Rota para criar conta
@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_conta():
    form = CriarContaForm()
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        try:
            bd = conectar_bd()
            cursor = bd.cursor()

            sql = "INSERT INTO usuarios (username, password, email) VALUES (%s, %s, %s)"
            valores = (username, password, email)

            cursor.execute(sql, valores)
            bd.commit()

            cursor.close()
            bd.close()

            flash('Conta criada com sucesso! Faça login para acessar.', 'success')
            return redirect(url_for('login'))

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dados no banco de dados: {erro}")
            flash('Erro ao criar conta.', 'error')

    return render_template('criar_conta.html', form=form)

# Rota para logout
@app.route('/logout')
def logout():
    if 'username' in session:
        username = session['username']
        session.pop('username', None)
        
        # Remover a sessão do banco de dados
        try:
            bd = conectar_bd()
            cursor = bd.cursor()
            
            sql = "DELETE FROM sessoes WHERE username = %s"
            valores = (username,)
            
            cursor.execute(sql, valores)
            bd.commit()
            
            cursor.close()
            bd.close()
            
            flash('Logout realizado com sucesso!', 'success')
        except mysql.connector.Error as erro:
            print(f"Erro ao remover sessão: {erro}")
            flash('Erro ao realizar logout.', 'error')
    
    return redirect(url_for('index'))

@app.route('/atender_contato')
def atender_contato():
    if 'username' in session:
        username = session['username']
        try:
            bd = conectar_bd()
            cursor = bd.cursor()

            # Consulta SQL para obter os contatos do usuário logado
            sql = """
                SELECT ct.nome, ct.email, ct.mensagem, ct.situacao
                FROM contatos AS ct
                INNER JOIN usuarios AS us ON ct.id = us.id
                WHERE us.username = %s
                ORDER BY ct.id
            """
            cursor.execute(sql, (username,))
            contatos = cursor.fetchall()

            cursor.close()
            bd.close()

            return render_template('atender_contato.html', contatos=contatos)

        except mysql.connector.Error as erro:
            print(f"Erro ao consultar contatos: {erro}")
            return render_template('erro.html', mensagem_erro="Erro ao consultar contatos."), 500
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))


# Rota para gerar relatório em PDF
@app.route('/gerar_pdf')
def gerar_pdf():
    if 'username' in session:
        # Cria um buffer de memória para o PDF
        buffer = BytesIO()

        # Gera o conteúdo do PDF
        c = canvas.Canvas(buffer)
        c.drawString(100, 750, "Relatório de Usuários")
        c.drawString(100, 730, "--------------------------------------------")

        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            cursor.close()
            bd.close()

            y = 700
            for usuario in usuarios:
                c.drawString(100, y, f"Nome: {usuario['username']}")
                c.drawString(100, y - 20, f"Email: {usuario['email']}")
                y -= 40

        except mysql.connector.Error as erro:
            print(f"Erro ao gerar PDF: {erro}")
            c.drawString(100, y, "Erro ao gerar PDF.")
        
        c.save()

        # Define o buffer para o início
        buffer.seek(0)

        # Retorna a resposta do PDF
        return Response(buffer, mimetype='application/pdf')
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

# Rota para gerar relatório em Excel
@app.route('/gerar_excel')
def gerar_excel():
    if 'username' in session:
        # Cria um buffer de memória para o Excel
        buffer = BytesIO()

        # Cria um novo workbook no Excel
        workbook = Workbook(buffer, {'in_memory': True})
        worksheet = workbook.add_worksheet('Usuários')

        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall()
            cursor.close()
            bd.close()

            worksheet.write(0, 0, 'Nome')
            worksheet.write(0, 1, 'Email')

            row = 1
            for usuario in usuarios:
                worksheet.write(row, 0, usuario['username'])
                worksheet.write(row, 1, usuario['email'])
                row += 1

        except mysql.connector.Error as erro:
            print(f"Erro ao gerar Excel: {erro}")
            worksheet.write(0, 0, "Erro ao gerar Excel.")
        
        workbook.close()

        # Define o buffer para o início
        buffer.seek(0)

        # Retorna a resposta do Excel
        return Response(buffer, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={"Content-Disposition": "attachment;filename=usuarios.xlsx"})
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

# Rota para a página de sucesso após o envio do contato
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True)
