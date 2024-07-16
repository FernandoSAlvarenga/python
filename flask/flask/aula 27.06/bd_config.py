import mysql.connector

def conecta_no_banco_de_dados():
    cnx = mysql.connector.connect(host='127.0.0.1', user='root', password='')

    cursor = cnx.cursor()
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "aula02";')

    num_results = cursor.fetchone()[0]

    cnx.close()

    if num_results > 0:
        print('O banco de dados aula02 existe e esta pronto para uso.')
    else:
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )

        cursor = cnx.cursor()
        cursor.execute('CREATE DATABASE aula02;')
        cnx.commit()

        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='aula02'
        )

        cursor = cnx.cursor()
        cursor.execute('CREATE TABLE contatos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,mensagem TEXT NOT NULL);')
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