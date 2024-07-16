from typing import NotRequired#Esta linha importa o tipo NotRequired do módulo typing. Este tipo é tipicamente usado com formulários Flask-WTF para indicar que um campo é opcional e pode ser enviado sem valor.
from flask import Flask, redirect, render_template, request, url_for,flash,session,g#Esta linha importa várias funções do módulo flask:Flask: Esta função é usada para criar uma instância de aplicativo Flask.redirect: Esta função é usada para redirecionar um usuário para uma URL diferente.render_template: Esta função é usada para renderizar um arquivo de modelo com dados.request: Este objeto fornece acesso às informações da solicitação web atual, como dados de formulário, cabeçalhos e cookies.
from flask_wtf import FlaskForm#Esta linha importa a classe FlaskForm do módulo flask_wtf. Esta classe é a classe base para criar formulários em aplicativos Flask que usam WTForms para validação e proteção CSRF.
from wtforms import StringField, EmailField, PasswordField, validators#Esta linha importa várias classes de campo de formulário e o módulo validators da biblioteca wtforms:StringField: Esta classe é usada para criar um campo de entrada de texto.EmailField: Esta classe é usada para criar um campo de entrada de email com validação básica de email.PasswordField: Esta classe é usada para criar um campo de entrada de senha que oculta os caracteres à medida que são digitados.validators: Este módulo fornece vários validadores que podem ser usados para verificar o formato, o comprimento e outras propriedades dos dados do formulário.
from bd_config import conecta_no_banco_de_dados#Esta linha importa a função conecta_no_banco_de_dados.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'
bd =conecta_no_banco_de_dados()
# cursor = bd.cursor()
# sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
# values = (nome, email, mensagem)
# cursor.execute(sql, values)
# bd.commit()
global id_usuario
class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = StringField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])
    #mensagem = StringField('Mensagem:', validators=[validators.Length(min=10)])

# Esta classe define um formulário chamado FormularioContato usando a classe FlaskForm do Flask-WTF.
# O campo nome é um campo de texto simples com o rótulo "Nome:" e o validador validators.DataRequired() garante que o campo não seja vazio.
# O campo email é um campo de texto com o rótulo "Email:" e os validadores validators.DataRequired() e validators.Email(). O primeiro garante que o campo não seja vazio e o segundo verifica se o valor digitado é um email válido.
# O campo mensagem é um campo de texto com o rótulo "Mensagem:" e os validadores validators.DataRequired() e validators.Length(min=10). O primeiro garante que o campo não seja vazio e o segundo verifica se o valor digitado tem pelo menos 10 caracteres.

@app.route('/', methods=['GET', 'POST'])

def pagina_login():
    
    
     # Limpa os dados da sessão
     session.clear()
      # Limpa o cookie do ID do usuário
     session.pop('usuario_id', None)
     # Renderiza o template 'login.html' e retorna a página HTML gerada.
     return render_template("login.html")

@app.route('/paginainicial')

def pagina_inicial():
     if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    # Renderiza o template 'paginainicial.htmlp' e retorna a página HTML gerada.
     usuario_id = session.get('usuario_id')
     nome_usuario = get_nome_usuario_por_id(usuario_id)
     g.nome_usuario = nome_usuario
     return render_template("paginainicial.html", nome_usuario=g.nome_usuario)

#Requisição POST: Método HTTP usado para enviar dados para um servidor. Os dados são enviados no corpo da requisição, e o servidor pode processá-los como quiser. 
#É frequentemente usada para criar novos recursos ou enviar dados para processamento.

#Requisição GET: Método HTTP usado para obter dados de um servidor. Os dados são enviados na URL, e o servidor pode processá-los como quiser. 
#É frequentemente usada para obter informações de um recurso, como uma lista de itens ou os detalhes de um item.
# Este decorador define a rota principal do aplicativo Flask, que é acessível através do URL /.
# Ele especifica que a função contato deve ser chamada quando um usuário solicita essa rota.
# O parâmetro methods indica que a função manipula requisições HTTP do tipo GET e POST.

# Método GET:

# Ao acessar a rota principal com o método GET, a função contato é executada.
# Essa função:
# Cria uma instância do formulário FormularioContato.
# Renderiza a página HTML contato.html, passando o formulário como contexto para que ele seja exibido na tela.
# O método GET, neste caso, serve para exibir o formulário de contato para que o usuário possa preenchê-lo e enviar seus dados.

