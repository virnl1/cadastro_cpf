import sqlite3

def connectar_db():
    return sqlite3.connect('cadastro.db')

def inserir_cliente(cpf, nome, email, telefone, data_nascimento):
    con = connectar_db()
    cur = con.cursor()
    cur.execute("""
    INSERT INTO clientes (CPF, nome, email, telefone, data_nascimento)
    VALUES (?, ?, ?, ?, ?)
    """, (cpf, nome, email, telefone, data_nascimento))
    con.commit()
    con.close()

def listar_clientes():
    con = connectar_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes")
    dados = cur.fetchall()
    con.close()
    return dados

def atualizar_cliente(id, cpf, nome, email, telefone, data_nascimento):
    con = connectar_db()
    cur = con.cursor()
    cur.execute("""
    UPDATE clientes
    SET CPF = ?, nome = ?, email = ?, telefone = ?, data_nascimento = ?
    WHERE id = ?
    """, (cpf, nome, email, telefone, data_nascimento, id))
    con.commit()
    con.close()

def excluir_cliente(id_cliente):
    con = connectar_db()
    cur = con.cursor()
    cur.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))
    con.commit()
    con.close()

def buscar_cliente_por_cpf(cpf):
    con = connectar_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes WHERE CPF = ?", (cpf,))
    dados = cur.fetchall()
    con.close()
    return dados

def buscar_por_nome(nome):
    con = connectar_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%' + nome + '%',))
    clientes = cur.fetchall()
    con.close()
    return clientes