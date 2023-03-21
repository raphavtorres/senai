import mysql.connector

# CRIANDO CONEXÃO
conexao = mysql.connector.connect(
    host='localhost',
    database='netflix',
    user='root',
    password=''
)

# TESTANDO CONEXÃO
if conexao.is_connected():
    db_info = conexao.get_server_info()
    print(f'Conectado a {db_info}')

# IMPRIMIR NOME DO BANCO DE DADOS
cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchall()
print(f'Banco = {linha[0][0]}')
# linha = cursor.fetchone()
# print(f'Banco = {linha[0]}')

sql = 'SELECT * from usuarios'
cursor.execute(sql)
# linhas1 = cursor.fetchone()
linhas2 = cursor.fetchall()

# print('one: ', linhas1)
print('all: ', linhas2)

# for linha in linhas2:
#     print(linha[0], end='\t')
#     print(linha[1], end='\t')
#     print(linha[2], end='\t')
#     print(linha[3], end='\t')
#     print(linha[4])


for linha in linhas2:
    print('*---' * 8)
    id, nome, email, *args = linha
    print('id: ', id)
    print('nome: ', nome)
    print('email: ', email)

