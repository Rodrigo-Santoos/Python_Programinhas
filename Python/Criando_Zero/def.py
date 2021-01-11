#======================Conectando com Banco de Dados Postgress================================#
import psycopg2

def conexao():
    conn = psycopg2.connect(
        host="localhost",
        database="rod",
        user="rod",
        password="1234"
    )
    
    return conn


#===========================Trazendo Informaçoes no Python======================================#
def trazTudo ():
    con = conexao()
    cursor = con.cursor()
    cursor.execute("select * from users")
    result = cursor.fetchall()
    for row in result:
        print(row)
    con.commit()
    con.close()

#===========================Inserindo Usuario===========================#===========================
def insertUser(nomeInsert, emailInsert):
    con = conexao()
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (nome, email) VALUES ('{}', '{}');".format(nomeInsert, emailInsert))
    con.commit()
    con.close()
    

nomeInsert = input('Digite um valor: ')
emailInsert = input('Digite o segundo: ')


insertUser(nomeInsert, emailInsert),
trazTudo()

