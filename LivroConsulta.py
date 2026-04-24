import sqlite3
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
        opcao = int(input("[1] Cadastrar Livro\n[2] Consultar livros cadastrados\n[3] Filtrar por autor\n[4] Atualizar\n[5] Remover livro\nEscolha uma opção: "))
        if opcao in (1,2,3,4,5):
            return opcao
        else:
            print("INSIRA OPÇÂO VÁLIDA!")
def opcoes(opcao):
    if opcao == 1:
        titulo_livro = str(input("Título do livro: "))
        autor_livro = str(input("Autor do livro: "))
        data_lancamento = str(input("Data de lançamento (DD/MM/AAAA): "))
        funcio.execute("INSERT INTO banco_livros (titulo, autor, lancamento) VALUES (?, ?, ?)",(titulo_livro,autor_livro,data_lancamento))
        banco.commit()
    if opcao == 2:
        autor_consulta = str(input("Autor do livro á consultar: "))
        funcio.execute("SELECT titulo FROM banco_livros WHERE autor = ?", (autor_consulta, ))
        consulta = funcio.fetchall()
        if consulta:
            for livro in consulta:
                print(f"- {livro[0]}")

while True:
    escolha = menu()
    opcoes(escolha)
#- Felipe: A Origem
#- Felipe: A Perda
#- Felipe: A Vingança
#- Felipe: Arco de Vilao
#- Felipe: Redenção
# Felipe: Destino
#- Felipe: Nós somos Felipe
#- Felipe: Legado