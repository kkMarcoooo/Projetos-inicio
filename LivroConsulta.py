import sqlite3
import time

import tabulate
banco = sqlite3.connect("Bd_Livro")
funcio = banco.cursor()
funcio.execute("""
    CREATE TABLE IF NOT EXISTS banco_livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    lancamento TEXT NOT NULL,
    lido BOOLEAN
)
""")
def menu():
    while True:
        opcao = int(input("[1] Cadastrar Livro\n[2] Consultar livros cadastrados\n[3] Filtrar por autor\n[4] Atualizar\n[5] Remover livro\n\nEscolha uma opção: "))
        if opcao in (1,2,3,4,5):
            return opcao
        else:
            print("INSIRA OPÇÂO VÁLIDA!")
def opcoes(opcao):
    if opcao == 1:
        titulo_livro = str(input("Título do livro: "))
        autor_livro = str(input("Autor do livro: "))
        data_lancamento = str(input("Data de lançamento (DD/MM/AAAA): "))
        livro_lido = False
        funcio.execute("INSERT INTO banco_livros (titulo, autor, lancamento, lido) VALUES (?, ?, ?, ?)",(titulo_livro,autor_livro,data_lancamento,livro_lido))
        banco.commit()
    if opcao == 2:
        funcio.execute("SELECT titulo, autor, lancamento, lido FROM banco_livros")
        consulta = funcio.fetchall()
        if consulta:
            print("\n")
            print(tabulate.tabulate(consulta, headers=["Título", "Autor", "Ano", "Status"], tablefmt="grid"))
    if opcao == 3:
        autor_consulta = str(input("Autor do livro á consultar: "))
        funcio.execute("SELECT titulo FROM banco_livros WHERE autor = ?", (autor_consulta, ))
        consulta = funcio.fetchall()
        if consulta:
            for livro in consulta:
                print(f"- {livro[0]}")
    if opcao == 4:
        nome_livro = str(input("Título do livro: "))
        funcio.execute("SELECT titulo FROM banco_livros WHERE titulo = ?",(nome_livro,))
        consulta = funcio.fetchall()
        if consulta:
            print("| [0] Não Lido | [1] Lido |")
            livro_status = int(input("Livro: "))
            if livro_status in (0,1):
                funcio.execute("UPDATE banco_livros SET lido = ? WHERE titulo = ?", (livro_status, nome_livro))
                banco.commit()
    if opcao == 5:
        livro_remover = str(input("Título do livro á remover: "))
        funcio.execute("SELECT titulo FROM banco_livros WHERE titulo = ?", (livro_remover,))
        consulta = funcio.fetchall()
        if consulta:
            confirmar = int(input(f"| [1] Sim | [2] Não |\nRemover '{livro_remover}'? "))
            if confirmar == 1:
                print(f"Deletando '{livro_remover}' do sistema...")
                funcio.execute("DELETE FROM banco_livros WHERE titulo = ?", (livro_remover,))
                banco.commit()
                time.sleep(1.25)
                print("Livro removido do sistema!")
            else:
                print("Operação cancelada!")
        else:
            print("Livro não encontrado!")
while True:
    escolha = menu()
    opcoes(escolha)
    print("\n")
