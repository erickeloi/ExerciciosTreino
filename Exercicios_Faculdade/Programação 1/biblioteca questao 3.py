# ALUNO: ERICK ELOI PIMENTA PIMENTEL
# MATRICULA: 202111140012

import sqlite3

con = sqlite3.connect('biblioteca.db')
cur = con.cursor()
cur.execute("CREATE TABLE if not exists livros (id integer primary key autoincrement, titulo text not null, autor text not null, ano number not null, sinopse text not null, editora text not null)")

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('biblioteca.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator


@commit_close
def db_insert(titulo: str, autor: str, ano: int, sinopse:str, editora:str):
    return f"""
    INSERT INTO livros (titulo, autor, ano, sinopse, editora)
    VALUES('{titulo}', '{autor}', '{ano}', '{sinopse}', '{editora}')
    """

def db_select_where(data, field):
    con = sqlite3.connect('biblioteca.db')
    cur = con.cursor()
    sql = f"""
    SELECT id, titulo, autor, ano, sinopse, editora
    FROM livros
    WHERE {field}={data}"""

    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

def db_select_all():
    con = sqlite3.connect('biblioteca.db')
    cur = con.cursor()
    sql = f"""
    SELECT *
    FROM livros"""
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

def menu():
    print("Operações na biblioteca")
    print("1 - Inserir Novos Livros")
    print("2 - Visualizar Livros Cadastrados")
    print("3 - Visualizar Livro Existente")
def option():
    while True:
        opt = input("Digite sua opção: ")
        if opt.isnumeric() and 1 <= int(opt) <= 3:
            return int(opt)
        else:
            print("ERRO! digite uma opção válida!")
    
def interface_principal():
    while True:
        menu()
        opt = option()
        if opt == 1:
            print("LEMBRE-SE!!! todas as informações Devem ser preenchidas!!!")
            titulo = input("Digite o titulo do livro: ")
            autor = input("Digite o Autor do livro: ")
            ano = int(input("Digite o Ano do livro (somente numeros): "))
            sinopse = input("Digite a sinopse do livro: ")
            editora = input("Digite a Editora do livro: ")

            print("Inserindo as informações no banco de dados...")
            db_insert(titulo, autor, ano, sinopse, editora)
            print("Informações inseridas com sucesso!")

            passar = input("Digite qualquer valor para continuar...")
        elif opt == 2:
            #Visualizar todos os livros
            print("Imprimindo Livros Cadastrados...")
            print("----- x -----")
            for dado in db_select_all():
                print(f"Id: {dado[0]}, Titulo: {dado[1]}, Autor: {dado[2]}, Ano: {dado[3]}, Sinopse: {dado[4]}, Editora: {dado[5]}")
                print("----- x -----")
            passar = input("Digite qualquer valor para continuar...")
        elif opt == 3:
            #Vizualizar por valor especifico       
            def menu_select():
                print("Você quer buscar o livro por qual informação?")
                print("1 - Identificação")
                print("2 - TITULO")
                print("3 - AUTOR")
                print("4 - ANO DE PUBLICAÇÃO")
                print("5 - SINOPSE")
                print("6 - EDITORA")
            def option_select():
                while True:
                    opt = input("Digite sua opção: ")
                    if opt.isnumeric() and 1 <= int(opt) <= 6:
                        return int(opt)
                    else:
                        print("ERRO! digite uma opção válida!")
                        menu_select()
            def get_data_str():
                info = input("Digite a informação do livro do campo desejado:")
                return info
            def data_number():
                info = int(input("Digite a informação do livro do campo desejado:"))
                return info
            while True:
                id = 0
                menu_select()
                opt = option_select()
                if opt == 1:
                    id = "id"
                    data = data_number()
                elif opt == 2:
                    id = "titulo"
                    data = get_data_str()
                elif opt == 3:
                    id = "autor"
                    data = get_data_str()
                elif opt == 4:
                    id = "ano"
                    data = data_number()
                elif opt == 5:
                    id = "sinopse"
                    data = get_data_str()
                elif opt == 6:
                    id = "editora"
                    data = get_data_str()
                else:
                    print("Opção invalida")
                    continue

                if data:
                    if db_select_where(data, id) != []:
                        print("Imprimindo Livros encontrados...")
                        print("----- x -----")
                        for inf in db_select_where(data, id):
                            print(f"Id: {inf[0]}, Titulo: {inf[1]}, Autor: {inf[2]}, Ano: {inf[3]}, Sinopse: {inf[4]}, Editora: {inf[5]}")
                        print("----- x -----")
                        passar = input("Digite qualquer valor para continuar...")
                        break
                    else:
                        print("Não foram encontrados livros com essas caracteristicas")
                        passar = input("Digite qualquer valor para continuar...")
                        break

interface_principal()