# Método POST:

# Quando o usuário preenche e submete o formulário, ele envia uma requisição HTTP POST para a rota /.
# A função contato é novamente executada, mas agora com os dados do formulário preenchidos.
# A função:
# Valida os dados do formulário usando os validadores definidos na classe FormularioContato.
# Se a validação for bem-sucedida:
# Extrai os valores dos campos do formulário (nome, email e mensagem).
# Tenta se conectar ao banco de dados usando a função conecta_no_banco_de_dados().
# Se a conexão for bem-sucedida:
# Cria um cursor para executar comandos SQL.
# Constrói a instrução SQL INSERT para inserir os dados do formulário na tabela contatos do banco de dados.
# Executa a instrução SQL usando o cursor.
# Confirma as alterações no banco de dados usando bd.commit().
# Imprime uma mensagem de sucesso no console.
# Redireciona o usuário para a rota /sucesso usando redirect('/sucesso').
# Se a conexão com o banco de dados falhar:
# Captura a mensagem de erro e imprime no console.
# Define uma mensagem de erro genérica para o usuário.
# Renderiza a página erro.html com a mensagem de erro.
# Retorna um código de status HTTP 500 (erro interno do servidor).
# Se a validação do formulário falhar:
# Renderiza a página contato.html novamente, mas com o formulário preenchido com os dados digitados pelo usuário e as mensagens de erro de validação.
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = FormularioContato()
    # A linha form = FormularioContato() cria uma instância do formulário FormularioContato definido anteriormente.
    # Isso torna os campos e funcionalidades do formulário disponíveis para uso dentro da função.



    # A condição if form.validate_on_submit():
    # Verifica se o formulário foi submetido e validado com sucesso.
    # form.validate_on_submit() retorna True se todos os campos obrigatórios forem preenchidos e os valores atenderem aos critérios de validação.
    # Se a validação falhar, o usuário verá o formulário novamente com as mensagens de erro.
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data    
        # As linhas nome = form.nome.data, email = form.email.data e mensagem = form.mensagem.data extraem os valores dos campos nome, email e mensagem do formulário, respectivamente.
        # O atributo data de cada campo do formulário fornece o valor digitado pelo usuário.
        
        try:
            
            bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
            cursor = bd.cursor()
            sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
            values = (nome, email, mensagem)
            cursor.execute(sql, values)
            bd.commit()

            print(f"Dados do formulário salvos com sucesso!")
            # Se a conexão com o banco de dados for bem-sucedida:
            # Um cursor para executar comandos SQL é criado usando cursor = bd.cursor().
            # A instrução SQL INSERT é construída na variável sql para inserir os dados do formulário na tabela contatos. A instrução utiliza marcadores de posição (%s) para os valores a serem inseridos.
            # Os valores extraídos do formulário são armazenados em uma tupla values na ordem correspondente aos marcadores de posição na instrução SQL.
            # O comando cursor.execute(sql, values) executa a instrução SQL, inserindo os dados do formulário na tabela.
            # A função bd.commit() é chamada para confirmar as alterações feitas no banco de dados.
            # Uma mensagem de sucesso informando que os dados foram salvos é impressa no console.
            
        except bd.connector.Error as err:
            print(f"Erro ao salvar dados no banco de dados: {err}")

            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
            # O bloco try...except tenta executar o código de gravação no banco de dados.
            # Se a exceção bd.connector.Error for lançada, significa que ocorreu um erro durante a interação com o banco de dados.
            # A mensagem de erro é capturada na variável err e impressa no console para fins de depuração.
            # Uma mensagem de erro genérica informando que houve um problema ao processar o contato é definida em mensagem_erro.
            # A função render_template('erro.html', mensagem_erro=mensagem_erro) renderiza a página erro.html e passa a mensagem de erro como contexto.
            # O código retorna um código de status HTTP 500, indicando um erro interno do servidor.
        finally:
            if bd is not None:
                bd.close()
                # O bloco finally é executado independentemente do sucesso ou falha da gravação no banco de dados.
                # A linha if bd is not None: verifica se a variável bd (referência à conexão com o banco de dados) não é None.
                # Se a conexão ainda estiver ativa, o método close() é chamado para fechá-la e liberar os recursos. 
        return redirect(url_for('pagina_login'))
        #Se a gravação no banco de dados for bem-sucedida, a linha return redirect('/sucesso') redireciona o usuário para a rota /sucesso, que provavelmente renderiza uma página de confirmação de envio.

    else:
        return render_template('contato.html', form=form)
        #Se o formulário não foi submetido ou a validação falhou, a linha return render_template('contato.html', form=form) renderiza

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')
# Esta função define a rota /sucesso do aplicativo Flask.
# O decorador @app.route('/sucesso') indica que a função sucesso deve ser chamada quando um usuário solicita a rota /sucesso.
# A função sucesso contém apenas uma linha de código:
# return render_template('sucesso.html'):
# Esta instrução renderiza a página HTML sucesso.html quando o usuário acessa a rota /sucesso.
# O arquivo sucesso.html provavelmente contém uma mensagem de confirmação informando que o contato foi enviado com sucesso.
@app.errorhandler(Exception)
def erro_geral(erro):
    mensagem_erro = str(erro)  
    
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500
# Esta função é um manipulador de erros global para o aplicativo Flask.
# O decorador @app.errorhandler(Exception) indica que a função erro_geral deve ser chamada sempre que uma exceção não tratada ocorrer em qualquer lugar do aplicativo.
# A função erro_geral recebe um parâmetro erro que representa a exceção que foi lançada.
# A função erro_geral realiza as seguintes ações:
# mensagem_erro = str(erro): Converte a exceção em uma string para que sua mensagem possa ser exibida na página de erro.
# return render_template('erro.html', mensagem_erro=mensagem_erro), 500:
# Renderiza a página HTML erro.html e passa a mensagem de erro mensagem_erro como contexto para que ela seja exibida na página.
# Retorna um código de status HTTP 500, indicando um erro interno do servidor.

