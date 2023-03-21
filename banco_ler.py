import conexao_bd as con

# TESTANDO CONEXÃO
if con.conexao.is_connected():
    db_info = con.conexao.get_server_info()
    print(f'Conectado a {db_info}')

# IMPRIMIR NOME DO BANCO DE DADOS
cursor = con.conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchall()
print(f'Banco = {linha[0][0]}')
# linha = cursor.fetchone()
# print(f'Banco = {linha[0]}')

sql = 'SELECT * from usuarios'
cursor.execute(sql)
linhas = cursor.fetchall()

# for linha in linhas:
#     print(linha[0], end='\t')
#     print(linha[1], end='\t')
#     print(linha[2], end='\t')
#     print(linha[3], end='\t')
#     print(linha[4])

for linha in linhas:
    print('*---' * 8)
    id, nome, email, *args = linha
    print('id: ', id)
    print('nome: ', nome)
    print('email: ', email)

