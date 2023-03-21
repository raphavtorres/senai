from aifc import Error

import conexao_bd as con

try:
    inserir_filmes = """
    INSERT INTO filmes (filme, plano, descricao, classificacao)
    values
    ('Matrix', 'basic', 'pílula', 12),
    ('Interestelar', 'medium', 'espaço', 10);
    """

    cursor = con.conexao.cursor()
    cursor.execute(inserir_filmes)
    con.conexao.commit()

    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    linhas = cursor.fecthall()

    print('-'*20)
    for linha in linhas:
        print(linha[0], '\t')
        print(linha[1], '\t')
        print(linha[2], '\t')
        print(linha[3])
except Error as e:
    print(f"Erro: {e}")

finally:
    if con.conexao.is_connected():
        cursor.close()
        con.conexao.close()
        print("Conexão encerrada")