@app.route('/validalogin', methods=['POST', 'GET'])
def login():
  
  email = request.form.get('email')
  senha = request.form.get('senha')

  # Validar as credenciais
  bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
  cursor = bd.cursor()
  cursor.execute("""
            SELECT *
            FROM usuarios
            WHERE email = %s AND senha = %s;
        """, (email, senha,))
  usuario = cursor.fetchone()
  cursor.close()
  bd.close()

  if usuario:
  # Login bem-sucedido

   session['usuario_id'] = usuario[0]
   nome_usuario = get_nome_usuario_por_id(usuario[0])
   g.nome_usuario = nome_usuario
   print()
   return redirect(url_for('pagina_inicial'))
  else:
    # Login inválido
    
    return redirect(url_for('pagina_login'))
def get_nome_usuario_por_id(usuario_id):
    
    bd =conecta_no_banco_de_dados()
    cursor = bd.cursor()

    # Executa a consulta para obter o nome do usuário
    try:
        cursor.execute("""
            SELECT nome
            FROM usuarios
            WHERE id = %s;
        """, (usuario_id,))
        resultado = cursor.fetchone()
        print(resultado[0])
        # Verifica se o usuário foi encontrado
        if resultado:
            nome_usuario = resultado[0]
        else:
            nome_usuario = None
    except bd.connector.Error as error:
        # Registra o erro e retorna None
        print(f"Erro ao buscar nome do usuário: {error}")
        nome_usuario = None

    finally:
        # Fecha o cursor e a conexão com o banco de dados
        cursor.close()
        bd.close()

    return nome_usuario
@app.route('/usuarios')
def pagina_usuarios():
  if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
  bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
  cursor = bd.cursor()
  cursor.execute('SELECT * FROM usuarios')
  usuarios = cursor.fetchall()

  return render_template("usuarios.html", usuarios=usuarios)


# Define a rota '/cadastro', permitindo tanto requisições POST quanto GET.
@app.route('/cadastro', methods=["POST","GET"])
def abre_cadastro():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    return render_template("cadastro.html")




