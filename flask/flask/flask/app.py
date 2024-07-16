from flask import Flask, render_template, request, redirect, url_for, session, flash, Response
import mysql.connector
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from io import BytesIO
from reportlab.pdfgen import canvas
from xlsxwriter.workbook import Workbook

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
    return 'usuario_id' in session

# Rota para a página inicial
@app.route('/')
def index():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)
            
            # Supondo que a tabela 'contatos' tenha uma coluna chamada 'conteudo'
            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            dados_pagina_inicial = cursor.fetchall()
            
            cursor.close()
            bd.close()
            
            return render_template('index.html', dados=dados_pagina_inicial)
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar a tabela contatos: {erro}")
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

@app.route('/atendimento')
def atendimento():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            contatos = cursor.fetchall()

            cursor.close()
            bd.close()

            return render_template('atender_contato.html', contatos=contatos)

        except mysql.connector.Error as erro:
            print(f"Erro ao consultar contatos: {erro}")
            flash('Erro ao consultar contatos.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
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
                session['usuario_id'] = usuario['id']
                flash('Login realizado como usuário com sucesso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Nome de usuário ou senha incorretos.', 'error')
        
        except mysql.connector.Error as erro:
            print(f"Erro ao consultar banco de dados: {erro}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o login."), 500
    
    return render_template('login.html')

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

            flash('Conta criada com sucesso!', 'success')
            return redirect(url_for('login'))

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dados no banco de dados: {erro}")
            flash('Erro ao criar conta.', 'error')

    return render_template('criar_conta.html', form=form)

@app.route('/listar_usuarios')
def listar_usuarios():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            usuarios = cursor.fetchall()

            cursor.close()
            bd.close()

            return render_template('listar_usuarios.html', usuarios=usuarios)

        except mysql.connector.Error as erro:
            print(f"Erro ao listar usuários: {erro}")
            flash('Erro ao listar usuários.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

@app.route('/excluir_usuario/<int:id>', methods=['POST'])
def excluir_usuario(id):
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor()

            sql = "DELETE FROM usuarios WHERE id = %s"
            valores = (id,)

            cursor.execute(sql, valores)
            bd.commit()

            cursor.close()
            bd.close()

            flash('Usuário excluído com sucesso!', 'success')
        except mysql.connector.Error as erro:
            print(f"Erro ao excluir usuário: {erro}")
            flash('Erro ao excluir usuário.', 'error')
        
        return redirect(url_for('listar_usuarios'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

class AtualizarUsuarioForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])

@app.route('/editar_usuario/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if verificar_sessao():
        form = AtualizarUsuarioForm()

        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data

            try:
                bd = conectar_bd()
                cursor = bd.cursor()

                sql = "UPDATE usuarios SET username = %s, email = %s WHERE id = %s"
                valores = (username, email, id)

                cursor.execute(sql, valores)
                bd.commit()

                cursor.close()
                bd.close()

                flash('Usuário atualizado com sucesso!', 'success')
                return redirect(url_for('listar_usuarios'))

            except mysql.connector.Error as erro:
                print(f"Erro ao atualizar usuário: {erro}")
                flash('Erro ao atualizar usuário.', 'error')

        else:
            try:
                bd = conectar_bd()
                cursor = bd.cursor(dictionary=True)

                sql = "SELECT * FROM usuarios WHERE id = %s"
                valores = (id,)

                cursor.execute(sql, valores)
                usuario = cursor.fetchone()

                form.username.data = usuario['username']
                form.email.data = usuario['email']

                cursor.close()
                bd.close()

            except mysql.connector.Error as erro:
                print(f"Erro ao buscar usuário para edição: {erro}")
                flash('Erro ao carregar dados do usuário.', 'error')

        return render_template('editar_usuario.html', form=form)
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))
    
@app.route('/listar_mensagens')
def listar_mensagens():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            mensagens = cursor.fetchall()

            cursor.close()
            bd.close()

            return render_template('listar_mensagens.html', mensagens=mensagens)

        except mysql.connector.Error as erro:
            print(f"Erro ao listar mensagens: {erro}")
            flash('Erro ao listar mensagens.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

@app.route('/atender_contato')
def atender_contato():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            contatos = cursor.fetchall()

            cursor.close()
            bd.close()

            return render_template('atender_contato.html', contatos=contatos)

        except mysql.connector.Error as erro:
            print(f"Erro ao consultar contatos: {erro}")
            flash('Erro ao consultar contatos.', 'error')
            return redirect(url_for('index'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

@app.route('/excluir_mensagem/<int:id>', methods=['POST'])
def excluir_mensagem(id):
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor()

            sql = "DELETE FROM contatos WHERE id = %s"
            valores = (id,)

            cursor.execute(sql, valores)
            bd.commit()

            cursor.close()
            bd.close()

            flash('Mensagem excluída com sucesso!', 'success')
        except mysql.connector.Error as erro:
            print(f"Erro ao excluir mensagem: {erro}")
            flash('Erro ao excluir mensagem.', 'error')
        
        return redirect(url_for('listar_mensagens'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

# Rota para gerar PDF de mensagens
@app.route('/gerar_pdf')
def gerar_pdf():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            mensagens = cursor.fetchall()

            cursor.close()
            bd.close()

            # Gerar PDF
            response = BytesIO()
            pdf = canvas.Canvas(response)

            pdf.drawString(100, 800, "Lista de Mensagens")

            linha = 750
            for mensagem in mensagens:
                linha -= 20
                pdf.drawString(100, linha, f"ID: {mensagem['id']}, Nome: {mensagem['nome']}, Email: {mensagem['email']}, Mensagem: {mensagem['mensagem']}")

            pdf.save()

            response.seek(0)
            return Response(response, mimetype='application/pdf', headers={'Content-Disposition': 'attachment; filename=listagem_mensagens.pdf'})

        except mysql.connector.Error as erro:
            print(f"Erro ao gerar PDF: {erro}")
            flash('Erro ao gerar PDF.', 'error')
            return redirect(url_for('listar_mensagens'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

# Rota para gerar Excel de mensagens
@app.route('/gerar_excel')
def gerar_excel():
    if verificar_sessao():
        try:
            bd = conectar_bd()
            cursor = bd.cursor(dictionary=True)

            sql = "SELECT * FROM contatos"
            cursor.execute(sql)
            mensagens = cursor.fetchall()

            cursor.close()
            bd.close()

            # Gerar Excel
            output = BytesIO()
            workbook = Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet()

            cabecalhos = ['ID', 'Nome', 'Email', 'Mensagem']
            for col, cabecalho in enumerate(cabecalhos):
                worksheet.write(0, col, cabecalho)

            linha = 1
            for mensagem in mensagens:
                worksheet.write(linha, 0, mensagem['id'])
                worksheet.write(linha, 1, mensagem['nome'])
                worksheet.write(linha, 2, mensagem['email'])
                worksheet.write(linha, 3, mensagem['mensagem'])
                linha += 1

            workbook.close()

            output.seek(0)
            return Response(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={'Content-Disposition': 'attachment; filename=listagem_mensagens.xlsx'})

        except mysql.connector.Error as erro:
            print(f"Erro ao gerar Excel: {erro}")
            flash('Erro ao gerar Excel.', 'error')
            return redirect(url_for('listar_mensagens'))
    else:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

# Rota para página de sucesso após envio de mensagem
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
