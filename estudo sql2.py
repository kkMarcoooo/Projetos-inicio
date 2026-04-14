import sqlite3
conexao = sqlite3.connect("banco_de_dados_maneiro")
funcionario = conexao.cursor()
funcionario.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL,
        estoque INTEGER
)
""")
print("=== CADASTRO ===")
nome_produto = input("Nome do produto: ")
preco_produto = float(input("Preço do produto: "))
estoque_produto = int(input("Quantidade em estoque: "))
funcionario.execute("""
    INSERT INTO produtos(nome,preco, estoque)
    VALUES(?,?,?)
""", (nome_produto, preco_produto, estoque_produto))
conexao.commit()
print("Produto salvo!")
conexao.close()