@app.route('/add_cadastro', methods=["POST","GET"])
def cadastro():
  if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
  # Obtém os valores dos campos "nome", "email" e "senha" do formulário submetido via POST.
  nome = request.form.get('nome')
  email = request.form.get('email')
  senha = request.form.get('senha')

   # Validação
  if not nome:
     flash('O nome é obrigatório.')
     return render_template('cadastro.html')
  if not email:
     flash('O e-mail é obrigatório.')
     return render_template('cadastro.html')
  if not senha:
    flash('A senha é obrigatória.')
    return render_template('cadastro.html')        
  # Abre uma conexão com o banco de dados MySQL usando as credenciais especificadas.
  bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
  cursor = bd.cursor()
          
  # Executa uma consulta SQL para verificar se já existe um usuário com o email informado.
  cursor.execute("""
    SELECT COUNT(*)
    FROM usuarios
    WHERE email = %s;
    """, (email,))
          
  # Obtém o resultado da consulta (o número de usuários encontrados).
  existe = cursor.fetchone()[0]
        
  # Fecha o cursor e a conexão com o banco de dados.
  cursor.close()
  bd.close()
  # Se a consulta anterior retornou um valor maior que zero (usuário já existe), renderiza o template 'cadastro.html' novamente, passando uma mensagem de erro.
  if existe > 0:
    flash('Email já cadastrado')
    return render_template('cadastro.html')
  else:
    try:
      # Reabre a conexão com o banco.
      bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
      cursor = bd.cursor()
                
      # Prepara a consulta SQL de inserção.
      sql = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'
      values = (nome, email, senha)

      # Executa a consulta com os valores obtidos do formulário.
      cursor.execute(sql, list(values))
      # Fecha o cursor e confirma a transação (commit).
      cursor.close()
      bd.commit()

      # Redireciona para a página inicial.
      return redirect(url_for('pagina_usuarios'))
    # Se ocorrer um erro de banco de dados, renderiza o template 'cadastro.html' novamente, passando a mensagem de erro SQL.
    except bd.connector.Error as e:   
            return render_template('cadastro', error=str(e)) 
          
          # Se o usuário não existe, tenta inserir o novo usuário no banco de dados:   
 
    
    
    
    
@app.route('/contatos')
def pagina_Contatos():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    bd =conecta_no_banco_de_dados()
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM contatos where situacao!="Atendimento" AND situacao!="Finalizado";')
    contatos = cursor.fetchall()
    return render_template("contatos.html", contatos=contatos)        
   

@app.route('/meus_contatos')
def pagina_Meus_Contatos():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    usuario_id = session.get('usuario_id')
    bd =conecta_no_banco_de_dados()
    cursor = bd.cursor()
    cursor.execute(  """
SELECT ct.*
FROM contatos AS ct
INNER JOIN usuario_contato AS uc ON uc.contato_id = ct.id_contato
WHERE uc.usuario_id = %s order by ct.id_contato
    """,
    (usuario_id,),)
    contatos = cursor.fetchall()
    return render_template("meus_contatos.html", contatos=contatos) 





   
@app.route('/excluir_usuario/<id>', methods=['GET', 'POST'])
def excluir_usuario(id):
    # Validar o ID
    if not id.isdigit():
        return render_template('excluir-usuario.html', error='ID inválido')
    # Executando a exclusão
    try:
        bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
        cursor = bd.cursor()
        cursor.execute("""
            DELETE FROM usuarios
            WHERE id = %s;
        """, (id,))
        cursor.close()
        bd.commit()

        return redirect(url_for('pagina_usuarios'))
    except bd.connector.Error as e:
        return render_template('excluir-usuario.html', error=str(e))


@app.route('/atendimento/<id>', methods=['GET', 'POST'])
def atenderchamado(id):

    # Validação do ID
    if not id.isdigit():
        return render_template('error', mensagem='ID inválido')

    # Recupera o ID do usuário logado
    usuario_id = session.get('usuario_id')

    try:

        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()

        sql = 'UPDATE contatos SET situacao = %s WHERE id_contato = %s;'
        values = ("Atendimento", int(id))
        cursor.execute(sql, values)
        bd.commit()
            # Inserindo o registro na tabela 'usuario_contato'
        sql = """
                INSERT INTO usuario_contato (usuario_id, contato_id, situacao)
                VALUES (%s, %s, %s);
            """
        values = (int(usuario_id), int(id), "Atendimento")  # Converte 'id' para inteiro
        cursor.execute(sql, values)

            # Confirmando as alterações
        bd.commit()
     
            # Redirecionamento para a página de contatos
        return redirect(url_for('pagina_inicial'))

    except Exception as e:  # Exceção genérica para capturar qualquer erro
        # Manipulação de erros
        print(f"Erro ao atender chamado: {e}")  # Registra o erro no console
        return render_template('error', mensagem=str(e))  # Exibe mensagem de erro genérica
