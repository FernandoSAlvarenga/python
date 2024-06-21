import mysql.connector

try:
    elo = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='pizzadofe'
    )
    print("Conexão bem-sucedida!")
    elo.close()
except mysql.connector.Error as err:
    print(f"Erro de conexão: {err}")