"""
DML - Manipulação de dados
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""
import sqlite3

# Como me conectar ao banco de dados sqlite3?
con = sqlite3.connect('base.db')

# Como posso executar os comandos e fazer as operações? com o cursor!!!
cur = con.cursor()

# OBS: Tirar o drop table ao fim dos testes
cur.execute("DROP TABLE if exists pessoas")

# Criando a tabela e os campos (se não existirem)
cur.execute("CREATE TABLE if not exists pessoas (nome text, idade number, telefone number)")

# Inserindo valores na tabela do banco
cur.execute("INSERT INTO pessoas VALUES ('Ana', 22, 69420)")
cur.execute("INSERT INTO pessoas VALUES ('Erick', 20, 40028922)")
cur.execute("INSERT INTO pessoas VALUES ('Dejair', 19, 80085)")

# Efetivando as alterações no banco:
con.commit()

# Exemplo de Consulta dos registros do banco:
cur.execute("SELECT * FROM pessoas")
dados = cur.fetchall()

# Retorna uma lista de tuplas com todos os registros encontrados:
#print(dados)

# Fechando a conexão com o banco após o término das operações
con.close()


# Exemplo de uso com os dados:
for dado in dados:
    if dado[0] == 'Erick':
        print("Imprimindo as informações do erick...")
        print(f"nome: {dado[0]}, idade: {dado[1]}, numero: {dado[2]}")





# --- PARA USO MAIS AVANÇADOS --- #

#import sqlite3

# Como me conectar ao banco de dados sqlite3?
con = sqlite3.connect('base.db')

# Como posso executar os comandos e fazer as operações? com o cursor!!!
cur = con.cursor()

# OBS: Tirar o drop table ao fim dos testes
cur.execute("DROP TABLE if exists pessoas")

# Criando a tabela e os campos (se não existirem)
cur.execute("CREATE TABLE if not exists pessoas (id integer primary key autoincrement, nome text not null, idade number not null, telefone number unique not null)")

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator


@commit_close
def db_insert(name: str, age, phone):
    return f"""
    INSERT INTO pessoas(nome, idade, telefone)
    VALUES('{name}', '{age}', '{phone}')
    """

@commit_close
def db_update_number(old_number, new_number):
    return f"""
    UPDATE pessoas SET telefone = '{new_number}' WHERE telefone = '{old_number}'
    """ 

@commit_close
def db_delete(data, field):
    return f"""
    DELETE FROM pessoas WHERE {field}='{data}'
    """

def db_select_where(data, field):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = f"""
    SELECT id, name, phone, email
    FROM pessoas
    WHERE {field}={data}"""

    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

def db_select_all():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = f"""
    SELECT *
    FROM pessoas"""
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

# Inserindo valores na tabela do banco
db_insert('Ana', 22, 69420)
db_insert('Erick', 20, 40028922)
db_insert('Ana', 19, 80085)

for dado in db_select_all():
    print(dado)