@app.route('/finalizar_atendimento/<id>', methods=['GET', 'POST'])
def finalizarchamado(id):

    # Validação do ID
    if not id.isdigit():
        return render_template('error', mensagem='ID inválido')

    # Recupera o ID do usuário logado
    usuario_id = session.get('usuario_id')

    try:

        bd = conecta_no_banco_de_dados()
        cursor = bd.cursor()

        sql = 'UPDATE contatos SET situacao = %s WHERE id_contato = %s;'
        values = ("Finalizado", int(id))
        cursor.execute(sql, values)
        bd.commit()
            # Inserindo o registro na tabela 'usuario_contato'
        sql = 'UPDATE usuario_contato SET situacao = %s where usuario_id =%s and contato_id=%s;'
        values = ("Finalizado",int(usuario_id), int(id))  # Converte 'id' para inteiro
        cursor.execute(sql,values)

            # Confirmando as alterações
        bd.commit()
     
            # Redirecionamento para a página de contatos
        return redirect(url_for('pagina_inicial'))

    except Exception as e:  # Exceção genérica para capturar qualquer erro
        # Manipulação de erros
        print(f"Erro ao atender chamado: {e}")  # Registra o erro no console
        return render_template('error', mensagem=str(e))  # Exibe mensagem de erro genérica
@app.route('/editarusuario/<id>', methods=['GET', 'POST'])
def atualizarusuario(id):

    # Valida o ID do usuário
    if not id.isdigit():
        return render_template('editarusuario/<id>', error='ID inválido.')

    # Obtém os dados do usuário do banco de dados
    bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
    cursor = bd.cursor()
    cursor.execute("""
        SELECT id, nome, email
        FROM usuarios
        WHERE id = %s;
    """, (id,))
    dados_usuario = cursor.fetchone()
    cursor.close()
    bd.close()

    # Processa o formulário
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
       
        # Valida o input
        if not nome:
            flash('O nome é obrigatório.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
        if not email:
            flash('O e-mail é obrigatório.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
        if not senha:
            flash('A senha é obrigatória.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
       

        # Realiza a atualização no banco de dados
        bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
        cursor = bd.cursor()
        sql = 'UPDATE usuarios SET nome = %s, email = %s, senha= %s WHERE id = %s;'
        values = (nome, email, senha,  id)
        cursor.execute(sql, values)
        bd.commit()
        cursor.close()
        bd.close()

        # Redireciona para a página inicial
        return redirect(url_for('pagina_inicial'))

    # Exibe o formulário
    return render_template('editarusuario.html', id=id, dados_usuario=dados_usuario)

@app.route('/atualizareditarusuario/<id>', methods=['POST','GET'])
def atualizareditarusuario(id):

    # Valida os dados do usuário.
    if not id.isdigit():
        return render_template('/editarusuario/<id>', error='ID inválido.')

    # Obtém os valores dos campos "nome", "email" e "senha" do formulário submetido via POST.
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Valida os campos obrigatórios.
    if not nome:
        return render_template('editarusuario.html', error='O nome é obrigatório.')
    if not email:
        return render_template('editarusuario.html', error='O e-mail é obrigatório.')
    if not senha:
        return render_template('editarusuario.html', error='A senha é obrigatória.')

    # Abre uma conexão com o banco de dados MySQL usando as credenciais especificadas.

    try:
        # Reabre a conexão com o banco.
        bd =conecta_no_banco_de_dados()
            # A linha bd = conecta_no_banco_de_dados() tenta estabelecer uma conexão com o banco de dados usando a função conecta_no_banco_de_dados().
            # Essa função, é responsável por lidar com os detalhes da conexão.
            
        cursor = bd.cursor()

        # Prepara a consulta SQL de atualização.
        sql = 'UPDATE usuarios ' \
              'SET nome = %s, ' \
              'email = %s, ' \
              'senha = %s ' \
              'WHERE id = %s;'
        values = (nome, email, senha, id)

        # Executa a consulta com os valores obtidos do formulário.
        cursor.execute(sql, values)

        # Fecha o cursor e confirma a transação (commit).
        cursor.close()
        bd.commit()

        # Redireciona para a página inicial.
        return redirect(url_for('pagina_inicial'))

    except bd.connector.Error as e:
        return render_template('/editarusuario/<id>',id, error=str(e))






if __name__ == '__main__':
    app.run(debug=True)
# Este bloco de código é executado apenas quando o script Python é executado diretamente, não quando ele é importado como um módulo.
# Dentro do bloco, a linha app.run(debug=True) inicia o aplicativo Flask.
# O parâmetro debug=True ativa o modo de depuração, que fornece informações mais detalhadas sobre erros e facilita a depuração do código.