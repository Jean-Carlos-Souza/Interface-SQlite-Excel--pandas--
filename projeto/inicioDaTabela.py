import sqlite3


conexao = sqlite3.connect('Clientes.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE clientes (
               nome text,
               sobrenome text,
               email text,
               telefone text
               )
''')

conexao.commit()

conexao.close()






