import sqlite3
conectar = sqlite3.connect("Banco_de_dados.db")
funcionario = conectar.cursor()
funcionario.execute("""
    CREATE TABLE IF NOT EXISTS pessoas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")
def seila():
    nome_user = str(input("Nome: "))
    idade_user = int(input("Idade: "))
    funcionario.execute("""
                        INSERT INTO pessoas(nome, idade)
                        VALUES (?, ?)
                        """, (nome_user, idade_user))
    conectar.commit()
seila()
print("\n--==Banco de Dados🎲🏦==--")
while True:
    funcionario.execute("SELECT * FROM pessoas")
    dados = funcionario.fetchall()
    for linha in dados:
        print(linha)
    acao = int(input("|[1] Adicionar | [2] Remover| [0] Sair |\nQual ação deseja fazer? "))
    if acao == 1:
        seila()
    if acao == 2:
        id_deletar = int(input("ID da pessoa á deletar: "))
        funcionario.execute(f"DELETE FROM pessoas WHERE id == {id_deletar}")
        conectar.commit()
    elif acao == 0:
        break
