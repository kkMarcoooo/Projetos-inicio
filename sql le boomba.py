import sqlite3
conexao = sqlite3.connect("Banco_de_dados_radicalYEAHHH")
escravo = conexao.cursor()
escravo.execute("""
    CREATE TABLE IF NOT EXISTS tabela_sigma(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        peso REAL
)
""")
print("--== Cadastro ==--")
while True:
    nome_user = str(input("Nome: "))
    idade_user = int(input("Idade: "))
    peso_user = float(input("Peso: "))
    escravo.execute("""
    INSERT INTO tabela_sigma(nome, idade, peso)
    VALUES(?,?,?)
    """, (nome_user, idade_user, peso_user))
    conexao.commit()
    continuar = str(input("Continuar? (S/N): ").upper().strip())
    if continuar == "S":
        continue
    else:
        break
conexao.close()
print("Conexão encerrada e dados salvos!")