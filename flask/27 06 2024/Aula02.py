from typing import NotRequired#Esta linha importa o tipo NotRequired do módulo typing. Este tipo é tipicamente usado com formulários Flask-WTF para indicar que um campo é opcional e pode ser enviado sem valor.
from flask import Flask, redirect, render_template, request#Esta linha importa várias funções do módulo flask:Flask: Esta função é usada para criar uma instância de aplicativo Flask.redirect: Esta função é usada para redirecionar um usuário para uma URL diferente.render_template: Esta função é usada para renderizar um arquivo de modelo com dados.request: Este objeto fornece acesso às informações da solicitação web atual, como dados de formulário, cabeçalhos e cookies.
from flask_wtf import FlaskForm#Esta linha importa a classe FlaskForm do módulo flask_wtf. Esta classe é a classe base para criar formulários em aplicativos Flask que usam WTForms para validação e proteção CSRF.
from wtforms import StringField, EmailField, PasswordField, validators#Esta linha importa várias classes de campo de formulário e o módulo validators da biblioteca wtforms:StringField: Esta classe é usada para criar um campo de entrada de texto.EmailField: Esta classe é usada para criar um campo de entrada de email com validação básica de email.PasswordField: Esta classe é usada para criar um campo de entrada de senha que oculta os caracteres à medida que são digitados.validators: Este módulo fornece vários validadores que podem ser usados para verificar o formato, o comprimento e outras propriedades dos dados do formulário.
from bd_config import conecta_no_banco_de_dados#Esta linha importa a função conecta_no_banco_de_dados.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'


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
        return redirect('/sucesso')
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


@app.route('/contatos')
def pagina_Contatos():
    bd =conecta_no_banco_de_dados()
    cursor = bd.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    return render_template("contatos.html", contatos=contatos)

if __name__ == '__main__':
    app.run(debug=True)
# Este bloco de código é executado apenas quando o script Python é executado diretamente, não quando ele é importado como um módulo.
# Dentro do bloco, a linha app.run(debug=True) inicia o aplicativo Flask.
# O parâmetro debug=True ativa o modo de depuração, que fornece informações mais detalhadas sobre erros e facilita a depuração do código.