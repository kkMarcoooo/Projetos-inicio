import datetime
import sqlite3
import time

import matplotlib.pyplot as plt

conexao = sqlite3.connect("Bd_gastos1")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos_user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datas TEXT,
    categoria TEXT,
    valor REAL
)
""")
print("=" * 41)
print("      GERENCIADOR de GASTOS PESSOAIS")
print("=" * 41)
def menu():
    while True:
        opcao = int(input("[1] Adicionar Novo Gasto\n[2] Visualizar Relatórios (Gráficos)\n[3] Ver Histórico (Tabela)\n[4] Sair\n\nEscolha uma opção: "))
        if opcao in (1,2,3,4):
            return opcao
        else:
            print("INSIRA UMA OPÇÂO VÁLIDA!")
def opcoes(menu):
    if menu == 1:
        valor = float(input("Digite o valor (ex: 45.90): "))
        if valor > 0:
            categoria = str(input("Digite a categoria (ex: Comida, Transporte, Lazer): ").lower())
            if categoria in ["comida","transporte","lazer"]:
                data_hoje = str(input("Digite a data (DD/MM/AAAA) ou aperte ENTER para hoje: "))
                if data_hoje == "":
                    data_hoje= datetime.date.today()
                cursor.execute("INSERT INTO gastos_user (datas, categoria, valor) VALUES(?,?,?)",(data_hoje, categoria, valor))
                conexao.commit()
                print(f"Gasto de R$ {valor} em '{categoria}' registrado!")
                print("-" * 41)
    if menu == 2:
        print("[INFO] Gerando gráfico de análise...")
        cursor.execute("SELECT categoria, SUM(valor) FROM gastos_user GROUP BY categoria")
        dados = cursor.fetchall()
        if dados:
            categorias = [item[0] for item in dados]
            valores = [item[1] for item in dados]
            plt.figure(figsize=(7, 7))
            plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
            plt.title("Meus Gastos por Categoria")
            time.sleep(1)
            print("[INFO] Feche a janela do gráfico para voltar ao menu.")
            plt.show()
        else:
            print("Aviso: Adicione gastos primeiro para gerar o relatório!")
while True:
    escolha = menu()
    if escolha == 4:
        print("Saindo... Até logo!")
        conexao.close()
        break
    opcoes(escolha)