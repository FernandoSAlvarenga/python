from flask import Flask, render_template#Esta linha importa a classe Flask do módulo Flask. # Esta classe é essencial para criar aplicativos web com Flask. # Ela fornece a funcionalidade principal para construir e executar servidores web,# lidar com solicitações e renderizar respostas.

app = Flask(__name__)
#Esta linha cria uma instância da classe Flask e a atribui à variável app. 
# Essa instância representa seu aplicativo web.
#__name__ é uma variável especial em Python que contém o nome do módulo atual. 
# É usado aqui para determinar o caminho raiz do aplicativo, 
# garantindo que recursos como modelos e arquivos estáticos possam ser encontrados 
# corretamente.
@app.route('/')
#Esta linha é um decorador que associa uma função a um caminho URL específico. 
# Neste caso, ele conecta a função index ao caminho raiz do aplicativo (/).
#Quando um usuário visita a página inicial do aplicativo (geralmente http://localhost:5000/ por padrão), esta função será executada para lidar com a solicitação.
def index():
    html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Desvendando o Flask</title>
</head>
<body>
    <h1>Desvendando o Flask: Um Framework Python Leve para Web Development</h1>
    <p>O Flask se destaca como um framework Python leve e minimalista para o desenvolvimento web. Ele oferece as ferramentas essenciais para construir aplicações web robustas e escaláveis, sem a necessidade de dominar bibliotecas complexas ou frameworks pesados.</p>

    <h2>O que é o Flask?</h2>
    <p>O Flask é um framework para desenvolvimento web em Python que se caracteriza por sua simplicidade e facilidade de aprendizado. Com ele, você pode construir desde APIs simples até aplicações web complexas, moldando a solução às suas necessidades.</p>

    <h2>Benefícios do Flask:</h2>
    <ul>
        <li><b>Simplicidade:</b>
            <ul>
                <li>Ideal para iniciantes e experientes em Python.</li>
                <li>Curva de aprendizado suave e rápida.</li>
            </ul>
        </li>
        <li><b>Flexibilidade:</b>
            <ul>
                <li>Permite construir desde APIs simples até aplicações web complexas.</li>
                <li>Liberdade para moldar a solução às suas necessidades.</li>
            </ul>
        </li>
        <li><b>Extensibilidade:</b>
            <ul>
                <li>Ampla gama de bibliotecas e extensões oficiais e de terceiros.</li>
                <li>Funcionalidades expansíveis para atender a diversos requisitos.</li>
            </ul>
        </li>
        <li><b>Leveza:</b>
            <ul>
                <li>Framework leve e eficiente, ideal para servidores com recursos limitados.</li>
                <li>Otimizado para desempenho e consumo de recursos.</li>
            </ul>
        </li>
    </ul>

    <h1>Configurando o Ambiente de Desenvolvimento Flask</h1>
    <p>Este guia apresenta os passos iniciais para configurar seu ambiente de desenvolvimento e criar sua primeira aplicação Flask.</p>

    <h2>Configurando o Ambiente de Desenvolvimento</h2>
    <p>Para começar sua jornada com o Flask, siga estas etapas:</p>

    <h3>Instale o Python:</h3>
    <p>Certifique-se de ter o Python 3.6 ou superior instalado em sua máquina. Você pode verificar a versão do Python no terminal com o comando:</p>
    <pre>python3 --version</pre>
    <p>Se necessário, baixe e instale o Python em: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></p>

    <h3>Instale o Virtualenv</h3>
    <p>O Virtualenv é uma ferramenta útil para isolar os ambientes de desenvolvimento de diferentes projetos. Para instalá-lo, execute o comando:</p>
    <pre>pip install virtualenv</pre>

    <h3>Crie um Ambiente Virtual:</h3>
    <p>Navegue até o diretório do seu projeto e crie um ambiente virtual com o comando:</p>
    <pre>python -m venv .venv</pre>
    <p>Ative o ambiente virtual:</p>
    <pre>.\.venv\Scripts\ activate</pre>

    <h3>Instale o Flask:</h3>
    <p>Instale o Flask no ambiente virtual com o comando:</p>
    <pre>pip install flask</pre>

    <h3>Verifique a Instalação:</h3>
    <p>Para confirmar que o Flask está instalado corretamente, execute:</p>
    <pre>python -c "import flask; print(flask.__version__)"</pre>
</body>
</html>
    """
    return html
   
#Esta linha retorna uma string HTML
#Com texto. Esta string será o conteúdo da página da web 
#Que o usuário vê quando visita o URL raiz do aplicativo.

@app.route('/rotas')
def rotas():
    return render_template("rotas.html",)
#Exemplo
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def pagina_inicial():
#     # Gera o HTML da página inicial
#     return "<h1>Página Inicial</h1>"
# @app.route("/contato")
# def pagina_contato():
#     # Gera o HTML da página de contato
#     return "<h1>Página de Contato</h1>"
# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/<usuario>')
def paginausuarios(usuario):
     mensagem = "Aproveite sua jornada no site!"
     return render_template("usuarios.html",usuario=usuario,mensagem=mensagem)

@app.route('/rendertemplate')
def rendertemplate():
    return render_template("rendertemplate.html",)





if __name__ == '__main__':
    app.run