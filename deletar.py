import sqlite3

conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()

cursor.execute("""drop table clientes""")

print("Tabela clientes removida com sucesso!")