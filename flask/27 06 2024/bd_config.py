import mysql.connector

def conecta_no_banco_de_dados():
    cnx = mysql.connector.connect(host='127.0.0.1',user='root',password='')

    # Executar a instrução SQL para verificar se o banco de dados existe
    cursor = cnx.cursor()
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "aula02";')

    # Obter o número de resultados
    num_results = cursor.fetchone()[0]

    # Fechar a conexão com o banco de dados
    cnx.close()

    # Se o número de resultados for maior que zero, o banco de dados existe
    if num_results > 0:
        print('O banco de dados aula02 existe e esta pronto para uso.')
    else:
        # Conectar-se ao servidor MySQL para criar o banco de dados
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )

        # Criar o banco de dados aula02
        cursor = cnx.cursor()
        cursor.execute('CREATE DATABASE aula02;')
        cnx.commit()

    # Conectar-se ao banco de dados aula02 recém-criado
        cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='aula02'  # Especificar o banco de dados
        )

    
        cursor = cnx.cursor()
        cursor.execute('CREATE TABLE contatos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,mensagem TEXT NOT NULL);')
         # Fechar a conexão com o banco de dados
        cnx.commit()
        cnx.close()
    try:
        bd = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='aula02'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return bd