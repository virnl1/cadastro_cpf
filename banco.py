import sqlite3

conexao = sqlite3.connect('cadastro.db')
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
               CPF varchar(11) NOT NULL ,
               nome TEXT NOT NULL,
                email TEXT NOT NULL ,
                telefone varchar(15) NOT NULL,
               data_nascimento DATE NOT NULL
                );
""")

conexao.close()

print("Banco de dados e tabela criados com sucesso!")