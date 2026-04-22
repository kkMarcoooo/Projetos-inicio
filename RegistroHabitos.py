import matplotlib.pyplot as plt
import sqlite3
cadastro = []
contador = 0
conexao = sqlite3.connect("Bd_semana")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados(
        dia TEXT,
        habito TEXT,
        status INTEGER
    )
""")
dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
while True:
    habitos = str(input("Registrar habito [stop] para parar: "))
    if habitos == "stop":
        break
    elif habitos == "pepero":
        cursor.execute("DELETE FROM dados")
        conexao.commit()
        print("Todos os registros foram apagados!")
    else:
        cadastro.append(habitos)
        contador += 1
print("| [1] Fez | [2] Não Fez |")
for dia in dias_semana:
    print("—" * 5)
    print(f"{dia}")
    print("—" * 5)
    for habito in cadastro:
        registro = int(input(f"Habito '{habito}' [1] Sim /[2] Não: "))
        cursor.execute('''
            INSERT INTO dados (dia, habito, status)
            VALUES (?, ?, ?)
        ''', (dia, habito, registro))
    conexao.commit()
pontos_y = []
for dia in dias_semana:
    cursor.execute("SELECT COUNT(*) FROM dados WHERE dia = ? AND status = 1",(dia,))
    total_feito = cursor.fetchone()[0]
    pontos_y.append(total_feito)
plt.plot(dias_semana, pontos_y, marker = "o")
plt.show()
