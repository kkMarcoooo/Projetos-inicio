import random, sqlite3
import time

conexao = sqlite3.connect("BD_aposta1.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados_users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    saldo REAL NOT NULL
)
""")


def email():
    while True:
        new_email = str(input("Email: "))
        if new_email.endswith(("@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com")):
            cursor.execute("SELECT * FROM dados_users WHERE email = ?", (new_email,))
            resultado = cursor.fetchone()
            if resultado:
                print("E-mail já cadastrado!")
            else:
                return new_email
        else:
            print("Email inválido!")


def nickname():
    while True:
        name = str(input("Apelido: "))
        cursor.execute("SELECT * FROM dados_users WHERE nome = ?", (name,))
        resultado_name = cursor.fetchone()
        if resultado_name:
            print("Apelido já registrado!")
        else:
           return name


def senha():
    while True:
        new_password = str(input("Senha: "))
        caracteres = len(new_password)
        if caracteres > 5 and caracteres < 21:
            conf_password = str(input("Confirme a senha: "))
            if conf_password == new_password:
                return new_password
            else:
                print("SENHAS NÃO COINCIDEM!")
        else:
            print("INSIRA UMA SENHA DE 6 A 20 CARACTERES!")


def login_email():
    while True:
        email_login = str(input("E-mail: "))
        cursor.execute("SELECT * FROM dados_users WHERE email = ?", (email_login,))
        resultado_email_login = cursor.fetchone()
        if resultado_email_login:
            return email_login
        else:
            print("E-mail não encontrado no sistema!")
            continue


def login_senha(email1):
    tentativas = 3
    while tentativas > 0:
        senha_login = str(input("Senha: "))
        cursor.execute("SELECT nome FROM dados_users WHERE email = ? AND senha = ?", (email1, senha_login))
        resultado_senha = cursor.fetchone()
        if resultado_senha:
            nome_login = resultado_senha[0]
            print(f"LOGIN FEITO!\nSeja bem vindo {nome_login}!")
            return
        else:
            tentativas -= 1
            print(f"Erro! Você ainda tem {tentativas} tentativas!")
    if tentativas == 0:
        print("ACESSO BLOQUEADO")
        print("...")
        time.sleep(1.5)
        cursor.close()


while True:
    action = int(input("| [1] Cadastrar | [2] Login |\nR: "))
    if action in (1,2):
        if action == 1:
            email = email()
            nome = nickname()
            senhaa = senha()
            saldo = 100
            cursor.execute("INSERT INTO dados_users (nome, email, senha, saldo) VALUES (?, ?, ?, ?)",(nome, email, senhaa, saldo))
            conexao.commit()
            print(f"Cadastro Feito, {nome}! Voltando para menu inicial...\n")
            time.sleep(2)
            continue
        if action == 2:
            email1 = login_email()
            login_senha(email1)
            break
def jogo(saldo):
    while True:
        print(f"Saldo: R$ {saldo}")
        aposta = float(input("Valor da aposta: "))
        if aposta <= saldo:
            roleta = random.randint(1, 8)
            saldo -= aposta
            print(roleta)
            sorteado = int(input("Digite o número secreto de 1 á 8: "))
            if sorteado == roleta:
                print("WIN!")
                saldo += aposta * 2
            else:
                print("You lost!")
                print(f"O número secreto era {roleta}!")
        else:
            print("SALDO INSUFICIENTE!")
